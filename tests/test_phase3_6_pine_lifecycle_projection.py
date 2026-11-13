"""Differential model checks, NOT Pine runtime acceptance.

Both copies are separate Python source interpretations. The frozen Pine source
is inspected for key transition guards, but only TradingView can execute Pine.
"""
from itertools import product
from pathlib import Path
import unittest

from research.phase3_6.lifecycle_parity_oracle import (
    Candle, Zone, Episode, advance_zone, advance_episode
)
from research.phase3_6.pine_lifecycle_projection import (
    PineReference, project_update_ref, project_cross, project_zone, project_episode
)

ROOT = Path(__file__).resolve().parents[1]


class PineSourceProjectedTransitionTests(unittest.TestCase):
    def test_zone_differential_grid(self):
        checked = 0
        for side, kind, state, close, open_price, known_at in product(
                (-1, 1), ("BLOCK", "GAP"),
                ("OPEN", "GEOMETRIC TEST", "INVALIDATED"),
                (94, 98, 101, 105), (96, 100, 104), (5, 10)):
            candle = Candle(5, open_price, max(open_price, close) + 2,
                            min(open_price, close) - 2, close)
            zone = Zone("z", kind, side, 97, 102, known_at, state)
            got = project_zone(zone, candle)
            want = advance_zone(zone, candle)
            self.assertEqual(got, want)
            checked += 1
        self.assertEqual(checked, 288)

    def test_episode_differential_grid(self):
        checked = 0
        for episode, close, open_price, bullish, context, support, wick, predecessor in product(
                (Episode(), Episode("A"), Episode("A", True), Episode("A", True, True)),
                (95, 99, 104, 109), (96, 101, 105),
                (False, True), (False, True), (False, True),
                (False, True),
                (Candle(0, 106, 108, 99, 100), Candle(0, 99, 103, 96, 101))):
            candle = Candle(5, open_price, max(open_price, close) + 2,
                            min(open_price, close) - 2, close)
            kw = dict(
                bar=candle, predecessor=predecessor, adjacent=True,
                context_ok=context, bullish_context=bullish,
                armed_anchor="A" if support else None,
                support_low=97 if support else None,
                support_high=102 if support else None,
                wick_alternative=wick)
            want = advance_episode(episode, **kw)
            proj = project_episode(episode, candle=kw.pop("bar"), **kw)
            self.assertEqual(proj, want)
            checked += 1
        self.assertEqual(checked, 1536)

    def test_invalid_final_bar_epoch_reset_matches_oracle(self):
        invalid = Candle(5, 100, 99, 101, 98)
        previous = Episode("HL-1", touched=True, ended=True)
        kw = dict(predecessor=Candle(0, 99, 104, 96, 101),
                  adjacent=True, context_ok=True, bullish_context=True,
                  armed_anchor="HL-1", support_low=97, support_high=102)
        self.assertEqual(
            project_episode(previous, candle=invalid, **kw),
            advance_episode(previous, bar=invalid, **kw))
        self.assertEqual(
            project_episode(previous, candle=invalid, **kw).state, Episode())

    def test_reference_arming_and_prebreach_policies(self):
        none = PineReference()
        a = project_update_ref(
            none, origin=10, level=100, role="HL",
            terminal_origin=None, terminal_status="", above=False,
            reset_allowed=False, close=99, cutoff=30)
        b = project_update_ref(
            none, origin=10, level=100, role="HL",
            terminal_origin=None, terminal_status="", above=False,
            reset_allowed=True, close=99, cutoff=30)
        self.assertEqual(a.state, "PREBREACHED")
        self.assertEqual(b.state, "RESET PENDING")
        self.assertIsNone(b.armed_at)
        reset = project_update_ref(
            b, origin=10, level=100, role="HL",
            terminal_origin=None, terminal_status="", above=False,
            reset_allowed=True, close=102, cutoff=35)
        self.assertEqual((reset.state, reset.armed_at), ("ARMED", 35))
        self.assertFalse(project_cross(
            reset, above=False, previous_close=102, current_close=99, opened=30))
        self.assertTrue(project_cross(
            reset, above=False, previous_close=102, current_close=99, opened=35))
        consumed = project_update_ref(
            reset, origin=10, level=100, role="HL",
            terminal_origin=10, terminal_status="CONSUMED", above=False,
            reset_allowed=True, close=99, cutoff=40)
        self.assertEqual(consumed.state, "CONSUMED")
        self.assertFalse(project_cross(
            consumed, above=False, previous_close=102, current_close=99, opened=40))

    def test_terminal_origin_is_only_one_slot_not_full_historical_ledger(self):
        # This pins a bounded source limitation, not an independently observed
        # trading event: if an old exact origin is reintroduced after a newer
        # terminal origin, updateRef alone can arm the old origin again.
        old = PineReference(origin=10, armed_at=30, level=100,
                            role="HH", state="CONSUMED")
        newer = project_update_ref(
            old, origin=20, level=110, role="HH",
            terminal_origin=20, terminal_status="CONSUMED",
            above=True, reset_allowed=False, close=100, cutoff=40)
        old_again = project_update_ref(
            newer, origin=10, level=100, role="HH",
            terminal_origin=20, terminal_status="CONSUMED",
            above=True, reset_allowed=False, close=99, cutoff=45)
        self.assertEqual(old_again.state, "ARMED")
        self.assertEqual(old_again.armed_at, 45)

    def test_source_frozen_pine_branch_guards(self):
        source = (ROOT / "pine/alpha-engine-research.pine").read_text()
        for needle in (
            "if origin == terminalOrigin",
            'previous.state == "ARMED"',
            'resetAllowed ? "RESET PENDING" : "PREBREACHED"',
            'next := ResearchReference.new(origin, time_close, level, role, "ARMED")',
            "aiUpper.armedAt <= time",
            "aiLower.armedAt <= time",
            "close[1] <= aiUpper.level and close > aiUpper.level",
            "close[1] >= aiLower.level and close < aiLower.level",
            "aiBlockState := \"INVALIDATED\"",
            "aiGapState := \"GEOMETRIC TEST\"",
            "aiEpisodeEnded := true",
            'aiWorkflow := not contiguous or not contextOK',
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, source)


if __name__ == "__main__":
    unittest.main()
