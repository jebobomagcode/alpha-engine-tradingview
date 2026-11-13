"""Finite hand-adjudicated synthetic cases for the v0.1.4 lifecycle proposal.

These run in Python CI only. Same-input Pine execution has NOT been performed.
"""
import unittest

from research.phase3_6.lifecycle_parity_oracle import (
    Candle, Zone, Episode, advance_zone, advance_episode
)


class BoundedLifecycleTests(unittest.TestCase):
    def test_new_block_is_not_tested_at_its_own_creation_close(self):
        block = Zone("ob-1", "BLOCK", 1, 97, 102, known_at=5)
        creation = Candle(0, 100, 103, 96, 100)
        next_bar = Candle(5, 100, 104, 98, 103)
        self.assertEqual(advance_zone(block, creation).state, "OPEN")
        self.assertEqual(advance_zone(block, next_bar).state, "GEOMETRIC TEST")

    def test_wrong_side_close_invalidates_even_when_wick_overlaps(self):
        bull = Zone("demand", "BLOCK", 1, 97, 102, known_at=5)
        bear = Zone("supply", "BLOCK", -1, 97, 102, known_at=5)
        self.assertEqual(advance_zone(bull, Candle(5, 98, 101, 95, 96)).state, "INVALIDATED")
        self.assertEqual(advance_zone(bear, Candle(5, 101, 104, 98, 103)).state, "INVALIDATED")

    def test_block_invalidation_persists_after_bounce(self):
        block = Zone("old", "BLOCK", 1, 97, 102, known_at=5)
        invalid = advance_zone(block, Candle(5, 98, 101, 95, 96))
        bounce = advance_zone(invalid, Candle(10, 96, 101, 94, 100))
        self.assertEqual(bounce.state, "INVALIDATED")

    def test_gap_is_geometry_only_not_an_order_fill_or_invalidation(self):
        gap = Zone("gap", "GAP", 1, 97, 102, known_at=5)
        self.assertEqual(advance_zone(gap, Candle(5, 105, 106, 103, 105)).state, "OPEN")
        tested = advance_zone(gap, Candle(10, 103, 104, 99, 100))
        self.assertEqual(tested.state, "GEOMETRIC TEST")
        self.assertEqual(advance_zone(tested, Candle(15, 100, 101, 90, 91)).state, "GEOMETRIC TEST")

    def test_nonfinal_and_missing_contiguity_withhold_zone_updates(self):
        block = Zone("ob", "BLOCK", -1, 97, 102, known_at=5)
        invalid = Candle(5, 102, 104, 100, 103)
        self.assertEqual(advance_zone(block, invalid, adjacent=False).state, "OPEN")
        self.assertEqual(advance_zone(block, Candle(5, 102, 104, 100, 103, final=False)).state, "OPEN")

    def test_first_contact_can_record_closed_engulf_same_bar(self):
        prev = Candle(0, 105, 106, 100, 101)
        bar = Candle(5, 100, 109, 98, 108)
        result = advance_episode(Episode(), bar=bar, predecessor=prev,
                                 adjacent=True, context_ok=True, bullish_context=True,
                                 armed_anchor="HL-1", support_low=98, support_high=102)
        self.assertTrue(result.overlap)
        self.assertTrue(result.reaction)
        self.assertEqual(result.status, "OBSERVED · closed reaction")
        self.assertTrue(result.state.touched)

    def test_support_closure_invalidates_before_same_bar_engulf(self):
        prev = Candle(0, 105, 106, 100, 101)
        bar = Candle(5, 100, 103, 95, 96)
        result = advance_episode(Episode(), bar=bar, predecessor=prev,
                                 adjacent=True, context_ok=True, bullish_context=True,
                                 armed_anchor="HL-1", support_low=97, support_high=102)
        self.assertEqual(result.status, "REASSESS · support closed through")
        self.assertFalse(result.reaction)
        self.assertTrue(result.state.ended)

    def test_departure_ends_existing_episode_and_blocks_later_touch(self):
        prior = Episode(anchor="HL-1", touched=True)
        departure = advance_episode(prior, bar=Candle(5, 104, 110, 104, 108),
                                    predecessor=Candle(0, 103, 107, 102, 104),
                                    adjacent=True, context_ok=True, bullish_context=True,
                                    armed_anchor="HL-1", support_low=97, support_high=102)
        self.assertTrue(departure.state.ended)
        self.assertEqual(departure.status, "REASSESS · episode ended")
        revisit = advance_episode(departure.state,
                                  bar=Candle(10, 108, 109, 99, 103),
                                  predecessor=Candle(5, 104, 110, 104, 108),
                                  adjacent=True, context_ok=True, bullish_context=True,
                                  armed_anchor="HL-1", support_low=97, support_high=102)
        self.assertEqual(revisit.status, "REASSESS · episode ended")
        self.assertFalse(revisit.reaction)

    def test_new_qualified_anchor_restarts_episode(self):
        old = Episode("HL-1", True, True)
        result = advance_episode(old, bar=Candle(5, 101, 105, 100, 104),
                                 predecessor=Candle(0, 102, 103, 101, 101),
                                 adjacent=True, context_ok=True, bullish_context=True,
                                 armed_anchor="HL-2", support_low=99, support_high=102)
        self.assertEqual(result.state.anchor, "HL-2")
        self.assertFalse(result.state.ended)

    def test_unqualified_context_never_promotes_a_trade(self):
        prev = Candle(0, 105, 106, 100, 101)
        bar = Candle(5, 100, 109, 98, 108)
        result = advance_episode(Episode(), bar=bar, predecessor=prev,
                                 adjacent=True, context_ok=False, bullish_context=False,
                                 armed_anchor="HL-1", support_low=98, support_high=102)
        self.assertEqual(result.status, "INSUFFICIENT · closed data")
        self.assertFalse(result.reaction)

    def test_malformed_final_candle_clears_stale_episode(self):
        """Pine marks incomplete OHLC contiguous=false and resets the epoch."""
        before = Episode("HL-1", touched=True, ended=True)
        malformed = Candle(10, 100, 101, 102, 99)
        result = advance_episode(
            before, bar=malformed, predecessor=Candle(5, 100, 104, 97, 103),
            adjacent=True, context_ok=True, bullish_context=True,
            armed_anchor="HL-1", support_low=97, support_high=102)
        self.assertEqual(result.status, "INSUFFICIENT · closed data")
        self.assertEqual(result.state, Episode())
        self.assertFalse(result.reaction)

    def test_nonfinal_candle_clears_stale_episode_in_research_projection(self):
        before = Episode("HL-1", touched=True, ended=True)
        forming = Candle(10, 100, 104, 97, 103, final=False)
        result = advance_episode(
            before, bar=forming, predecessor=Candle(5, 100, 104, 97, 103),
            adjacent=True, context_ok=True, bullish_context=True,
            armed_anchor="HL-1", support_low=97, support_high=102)
        self.assertEqual(result.status, "INSUFFICIENT · closed data")
        self.assertEqual(result.state, Episode())
        self.assertFalse(result.reaction)

    def test_gap_clears_reaction_state_without_claiming_event(self):
        old = Episode("HL-1", True, True)
        result = advance_episode(old, bar=Candle(10, 101, 104, 97, 99),
                                 predecessor=None, adjacent=False, context_ok=True,
                                 bullish_context=True, armed_anchor=None,
                                 support_low=None, support_high=None)
        self.assertEqual(result.status, "INSUFFICIENT · closed data")
        self.assertEqual(result.state, Episode())


if __name__ == "__main__":
    unittest.main()
