"""Phase 3.5 candidate: independent M01 price-domain + retained-evidence checks.

Research-only Python mirror, source-diff guard, and archived Binance OHLC checks.
They do NOT compile Pine or establish native TradingView acceptance.
"""
from pathlib import Path
from decimal import Decimal
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATH = "pine/lesson08-diagnostic.pine"
PINNED = "3458ff6854e9c349aef10a30e487a908a3648441"
BASE = subprocess.check_output(["git", "show", f"{PINNED}:{PATH}"], cwd=ROOT).decode()
SOURCE = (ROOT / PATH).read_text(encoding="utf-8")
STEP = 300_000


def bar(t, h, l, o=None, c=None, end=None):
    h, l = Decimal(str(h)), Decimal(str(l))
    return {"t": t, "end": t + STEP if end is None else end,
            "o": (h + l) / 2 if o is None else Decimal(str(o)),
            "h": h, "l": l, "c": (h + l) / 2 if c is None else Decimal(str(c))}


def audit_window(bars, left=2, right=2):
    """Separate insufficient history, invalid evidence and valid no-event."""
    if len(bars) < left + right + 1:
        return "INSUFFICIENT", None, None
    window = bars[-(left + right + 1):]
    for i, x in enumerate(window):
        if x is None or not all(k in x and x[k] is not None for k in ("t", "end", "o", "h", "l", "c")):
            return "INVALID", None, None
        if (x["end"] != x["t"] + STEP or x["l"] <= 0 or
                x["h"] < max(x["o"], x["c"]) or x["l"] > min(x["o"], x["c"])):
            return "INVALID", None, None
        if i > 0 and x["t"] - window[i - 1]["t"] != STEP:
            return "INVALID", None, None
    mid = window[left]
    high = all(mid["h"] > x["h"] for i, x in enumerate(window) if i != left)
    low = all(mid["l"] < x["l"] for i, x in enumerate(window) if i != left)
    mk = lambda price: {"price": price, "origin": mid["t"], "known": window[-1]["end"]}
    return "VALID", mk(mid["h"]) if high else None, mk(mid["l"]) if low else None


def confirmed_stream(windows):
    """Preserve earlier events, while reporting validity of latest closed window."""
    high_record = low_record = None
    result = []
    for window in windows:
        state, high, low = audit_window(window)
        if high is not None:
            high_record = high
        if low is not None:
            low_record = low
        result.append((state, high_record, low_record))
    return result


class Phase35DataValidity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start = 1794355200000
        cls.positive = [bar(cls.start + i * STEP, hi, lo)
                        for i, (hi, lo) in enumerate(
                            ((106, 103), (108, 104), (111, 99), (109, 101), (107, 102)))]

    def test_old_counterexample_is_now_invalid(self):
        shifted = [bar(x["t"], x["h"] - 111, x["l"] - 111) for x in self.positive]
        self.assertEqual(audit_window(shifted), ("INVALID", None, None))

    def test_nonpositive_price_any_window_position_rejected(self):
        for position in range(5):
            for value in ("0", "-0.01"):
                rows = [dict(x) for x in self.positive]
                rows[position]["l"] = Decimal(value)
                with self.subTest(position=position, value=value):
                    self.assertEqual(audit_window(rows), ("INVALID", None, None))

    def test_zero_open_or_close_rejected_by_positive_low_consistency(self):
        for field in ("o", "c"):
            rows = [dict(x) for x in self.positive]
            rows[2][field] = Decimal(0)
            # A zero body with a positive low is internally invalid.
            self.assertEqual(audit_window(rows), ("INVALID", None, None))

    def test_missing_and_irregular_timestamps_invalid(self):
        missing = [dict(x) for x in self.positive]
        missing[1]["c"] = None
        self.assertEqual(audit_window(missing), ("INVALID", None, None))
        gap = [dict(x) for x in self.positive]
        gap[3]["t"] += STEP
        gap[3]["end"] += STEP
        self.assertEqual(audit_window(gap), ("INVALID", None, None))

    def test_insufficient_history_separated_from_valid_no_pivot(self):
        self.assertEqual(audit_window(self.positive[:4])[0], "INSUFFICIENT")
        monotone = [bar(self.start + i * STEP, 105 + i, 100 + i) for i in range(5)]
        self.assertEqual(audit_window(monotone), ("VALID", None, None))

    def test_existing_positive_dual_extremum_kept(self):
        status, high, low = audit_window(self.positive)
        self.assertEqual(status, "VALID")
        self.assertEqual((high["price"], low["price"]), (111, 99))
        self.assertEqual(high["known"], self.start + 5 * STEP)

    def test_retention_does_not_imply_current_window_validity(self):
        bad = [dict(x) for x in self.positive]
        bad[4]["l"] = Decimal(0)
        records = confirmed_stream([self.positive, bad])
        self.assertEqual(records[0][0], "VALID")
        self.assertEqual(records[1][0], "INVALID")
        self.assertEqual(records[0][1:], records[1][1:])

    def test_source_build_hash_and_no_trade_features(self):
        hit = re.search(r'const string BUILD_ID = "(L08-0\.1\.3-([0-9a-f]{12}))"', SOURCE)
        self.assertIsNotNone(hit)
        self.assertEqual(hashlib.sha256(SOURCE.replace(hit.group(1), "__BUILD__", 1).encode()).hexdigest()[:12], hit.group(2))
        self.assertIn("low[offset] > 0", SOURCE)
        self.assertIn("[strictHigh, strictLow, validWindow, enough]", SOURCE)
        self.assertEqual(SOURCE.count("request.security("), 1)
        self.assertNotIn("strategy(", SOURCE)
        self.assertNotIn("alertcondition(", SOURCE)

    def test_status_updates_only_on_confirmed_bar_and_toggle(self):
        self.assertIn("var string pivotEvidence = ", SOURCE)
        self.assertIn("if chartOK and pivotProbe and barstate.isconfirmed\n    pivotEvidence :=", SOURCE)
        self.assertIn('"INVALID · 5m OHLC/clock window"', SOURCE)
        self.assertIn('"INSUFFICIENT · 5m history"', SOURCE)
        self.assertIn('"VALID · no new pivot"', SOURCE)
        self.assertIn('"M01 evidence"', SOURCE)
        self.assertIn('not pivotProbe ? "Off · research"', SOURCE)
        self.assertIn("retained historical confirmations", SOURCE)

    def test_original_lesson08_functions_and_panel_rows_unchanged(self):
        for begin, end in (
            ("// Deterministic core.", "// Pivots are only declared at the CLOSE"),
            ("nominalRisk(", "// Evaluate on every chart bar for stable history."),
            ("[overlap, departure, invalid, engulf] = barFacts(", "var box support = na"),
            ("var box support = na", "var table panel = table.new"),
        ):
            with self.subTest(begin=begin):
                self.assertEqual(SOURCE.split(begin, 1)[1].split(end, 1)[0],
                                 BASE.split(begin, 1)[1].split(end, 1)[0])
        for row in range(13):
            pattern = rf'(?m)^    row\(panel, {row}, .+$'
            self.assertEqual(re.findall(pattern, SOURCE), re.findall(pattern, BASE))
        self.assertEqual(SOURCE.count("label.new("), BASE.count("label.new("))

    def test_five_archived_binance_spot_pivots_unchanged(self):
        receipt = json.loads((ROOT / "docs/research/evidence/phase34-audit-paxgusdt-5m-2026-11-12.json").read_text())
        self.assertEqual(receipt["parameters"]["symbol"], "PAXGUSDT")
        candles = [
            {"t": int(r[0]), "end": int(r[6])+1, "o": Decimal(r[1]),
             "h": Decimal(r[2]), "l": Decimal(r[3]), "c": Decimal(r[4])}
            for r in receipt["rows"]
        ]
        origins = [
            ("2026-11-12T07:30:00Z", "low", "3952.13", "2026-11-12T07:45:00Z"),
            ("2026-11-12T07:55:00Z", "high", "3961.97", "2026-11-12T08:10:00Z"),
            ("2026-11-12T09:00:00Z", "low", "3922.30", "2026-11-12T09:15:00Z"),
            ("2026-11-12T09:15:00Z", "low", "3922.84", "2026-11-12T09:30:00Z"),
            ("2026-11-12T09:55:00Z", "low", "3938.08", "2026-11-12T10:10:00Z"),
        ]
        ts = lambda s: int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp() * 1000)
        for origin, kind, price, known in origins:
            with self.subTest(origin=origin):
                index = next(i for i, b in enumerate(candles) if b["t"] == ts(origin))
                state, hi, lo = audit_window(candles[index - 2:index + 3])
                event = hi if kind == "high" else lo
                self.assertEqual(state, "VALID")
                self.assertIsNotNone(event)
                self.assertEqual(event["price"], Decimal(price))
                self.assertEqual(event["known"], ts(known))


if __name__ == "__main__":
    unittest.main()
