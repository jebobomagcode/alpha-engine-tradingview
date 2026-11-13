"""Source-projected Pine v0.1.4 transition helpers, for DIFFERENTIAL research.

This is independently transcribed from the frozen Pine source's updateRef,
block/gap and support reaction statements, not an execution of Pine or a
TradingView native acceptance. Model bar clock in integral minute cutoffs;
prices use integer quote ticks. There is no live feed or trading behavior.
"""
from dataclasses import dataclass, replace

from research.phase3_6.lifecycle_parity_oracle import Candle, Zone, Episode, EpisodeDecision


@dataclass(frozen=True)
class PineReference:
    origin: int | None = None
    armed_at: int | None = None
    level: int | None = None
    role: str = ""
    state: str = "WAIT"


def project_update_ref(
    previous: PineReference, *, origin: int | None, level: int | None,
    role: str, terminal_origin: int | None, terminal_status: str,
    above: bool, reset_allowed: bool, close: int, cutoff: int
) -> PineReference:
    """Exact branch priority of v0.1.4 updateRef; no idealized history ledger."""
    nxt = PineReference()
    if origin is not None:
        if level is None:
            raise ValueError("a declared reference must have a level")
        broken = close > level if above else close < level
        if origin == terminal_origin:
            return PineReference(
                origin,
                previous.armed_at if previous.origin == origin else None,
                level, role, terminal_status,
            )
        if previous.origin == origin and previous.role == role and previous.state == "ARMED":
            return previous
        if broken:
            return PineReference(
                origin, None, level, role,
                "RESET PENDING" if reset_allowed else "PREBREACHED",
            )
        return PineReference(origin, cutoff, level, role, "ARMED")
    return nxt


def project_cross(
    reference: PineReference, *, above: bool,
    previous_close: int, current_close: int, opened: int, adjacent: bool = True
) -> bool:
    """Pine's closed-bar first-cross formula for frozen previous-open refs."""
    if not adjacent or reference.state != "ARMED" or reference.armed_at is None:
        return False
    if reference.armed_at > opened or reference.level is None:
        return False
    if above:
        return previous_close <= reference.level < current_close
    return previous_close >= reference.level > current_close


def project_zone(zone: Zone, candle: Candle, *, adjacent: bool = True) -> Zone:
    """Pine block/gap update ordering; creation is external to this function."""
    if zone.kind not in {"BLOCK", "GAP"} or zone.side not in (1, -1):
        raise ValueError("unsupported zone")
    if zone.low <= 0 or zone.high < zone.low or zone.known_at < 0:
        raise ValueError("malformed zone")
    if (not adjacent or not candle.valid() or candle.opened < zone.known_at
            or zone.state == "INVALIDATED"):
        return zone
    if zone.kind == "BLOCK":
        invalidated = (zone.side == 1 and candle.c < zone.low) or (
            zone.side == -1 and candle.c > zone.high)
        if invalidated:
            return replace(zone, state="INVALIDATED")
    if candle.h >= zone.low and candle.l <= zone.high and zone.state == "OPEN":
        return replace(zone, state="GEOMETRIC TEST")
    return zone


def project_episode(
    previous: Episode, *, candle: Candle, predecessor: Candle | None,
    adjacent: bool, context_ok: bool, bullish_context: bool,
    armed_anchor: str | None, support_low: int | None,
    support_high: int | None, wick_alternative: bool = False,
) -> EpisodeDecision:
    """Model Pine's supportKnown, touch, invalidSupport, departure, reaction."""
    if not candle.valid() or not adjacent:
        return EpisodeDecision(Episode(), "INSUFFICIENT · closed data")
    support = (armed_anchor is not None and support_low is not None
               and support_high is not None)
    if support and (support_low <= 0 or support_high < support_low):
        raise ValueError("invalid support")
    episode = previous
    if support and (episode.anchor is None or episode.anchor != armed_anchor):
        episode = Episode(armed_anchor, False, False)
    touch = bool(support and candle.h >= support_low and candle.l <= support_high)
    invalid_support = bool(support and candle.c < support_low)
    departed = bool(support and episode.touched and candle.l > support_high)
    if departed or invalid_support:
        episode = replace(episode, ended=True)
    if touch and bullish_context and not episode.ended:
        episode = replace(episode, touched=True)
    engulfed = bool(
        predecessor is not None and predecessor.valid()
        and predecessor.c < predecessor.o and candle.c > candle.o
        and candle.o < predecessor.c and candle.c > predecessor.o)
    rejected = bool(
        wick_alternative and support and candle.c > candle.o
        and min(candle.o, candle.c) - candle.l >= 2 * abs(candle.c - candle.o)
        and candle.c > support_high)
    reacted = bool(touch and bullish_context and not episode.ended
                   and (engulfed or rejected))
    if not context_ok:
        status = "INSUFFICIENT · closed data"
    elif not bullish_context:
        status = "WAIT · 1H / 4H bullish alignment"
    elif not support:
        status = "WAIT · prior UP support"
    elif invalid_support:
        status = "REASSESS · support closed through"
    elif episode.ended:
        status = "REASSESS · episode ended"
    elif not touch:
        status = "WAIT · geometric overlap"
    elif reacted:
        status = "OBSERVED · closed reaction"
    else:
        status = "WAIT · closed reaction"
    return EpisodeDecision(episode, status, touch, reacted)
