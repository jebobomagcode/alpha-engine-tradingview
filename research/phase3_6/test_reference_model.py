"""Pinned expectations adjudicated from constructed closed bars and declarations."""

from dataclasses import replace
import unittest

from reference_model import (
    Bar, Frame, Reference, Swing, lesson08_structure_isolation, ordered_segment,
    regime, replay, strict_pivot,
)


OUTSIDE = (
    Bar(600, 101, 104, 100, 103),
    Bar(605, 102, 106, 99, 105),
    Bar(610, 100, 112, 95, 110),
    Bar(615, 107, 108, 98, 100),
    Bar(620, 102, 105, 100, 103),
)
SWING_WINDOW = (
    Bar(575, 101, 103, 100, 102),
    Bar(580, 102, 104, 101, 103),
    Bar(585, 103, 106, 102, 104),
    Bar(590, 104, 105, 101, 103),
    Bar(595, 103, 105, 102, 104),
)
EXCURSION = Bar(600, 104, 108, 103, 107)
PERSISTS = Bar(605, 107, 108, 105, 107)
RETURNS = Bar(605, 107, 108, 104, 105)
RESET = Bar(610, 106, 107, 104, 105)
RECROSS = Bar(615, 105, 109, 104, 108)
ARM_BOUNDARIES = (600, 605, 610, 615, 620)
KNOWN_HIGH = Swing(585, "H", 106, 600, 600)
HIGH_REF = Reference(KNOWN_HIGH, "UP", "HH", 600)


def events(frames):
    return [(frame.cutoff, frame.event) for frame in frames if frame.event is not None]


def declared(origin, side, level, known=None):
    return Swing(origin, side, level, origin + 15, origin + 15 if known is None else known)


class StructuralCases(unittest.TestCase):
    def test_f01_dual_strict_window_is_observed_but_unordered(self):
        self.assertEqual(strict_pivot(OUTSIDE, 610, 2, 2, 624), ("PENDING", ()))
        result, raw = strict_pivot(OUTSIDE, 610, 2, 2, 625)
        self.assertEqual(result, "DUAL_EXTREME_AMBIGUOUS")
        self.assertEqual(raw, (Swing(610, "H", 112, 625, 625), Swing(610, "L", 95, 625, 625)))
        self.assertEqual(ordered_segment([raw]), ())

    def test_f02_tie_disqualifies_only_its_side(self):
        high_tie = (OUTSIDE[0], replace(OUTSIDE[1], high=112), *OUTSIDE[2:])
        low_tie = (*OUTSIDE[:3], replace(OUTSIDE[3], low=95), OUTSIDE[4])
        self.assertEqual(strict_pivot(high_tie, 610, 2, 2, 625), ("OBSERVED", (Swing(610, "L", 95, 625, 625),)))
        self.assertEqual(strict_pivot(low_tie, 610, 2, 2, 625), ("OBSERVED", (Swing(610, "H", 112, 625, 625),)))

    def test_f03_gap_invalid_and_duplicate_are_insufficient(self):
        bad_windows = (
            (*OUTSIDE[:3], OUTSIDE[4], Bar(625, 103, 106, 101, 104)),
            (*OUTSIDE[:3], replace(OUTSIDE[3], low=0), OUTSIDE[4]),
            (*OUTSIDE[:3], replace(OUTSIDE[3], high=106), OUTSIDE[4]),
            (*OUTSIDE[:3], replace(OUTSIDE[3], final=False), OUTSIDE[4]),
            (*OUTSIDE, OUTSIDE[3]),
        )
        for bars in bad_windows:
            with self.subTest(bars=bars):
                self.assertEqual(strict_pivot(bars, 610, 2, 2, 630), ("INSUFFICIENT", ()))

    def test_f04_two_turns_cannot_establish_regime(self):
        pair = (declared(570, "H", 110), declared(580, "L", 100))
        self.assertEqual(regime(pair), "UNKNOWN")

    def test_f05_confirmed_high_then_unreverted_prebreach(self):
        bars = (*SWING_WINDOW, EXCURSION, PERSISTS, RESET, RECROSS)
        self.assertEqual(strict_pivot(bars, 585, 2, 2, 600), ("OBSERVED", (KNOWN_HIGH,)))
        ref = replace(HIGH_REF, context_known=610)
        a = replay(bars, ref, "A", ARM_BOUNDARIES)
        b = replay(bars, ref, "B", ARM_BOUNDARIES)
        self.assertEqual([frame.status for frame in a], ["WAIT", "WAIT", "PREBREACHED", "PREBREACHED", "PREBREACHED"])
        self.assertEqual([frame.status for frame in b], ["WAIT", "WAIT", "RESET_PENDING", "ARMED", "CONSUMED"])
        self.assertEqual(events(a), [])
        self.assertEqual(events(b), [(620, "BOS_CANDIDATE_UP")])
        self.assertEqual(events(replay(bars, ref, "HISTORY", ARM_BOUNDARIES)), [])

    def test_f06_return_before_arm_separates_latest_close_from_history(self):
        bars = (*SWING_WINDOW, EXCURSION, RETURNS, RESET, RECROSS)
        ref = replace(HIGH_REF, context_known=610)
        for policy in ("A", "B"):
            with self.subTest(policy=policy):
                actual = replay(bars, ref, policy, ARM_BOUNDARIES)
                self.assertEqual(actual[2], Frame(610, "ARMED"))
                self.assertEqual(events(actual), [(620, "BOS_CANDIDATE_UP")])
        history = replay(bars, ref, "HISTORY", ARM_BOUNDARIES)
        self.assertEqual(history[2], Frame(610, "HISTORY_VETO"))
        self.assertEqual(events(history), [])

    def test_f07_consumed_anchor_cannot_reemit_under_role_alias(self):
        bars = (*SWING_WINDOW, EXCURSION, PERSISTS, RESET, RECROSS)
        self.assertEqual(events(replay(bars, HIGH_REF, "A", ARM_BOUNDARIES)), [(605, "BOS_CANDIDATE_UP")])
        alias = replace(HIGH_REF, trend="DOWN", role="LH", context_known=615)
        self.assertEqual(replay(bars, alias, "A", (615, 620), consumed=(HIGH_REF.anchor,)),
                         (Frame(615, "CONSUMED"), Frame(620, "CONSUMED")))

    def test_f08_wick_and_close_comparison(self):
        wick = Bar(600, 104, 108, 103, 105)
        bars = (*SWING_WINDOW, wick)
        self.assertEqual(replay(bars, HIGH_REF, "A", (600, 605))[-1], Frame(605, "ARMED", wick_test=True))
        closed = (*SWING_WINDOW, replace(wick, close=107))
        self.assertEqual(replay(closed, HIGH_REF, "A", (600, 605))[-1],
                         Frame(605, "CONSUMED", "BOS_CANDIDATE_UP", True))

    def test_f09_regime_arrival_at_close_cannot_classify_that_bar(self):
        bars = (*SWING_WINDOW, EXCURSION, RETURNS, Bar(610, 105, 109, 104, 108))
        at_previous_boundary = replay(bars, HIGH_REF, "A", (600, 605))
        self.assertEqual(events(at_previous_boundary), [(605, "BOS_CANDIDATE_UP")])
        at_crossing_close = replace(HIGH_REF, context_known=605)
        self.assertEqual(replay(bars, at_crossing_close, "A", (600, 605))[-1], Frame(605, "PREBREACHED"))
        reset = replay(bars, at_crossing_close, "B", ARM_BOUNDARIES[:-1])
        self.assertEqual(events(reset), [(615, "BOS_CANDIDATE_UP")])

    def test_f10_choch_is_possible_shift_in_both_directions(self):
        low = Swing(585, "L", 96, 600, 600)
        rising = (*SWING_WINDOW, EXCURSION)
        falling = tuple(Bar(bar.start, 202 - bar.open, 202 - bar.low, 202 - bar.high, 202 - bar.close)
                        for bar in rising)
        self.assertEqual(strict_pivot(falling, 585, 2, 2, 600), ("OBSERVED", (low,)))
        for bars, ref, event in (
            (rising, replace(HIGH_REF, trend="DOWN", role="LH"), "CHOCH_CANDIDATE_UP"),
            (falling, Reference(low, "UP", "HL", 600), "CHOCH_CANDIDATE_DOWN"),
        ):
            with self.subTest(event=event):
                self.assertEqual(replay(bars, ref, "A", (600, 605))[-1], Frame(605, "POSSIBLE_SHIFT", event, True))
                self.assertEqual(replay(bars, ref, "A", (600, 605, 610))[-1], Frame(610, "POSSIBLE_SHIFT"))
        self.assertEqual(events(replay(falling, Reference(low, "DOWN", "LL", 600), "A", (600, 605))),
                         [(605, "BOS_CANDIDATE_DOWN")])

    def test_f11_later_context_reassessment_preserves_prior_prefix(self):
        bars = (*SWING_WINDOW, Bar(600, 104, 105, 103, 104), Bar(605, 104, 106, 103, 105),
                Bar(610, 105, 109, 104, 108))
        prefix = replay(bars[:6], HIGH_REF, "A", (600, 605))
        extended = replay(bars, HIGH_REF, "A", (600, 605, 610, 615), retire_at=610)
        self.assertEqual(extended, (*prefix, Frame(610, "RETIRED"), Frame(615, "RETIRED")))

    def test_f12_wrong_product_timeframe_or_late_manual_declaration(self):
        bars = (*SWING_WINDOW, EXCURSION)
        for market in (("OTHER", "Spot", "PAXGUSDT", "trade", 5), ("BINANCE", "Perp", "PAXGUSDT", "trade", 5),
                       ("BINANCE", "Spot", "PAXGUSDT", "trade", 60), ("BINANCE", "Spot", "PAXGUSDT", "mark", 5)):
            with self.subTest(market=market):
                ref = replace(HIGH_REF, market=market)
                self.assertEqual(replay(bars, ref, "A", (600, 605))[-1], Frame(605, "INSUFFICIENT"))
        late = replace(HIGH_REF, declaration_known=610)
        self.assertEqual(replay(bars, late, "A", (600, 605))[-1], Frame(605, "WAIT"))

    def test_f13_structural_event_cannot_promote_lesson08(self):
        bars = (*SWING_WINDOW, EXCURSION)
        self.assertEqual(events(replay(bars, HIGH_REF, "A", (600, 605))), [(605, "BOS_CANDIDATE_UP")])
        self.assertEqual(lesson08_structure_isolation(zone_known=False, contact=False, reaction_closed=True), "WAIT_ZONE")
        self.assertEqual(lesson08_structure_isolation(zone_known=True, contact=True, reaction_closed=False), "WAIT_REACTION")

    def test_f14_same_side_extrema_need_explicit_policy(self):
        sequence = (
            declared(550, "L", 90), declared(560, "H", 105), declared(570, "L", 95),
            declared(580, "H", 111), declared(590, "H", 104),
        )
        batches = [(swing,) for swing in sequence]
        self.assertEqual(ordered_segment(batches), (sequence[-1],))
        self.assertEqual(regime(ordered_segment(batches)), "UNKNOWN")
        self.assertEqual(ordered_segment(batches, compress=True), sequence[:4])
        self.assertEqual(regime(ordered_segment(batches, compress=True)), "UP")
        mirrored = tuple(replace(p, side={"H": "L", "L": "H"}[p.side], level=220 - p.level) for p in sequence)
        self.assertEqual(regime(ordered_segment([(p,) for p in mirrored], compress=True)), "DOWN")

    def test_f15_late_left_bar_moves_known_at_but_never_backfills_old_frame(self):
        bars = (replace(SWING_WINDOW[0], received=603), *SWING_WINDOW[1:], EXCURSION, PERSISTS)
        self.assertEqual(strict_pivot(bars, 585, 2, 2, 600), ("INSUFFICIENT", ()))
        observed = Swing(585, "H", 106, 600, 603)
        self.assertEqual(strict_pivot(bars, 585, 2, 2, 603), ("OBSERVED", (observed,)))
        self.assertEqual(replay(bars, replace(HIGH_REF, swing=observed), "A", (600, 605, 610)),
                         (Frame(600, "WAIT"), Frame(605, "PREBREACHED"), Frame(610, "PREBREACHED")))

    def test_f16_equality_and_one_tick_buffer(self):
        bars = (*SWING_WINDOW, Bar(600, 104, 107, 103, 106), Bar(605, 106, 108, 104, 107),
                Bar(610, 107, 109, 105, 108))
        self.assertEqual(events(replay(bars, HIGH_REF, "A", (600, 605, 610, 615))), [(610, "BOS_CANDIDATE_UP")])
        buffered = replace(HIGH_REF, buffer=1)
        self.assertEqual(events(replay(bars, buffered, "A", (600, 605, 610, 615))), [(615, "BOS_CANDIDATE_UP")])
        bad = Reference(Swing(585, "L", 1, 600, 600), "DOWN", "LL", 600, buffer=1)
        self.assertEqual(replay(bars, bad, "A", (600,)), (Frame(600, "INSUFFICIENT"),))

    def test_f17_same_batch_can_order_distinct_origins_but_late_origin_splits(self):
        p1, p2, p3 = declared(550, "L", 90, 590), declared(560, "H", 106, 590), declared(570, "L", 95, 590)
        self.assertEqual(ordered_segment([(p3, p1, p2)]), (p1, p2, p3))
        self.assertEqual(ordered_segment([(p1,), (p3,), (replace(p2, known=595),)]), ())
        self.assertEqual(ordered_segment([(p1, p2), (), (p3,)]), (p3,))

    def test_f18_missing_or_late_predecessor_and_complete_history_are_distinct(self):
        missing = (*SWING_WINDOW, RETURNS, RESET, RECROSS)
        ref = replace(HIGH_REF, context_known=610)
        self.assertEqual(replay(missing, ref, "HISTORY", ARM_BOUNDARIES)[2], Frame(610, "INSUFFICIENT"))
        self.assertEqual(events(replay(missing, ref, "A", ARM_BOUNDARIES)), [(620, "BOS_CANDIDATE_UP")])
        late = (*SWING_WINDOW, replace(Bar(600, 104, 105, 103, 104), received=607), RETURNS)
        actual = replay(late, HIGH_REF, "A", (600, 605, 610))
        self.assertEqual(actual, (Frame(600, "ARMED"), Frame(605, "INSUFFICIENT"), Frame(610, "INSUFFICIENT")))

    def test_f19_outside_wicks_do_not_establish_crossing_order_or_two_closes(self):
        bar = Bar(600, 104, 108, 94, 104)
        down_ref = Reference(Swing(580, "L", 101, 585, 595), "UP", "HL", 600)
        for ref in (HIGH_REF, down_ref):
            with self.subTest(side=ref.swing.side):
                self.assertEqual(replay((*SWING_WINDOW, bar), ref, "A", (600, 605))[-1],
                                 Frame(605, "ARMED", wick_test=True))

    def test_f20_required_right_bar_breach_rejects_strict_high(self):
        impossible = (*SWING_WINDOW[:4], Bar(595, 103, 108, 102, 107), EXCURSION)
        self.assertEqual(strict_pivot(impossible, 585, 2, 2, 600), ("NO_PIVOT", ()))

    def test_s0_s1_same_prefix_role_and_scale_disagreement(self):
        closes = (104, 103, 100, 103, 110, 107, 105, 108, 107, 106, 107, 112, 109, 108, 109)
        bars = tuple(Bar(i * 5, c, c + 1, c - 1, c) for i, c in enumerate(closes))
        manual = (Swing(10, "L", 99, 15, 65), Swing(20, "H", 111, 25, 65),
                  Swing(30, "L", 104, 35, 65), Swing(55, "H", 113, 60, 65))
        self.assertEqual(regime(manual), "UP")

        def strict_segment(left_right, cutoff):
            raw = [strict_pivot(bars, bar.start, left_right, left_right, cutoff)[1] for bar in bars]
            return ordered_segment([observations for observations in raw if observations])

        earlier = strict_segment(2, 65)
        self.assertEqual([(p.start, p.side, p.level) for p in earlier],
                         [(10, "L", 99), (20, "H", 111), (30, "L", 104), (35, "H", 109), (45, "L", 105)])
        self.assertEqual(regime(earlier), "UNKNOWN")
        self.assertEqual(regime(strict_segment(1, 65)), "UP")
        self.assertEqual(regime(strict_segment(2, 70)), "UP")
        self.assertEqual(regime(strict_segment(3, 75)), "UNKNOWN")
        self.assertEqual(strict_segment(2, 70)[-2].level, 105)


if __name__ == "__main__":
    unittest.main()
