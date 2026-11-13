"""Research-only lifecycle oracle for bounded v0.1.4 Pine parity investigations.

This is a separately testable interpretation of the documented zone and
reaction lifecycle. It DOES NOT execute TradingView/Pine or prove native parity.
Input bars are synthetic integer-tick 5m closed evidence, not venue receipts.
"""
from dataclasses import dataclass, replace

PROVENANCE = "AI_INDEPENDENT_EXPERIMENTAL"


@dataclass(frozen=True)
class Candle:
    opened: int
    o: int
    h: int
    l: int
    c: int
    final: bool = True

    @property
    def cutoff(self):
        return self.opened + 5

    def valid(self):
        return (self.final and all(type(p) is int and p > 0 for p in
                (self.o, self.h, self.l, self.c)) and
                self.l <= min(self.o, self.c) <= self.h and
                self.l <= max(self.o, self.c) <= self.h)


@dataclass(frozen=True)
class Zone:
    identity: str
    kind: str  # BLOCK or GAP
    side: int  # +1 bullish, -1 bearish
    low: int
    high: int
    known_at: int
    state: str = "OPEN"


@dataclass(frozen=True)
class Episode:
    anchor: str | None = None
    touched: bool = False
    ended: bool = False


@dataclass(frozen=True)
class EpisodeDecision:
    state: Episode
    status: str
    overlap: bool = False
    reaction: bool = False


def advance_zone(zone: Zone, bar: Candle, *, adjacent: bool = True):
    """Return state at bar close. Admit/revise only if zone predates its open."""
    if zone.kind not in {"BLOCK", "GAP"} or zone.side not in (1, -1):
        raise ValueError("unsupported zone")
    if zone.low <= 0 or zone.high < zone.low or zone.known_at < 0:
        raise ValueError("malformed zone")
    if not adjacent or not bar.valid() or bar.opened < zone.known_at:
        return zone
    if zone.state == "INVALIDATED":
        return zone
    invalid = (zone.side == 1 and bar.c < zone.low) or (
        zone.side == -1 and bar.c > zone.high)
    overlap = bar.h >= zone.low and bar.l <= zone.high
    if zone.kind == "BLOCK" and invalid:
        return replace(zone, state="INVALIDATED")
    if zone.state == "OPEN" and overlap:
        return replace(zone, state="GEOMETRIC TEST")
    return zone


def advance_episode(
    previous: Episode,
    *,
    bar: Candle,
    predecessor: Candle | None,
    adjacent: bool,
    context_ok: bool,
    bullish_context: bool,
    armed_anchor: str | None,
    support_low: int | None,
    support_high: int | None,
    wick_alternative: bool = False,
) -> EpisodeDecision:
    """Contract mirror: evaluate only final bars and prior-open armed support.

    'armed_anchor' is supplied by the frozen structure reference ledger.
    This does not independently verify whether the structure was actually
    eligible. If a retired anchor reappears without a new identity, existing
    terminal episode state remains; that lifecycle choice requires native QA.
    """
    # Pine's enclosing finalized-bar evaluation clears the episode when
    # complete=false, because contiguous = complete and adjacent.
    if not bar.valid() or not adjacent:
        return EpisodeDecision(Episode(), "INSUFFICIENT · closed data")
    support = armed_anchor is not None and support_low is not None and support_high is not None
    if support and (support_low <= 0 or support_high < support_low):
        raise ValueError("invalid support")
    active = previous
    if support and previous.anchor != armed_anchor:
        active = Episode(anchor=armed_anchor)
    touch = support and bar.h >= support_low and bar.l <= support_high
    invalid = support and bar.c < support_low
    departure = support and active.touched and bar.l > support_high
    if invalid or departure:
        active = replace(active, ended=True)
    if touch and bullish_context and not active.ended:
        active = replace(active, touched=True)
    engulf = (predecessor is not None and predecessor.valid() and
              predecessor.c < predecessor.o and bar.c > bar.o and
              bar.o < predecessor.c and bar.c > predecessor.o)
    wick = (support and wick_alternative and bar.c > bar.o and
            min(bar.o, bar.c) - bar.l >= 2 * abs(bar.c - bar.o) and
            bar.c > support_high)
    reacted = bool(touch and bullish_context and not active.ended and (engulf or wick))
    if not context_ok:
        reason = "INSUFFICIENT · closed data"
    elif not bullish_context:
        reason = "WAIT · 1H / 4H bullish alignment"
    elif not support:
        reason = "WAIT · prior UP support"
    elif invalid:
        reason = "REASSESS · support closed through"
    elif active.ended:
        reason = "REASSESS · episode ended"
    elif not touch:
        reason = "WAIT · geometric overlap"
    elif reacted:
        reason = "OBSERVED · closed reaction"
    else:
        reason = "WAIT · closed reaction"
    return EpisodeDecision(active, reason, bool(touch), reacted)
