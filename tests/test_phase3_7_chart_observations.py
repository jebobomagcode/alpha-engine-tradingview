"""Pin the observation taps and draw behavior against independent fixtures."""

from fractions import Fraction
from pathlib import Path
import subprocess
import unittest

from overlay_source_fixture import without_observation_visuals
from research.phase3_6.lifecycle_parity_oracle import Candle, Episode, advance_episode


ROOT = Path(__file__).resolve().parents[1]
PATH = "pine/alpha-engine-research.pine"
GUIDE_COMMIT = "579ed3ec997c3f9a7807f076ade4daf1e3351149"


class ChartObservationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (ROOT / PATH).read_text()
        cls.core, cls.display = cls.source.split("\n// Chart contact, reaction and nominal geometry.", 1)

    def test_guide_increment_and_engine_are_unchanged_after_removing_display_taps(self):
        before = subprocess.check_output(["git", "show", f"{GUIDE_COMMIT}:{PATH}"], cwd=ROOT)
        self.assertEqual(without_observation_visuals(self.source).encode(), before)

    def test_contact_reaction_and_terminal_events_use_qualified_closed_state(self):
        self.assertIn("if aiEnabled and researchChartOK and barstate.isconfirmed", self.display)
        self.assertIn("aiVisualContact := touch and bullishContext and not aiEpisodeEnded and not aiTouched", self.core)
        self.assertIn("aiVisualReaction := reaction", self.core)
        self.assertIn('aiVisualInvalid := not aiEpisodeEnded ? (invalidSupport ? "Support closed through" : supportConsumed ?', self.core)
        self.assertLess(self.core.index("aiVisualContact := touch"), self.core.index("        aiTouched := true"))
        self.assertIn("addStructureLabel(visualObservations, aiDecisionAt", self.display)
        self.assertIn('"Contact + reaction"', self.display)
        self.assertNotIn("time[", self.display)

    def test_first_contact_and_reaction_can_coincide_then_termination_blocks_them(self):
        predecessor = Candle(0, 106, 107, 103, 104)
        close = Candle(5, 103, 111, 100, 110)
        args = dict(predecessor=predecessor, adjacent=True, context_ok=True, bullish_context=True,
                    armed_anchor="HL", support_low=100, support_high=103)
        accepted = advance_episode(Episode(), bar=close, **args)
        self.assertTrue(accepted.overlap and accepted.reaction and accepted.state.touched)
        repeated = advance_episode(accepted.state, bar=close, **args)
        self.assertTrue(repeated.reaction and repeated.state.touched)
        broken = advance_episode(accepted.state, bar=Candle(10, 103, 104, 99, 99), **args)
        self.assertEqual(broken.status, "REASSESS · support closed through")
        self.assertTrue(broken.state.ended)
        self.assertFalse(advance_episode(broken.state, bar=close, **args).reaction)

    def test_geometry_matches_dashboard_formula_and_expires_on_next_absent_cutoff(self):
        self.assertEqual((Fraction(116) - 108) / (108 - 98), Fraction(4, 5))
        self.assertIn("if stopLevel > 0 and stopLevel < close and close < targetLevel", self.core)
        self.assertIn("aiGeometryR := (targetLevel - close) / (close - stopLevel)", self.core)
        self.assertIn("showGeometry = visualGeometry and not na(aiGeometryR)", self.display)
        self.assertIn("if showGeometry or not na(visualRiskBadge)", self.display)
        for level in ("Entry", "Stop", "Target"):
            self.assertIn(f"aiDecisionAt, showGeometry ? aiGeometry{level} : na", self.display)
        self.assertIn("label.delete(visualRiskBadge)", self.display)
        self.assertIn('"Entry / stop / target · " + aiGeometry', self.display)

    def test_bounded_drawings_and_optional_dashboard_layout(self):
        self.assertIn("max_boxes_count = 3, max_labels_count = 54, max_lines_count = 8", self.core)
        self.assertEqual(self.display.count("var line "), 3)
        self.assertEqual(self.display.count("label.new("), 1)
        self.assertIn('visualGeometry = input.bool(false, "Nominal entry / stop / target"', self.display)
        self.assertIn('options = ["Corners", "Both left", "Research only", "Hidden"]', self.display)
        self.assertIn("table.set_position(panel,", self.display)
        self.assertIn("table.clear(aiPanel, 0, 0, 1, 10)", self.display)
        self.assertIn("table.clear(panel, 0, 0, 1, 15)", self.display)
