"""Static candidate isolation and provenance. Native Pine runs are separate."""

import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "pine/lesson08-diagnostic.pine"
CANDIDATE = ROOT / "pine/alpha-engine-research.pine"
EXTENSION = "\n// Independent experimental extension."


class IntegratedResearchSourceTests(unittest.TestCase):
    def test_candidate_preserves_accepted_lesson08_body(self):
        candidate_core = CANDIDATE.read_text().split(EXTENSION, 1)[0]
        baseline = BASELINE.read_text()
        self.assertEqual(candidate_core.replace(
            "if barstate.islast and syminfo.tickerid == SYMBOL", "if barstate.islast",
        ).splitlines()[5:], baseline.splitlines()[5:])
        self.assertEqual(hashlib.sha256(BASELINE.read_bytes()).hexdigest(),
                         "8d168c72506b8bc6b4f1595598d8743070675509e79dcee6574dddacc586fe4a")

    def test_build_id_is_derived_from_candidate_bytes(self):
        source = CANDIDATE.read_bytes()
        match = re.search(rb'const string BUILD_ID = "(AE-0\.1\.6-[a-f0-9]{12})"', source)
        self.assertIsNotNone(match)
        normalized = source.replace(match[1], b"__BUILD__", 1)
        self.assertEqual(match[1], b"AE-0.1.6-" + hashlib.sha256(normalized).hexdigest()[:12].encode())

    def test_higher_timeframe_inputs_all_use_previous_bar(self):
        extension = CANDIDATE.read_text().split(EXTENSION, 1)[1]
        requests = [line for line in extension.splitlines() if "request.security" in line]
        self.assertEqual(len(requests), 2)
        for request in requests:
            self.assertIn("request.security(syminfo.tickerid,", request)
            self.assertIn("[time[1], time_close[1], time[50], ta.ema(close, 20)[1], ta.ema(close, 50)[1]]", request)
            self.assertIn("lookahead = barmerge.lookahead_on", request)

    def test_event_and_reaction_precede_pivot_admission(self):
        extension = CANDIDATE.read_text().split(EXTENSION, 1)[1]
        close_gate = extension.index("if aiEnabled and researchChartOK and barstate.isconfirmed")
        crossing = extension.index("bool crossHigh")
        reaction = extension.index("bool reaction")
        admission = extension.index("if aiEnough and aiPivotValid")
        self.assertLess(close_gate, crossing)
        self.assertLess(crossing, reaction)
        self.assertLess(reaction, admission)
        self.assertNotRegex(extension, r"\b(?:strategy\.|alertcondition\(|alert\()")
