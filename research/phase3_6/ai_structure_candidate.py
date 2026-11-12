"""Research-only AI-defined strict-pivot structure pipeline.

No Coach-certified pivot scale, trade recommendation, backtest, or live signal.
As-of snapshots include only bars available at their modeled evaluation cutoff.
"""

from dataclasses import dataclass
from collections import defaultdict
from typing import Sequence

from research.phase3_6.reference_model import (
    Bar, Swing, INTERVAL, MARKET, ROLES, closed_at, strict_pivot, ordered_segment, regime
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


@dataclass(frozen=True)
class StructuralEvent:
    cutoff: int
    policy: str
    classification: str
    reference: CandidateReference
    predecessor_close: int
    close: int
    provenance: str = PROVENANCE


@dataclass(frozen=True)
class ActiveReference:
    reference: CandidateReference
    status: str
    armed_at: int | None


@dataclass(frozen=True)
class StructureFrame:
    structure: StructureSnapshot
    status: str
    references: tuple[ActiveReference, ...]
    events: tuple[StructuralEvent, ...]
    retired: tuple[ActiveReference, ...] = ()


def _roles(segment, trend):
    if trend not in ALLOWED_ROLES:
        return ()
    out = []
    for name, side in ALLOWED_ROLES[trend]:
        points = [swing for swing in segment if swing.side == side]
        if len(points) < 2:
            return ()
        out.append((name, points[-1]))
    return tuple(out) if out[0][1].level > out[1][1].level else ()


def evaluate_structure(
    bars: Sequence[Bar],
    *,
    as_of: int,
    left: int = 2,
    right: int = 2,
    compress: bool = False,
) -> StructureSnapshot:
    """Return the final causal structure snapshot at the modeled cutoff."""
    indexed = _index_bars(bars)
    _validate_settings(as_of, left, right)
    empty = StructureSnapshot(as_of, "UNKNOWN", (), (), (), 0, 0, 0, 0)
    snapshot = empty
    for snapshot in _snapshots(indexed, as_of, left, right, compress):
        pass
    return snapshot


def _validate_settings(as_of, left, right):
    if type(as_of) is not int or as_of % INTERVAL:
        raise ValueError("as_of must be a 5m-aligned integer modeled cutoff")
    if type(left) is not int or type(right) is not int or not (1 <= left <= 8 and 1 <= right <= 8):
        raise ValueError("left/right must be declared integer settings 1..8")


def _index_bars(bars):
    indexed = defaultdict(list)
    for bar in bars:
        if not isinstance(bar, Bar) or type(bar.start) is not int or bar.start % INTERVAL:
            raise ValueError("Bar origins must use aligned integer minute timestamps")
        if bar.received is not None and type(bar.received) is not int:
            raise ValueError("Modeled availability must use integer minutes")
        indexed[bar.cutoff].append(bar)
    return indexed


def _snapshots(indexed, as_of, left, right, compress):
    if not indexed:
        return
    earliest = min(indexed) - INTERVAL
    delayed = {}
    segment = ()
    raw = []
    released_origin = None
    active_first = {}
    missing_count = 0
    late_origins = 0
    dual_origins = 0
    usable = {}
    epoch_start = earliest
    arrivals = defaultdict(set)
    for end, versions in indexed.items():
        for bar in versions:
            if bar.available > end:
                arrivals[bar.available].add(end)

    for cutoff in range(earliest + INTERVAL, as_of + 1, INTERVAL):
        changed = set()
        for end in range(cutoff - INTERVAL + 1, cutoff + 1):
            for arrival in arrivals.get(end, ()):
                changed.add(arrival)
        changed.add(cutoff)
        for end in changed:
            usable[end] = closed_at(indexed.get(end, ()), end, cutoff)
        if any(usable[end] is None for end in changed):
            segment = ()
            active_first.clear()
            epoch_start = cutoff

        origin = cutoff - (right + 1) * INTERVAL
        candidates = {p for p, window in delayed.items() if changed.intersection(window)}
        if origin >= earliest + left * INTERVAL:
            candidates.add(origin)
        for candidate in sorted(candidates):
            window = range(candidate + (1 - left) * INTERVAL, candidate + (right + 2) * INTERVAL, INTERVAL)
            available = [usable.get(end) for end in window]
            if None in available:
                if candidate not in delayed:
                    delayed[candidate] = window
                    missing_count += 1
                continue
            delayed.pop(candidate, None)
            _, observations = strict_pivot(available, candidate, left, right, cutoff)
            if not observations:
                continue
            raw.extend(observations)
            if len(observations) > 1:
                dual_origins += 1
            if released_origin is not None and candidate <= released_origin:
                late_origins += 1
                segment = ()
                active_first.clear()
                continue
            released_origin = candidate
            if window.start - INTERVAL < epoch_start:
                continue
            segment = ordered_segment((segment, observations), compress=compress)

        trend = regime(segment)
        roles = _roles(segment, trend)
        if not roles:
            trend = "UNKNOWN"
        active_first = {
            (name, point): active_first.get((name, point), cutoff)
            for name, point in roles
        }
        refs = tuple(CandidateReference(
            role=name, origin_open=point.start, side=point.side,
            level_ticks=point.level, pivot_known_at=point.known,
            first_regime_observed_at=seen, earliest_cross_close=seen + INTERVAL,
        ) for (name, point), seen in active_first.items())
        yield StructureSnapshot(
            cutoff, trend, segment, tuple(raw), refs, missing_count, late_origins,
            len(delayed), dual_origins,
        )


def _anchor(reference):
    return MARKET, reference.origin_open, reference.side, reference.level_ticks


def _beyond(reference, price, buffer_ticks):
    if reference.side == "H":
        return price > reference.level_ticks + buffer_ticks
    return price < reference.level_ticks - buffer_ticks


def replay_structure(bars: Sequence[Bar], *, as_of: int, policy: str = "A",
                     left: int = 2, right: int = 2, compress: bool = False,
                     buffer_ticks: int = 0) -> tuple[StructureFrame, ...]:
    """Freeze prior-open references, evaluate the close, then arm the next interval."""
    _validate_settings(as_of, left, right)
    if policy not in {"A", "B"} or type(buffer_ticks) is not int or buffer_ticks < 0:
        raise ValueError("Choose policy A or B and a nonnegative integer tick buffer")
    indexed = _index_bars(bars)
    frames = []
    active = ()
    terminal = {}
    shift_at = None
    for snapshot in _snapshots(indexed, as_of, left, right, compress):
        now = snapshot.evaluated_at
        current = closed_at(indexed.get(now, ()), now, now)
        previous = closed_at(indexed.get(now - INTERVAL, ()), now - INTERVAL, now - INTERVAL)
        events = []
        if current is not None and previous is not None:
            for item in active:
                ref = item.reference
                if item.status != "ARMED" or not _beyond(ref, current.close, buffer_ticks):
                    continue
                if _beyond(ref, previous.close, buffer_ticks):
                    continue
                trend = "UP" if ref.role in {"HH", "HL"} else "DOWN"
                classification = ROLES[(trend, ref.role)][1]
                events.append(StructuralEvent(now, policy, classification, ref, previous.close, current.close))
                terminal[_anchor(ref)] = "CONSUMED"
                if classification.startswith("CHOCH"):
                    shift_at = now

        old = {item.reference: item for item in active}
        active = ()
        shift_pending = shift_at is not None and (
            len(snapshot.ordered) < 4 or snapshot.ordered[-4].start < shift_at
        )
        if not shift_pending and current is not None:
            active = tuple(_arm(ref, current.close, now, old.get(ref), terminal, policy, buffer_ticks)
                           for ref in snapshot.references)
        retained = {item.reference for item in active}
        retired = tuple(
            ActiveReference(ref, terminal.get(_anchor(ref), "RETIRED"), old[ref].armed_at)
            for ref in old if ref not in retained
        )
        if current is None:
            status = "INSUFFICIENT"
        elif shift_pending:
            status = "POSSIBLE_SHIFT"
        else:
            status = snapshot.trend
        frames.append(StructureFrame(snapshot, status, active, tuple(events), retired))
    return tuple(frames)


def _arm(ref, close, cutoff, old, terminal, policy, buffer_ticks):
    anchor = _anchor(ref)
    if ref.side == "L" and ref.level_ticks <= buffer_ticks:
        return ActiveReference(ref, "INSUFFICIENT", None)
    if anchor in terminal:
        return ActiveReference(ref, terminal[anchor], old.armed_at if old else None)
    if old is not None and old.status == "ARMED":
        return old
    if _beyond(ref, close, buffer_ticks):
        if policy == "B":
            return ActiveReference(ref, "RESET_PENDING", None)
        terminal[anchor] = "PREBREACHED"
        return ActiveReference(ref, "PREBREACHED", None)
    return ActiveReference(ref, "ARMED", cutoff)
