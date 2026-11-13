"""P36 I1 AI-only structure candidate: independent declared outcomes, not market claims."""

import unittest
from dataclasses import replace
from decimal import Decimal
import hashlib
import json
from pathlib import Path

from research.phase3_6.reference_model import Bar
from research.phase3_6.ai_structure_candidate import evaluate_structure, replay_structure, PROVENANCE


def sequence():
    values = (104, 103, 100, 103, 110, 107, 105, 108, 107, 106, 107, 112, 109, 108, 109)
    return tuple(Bar(i * 5, p, p + 1, p - 1, p) for i, p in enumerate(values))


def recross_sequence():
    closes = (104, 105, 94, 91, 96, 98, 91, 104, 101, 96, 100, 101, 106, 92, 93, 91, 96, 92, 97, 92, 109, 108)
    return tuple(Bar(i * 5, c, c + 1, c - 1, c) for i, c in enumerate(closes))


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
                evaluate_structure(sequence(), **({"as_of": 65} | kw))

    def test_no_bars_is_unknown_not_a_signal(self):
        result = evaluate_structure((), as_of=65)
        self.assertEqual(result.trend, "UNKNOWN")
        self.assertEqual(result.references, ())

    def test_prebreach_policies_diverge_without_backdating(self):
        tape = recross_sequence()
        a = replay_structure(tape, as_of=110)
        b = replay_structure(tape, as_of=110, policy="B")
        self.assertEqual(a[14].references[1].status, "PREBREACHED")
        self.assertEqual(a[16].references[1].status, "PREBREACHED")
        self.assertEqual(b[14].references[1].status, "RESET_PENDING")
        self.assertEqual(b[16].references[1].armed_at, 85)
        self.assertEqual([event for frame in a for event in frame.events], [])
        self.assertEqual([(e.cutoff, e.classification, e.predecessor_close, e.close)
                          for frame in b for e in frame.events],
                         [(90, "CHOCH_CANDIDATE_DOWN", 96, 92)])
        self.assertEqual(b[17].status, "POSSIBLE_SHIFT")
        self.assertEqual([r.status for r in b[17].retired], ["RETIRED", "CONSUMED"])

    def test_fresh_bos_uses_prior_snapshot_then_consumes_once(self):
        tape = (*sequence()[:14], Bar(70, 108, 116, 107, 115),
                Bar(75, 115, 116, 110, 111), Bar(80, 111, 116, 110, 115))
        frames = replay_structure(tape, as_of=85)
        events = [e for frame in frames for e in frame.events]
        self.assertEqual([(e.cutoff, e.classification) for e in events], [(75, "BOS_CANDIDATE_UP")])
        self.assertEqual(events[0].reference.first_regime_observed_at, 70)
        self.assertEqual(events[0].reference.level_ticks, 113)

    def test_malformed_current_and_missing_predecessor_do_not_emit(self):
        tape = (*sequence()[:14], Bar(70, 108, 110, 107, 115),
                Bar(75, 111, 116, 110, 115))
        for bad in (tape, (*tape[:14], tape[15]), (*tape[:14], replace(tape[14], received=76), tape[15])):
            with self.subTest(tape=bad):
                frames = replay_structure(bad, as_of=80)
                self.assertEqual(frames[14].status, "INSUFFICIENT")
                self.assertEqual([e for frame in frames for e in frame.events], [])
                self.assertEqual(frames[14].references, ())

    def test_frozen_binance_receipt_prefix_invariance(self):
        file = (Path(__file__).resolve().parents[1] / "docs/research/evidence"
                / "m07-paxgusdt-spot-v1/klines-5m.json")
        payload = file.read_bytes()
        self.assertEqual(hashlib.sha256(payload).hexdigest(),
                         "48c2cb774b312a6a7061fae4b9dd8fae8b0274cea0cb476f0a1e54033163e180")
        rows = json.loads(payload)["result"]
        tape = tuple(Bar(row[0] // 60_000, *(int(Decimal(p) * 100) for p in row[1:5])) for row in rows)
        self.assertEqual(len(tape), 288)
        for left in (1, 2, 3):
            for policy in ("A", "B"):
                full = replay_structure(tape, as_of=tape[-1].cutoff, policy=policy, left=left, right=left)
                self.assertEqual(len(full), 288)
                for n in (5, 72, 144, 216):
                    prefix = replay_structure(tape[:n], as_of=tape[n - 1].cutoff,
                                              policy=policy, left=left, right=left)
                    self.assertEqual(full[:n], prefix)
                events = [e for frame in full for e in frame.events]
                keys = {(e.reference.origin_open, e.reference.side, e.reference.level_ticks) for e in events}
                self.assertEqual(len(events), len(keys))
                self.assertTrue(all(e.cutoff >= e.reference.earliest_cross_close for e in events))
                for previous, current in zip(full, full[1:]):
                    if previous.status in {"UP", "DOWN"} and current.status == "POSSIBLE_SHIFT":
                        self.assertTrue(any(e.classification.startswith("CHOCH") for e in current.events))


if __name__ == "__main__":
    unittest.main()
