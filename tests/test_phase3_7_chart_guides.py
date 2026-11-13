"""Check native bindings and independent Fibonacci arithmetic."""

from fractions import Fraction
from pathlib import Path
import re
import subprocess
import unittest

from overlay_source_fixture import without_new_visuals

ROOT = Path(__file__).resolve().parents[1]
PATH = "pine/alpha-engine-research.pine"
BASE = "7c9f2c1ab08f6af40af0ffc4808c4f927eb480ed"


class ChartGuidesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (ROOT / PATH).read_text()
        cls.core, cls.guides = cls.source.split("\n// Chart Fibonacci and EMA overlays.", 1)

    def test_v018_engine_and_drawing_layers_remain_exact(self):
        baseline = subprocess.check_output(["git", "show", f"{BASE}:{PATH}"], cwd=ROOT)
        self.assertEqual(without_new_visuals(self.source).encode(), baseline)

    def test_fibonacci_levels_share_the_dashboard_calculation(self):
        values = re.findall(r"(?m)^ +aiFib(\d+) := startFib \+ direction \* distance \* ([\d.]+)$", self.core)
        self.assertEqual(values, [("50", "0.5"), ("618", "0.618"), ("705", "0.705")])
        for suffix, ratio in values:
            f = Fraction(ratio)
            up = 200 - 100 * f
            down = 100 + 100 * f
            self.assertEqual(up + down, 300)
            self.assertTrue(100 < up < 200 and 100 < down < 200)
            self.assertIn(f"str.tostring(aiFib{suffix}, format.mintick)", self.core)
            self.assertIn(f"hasFib ? aiFib{suffix} : na", self.guides)

    def test_fibonacci_birth_replacement_and_retirement_are_causal(self):
        self.assertIn("if aiEnabled and researchChartOK and barstate.isconfirmed", self.guides)
        self.assertIn("line.new(knownAt, level, knownAt + STEP, level", self.guides)
        self.assertIn("aiDecisionAt, hasFib", self.guides)
        for field in ("UpperOrigin", "LowerOrigin", "Up"):
            self.assertIn(f"aiFib{field} != visualFib{field}", self.guides)
        self.assertIn("not hasFib and not na(visualFib50)", self.guides)
        self.assertIn("line.delete(drawing)", self.guides)
        self.assertNotIn("time[", self.guides)
        self.assertIn("max_lines_count = 5", self.core)

    def test_ema_switches_use_confirmed_momentum_series_and_warmup(self):
        self.assertIn("bool emaOverlayReady = aiEnabled and researchChartOK and barstate.isconfirmed and aiRun >= 200 and not na(aiRsi)", self.guides)
        for period in (20, 50, 200):
            self.assertIn(f"float aiEma{period} = ta.ema(close, {period})", self.core)
            self.assertIn(f'visualEma{period} = input.bool(false, "EMA {period}"', self.guides)
            self.assertIn(f"plot(visualEma{period} and emaOverlayReady ? aiEma{period} : na", self.guides)
        self.assertEqual(self.guides.count("plot.style_linebr"), 3)
        self.assertNotIn("ta.ema(", self.guides)
