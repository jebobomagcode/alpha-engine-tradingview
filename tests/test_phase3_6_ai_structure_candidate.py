"""P36 I1 AI-only structure candidate: independent declared outcomes, not market claims."""

import unittest
from dataclasses import replace

from research.phase3_6.reference_model import Bar
from research.phase3_6.ai_structure_candidate import evaluate_structure, PROVENANCE


def sequence():
    values = (104, 103, 100, 103, 110, 107, 105, 108, 107, 106, 107, 112, 109, 108, 109)
    return tuple(Bar(i * 5, p, p + 1, p - 1, p) for i, p in enumerate(values))


DUAL = (
    Bar(600, 101, 104, 100, 103),
    Bar(605, 102, 106, 99, 105),
    Bar(610, 100, 112, 95, 110),
    Bar(615, 107, 108, 98, 100),
    Bar(620, 102, 105, 100, 103),
)


class AIOnlyStructuralCandidateTests(unittest.TestCase):
    def test_original_shared_prefix_l2_r2_unknown_then_up(self):
        tape = sequence()
        before = evaluate_structure(tape, as_of=65, left=2, right=2)
        after = evaluate_structure(tape, as_of=70, left=2, right=2)
        self.assertEqual(before.trend, "UNKNOWN")
        self.assertEqual(after.trend, "UP")
        self.assertEqual({r.role for r in after.references}, {"HH", "HL"})
        self.assertTrue(all(r.earliest_cross_close > 70 for r in after.references))

    def test_window_setting_sensitivity_is_not_coach_certification(self):
        tape = sequence()
        narrow = evaluate_structure(tape, as_of=65, left=1, right=1)
        broad = evaluate_structure(tape, as_of=65, left=3, right=3)
        self.assertEqual(narrow.trend, "UP")
        self.assertEqual(broad.trend, "UNKNOWN")
        self.assertEqual(narrow.provenance, PROVENANCE)

    def test_asof_hides_future_bars_and_later_snapshots(self):
        tape = sequence()
        with_future = evaluate_structure(tape, as_of=65)
        without_future = evaluate_structure(tuple(b for b in tape if b.cutoff <= 65), as_of=65)
        self.assertEqual(with_future, without_future)

    def test_dual_extreme_does_not_assign_fabricated_ordinal_structure(self):
        before = evaluate_structure(DUAL, as_of=620, left=2, right=2)
        after = evaluate_structure(DUAL, as_of=625, left=2, right=2)
        self.assertEqual(before.raw_observations, ())
        self.assertEqual(after.trend, "UNKNOWN")
        self.assertEqual(after.origin_dual_ambiguous, 1)
        self.assertEqual(len(after.raw_observations), 2)
        self.assertEqual(after.references, ())

    def test_tie_disqualifies_one_side_not_both(self):
        tie = list(DUAL)
        tie[1] = replace(tie[1], high=112)
        outcome = evaluate_structure(tuple(tie), as_of=625)
        self.assertEqual([(p.side, p.level) for p in outcome.raw_observations], [("L", 95)])

    def test_missing_or_nonfinal_right_bar_must_not_confirm_pivot(self):
        missing = tuple(b for b in DUAL if b.start != 615)
        forming = tuple(replace(b, final=False) if b.start == 620 else b for b in DUAL)
        for case in (missing, forming):
            with self.subTest(case=case):
                result = evaluate_structure(case, as_of=625)
                self.assertEqual(result.raw_observations, ())
                self.assertGreater(result.invalid_windows_first_seen, 0)

    def test_delayed_left_observation_cannot_backdate_confirmation(self):
        initial = (
            Bar(575, 101, 103, 100, 102, received=603),
            Bar(580, 102, 104, 101, 103),
            Bar(585, 103, 106, 102, 104),
            Bar(590, 104, 105, 101, 103),
            Bar(595, 103, 105, 102, 104),
        )
        early = evaluate_structure(initial, as_of=600)
        late = evaluate_structure(initial, as_of=605)
        self.assertFalse(any(x.start == 585 for x in early.raw_observations))
        self.assertTrue(any(x.start == 585 and x.known == 603 for x in late.raw_observations))

    def test_invalid_parameter_settings_rejected(self):
        for kw in ({"left": 0}, {"right": 9}, {"left": 2.0}, {"as_of": 66}):
            with self.subTest(kw=kw), self.assertRaises(ValueError):
                evaluate_structure(sequence(), as_of=65, **kw)

    def test_no_bars_is_unknown_not_a_signal(self):
        result = evaluate_structure((), as_of=65)
        self.assertEqual(result.trend, "UNKNOWN")
        self.assertEqual(result.references, ())


if __name__ == "__main__":
    unittest.main()
