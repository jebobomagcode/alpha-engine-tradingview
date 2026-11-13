"""Source bindings plus bounded zone lifecycle fixtures for chart rendering."""

from hashlib import sha256
from pathlib import Path
import re
import subprocess
import unittest

from overlay_source_fixture import without_new_visuals

from research.phase3_6.integrated_replay import replay_integrated
from research.phase3_6.lifecycle_parity_oracle import Candle, Zone, advance_zone
from research.phase3_6.reference_model import Bar
from test_phase3_6_integrated_replay import frozen_tape


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "pine/alpha-engine-research.pine"
BASE = "71f48925063b65ca4043a8fe8ee2575480a0d324"


class ZoneOverlayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = without_new_visuals((ROOT / SOURCE).read_text())
        cls.core, cls.overlay = source.split("\n// Chart zone overlay.", 1)

    def test_previous_engine_dashboard_and_structure_overlay_are_exact(self):
        baseline = subprocess.check_output(["git", "show", f"{BASE}:{SOURCE}"], cwd=ROOT)
        self.assertEqual(sha256(baseline).hexdigest(),
                         "bb9c39801c0729279ddf06ed45c6b9bb85470beeb74983e6e1ff12471f17caa1")
        restored = self.core.replace("Integrated Research v0.1.8", "Integrated Research v0.1.7", 1)
        restored = restored.replace("max_boxes_count = 3, max_labels_count = 37",
                                    "max_boxes_count = 1, max_labels_count = 35", 1)
        restored = re.sub(r"AE-0\.1\.8-[0-9a-f]{12}", "AE-0.1.7-9e93706426d6", restored, count=1)
        self.assertEqual(restored.encode(), baseline)

    def test_reads_committed_zone_state_and_uses_known_at_for_left_edge(self):
        guard = "if aiEnabled and researchChartOK and barstate.isconfirmed"
        operations = self.overlay.split(guard, 1)[1].splitlines()
        for family, visibility, is_gap in (("Block", "Blocks", "false"), ("Gap", "Gaps", "true")):
            self.assertIn(
                f"    visual{family} := drawResearchZone(visual{family}, visual{visibility}, {is_gap}, "
                f"ai{family}Known, aiDecisionAt, ai{family}Lo, ai{family}Hi, ai{family}Side, ai{family}State)",
                operations,
            )
        self.assertEqual(sum("input.bool(" in line for line in self.overlay.splitlines()), 2)
        self.assertIn("knownAt <= cutoff", self.overlay)
        self.assertIn("box.new(knownAt, hi, knownAt + STEP, lo, xloc = xloc.bar_time", self.overlay)
        self.assertIn("label.set_x(drawing.badge, cutoff)", self.overlay)
        self.assertNotRegex(self.overlay, r"\bai\w+\s*:?=")
        self.assertNotRegex(self.overlay, r"\b(?:open|high|low|close|time)\[|request\.security")

    def test_replaces_or_clears_before_allocating_and_freezes_invalidated_right(self):
        self.assertIn("not valid or drawing.knownAt != knownAt", self.overlay)
        self.assertLess(self.overlay.index("box.delete(drawing.band)"), self.overlay.index("box.new("))
        self.assertLess(self.overlay.index("label.delete(drawing.badge)"), self.overlay.index("label.new("))
        self.assertIn("if drawing.state != state", self.overlay)
        self.assertIn("box.set_right(drawing.band, cutoff)", self.overlay)
        self.assertIn("box.set_extend(drawing.band, extend.none)", self.overlay)
        self.assertIn('family + " · " + state', self.overlay)
        self.assertIn("max_boxes_count = 3, max_labels_count = 37", self.core)
        self.assertEqual(self.overlay.count("var ZoneDrawing "), 2)
        self.assertNotIn("array.", self.overlay)

    def test_block_and_gap_share_overlap_evidence_but_only_block_invalidates(self):
        block = Zone("B:15", "BLOCK", 1, 100, 106, 15)
        gap = Zone("G:15", "GAP", 1, 100, 106, 15)
        before_known = Candle(10, 104, 105, 98, 99)
        overlap = Candle(15, 107, 108, 106, 107)
        close_through = Candle(20, 102, 105, 98, 99)
        self.assertEqual(advance_zone(block, before_known), block)
        self.assertEqual(advance_zone(block, Candle(15, 104, 105, 98, 99, False)), block)
        self.assertEqual(advance_zone(block, overlap).state, "GEOMETRIC TEST")
        invalidated = advance_zone(block, close_through)
        self.assertEqual(invalidated.state, "INVALIDATED")
        self.assertEqual(advance_zone(invalidated, overlap), invalidated)
        self.assertEqual(advance_zone(gap, close_through).state, "GEOMETRIC TEST")

    def test_replacement_wins_at_the_same_cutoff_and_data_break_clears(self):
        bars = (
            Bar(0, 100, 101, 99, 100),
            Bar(5, 100, 102, 99, 101),
            Bar(10, 106, 108, 105, 107),
            Bar(15, 108, 110, 103, 104),
            Bar(25, 103, 107, 102, 106),
        )
        frames = replay_integrated(bars, as_of=30)
        by_cutoff = {frame.cutoff: frame for frame in frames}
        self.assertEqual((by_cutoff[15].gap.known_at, by_cutoff[15].gap.state), (15, "OPEN"))
        self.assertEqual((by_cutoff[20].gap.known_at, by_cutoff[20].gap.state), (20, "OPEN"))
        self.assertIsNone(by_cutoff[30].gap)

    def test_frozen_projection_never_moves_knowledge_before_its_source_close(self):
        bars = frozen_tape()
        for policy in ("A", "B"):
            frames = replay_integrated(bars, as_of=bars[-1].cutoff, policy=policy)
            states = {"block": set(), "gap": set()}
            for family in states:
                previous = None
                for frame in frames:
                    zone = getattr(frame, family)
                    if zone is not None:
                        self.assertLessEqual(zone.known_at, frame.cutoff)
                        if previous is None or previous.identity != zone.identity:
                            self.assertEqual((zone.known_at, zone.state), (frame.cutoff, "OPEN"))
                        states[family].add(zone.state)
                    previous = zone
            self.assertEqual(states["gap"], {"OPEN", "GEOMETRIC TEST"})
            self.assertIn("OPEN", states["block"])
            for count in (36, 120, 216):
                as_of = bars[count - 1].cutoff
                self.assertEqual(replay_integrated(bars[:count], as_of=as_of, policy=policy), frames[:count])
