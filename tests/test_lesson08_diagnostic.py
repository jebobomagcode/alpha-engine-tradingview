"""Execute the small Pine decision core on pinned cases using only Python's stdlib.

This adapter supports the core's syntax subset. TradingView separately checks the
actual Pine types, runtime, data alignment and rollback behavior.
"""
import hashlib
import json
import re
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "pine/lesson08-diagnostic.pine").read_text(encoding="utf-8")
RESEARCH = ROOT / "docs/research"
FIXTURES = json.loads(
    (RESEARCH / "phase2-frozen-prefix-evidence-v1.md")
    .read_text(encoding="utf-8").split("~~~json\n", 1)[1].split("\n~~~", 1)[0]
)
EMPTY = ("", None, None, None)
STEP = 300
PREFIX = "INSUFFICIENT · "


def pine_core(name):
    """Translate local assignments, branches and the final tuple from one function."""
    match = re.search(rf"(?m)^{name}\(([^\n]*)\) =>\n((?:    [^\n]+\n)+)", SOURCE)
    signature, body = match.groups()
    params = [item.split()[1] for item in signature.split(", ")]
    lines = [f"def {name}({', '.join(params)}):"]
    for line in body.splitlines():
        indent = len(line) - len(line.lstrip())
        value = line.strip()
        if value.startswith("//"):
            continue
        value = re.sub(r"^(bool|int|float|string) ", "", value)
        value = re.sub(r"\bna\b(?!\()", "None", value)
        value = value.replace(":=", "=")
        if value.startswith(("if ", "else if ", "else")):
            value = value.replace("else if ", "elif ", 1) + ":"
        elif value.startswith("["):
            value = "return tuple(" + value + ")"
        elif not re.match(r"^\w+ = ", value):
            raise ValueError(f"Unsupported Pine core line: {value}")
        lines.append(" " * indent + value)
    env = {"na": lambda value: value is None, "tuple": tuple, "__builtins__": {}}
    exec("\n".join(lines), env)
    return env[name]


bar_facts = pine_core("barFacts")
assess = pine_core("assess")
risk = pine_core("nominalRisk")


def run_bars(rows, *, available=-20, expires=930):
    state = EMPTY
    outputs = {}
    previous = rows[0]
    gap = False
    for bar in rows[1:]:
        opened, closed, o, h, low, c, _, _ = bar
        adjacent = previous[0] == opened - STEP
        gap |= not adjacent and opened - STEP >= available
        facts = bar_facts(o, h, low, c, 99, 100, adjacent, previous[2], previous[5])
        output = assess(*state, True, gap, True, True, adjacent, *facts,
                        opened, closed, available, expires)
        outputs[closed] = output
        state = output[1:]
        previous = bar
    return outputs


class DiagnosticCases(unittest.TestCase):
    def cases(self, key):
        return FIXTURES["cases"][key]["bars"]

    def test_same_bar_contact_can_qualify_only_baseline(self):
        first = run_bars(self.cases("P01"))[300]
        self.assertEqual(first, ("QUALIFIED · geometric reaction", "", 0, 300, None))

    def test_later_engulf_can_complete_the_episode_on_departure(self):
        rows = self.cases("P11")
        out = run_bars(rows)
        self.assertEqual(out[300][2:], (0, 300, None))
        self.assertEqual(out[600][2:], (0, 300, None))
        self.assertEqual(out[900][2:], (0, 300, 900))
        self.assertEqual(out[900][1], "REASSESS · episode ended")
        self.assertEqual(run_bars(rows[:2])[300], out[300])

    def test_earlier_touch_later_reaction_and_unknown_receipt(self):
        out = run_bars(self.cases("P04"))
        self.assertEqual(out[300][2:], (0, None, None))
        self.assertEqual(out[600][2:], (0, 600, 600))
        self.assertIn('na(firstA) ? "Waiting for later candidate" : "UNKNOWN · receipt order"', SOURCE)

    def test_no_contact_for_outside_engulf(self):
        facts = bar_facts(101, 105, 100.25, 104, 99, 100, True, 103, 102)
        self.assertEqual(facts, (False, True, False, True))
        out = assess(*EMPTY, True, False, True, True, True, *facts, 0, 300, -20, 930)
        self.assertEqual(out, ("WAIT · zone overlap", *EMPTY))

    def test_context_or_zone_released_after_open_cannot_backdate(self):
        out = run_bars(self.cases("P09"), available=120)
        self.assertEqual(out[300], ("WAIT · declaration not yet available at open", *EMPTY))
        self.assertTrue(all(record[2:] == (None, None, None) for record in out.values()))

    def test_missing_inputs_have_specific_reasons(self):
        for flags, reason in [
            ((False, False, True, True, True), "setup declaration"),
            ((True, True, True, True, True), "setup history gap"),
            ((True, False, False, True, True), "confirmed 1H reference"),
            ((True, False, True, False, True), "closed 5m OHLC"),
            ((True, False, True, True, False), "adjacent 5m predecessor"),
        ]:
            with self.subTest(reason=reason):
                out = assess(*EMPTY, *flags, True, False, False, True, 0, 300, -20, 930)
                self.assertEqual(out[0], PREFIX + reason)
                self.assertEqual(out[3:], (None, None))

    def test_missing_active_5m_bar_blocks_first_event(self):
        rows = self.cases("P11")
        out = run_bars([rows[0], rows[1], rows[3]])
        self.assertEqual(out[900][0], PREFIX + "setup history gap")
        self.assertEqual(out[900][2:], (0, 300, None))

    def test_closing_invalidation_has_priority_over_overlap(self):
        out = run_bars(self.cases("P07"))
        self.assertEqual(out[300], ("INVALIDATED · close below support",
                                    "INVALIDATED · close below support", None, None, None))
        self.assertEqual(out[600], out[300])

    def test_expiry_is_exclusive_and_terminal(self):
        rows = self.cases("P11")
        out = run_bars(rows, expires=300)
        self.assertEqual(out[300], ("EXPIRED · exclusive cutoff",
                                    "EXPIRED · exclusive cutoff", None, None, None))
        self.assertEqual(out[900], out[300])

    def test_late_bar_absent_from_nominal_prefix_and_expiry_blocks_revival(self):
        rows = self.cases("P08")
        nominal = [row for row in rows if row[6] <= row[1]]
        out = run_bars(nominal)[900]
        self.assertEqual(out[0], PREFIX + "setup history gap")
        expired = assess(*out[1:], True, True, True, True, True, True,
                         False, False, True, 900, 1200, -20, 930)
        self.assertEqual(expired[0], "EXPIRED · exclusive cutoff")
        self.assertEqual(expired[3:], (None, None))

    def test_correction_is_a_different_input_snapshot(self):
        fixture = FIXTURES["cases"]["P12"]
        original = run_bars(fixture["bars"])[300]
        corrected = run_bars([fixture["bars"][0], fixture["revision"]])[300]
        self.assertEqual(original[2:], (0, 300, None))
        self.assertEqual(corrected[2:], (None, None, None))
        self.assertEqual(run_bars(fixture["bars"][:2])[300], original)

    def test_separator_never_rearms_original_version(self):
        out = run_bars(self.cases("P06"))
        self.assertEqual(out[600], ("REASSESS · episode ended", "REASSESS · episode ended",
                                    0, None, None))
        self.assertEqual(out[900], out[600])

    def test_straddle_can_qualify_geometrically_without_a_zone_print(self):
        self.assertFalse(any(99 <= p <= 100 for _, p in FIXTURES["cases"]["P10"]["tape"]["prices"]))
        self.assertEqual(run_bars(self.cases("P10"))[300][2:], (0, 300, None))

    def test_inclusive_zone_edge_strict_body_edges(self):
        self.assertTrue(bar_facts(101, 104, 100, 103, 99, 100, True, 102, 101.5)[0])
        self.assertFalse(bar_facts(101, 104, 100, 103, 99, 100, True, 102, 101)[3])
        self.assertFalse(bar_facts(101, 104, 100, 103, 99, 100, True, 103, 102)[3])

    def test_repeat_qualification_retains_both_first_cutoffs(self):
        out = assess("", 0, 300, 900, True, False, True, True, True, True,
                     False, False, True, 900, 1200, -20, 1500)
        self.assertEqual(out[2:], (0, 300, 900))

    def test_nominal_geometry_and_invalid_directions(self):
        self.assertEqual(risk(100, 96, 105, 99), (4, 5))
        for values in [(100, 100, 105, 99), (100, 102, 105, 99),
                       (100, 96, 95, 99), (100, 99, 105, 99), (100, 0, 105, 99)]:
            self.assertEqual(risk(*values), (None, None))

    def test_adapter_static_safety_and_timing_guards(self):
        self.assertTrue(SOURCE.startswith("//@version=6\nindicator("))
        self.assertNotRegex(SOURCE, r"(?m)\b(?:strategy|alertcondition|alert)\s*\(")
        self.assertEqual(SOURCE.count("request.security("), 1)
        self.assertIn('[time[1], time_close[1], close[1]]', SOURCE)
        self.assertIn("lookahead = barmerge.lookahead_on", SOURCE)
        self.assertIn("hourClose == requiredHourClose and hourOpen == requiredHourClose - HOUR", SOURCE)
        self.assertIn("timeframe.multiplier == 5 and chart.is_standard", SOURCE)
        self.assertEqual(re.findall(r"(?m)^( +)\[reason, disposition,", SOURCE), ["    "])
        self.assertIn("if chartOK and barstate.isconfirmed\n", SOURCE)


class FrozenBinance(unittest.TestCase):
    def test_exact_receipt_integrity_and_hour_aggregation(self):
        path = RESEARCH / "evidence/m07-paxgusdt-spot-v1"
        receipt = (RESEARCH / "phase2-m07-frozen-market-evidence.md").read_text(encoding="utf-8")
        data = {}
        for name in ("klines-5m", "klines-1h", "exchange-info"):
            content = (path / (name + ".json")).read_bytes()
            self.assertIn(hashlib.sha256(content).hexdigest(), receipt)
            payload = json.loads(content)
            data[name] = payload if name == "exchange-info" else payload["result"]
        symbol, = data["exchange-info"]["symbols"]
        self.assertEqual((symbol["symbol"], symbol["baseAsset"], symbol["quoteAsset"]),
                         ("PAXGUSDT", "PAXG", "USDT"))
        self.assertTrue(symbol["isSpotTradingAllowed"])
        five, hour = data["klines-5m"], data["klines-1h"]
        for rows, interval, count, start in ((five, 300000, 288, 1794355200000),
                                             (hour, 3600000, 48, 1794268800000)):
            self.assertEqual(len(rows), count)
            self.assertEqual([r[0] for r in rows], list(range(start, start + interval*count, interval)))
            for row in rows:
                self.assertEqual(row[6], row[0] + interval - 1)
                o, h, low, c = map(Decimal, row[1:5])
                self.assertTrue(0 < low <= min(o, c) <= max(o, c) <= h)
        for index, reference in enumerate(hour[24:]):
            children = five[12*index:12*(index+1)]
            self.assertEqual(children[0][0], reference[0])
            self.assertEqual(children[-1][6], reference[6])
            aggregate = [Decimal(children[0][1]), max(Decimal(r[2]) for r in children),
                         min(Decimal(r[3]) for r in children), Decimal(children[-1][4])]
            aggregate += [sum(Decimal(r[j]) for r in children) for j in (5, 7, 8, 9, 10)]
            self.assertEqual(aggregate, [Decimal(reference[j]) for j in (1, 2, 3, 4, 5, 7, 8, 9, 10)])

    def test_prior_hour_mapping_at_two_frozen_ltf_opens(self):
        start = 1794355200000
        for ltf_open, expected in [(start + 55*60000, start), (start + 3600000, start + 3600000)]:
            self.assertEqual(ltf_open - ltf_open % 3600000, expected)


if __name__ == "__main__":
    unittest.main()
