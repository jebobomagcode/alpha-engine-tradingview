"""Constructed-evidence research model. No market ingestion or trading logic."""

from dataclasses import dataclass
from itertools import groupby


INTERVAL = 5
MARKET = ("BINANCE", "Spot", "PAXGUSDT", "trade", INTERVAL)
ROLES = {
    ("UP", "HH"): ("H", "BOS_CANDIDATE_UP"),
    ("DOWN", "LL"): ("L", "BOS_CANDIDATE_DOWN"),
    ("DOWN", "LH"): ("H", "CHOCH_CANDIDATE_UP"),
    ("UP", "HL"): ("L", "CHOCH_CANDIDATE_DOWN"),
}


@dataclass(frozen=True)
class Bar:
    start: int
    open: int
    high: int
    low: int
    close: int
    received: int | None = None
    final: bool = True

    @property
    def cutoff(self):
        return self.start + INTERVAL

    @property
    def available(self):
        return self.cutoff if self.received is None else self.received

    def usable(self, as_of):
        prices = (self.open, self.high, self.low, self.close)
        return (
            self.final
            and self.cutoff <= self.available <= as_of
            and all(type(price) is int and price > 0 for price in prices)
            and self.low <= min(self.open, self.close)
            and max(self.open, self.close) <= self.high
        )


@dataclass(frozen=True)
class Swing:
    start: int
    side: str
    level: int
    cutoff: int
    known: int


def closed_at(bars, cutoff, as_of):
    matches = [bar for bar in bars if bar.cutoff == cutoff and bar.available <= as_of]
    if len(matches) == 1 and matches[0].usable(as_of):
        return matches[0]
    return None


def strict_pivot(bars, origin, left, right, as_of):
    last_cutoff = origin + (right + 1) * INTERVAL
    if as_of < last_cutoff:
        return "PENDING", ()
    window = [
        closed_at(bars, origin + (offset + 1) * INTERVAL, as_of)
        for offset in range(-left, right + 1)
    ]
    if None in window:
        return "INSUFFICIENT", ()
    center = window[left]
    others = window[:left] + window[left + 1:]
    known = max(bar.available for bar in window)
    pivots = []
    if center.high > max(bar.high for bar in others):
        pivots.append(Swing(origin, "H", center.high, last_cutoff, known))
    if center.low < min(bar.low for bar in others):
        pivots.append(Swing(origin, "L", center.low, last_cutoff, known))
    labels = ("NO_PIVOT", "OBSERVED", "DUAL_EXTREME_AMBIGUOUS")
    return labels[len(pivots)], tuple(pivots)


def ordered_segment(batches, *, compress=False):
    """Each batch is as delivered; an empty batch marks unusable continuity."""
    segment = []
    released_origin = None
    for batch in batches:
        if not batch:
            segment.clear()
            continue
        by_origin = sorted(batch, key=lambda candidate: candidate.start)
        for origin, observations in groupby(by_origin, key=lambda candidate: candidate.start):
            group = tuple(observations)
            if released_origin is not None and origin <= released_origin:
                segment.clear()
                continue
            released_origin = origin
            if len(group) != 1:
                segment.clear()
                continue
            pivot = group[0]
            if not segment or segment[-1].side != pivot.side:
                segment.append(pivot)
                continue
            if not compress:
                segment[:] = [pivot]
                continue
            previous = segment[-1]
            more_extreme = pivot.level > previous.level if pivot.side == "H" else pivot.level < previous.level
            if more_extreme:
                segment[-1] = pivot
    return tuple(segment)


def regime(segment):
    highs = [swing.level for swing in segment if swing.side == "H"]
    lows = [swing.level for swing in segment if swing.side == "L"]
    if len(highs) >= 2 and len(lows) >= 2:
        if highs[-2] < highs[-1] and lows[-2] < lows[-1]:
            return "UP"
        if highs[-2] > highs[-1] and lows[-2] > lows[-1]:
            return "DOWN"
    return "UNKNOWN"


@dataclass(frozen=True)
class Reference:
    swing: Swing
    trend: str
    role: str
    context_known: int
    market: tuple = MARKET
    declaration_known: int = 0
    buffer: int = 0

    @property
    def anchor(self):
        return self.market, self.swing.start, self.swing.side, self.swing.level


@dataclass(frozen=True)
class Frame:
    cutoff: int
    status: str
    event: str | None = None
    wick_test: bool = False


def replay(bars, reference, policy, boundaries, *, consumed=(), retire_at=None):
    """Use ordered phases at a modeled boundary, with no asynchronous backfill."""
    if policy not in {"A", "B", "HISTORY"}:
        raise ValueError("Choose an explicit arming policy")
    swing = reference.swing
    role = ROLES.get((reference.trend, reference.role))
    if role is None or role[0] != swing.side or reference.market != MARKET:
        return tuple(Frame(t, "INSUFFICIENT") for t in boundaries)
    if type(swing.level) is not int or type(reference.buffer) is not int or reference.buffer < 0:
        return tuple(Frame(t, "INSUFFICIENT") for t in boundaries)
    threshold = swing.level + reference.buffer if swing.side == "H" else swing.level - reference.buffer
    if swing.level <= 0 or threshold <= 0:
        return tuple(Frame(t, "INSUFFICIENT") for t in boundaries)
    if reference.anchor in consumed:
        return tuple(Frame(t, "CONSUMED") for t in boundaries)

    def beyond(price):
        return price > threshold if swing.side == "H" else price < threshold

    premise = max(swing.cutoff, swing.known, reference.context_known, reference.declaration_known)
    state = "WAIT"
    frames = []
    for now in boundaries:
        current = closed_at(bars, now, now)
        event = None
        wick = False
        display = state
        if state == "ARMED":
            previous = closed_at(bars, now - INTERVAL, now - INTERVAL)
            if current is None or previous is None:
                display = "INSUFFICIENT"
            elif not beyond(previous.close):
                wick_price = current.high if swing.side == "H" else current.low
                wick = beyond(wick_price)
                if beyond(current.close):
                    event = role[1]
                    state = "POSSIBLE_SHIFT" if event.startswith("CHOCH") else "CONSUMED"
                    display = state
        if retire_at is not None and now >= retire_at and state in {"WAIT", "ARMED", "RESET_PENDING"}:
            state = display = "RETIRED"
        if state == "WAIT" and now >= premise:
            history = (
                [closed_at(bars, t, now) for t in range(swing.cutoff + INTERVAL, now + 1, INTERVAL)]
                if policy == "HISTORY" else []
            )
            if current is None or None in history:
                display = "INSUFFICIENT"
            elif beyond(current.close):
                state = display = "RESET_PENDING" if policy == "B" else "PREBREACHED"
            elif any(beyond(bar.close) for bar in history):
                state = display = "HISTORY_VETO"
            else:
                state = display = "ARMED"
        elif state == "RESET_PENDING" and current is not None and not beyond(current.close):
            state = display = "ARMED"
        frames.append(Frame(now, display, event, wick))
    return tuple(frames)


def lesson08_structure_isolation(*, zone_known, contact, reaction_closed):
    if not zone_known or not contact:
        return "WAIT_ZONE"
    return "REACTION_EVIDENCE" if reaction_closed else "WAIT_REACTION"
