"""Run the bounded M01 Pine source fragments on synthetic closed-bar evidence.

This adapter models Pine's history indexing, inclusive loop, missing values and
lazy booleans for the tested expressions. Fixtures use ordinary Spot-price
precision. It does not emulate Pine float rounding or TradingView execution.
"""
import re
import unittest
from math import isnan, nan

from test_phase3_5_m01_evidence import SOURCE, STEP, bar


OFF = "Off · research"
WRONG_CHART = "INSUFFICIENT · chart identity"
NO_CLOSE = "INSUFFICIENT · no closed 5m evaluation"
HISTORY = "INSUFFICIENT · 5m history"
INVALID = "INVALID · 5m OHLC/clock window"
NO_EVENT = "VALID · no new pivot"
NEW_EVENT = "VALID · new pivot"


def expression(pine):
    # The M01 ternaries are right-associated chains with string true branches.
    match = re.fullmatch(r'(.+?) \? ("[^"]*") : (.+)', pine)
    if match:
        condition, when_true, when_false = match.groups()
        return f"({when_true} if {expression(condition)} else {expression(when_false)})"
    if pine.startswith('"'):
        return pine
    pine = re.sub(r"\b(true|false)\b", lambda m: m[0].capitalize(), pine)
    pine = re.sub(r"\bna\b(?!\s*\()", "nan", pine)
    pine = re.sub(r"\b(time_close|time|open|high|low|close)\b(?!\s*\[)", r"\1[0]", pine)
    return (pine.replace("math.max(", "max(").replace("math.min(", "min(")
            .replace("barstate.isconfirmed", "confirmed"))


def translate(block):
    lines = []
    for line in block.splitlines():
        text = line.strip()
        if not text or text.startswith("//"):
            continue
        indent = line[:len(line) - len(line.lstrip())]
        if text.startswith("if "):
            statement = f"if {expression(text[3:])}:"
        elif match := re.fullmatch(r"for (\w+) = 0 to (.+)", text):
            statement = f"for {match[1]} in range(({expression(match[2])}) + 1):"
        elif match := re.fullmatch(r"(?:(?:var )?(?:bool|float|int|string) )?"
                                   r"(\w+|\[[\w, ]+\])\s*(?::=|=)\s*(.+)", text):
            statement = f"{match[1]} = {expression(match[2])}"
        elif re.fullmatch(r"\[[\w, ]+\]", text):
            statement = f"return {text}"
        else:
            raise ValueError(f"Unsupported M01 Pine statement: {text}")
        lines.append(indent + statement)
    return "\n".join(lines)


class History:
    def __init__(self, bars, field):
        self.bars = bars
        self.field = field

    def __getitem__(self, offset):
        if not 0 <= offset < len(self.bars):
            return nan
        value = self.bars[-1 - offset].get(self.field)
        return nan if value is None else value


class SourceProbe:
    series = dict(time="t", time_close="end", open="o", high="h", low="l", close="c")

    def __init__(self, source):
        function = re.search(r"(?m)^strictPivots\(int (\w+), int (\w+)\) =>\n"
                             r"((?:    .+\n)+)", source)
        adapter = re.search(r"(?m)^(\[[\w, ]+\]\s*=\s*strictPivots\([^\n]+\))\n"
                            r"([\s\S]+?)^\[overlap, departure,", source)
        declarations, updates = adapter[2].split("\nif ", 1)
        display = re.search(r'(?m)^\s*row\(panel, \d+, "M01 evidence", '
                            r'(.+), "[^"]*"\)$', source)
        step = int(re.search(r"(?m)^const int STEP = (\d+)$", source)[1])
        self.scope = {"__builtins__": {}, "min": min, "max": max, "range": range,
                      "STEP": step, "na": isnan, "nan": nan}
        self.function = compile(f"def strictPivots({function[1]}, {function[2]}):\n"
                                + translate(function[3]), "Pine strictPivots", "exec")
        self.initial = {}
        exec(translate(declarations), self.scope, self.initial)
        self.update = compile(translate(adapter[1] + "\nif " + updates),
                              "Pine M01 adapter", "exec")
        self.display = compile(expression(display[1]), "Pine M01 evidence row", "eval")

    def sample(self, bars, previous=None, *, left=2, right=2, confirmed=True,
               enabled=True, chart_ok=True):
        scope = self.scope | {name: History(bars, field) for name, field in self.series.items()}
        scope.update(bar_index=len(bars) - 1)
        exec(self.function, scope)
        variables = (self.initial if previous is None else previous) | {
            "pivotLeft": left, "pivotRight": right, "confirmed": confirmed,
            "pivotProbe": enabled, "chartOK": chart_ok,
        }
        exec(self.update, scope, variables)
        status = eval(self.display, scope, variables)
        flags = tuple(variables[name] for name in (
            "pivotWindowEnough", "pivotWindowValid", "pivotHighNow", "pivotLowNow",
        ))
        return status, flags, {name: variables[name] for name in self.initial}


def records(state):
    def record(direction):
        return tuple(None if isnan(state[name]) else state[name] for name in (
            f"latestPivot{direction}", f"{direction.lower()}OriginUTC",
            f"{direction.lower()}KnownUTC",
        ))

    return record("High"), record("Low")


class Phase35CandidateSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.probe = SourceProbe(SOURCE)

    def test_complete_window_rejects_nonpositive_low(self):
        positive = [bar(i * STEP, high, low) for i, (high, low) in enumerate(
            ((6, 4), (7, 5), (10, 1), (8, 6), (9, 7))
        )]
        for position in range(len(positive)):
            for low in (0, -1, 1):
                with self.subTest(position=position, low=low):
                    bars = positive.copy()
                    bars[position] = dict(bars[position], l=low)
                    status, flags, state = self.probe.sample(bars)
                    if low > 0:
                        self.assertEqual(flags, (True, True, True, position == 2))
                        self.assertEqual(status, NEW_EVENT)
                    else:
                        self.assertFalse(flags[1], "Nonpositive low admitted by Pine window")
                        self.assertEqual((status, flags), (INVALID, (True, False, False, False)))
                        self.assertEqual(records(state), ((None,) * 3, (None,) * 3))

    def test_evidence_status_matches_each_closed_window_outcome(self):
        monotone = [bar(i * STEP, 10 + i, 2 + i) for i in range(5)]
        high = bar(2 * STEP, 20, 4)
        low = bar(2 * STEP, 12, 1)
        both = bar(2 * STEP, 20, 1)
        bad = dict(monotone[2], c=None)
        for label, window, flags, expected in (
            ("incomplete", monotone[:4], (False, False, False, False), HISTORY),
            ("invalid", monotone[:2] + [bad] + monotone[3:], (True, False, False, False), INVALID),
            ("no pivot", monotone, (True, True, False, False), NO_EVENT),
            ("high only", monotone[:2] + [high] + monotone[3:], (True, True, True, False), NEW_EVENT),
            ("low only", monotone[:2] + [low] + monotone[3:], (True, True, False, True), NEW_EVENT),
            ("both", monotone[:2] + [both] + monotone[3:], (True, True, True, True), NEW_EVENT),
        ):
            with self.subTest(outcome=label):
                status, result, _ = self.probe.sample(window)
                self.assertEqual(result, flags)
                self.assertEqual(status, expected)

    def test_evidence_display_precedence_and_no_unqualified_commit(self):
        bars = [bar(i * STEP, h, low) for i, (h, low) in enumerate(
            ((4, 2), (6, 1), (5, 3))
        )]
        for label, options, expected in (
            ("disabled", {"enabled": False}, OFF),
            ("wrong chart", {"chart_ok": False}, WRONG_CHART),
            ("disabled on wrong chart", {"enabled": False, "chart_ok": False}, OFF),
            ("forming first evaluation", {"confirmed": False}, NO_CLOSE),
        ):
            with self.subTest(mode=label):
                status, flags, state = self.probe.sample(bars, left=1, right=1, **options)
                self.assertEqual(flags, (True, True, True, True))
                self.assertEqual(status, expected)
                self.assertEqual(state["pivotEvidence"], NO_CLOSE)
                self.assertEqual(records(state), ((None,) * 3, (None,) * 3))

    def test_panel_rows_fit_declared_height_exactly_once(self):
        dimensions = re.findall(r"(?m)^var table panel\s*=\s*table\.new\("
                                r"[^,\n]+,\s*(\d+),\s*(\d+)\s*,", SOURCE)
        self.assertEqual(len(dimensions), 1, "Expected one panel with literal dimensions")
        columns, height = map(int, dimensions[0])
        rows = re.findall(r"(?m)^[ \t]*row\(\s*panel\s*,\s*([^,\n]+),\s*([^\n]+)", SOURCE)
        self.assertTrue(all(re.fullmatch(r"-?\d+", index.strip()) for index, _ in rows),
                        "Expected literal indexes for all panel rows")
        actual = sorted(int(index) for index, _ in rows)
        expected = list(range(height))
        self.assertEqual(actual, expected, "Panel has missing, duplicate or out-of-range row indexes")
        labels = [re.match(r'"([^"]+)"\s*,', body) for _, body in rows]
        self.assertTrue(all(labels), "Expected a literal label for each panel row")
        for required in ("M01 high", "M01 low", "M01 evidence"):
            self.assertEqual(sum(label[1] == required for label in labels), 1, f"Expected one {required} row")
        # The row helper must pass its row index through to every cell.
        cells = re.findall(r"(?m)^[ \t]*table\.cell\(\s*panel\s*,\s*([^,\n]+),\s*([^,\n]+),", SOURCE)
        self.assertCountEqual([(column.strip(), index.strip()) for column, index in cells],
                              [(str(column), "n") for column in range(columns)])

    def test_sequential_gap_recovery_and_independent_pivot_records(self):
        # Slot 5 is absent. Prices after the gap rise through the first clean
        # window, then produce a high-only pivot at slot 11 and a low at slot 14.
        rows = [
            (0, 103, 100), (1, 104, 101), (2, 110, 95), (3, 105, 102), (4, 106, 103),
            (6, 107, 104), (7, 108, 105), (8, 109, 106), (9, 110, 107), (10, 111, 108),
            (11, 120, 109), (12, 113, 110), (13, 114, 111), (14, 115, 100),
            (15, 116, 112), (16, 117, 113),
        ]
        bars = [bar(slot * STEP, high, low) for slot, high, low in rows]
        empty = (None,) * 3
        initial_high, initial_low = (110, 2 * STEP, 5 * STEP), (95, 2 * STEP, 5 * STEP)
        next_high, next_low = (120, 11 * STEP, 14 * STEP), (100, 14 * STEP, 17 * STEP)
        for left, recovery, fourth_status in ((2, 11, HISTORY), (1, 10, NO_EVENT)):
            # These expected cutoffs are fixture facts, independent of the adapter.
            status_by_cutoff = {1: HISTORY, 2: HISTORY, 3: HISTORY, 4: fourth_status,
                                5: NEW_EVENT, 14: NEW_EVENT, 17: NEW_EVENT}
            status_by_cutoff.update(dict.fromkeys(range(7, recovery), INVALID))
            previous = self.probe.initial
            cutoffs = []
            for length, (slot, _, _) in enumerate(rows, start=1):
                prefix = bars[:length]
                cutoff = slot + 1
                options = {"left": left, "right": 2}
                with self.subTest(left=left, right=2, cutoff_minutes=cutoff * 5):
                    self.assertEqual(prefix[-1]["end"], cutoff * STEP)
                    cutoffs.append(cutoff)
                    forming, _, state = self.probe.sample(prefix, previous, confirmed=False, **options)
                    self.assertEqual(forming, previous["pivotEvidence"])
                    self.assertEqual(records(state), records(previous), "Forming bar changed pivot history")

                    status, flags, previous = self.probe.sample(prefix, previous, **options)
                    self.assertEqual(status, status_by_cutoff.get(cutoff, NO_EVENT))
                    self.assertEqual(flags[2:], (cutoff in (5, 14), cutoff in (5, 17)))
                    high = empty if cutoff < 5 else initial_high if cutoff < 14 else next_high
                    low = empty if cutoff < 5 else initial_low if cutoff < 17 else next_low
                    self.assertEqual(records(previous), (high, low))
            self.assertEqual(cutoffs, [1, 2, 3, 4, 5, *range(7, 18)])


if __name__ == "__main__":
    unittest.main()
