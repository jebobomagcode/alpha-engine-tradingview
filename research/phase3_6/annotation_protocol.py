"""Phase 3.6 S0 annotation-pilot input validator. No data collection or trading."""

from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
import re

PROTOCOL = "P36-S0-PILOT-V1"
INSTRUMENT = "BINANCE:PAXGUSDT"
UTC = timezone.utc
PHT = timezone(timedelta(hours=8))
SLOTS = {
    f"P36-{day.strftime('%Y%m%d')}-{hour:02d}00-PHT":
    day.replace(hour=hour, minute=0, tzinfo=PHT).astimezone(UTC)
    for day in (datetime(2026, 11, d) for d in (14, 15, 16, 17))
    for hour in (9, 15, 21)
}
ROLES = {"HH": ("UP", "HIGH"), "HL": ("UP", "LOW"),
         "LH": ("DOWN", "HIGH"), "LL": ("DOWN", "LOW")}
STAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\Z")
DIGEST = re.compile(r"[0-9a-f]{64}\Z")


def parse_utc(value):
    if not isinstance(value, str) or STAMP.fullmatch(value) is None:
        raise ValueError("Expected UTC timestamp with seconds and Z")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return result


def verify(record):
    """Return scoped evidence classification, never independent time authentication."""
    if not isinstance(record, dict) or set(record) != {"protocol", "case_id", "capture", "annotation"}:
        raise ValueError("Unexpected top-level schema")
    if record["protocol"] != PROTOCOL or record["case_id"] not in SLOTS:
        raise ValueError("Unknown protocol or preregistered case")
    cutoff = SLOTS[record["case_id"]]
    capture, ann = record["capture"], record["annotation"]
    if not isinstance(capture, dict) or not isinstance(ann, dict):
        raise ValueError("Capture and annotation must be objects")
    capture_keys = {"instrument", "market_type", "candle_kind", "timeframe", "source_mode",
                    "target_cutoff_utc", "last_visible_closed_utc", "captured_at_utc",
                    "future_hidden", "snapshot_sha256"}
    ann_keys = {"reviewer_id", "recorded_at_utc", "blind_to_peer", "selection", "regime",
                "swing_side", "pivot_origin_utc", "level_quote", "role", "scale", "reason"}
    if set(capture) != capture_keys or set(ann) != ann_keys:
        raise ValueError("Missing or unexpected field")
    if (capture["instrument"], capture["market_type"], capture["candle_kind"],
            capture["timeframe"]) != (INSTRUMENT, "SPOT", "STANDARD", "5m"):
        raise ValueError("Wrong instrument, market type, candle kind or timeframe")
    if capture["source_mode"] not in {"LIVE_CHART", "FROZEN_PREFIX_PRACTICE"}:
        raise ValueError("Unsupported evidence mode")
    if capture["future_hidden"] is not True or ann["blind_to_peer"] is not True:
        raise ValueError("Future/peer blinding not declared")
    if not isinstance(capture["snapshot_sha256"], str) or DIGEST.fullmatch(capture["snapshot_sha256"]) is None:
        raise ValueError("Missing SHA-256 syntax")
    if (parse_utc(capture["target_cutoff_utc"]) != cutoff or
            parse_utc(capture["last_visible_closed_utc"]) != cutoff):
        raise ValueError("Snapshot does not have the preregistered last-closed cutoff")
    captured, declared = parse_utc(capture["captured_at_utc"]), parse_utc(ann["recorded_at_utc"])
    if not cutoff <= captured <= declared:
        raise ValueError("Capture/declaration chronology contradicts cutoff")
    if capture["source_mode"] == "LIVE_CHART" and declared >= cutoff + timedelta(minutes=5):
        raise ValueError("LIVE_CHART declaration was not before next 5m close")
    if ann["reviewer_id"] not in {"R1", "R2"} or ann["scale"] != "5M_STRUCTURAL":
        raise ValueError("Unknown reviewer or scale")
    if not isinstance(ann["reason"], str) or not ann["reason"].strip():
        raise ValueError("A reason, including for abstention, is required")
    if ann["regime"] not in {"UP", "DOWN", "UNKNOWN", "RANGE_CANDIDATE"}:
        raise ValueError("Unknown regime")
    if ann["selection"] == "ABSTAIN":
        if any(ann[key] is not None for key in ("swing_side", "pivot_origin_utc", "level_quote", "role")):
            raise ValueError("Abstention must not invent a reference")
    elif ann["selection"] == "ANCHOR":
        if ann["swing_side"] not in {"HIGH", "LOW"}:
            raise ValueError("Anchor needs HIGH or LOW side")
        origin = parse_utc(ann["pivot_origin_utc"])
        if origin >= cutoff or origin.second or origin.minute % 5:
            raise ValueError("Pivot origin must be a prior aligned 5m bar open")
        value = ann["level_quote"]
        if not isinstance(value, str) or not re.fullmatch(r"\d+(?:\.\d+)?", value):
            raise ValueError("Reference price must be a positive decimal string")
        try:
            if not Decimal(value).is_finite() or Decimal(value) <= 0:
                raise ValueError("Reference price must be positive")
        except InvalidOperation as exc:
            raise ValueError("Invalid decimal price") from exc
        role = ann["role"]
        if role is not None and (role not in ROLES or ROLES[role] != (ann["regime"], ann["swing_side"])):
            raise ValueError("Structural role contradicts declared regime or side")
    else:
        raise ValueError("Unknown annotation selection")
    return ("REPORTED_LIVE_TIMELINESS_NOT_AUTHENTICATED" if
            capture["source_mode"] == "LIVE_CHART" else "FROZEN_PREFIX_PRACTICE_ONLY")


def compare_pair(first, second):
    """Descriptive only; no inference of genuine peer blinding or timestamp truth."""
    verify(first)
    verify(second)
    a, b = first["annotation"], second["annotation"]
    if first["case_id"] != second["case_id"] or first["capture"]["snapshot_sha256"] != second["capture"]["snapshot_sha256"]:
        raise ValueError("Comparison requires same case and identical captured prefix")
    if a["reviewer_id"] == b["reviewer_id"]:
        raise ValueError("Comparison requires different reviewer identities")
    if first["capture"]["source_mode"] != second["capture"]["source_mode"]:
        raise ValueError("Do not combine live and frozen-prefix practice as one cohort")
    if a["selection"] != "ANCHOR" or b["selection"] != "ANCHOR":
        return {"paired": True, "both_anchored": False, "exact_reference": None,
                "same_regime": a["regime"] == b["regime"]}
    fields = ("swing_side", "pivot_origin_utc", "level_quote", "role", "scale")
    return {"paired": True, "both_anchored": True,
            "exact_reference": all(a[k] == b[k] for k in fields),
            "same_regime": a["regime"] == b["regime"]}
