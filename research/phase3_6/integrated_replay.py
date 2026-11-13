"""Bounded as-of structural + zone + reaction research replay.

Reads constructed/frozen five-minute OHLC. Does not execute Pine, does not
authenticate venue receipts, and does not reconstruct 1H/4H from unavailable
source. Context availability is explicitly supplied, not inferred from a 5m
series. This is a candidate comparator, NOT a profitable trading system.
"""
from dataclasses import dataclass

from research.phase3_6.ai_structure_candidate import replay_structure
from research.phase3_6.reference_model import Bar, closed_at
from research.phase3_6.lifecycle_parity_oracle import (
    Candle, Episode, Zone, advance_episode, advance_zone
)


@dataclass(frozen=True)
class IntegratedFrame:
    cutoff: int
    structural_status: str
    reference_ids: tuple[str, ...]
    event_classes: tuple[str, ...]
    block: Zone | None
    gap: Zone | None
    episode: Episode
    reaction_status: str
    reaction_observed: bool


def _as_candle(bar):
    return Candle(bar.start, bar.open, bar.high, bar.low, bar.close, bar.final)


def _anchor_identity(reference):
    return f"{reference.origin_open}:{reference.side}:{reference.level_ticks}:{reference.role}"


def replay_integrated(bars: tuple[Bar, ...], *, as_of: int,
                      policy: str = "A", width: int = 2,
                      support_tolerance_ticks: int = 1,
                      confirmed_bullish_context: bool | None = None,
                      wick_alternative: bool = False,
                      ) -> tuple[IntegratedFrame, ...]:
    """Compare frozen structural refs to simple latest-only zone lifecycles.

    Context True/False must be externally qualified for the relevant 1H/4H
    period; None means unqualified and prevents reaction observations. This
    model is exploratory and does not infer HTF inputs from 5m bars.
    """
    if type(support_tolerance_ticks) is not int or support_tolerance_ticks < 0:
        raise ValueError("support tolerance must be nonnegative integer ticks")
    if confirmed_bullish_context is not None and type(confirmed_bullish_context) is not bool:
        raise ValueError("HTF context must be explicit bool or unavailable")
    if type(wick_alternative) is not bool:
        raise ValueError("wick alternative must be an explicit bool")

    source = {}
    for bar in bars:
        source.setdefault(bar.cutoff, []).append(bar)
    structure = replay_structure(bars, as_of=as_of, policy=policy,
                                 left=width, right=width)
    block = None
    gap = None
    episode = Episode()
    previous_frame = None
    result = []
    for frame in structure:
        cutoff = frame.structure.evaluated_at
        current = closed_at(source.get(cutoff, ()), cutoff, cutoff)
        predecessor = closed_at(source.get(cutoff - 5, ()), cutoff - 5, cutoff - 5)
        two_back = closed_at(source.get(cutoff - 10, ()), cutoff - 10, cutoff - 10)
        contiguous = (current is not None and predecessor is not None
                      and current.start == predecessor.start + 5)
        if not contiguous:
            block = None
            gap = None
            episode = Episode()

        if current is None:
            status = "INSUFFICIENT · closed data"
            reaction = False
        else:
            candle = _as_candle(current)
            if block is not None:
                block = advance_zone(block, candle, adjacent=contiguous)
            if gap is not None:
                gap = advance_zone(gap, candle, adjacent=contiguous)

            previous_refs = previous_frame.references if previous_frame is not None else ()
            protected = next(
                (item for item in previous_refs if item.reference.role == "HL"
                 and item.status == "ARMED" and item.armed_at is not None
                 and item.armed_at <= current.start), None)
            ref = protected.reference if protected is not None else None
            low = ref.level_ticks - support_tolerance_ticks if ref else None
            high = ref.level_ticks + support_tolerance_ticks if ref else None
            if low is not None and low <= 0:
                ref, low, high = None, None, None
            qualified = confirmed_bullish_context is not None
            reaction_result = advance_episode(
                episode, bar=candle,
                predecessor=_as_candle(predecessor) if predecessor is not None else None,
                adjacent=contiguous,
                context_ok=qualified,
                bullish_context=confirmed_bullish_context is True,
                armed_anchor=_anchor_identity(ref) if ref is not None else None,
                support_low=low, support_high=high,
                wick_alternative=wick_alternative,
                reference_consumed=ref is not None and any(event.reference == ref for event in frame.events),
            )
            episode = reaction_result.state
            status = reaction_result.status
            reaction = reaction_result.reaction

            # The structural event is observed at this close. The candidate
            # preceding body block becomes usable no earlier than NEXT bar.
            if contiguous and frame.events:
                for event in frame.events:
                    bullish = event.classification == "BOS_CANDIDATE_UP"
                    bearish = event.classification == "BOS_CANDIDATE_DOWN"
                    if ((bullish and predecessor.close < predecessor.open) or
                        (bearish and predecessor.close > predecessor.open)):
                        block = Zone(
                            identity=f"OB:{cutoff}:{event.reference.origin_open}",
                            kind="BLOCK", side=1 if bullish else -1,
                            low=predecessor.low, high=predecessor.high,
                            known_at=cutoff,
                        )

            # Use the prior two adjacent final candles as in Pine. This
            # candidate can only be tested on a later close.
            if contiguous and two_back is not None and predecessor.start == two_back.start + 5:
                if current.low > two_back.high or current.high < two_back.low:
                    bullish = current.low > two_back.high
                    gap = Zone(
                        identity=f"GAP:{cutoff}",
                        kind="GAP", side=1 if bullish else -1,
                        low=two_back.high if bullish else current.high,
                        high=current.low if bullish else two_back.low,
                        known_at=cutoff,
                    )

        result.append(IntegratedFrame(
            cutoff=cutoff, structural_status=frame.status,
            reference_ids=tuple(_anchor_identity(item.reference) + ":" + item.status
                                for item in frame.references),
            event_classes=tuple(event.classification for event in frame.events),
            block=block, gap=gap, episode=episode,
            reaction_status=status, reaction_observed=reaction,
        ))
        previous_frame = frame
    return tuple(result)
