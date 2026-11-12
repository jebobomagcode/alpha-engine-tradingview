"""Phase 3.4: verify opt-in M01 pivot audit does not modify Lesson 08 semantics.

The v0.1.1 baseline is recovered from THIS repo's Git history. Tests compare
actual Pine text and a limited, separate Python interpreter of the decision core.
A green result is NOT native Pine execution or realtime TradingView parity.
"""
from pathlib import Path
import re
import subprocess
import unittest

import test_lesson08_diagnostic as l08

ROOT = Path(__file__).resolve().parents[1]
PINNED_V011 = "74e7814e308a40f769d9b57607ebde145f492b8d"
SOURCE_PATH = "pine/lesson08-diagnostic.pine"
V012 = (ROOT / SOURCE_PATH).read_text(encoding="utf-8")


def v011_source():
    return subprocess.check_output(
        ["git", "show", f"{PINNED_V011}:{SOURCE_PATH}"], cwd=ROOT
    ).decode("utf-8")


def remove_between_once(source, start, end):
    assert source.count(start) == 1, f"Missing/ambiguous block start {start!r}"
    left = source.index(start)
    assert source.count(end) == 1, f"Missing/ambiguous block end {end!r}"
    right = source.index(end, left + len(start))
    return source[:left] + source[right:]


def reverse_only_the_authorized_m01_patch(source):
    """Mechanical reverse of the approved opt-in probe additions.

    Reconstructing the original source byte-for-byte is stronger than comparing
    selected named functions: it covers the full active decision adapter, panel
    rows 0–12, all labels, risk, declarations and the confirmed-hour request.
    """
    assert source.count('Research v0.1.2"') == 1
    assert source.count('const string BUILD_ID = "L08-0.1.2-3b9eb3065294"') == 1
    assert source.count("var table panel = table.new(position.top_right, 2, 15,") == 1
    source = source.replace('Research v0.1.2"', 'Research v0.1.1"', 1)
    source = source.replace(
        'const string BUILD_ID = "L08-0.1.2-3b9eb3065294"',
        'const string BUILD_ID = "L08-0.1.1-7fbb3eb381b6"', 1
    )
    source = source.replace(
        "var table panel = table.new(position.top_right, 2, 15,",
        "var table panel = table.new(position.top_right, 2, 13,", 1
    )
    source = remove_between_once(
        source, "// M01-P1 research comparator:", "// Deterministic core."
    )
    source = remove_between_once(
        source, "// Pivots are only declared at the CLOSE", "nominalRisk(float e, float s, float t, float lo) =>"
    )
    source = remove_between_once(
        source, "// Evaluate on every chart bar for stable history.",
        "[overlap, departure, invalid, engulf] = barFacts("
    )
    lines = source.splitlines(keepends=True)
    removed = [line for line in lines
               if line.startswith('    row(panel, 13, "M01 high"')
               or line.startswith('    row(panel, 14, "M01 low"')]
    assert len(removed) == 2, "Expected exactly two optional M01 table rows"
    return "".join(line for line in lines if line not in removed)


def translated_core(source, name):
    previous = l08.SOURCE
    try:
        l08.SOURCE = source
        return l08.pine_core(name)
    finally:
        l08.SOURCE = previous


def replay_with(rows, facts, assess, *, available=-20, expires=930):
    state = ("", None, None, None)
    snapshots = []
    prev = rows[0]
    gap = False
    for bar in rows[1:]:
        opened, closed, o, h, lo, c, _, _ = bar
        adjacent = prev[0] == opened - l08.STEP
        gap |= not adjacent and opened - l08.STEP >= available
        signals = facts(o, h, lo, c, 99, 100, adjacent, prev[2], prev[5])
        result = assess(*state, True, gap, True, True, adjacent, *signals,
                        opened, closed, available, expires)
        snapshots.append((closed, result))
        state = result[1:]
        prev = bar
    return snapshots


class Phase34M01Isolation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v011 = v011_source()

    def test_exact_original_source_after_only_m01_reverse_patch(self):
        self.assertEqual(reverse_only_the_authorized_m01_patch(V012), self.v011)

    def test_closed_bar_decision_adapter_and_markers_are_unchanged(self):
        begin = "[overlap, departure, invalid, engulf] = barFacts("
        end = "var box support = na"
        self.assertEqual(
            V012.split(begin, 1)[1].split(end, 1)[0],
            self.v011.split(begin, 1)[1].split(end, 1)[0],
        )
        self.assertEqual(V012.count("request.security("), 1)
        self.assertEqual(V012.count("label.new("), 3)
        self.assertEqual(V012.count("if chartOK and barstate.isconfirmed"), 1)
        self.assertNotIn("pivotProbe", V012.split(begin, 1)[1].split(end, 1)[0])
        self.assertNotIn("pivotLeft", V012.split(begin, 1)[1].split(end, 1)[0])
        self.assertNotIn("pivotRight", V012.split(begin, 1)[1].split(end, 1)[0])

    def test_existing_panel_rows_remain_identical_with_audit_on_or_off(self):
        for n in range(13):
            pattern = rf'(?m)^\s*row\(panel, {n}, .+$'
            self.assertEqual(
                re.findall(pattern, self.v011),
                re.findall(pattern, V012), f"Existing display row {n} changed"
            )
        self.assertIn('pivotProbe = input.bool(false,', V012)
        self.assertIn('pivotProbe and barstate.isconfirmed', V012)

    def test_frozen_prefix_decisions_equal_between_versions(self):
        old_facts = translated_core(self.v011, "barFacts")
        old_assess = translated_core(self.v011, "assess")
        new_facts = translated_core(V012, "barFacts")
        new_assess = translated_core(V012, "assess")
        cases = ("P01", "P04", "P09", "P10", "P11")
        scenarios = ((-20, 930), (120, 930), (-20, 600))
        count = 0
        for name in cases:
            rows = l08.FIXTURES["cases"][name]["bars"]
            for available, expiry in scenarios:
                with self.subTest(case=name, available=available, expires=expiry):
                    baseline = replay_with(rows, old_facts, old_assess,
                                           available=available, expires=expiry)
                    current = replay_with(rows, new_facts, new_assess,
                                          available=available, expires=expiry)
                    self.assertEqual(current, baseline)
                    count += 1
        self.assertEqual(count, 15)

    def test_source_boundaries_do_not_conflate_pivot_with_reaction(self):
        # These are separate state variables and no M01 symbol may affect
        # the existing L08 input-to-transition function boundary.
        core = V012.split("assess(", 1)[1].split("// Pivots are only declared", 1)[0]
        for name in ("pivotProbe", "pivotLeft", "pivotRight",
                     "latestPivotHigh", "latestPivotLow", "highKnownUTC", "lowKnownUTC"):
            self.assertNotIn(name, core)
        self.assertTrue(V012.count("strictPivots(") == 2)
        self.assertTrue("row(panel, 13, \"M01 high\"" in V012)
        self.assertTrue("row(panel, 14, \"M01 low\"" in V012)


if __name__ == "__main__":
    unittest.main()
