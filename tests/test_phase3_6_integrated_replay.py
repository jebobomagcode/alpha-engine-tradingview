"""Finite integration checks against the accepted read-only v0.1.4 research contract.

The implementation is a Python shadow model, not a Pine interpreter.
"""
from decimal import Decimal
import json
import unittest
from pathlib import Path

from research.phase3_6.reference_model import Bar
from research.phase3_6.integrated_replay import replay_integrated

ROOT = Path(__file__).resolve().parents[1]


def frozen_tape():
    data = json.loads((ROOT / "docs/research/evidence/m07-paxgusdt-spot-v1/klines-5m.json").read_text())["result"]
    return tuple(Bar(row[0] // 60_000, *(int(Decimal(p) * 100) for p in row[1:5]))
                 for row in data)


class IntegratedLifecycleChecks(unittest.TestCase):
    def test_new_three_bar_gap_cannot_be_tested_on_creation_close(self):
        bars = (
            Bar(0, 100, 101, 99, 100),
            Bar(5, 100, 102, 99, 101),
            Bar(10, 106, 108, 105, 107),
            Bar(15, 108, 110, 101, 104),
        )
        result = replay_integrated(bars, as_of=20)
        self.assertIsNone(result[1].gap)
        self.assertEqual((result[2].gap.low, result[2].gap.high), (101, 105))
        self.assertEqual(result[2].gap.state, "OPEN")
        self.assertEqual(result[3].gap.state, "GEOMETRIC TEST")

    def test_fresh_three_bar_gap_replaces_latest_tested_gap(self):
        # The later candle tests GAP:15 yet also creates GAP:20.
        # Pine reports only the most recently created candidate.
        bars = (
            Bar(0, 100, 101, 99, 100),
            Bar(5, 100, 102, 99, 101),
            Bar(10, 106, 108, 105, 107),
            Bar(15, 108, 110, 103, 104),
        )
        frames = replay_integrated(bars, as_of=20)
        self.assertEqual(frames[2].gap.identity, "GAP:15")
        self.assertEqual(frames[3].gap.identity, "GAP:20")
        self.assertEqual(frames[3].gap.state, "OPEN")

    def test_missing_adjacent_bar_resets_gap_and_reaction_epoch(self):
        bars = (
            Bar(0, 100, 101, 99, 100),
            Bar(5, 100, 102, 99, 101),
            Bar(10, 106, 108, 105, 107),
            Bar(20, 108, 110, 103, 104),
        )
        result = replay_integrated(bars, as_of=25)
        self.assertIsNotNone(result[2].gap)
        self.assertIsNone(result[4].gap)
        self.assertEqual(result[4].reaction_status, "INSUFFICIENT · closed data")
        self.assertIsNone(result[4].episode.anchor)
        self.assertEqual(result[4].structural_status, "INSUFFICIENT")

    def test_unqualified_higher_timeframes_cannot_produce_reaction(self):
        result = replay_integrated(frozen_tape(), as_of=frozen_tape()[-1].cutoff)
        self.assertFalse(any(frame.reaction_observed for frame in result))
        self.assertTrue(all(frame.reaction_status == "INSUFFICIENT · closed data"
                            for frame in result))

    def test_context_scenarios_explicit_not_silently_inferred(self):
        bars = frozen_tape()
        unknown = replay_integrated(bars, as_of=bars[-1].cutoff)
        bearish = replay_integrated(bars, as_of=bars[-1].cutoff,
                                   confirmed_bullish_context=False)
        bullish = replay_integrated(bars, as_of=bars[-1].cutoff,
                                   confirmed_bullish_context=True)
        self.assertEqual(len(unknown), len(bearish))
        self.assertEqual(len(unknown), len(bullish))
        self.assertEqual(
            [(v.event_classes, v.reference_ids, v.block, v.gap) for v in unknown],
            [(v.event_classes, v.reference_ids, v.block, v.gap) for v in bullish],
        )
        self.assertFalse(any(v.reaction_observed for v in unknown))

    def test_prefix_invariance_for_width_policy_and_zone_lifecycle(self):
        tape = frozen_tape()
        self.assertEqual(len(tape), 288)
        for width in (1, 2, 3):
            for policy in ("A", "B"):
                with self.subTest(width=width, policy=policy):
                    full = replay_integrated(tape, as_of=tape[-1].cutoff,
                                             policy=policy, width=width)
                    self.assertEqual(len(full), 288)
                    for n in (16, 72, 144, 216):
                        short = replay_integrated(tape[:n], as_of=tape[n - 1].cutoff,
                                                  policy=policy, width=width)
                        self.assertEqual(full[:n], short)
                    self.assertTrue(all(not x.reaction_observed for x in full))
                    self.assertTrue(all(
                        block.known_at <= x.cutoff for x in full if (block := x.block)))
                    self.assertTrue(all(
                        gap.known_at <= x.cutoff for x in full if (gap := x.gap)))

    def test_bad_tolerance_is_rejected(self):
        for value in (-1, 0.2, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                replay_integrated((), as_of=5, support_tolerance_ticks=value)

    def test_consumed_support_reassesses_at_inclusive_band_boundary(self):
        closes = (104, 105, 94, 91, 96, 98, 91, 104, 101, 96, 100, 101, 106, 92, 93, 91, 96, 92)
        bars = tuple(Bar(i * 5, p, p + 1, p - 1, p) for i, p in enumerate(closes))
        a = replay_integrated(bars, as_of=90, confirmed_bullish_context=True, support_tolerance_ticks=3)
        b = replay_integrated(bars, as_of=90, policy="B",
                              confirmed_bullish_context=True, support_tolerance_ticks=3)
        self.assertEqual(a[-1].event_classes, ())
        self.assertEqual(b[-1].event_classes, ("CHOCH_CANDIDATE_DOWN",))
        self.assertEqual(b[-1].reaction_status, "REASSESS · support reference consumed")
        self.assertTrue(b[-1].episode.ended)
        self.assertFalse(b[-1].reaction_observed)

    def test_integrated_wick_comparator_changes_only_reaction(self):
        closes = (104, 105, 94, 91, 96, 98, 91, 104, 101, 96, 100, 101, 106, 92, 93, 91, 96)
        bars = tuple(Bar(i * 5, p, p + 1, p - 1, p) for i, p in enumerate(closes))
        bars += (Bar(85, 99, 102, 95, 101),)
        kw = dict(as_of=90, policy="B", confirmed_bullish_context=True, support_tolerance_ticks=3)
        strict = replay_integrated(bars, **kw)
        wick = replay_integrated(bars, **kw, wick_alternative=True)
        self.assertEqual(strict[:-1], wick[:-1])
        self.assertEqual(strict[-1].reaction_status, "WAIT · closed reaction")
        self.assertEqual(wick[-1].reaction_status, "OBSERVED · closed reaction")
        self.assertEqual(strict[-1].event_classes, wick[-1].event_classes)

    def test_htf_context_type_cannot_implicitly_coerce_numeric_or_text(self):
        for value in (0, 1, "UP", 1.0):
            with self.subTest(value=value), self.assertRaises(ValueError):
                replay_integrated((), as_of=5, confirmed_bullish_context=value)

    def test_static_pine_ordering_guards_remain_visible(self):
        source = (ROOT / "pine/alpha-engine-research.pine").read_text()
        extension = source.split("// Independent experimental extension.", 1)[1]
        close_gate = extension.index("if aiEnabled and chartOK and barstate.isconfirmed")
        cross = extension.index("bool crossHigh")
        block_update = extension.index('if contiguous and not na(aiBlockKnown)')
        contact = extension.index("bool touch")
        reaction = extension.index("bool reaction")
        gap_update = extension.index('if contiguous and not na(aiGapKnown)')
        gap_create = extension.index("if contiguous and adjacent[1]")
        pivot_admission = extension.index("if aiEnough and aiPivotValid")
        self.assertTrue(close_gate < cross < block_update < contact < reaction <
                        gap_update < gap_create < pivot_admission)
        self.assertIn("aiUpper.armedAt <= time", extension)
        self.assertIn("aiLower.armedAt <= time", extension)
        self.assertIn("aiBlockState := \"INVALIDATED\"", extension)
        self.assertIn('aiEpisodeEnded := true', extension)
        self.assertIn("time >= aiGapKnown and aiGapState == \"OPEN\"", extension)


if __name__ == "__main__":
    unittest.main()
