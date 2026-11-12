"""Research-only AI-defined strict-pivot structure pipeline.

No Coach-certified pivot scale, trade recommendation, backtest, or live signal.
As-of snapshots include only bars available at their modeled evaluation cutoff.
"""

from dataclasses import dataclass
from typing import Sequence

from research.phase3_6.reference_model import (
    Bar, Swing, INTERVAL, MARKET, strict_pivot, ordered_segment, regime
)

PROVENANCE = "AI_INDEPENDENT_EXPERIMENTAL"
ALLOWED_ROLES = {"UP": (("HH", "H"), ("HL", "L")),
                 "DOWN": (("LH", "H"), ("LL", "L"))}


@dataclass(frozen=True)
class CandidateReference:
    role: str
    origin_open: int
    side: str
    level_ticks: int
    pivot_known_at: int
    first_regime_observed_at: int
    earliest_cross_close: int
    policy: str = "S1_STRICT_PIVOT_UNSELECTED"
    provenance: str = PROVENANCE


@dataclass(frozen=True)
class StructureSnapshot:
    evaluated_at: int
    trend: str
    ordered: tuple[Swing, ...]
    raw_observations: tuple[Swing, ...]
    references: tuple[CandidateReference, ...]
    invalid_windows_first_seen: int
    unorderable_late_origins: int
    pending_windows: int
    origin_dual_ambiguous: int
    provenance: str = PROVENANCE


def _roles(segment, trend):
    if trend not in ALLOWED_ROLES:
        return ()
    out = []
    for name, side in ALLOWED_ROLES[trend]:
        points = [swing for swing in segment if swing.side == side]
        if len(points) < 2:
            return ()
        out.append((name, points[-1]))
    return tuple(out)


def evaluate_structure(
    bars: Sequence[Bar],
    *,
    as_of: int,
    left: int = 2,
    right: int = 2,
    compress: bool = False,
) -> StructureSnapshot:
    """Reconstruct causal historical chart-clock observations through as_of.

    Returned role references are *experimental proposals*, never actionable
    events. Earliest crossing close is at least one complete bar AFTER the
    reference first becomes eligible, and actual venue receipt is unverified.

    Missing windows invalidate their chronological swing segment once; later
    arrivals cannot retroactively modify older published snapshots. A late
    earlier-origin pivot is quarantined rather than spliced into past structure.
    """
    if type(as_of) is not int or as_of % INTERVAL:
        raise ValueError("as_of must be a 5m-aligned integer modeled cutoff")
    if type(left) is not int or type(right) is not int or not (1 <= left <= 8 and 1 <= right <= 8):
        raise ValueError("left/right must be declared integer settings 1..8")
    if not bars:
        return StructureSnapshot(as_of, "UNKNOWN", (), (), (), 0, 0, 0, 0)
    if any(type(b.start) is not int or b.start % INTERVAL for b in bars):
        raise ValueError("Bar origins must use aligned integer minute timestamps")

    earliest = min(b.start for b in bars)
    pending = set()
    batches = []
    raw = []
    missing_announced = set()
    released_origin = None
    observed_first = {}
    late_origins = 0
    dual_origins = 0

    for cutoff in range(earliest + INTERVAL, as_of + 1, INTERVAL):
        origin = cutoff - (right + 1) * INTERVAL
        if origin >= earliest + left * INTERVAL:
            pending.add(origin)

        now_batch = []
        for candidate in sorted(tuple(pending)):
            status, observations = strict_pivot(bars, candidate, left, right, cutoff)
            if status in {"PENDING", "INSUFFICIENT"}:
                if status == "INSUFFICIENT" and candidate not in missing_announced:
                    missing_announced.add(candidate)
                    batches.append(())
                continue
            pending.remove(candidate)
            if not observations:
                continue
            if released_origin is not None and candidate <= released_origin:
                late_origins += 1
                batches.append(())
                continue
            released_origin = candidate
            raw.extend(observations)
            if len(observations) > 1:
                dual_origins += 1
            now_batch.extend(observations)

        if now_batch:
            batches.append(tuple(now_batch))
        ordered = ordered_segment(batches, compress=compress)
        trend = regime(ordered)
        for role_name, point in _roles(ordered, trend):
            observed_first.setdefault((role_name, point.start, point.side, point.level), cutoff)

    ordered = ordered_segment(batches, compress=compress)
    trend = regime(ordered)
    refs = []
    for role_name, point in _roles(ordered, trend):
        seen = observed_first[(role_name, point.start, point.side, point.level)]
        refs.append(CandidateReference(
            role=role_name, origin_open=point.start, side=point.side,
            level_ticks=point.level, pivot_known_at=point.known,
            first_regime_observed_at=seen,
            earliest_cross_close=max(point.known, seen) + INTERVAL,
        ))
    return StructureSnapshot(
        evaluated_at=as_of, trend=trend, ordered=ordered,
        raw_observations=tuple(raw), references=tuple(refs),
        invalid_windows_first_seen=len(missing_announced),
        unorderable_late_origins=late_origins,
        pending_windows=len(pending), origin_dual_ambiguous=dual_origins,
    )
