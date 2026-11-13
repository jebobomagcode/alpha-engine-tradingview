"""Check the structural overlay's source boundaries and frozen behavior."""

from hashlib import sha256
from pathlib import Path
import re
import subprocess
import unittest

from research.phase3_6.ai_structure_candidate import replay_structure
from test_phase3_6_integrated_replay import frozen_tape


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = "pine/alpha-engine-research.pine"
RELEASE = "9b765df5bb9ceebe77ce57b216281be6c6ba3282"
SEPARATOR = "\n// Chart structure overlay. Read only the accepted closed research state.\n"


class StructureOverlayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = (ROOT / SOURCE_PATH).read_text()
        cls.core, cls.overlay = source.split(SEPARATOR, 1)

    def test_research_engine_and_dashboard_are_exactly_the_accepted_release(self):
        accepted = subprocess.check_output(
            ["git", "show", f"{RELEASE}:{SOURCE_PATH}"], cwd=ROOT
        )
        self.assertEqual(sha256(accepted).hexdigest(),
                         "9376df68e43cb76d260ab109ca69b1b2813366a75072856b506ae2397f76fcec")
        restored = self.core.replace("Integrated Research v0.1.7", "Integrated Research v0.1.6", 1)
        restored = restored.replace("max_labels_count = 35, max_lines_count = 2", "max_labels_count = 3", 1)
        restored = re.sub(r'AE-0\.1\.7-[0-9a-f]{12}', "AE-0.1.6-00d26a21011a", restored, count=1)
        self.assertEqual(restored.encode(), accepted)
        self.assertNotRegex(self.overlay, r"\bai\w+\s*:=")
        self.assertNotIn("request.security", self.overlay)

    def test_markers_use_observation_cutoffs_and_preserve_experimental_status(self):
        self.assertIn("if aiEnabled and researchChartOK and barstate.isconfirmed", self.overlay)
        self.assertIn("label.new(cutoff, y, caption, xloc = xloc.bar_time", self.overlay)
        for side, seen in (("Upper", "High"), ("Lower", "Low")):
            self.assertIn(f"ai{side}.origin > visual{seen}Seen", self.overlay)
            self.assertRegex(self.overlay, rf"addStructureLabel\(visualSwingLabels, time_close,[^\n]+ai{side}\.role")
        self.assertIn("if visualEvents and aiEventAt == time_close", self.overlay)
        self.assertIn("addStructureLabel(visualEventLabels, aiEventAt,", self.overlay)
        self.assertIn('"BOS? " : "CHoCH? "', self.overlay)
        self.assertNotIn("time[aiWindow]", self.overlay)

    def test_only_armed_lines_survive_and_objects_are_bounded(self):
        self.assertIn('if ref.state != "ARMED" or na(ref.armedAt)', self.overlay)
        self.assertIn("line.delete(drawing)", self.overlay)
        self.assertIn("line.new(ref.armedAt, ref.level, ref.armedAt + STEP, ref.level,", self.overlay)
        self.assertIn("line.set_xy1(drawing, ref.armedAt, ref.level)", self.overlay)
        self.assertIn("visualResistance := drawArmedReference(visualResistance, aiUpper,", self.overlay)
        self.assertIn("visualSupport := drawArmedReference(visualSupport, aiLower,", self.overlay)
        self.assertIn('maxval = 16, group = VISUAL_GROUP', self.overlay)
        self.assertLess(self.overlay.index("label.delete(array.shift(labels))"), self.overlay.index("label.new("))
        self.assertIn("max_labels_count = 35, max_lines_count = 2", self.core)

    def test_frozen_references_and_events_supply_distinct_causal_anchors(self):
        tape = frozen_tape()
        roles = set()
        event_classes = set()
        for policy in ("A", "B"):
            frames = replay_structure(tape, as_of=tape[-1].cutoff, policy=policy)
            for frame in frames:
                now = frame.structure.evaluated_at
                for item in frame.references:
                    ref = item.reference
                    roles.add(ref.role)
                    if item.status == "ARMED":
                        self.assertLess(ref.origin_open, item.armed_at)
                        self.assertLessEqual(item.armed_at, now)
                for event in frame.events:
                    event_classes.add(event.classification.split("_", 1)[0])
                    self.assertEqual(event.cutoff, now)
                    self.assertLess(event.reference.origin_open, now)
        self.assertEqual(roles, {"HH", "HL", "LH", "LL"})
        self.assertEqual(event_classes, {"BOS", "CHOCH"})
