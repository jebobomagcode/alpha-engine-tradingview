"""Phase 3.3 manual-equivalence tests for the M01-P1 opt-in 5m pivot audit.

These execute a Python mirror of Pine's strictPivots; not a Pine compiler or a
native TradingView chart test. Tests inspect the committed Pine syntax separately.
"""
from pathlib import Path
import unittest
import hashlib
import re

# Historical v0.1.2 study must remain pinned when a newer candidate exists.
import subprocess
ROOT = Path(__file__).resolve().parents[1]
SOURCE = subprocess.check_output(["git", "show", "3458ff6854e9c349aef10a30e487a908a3648441:pine/lesson08-diagnostic.pine"], cwd=ROOT).decode("utf-8")
STEP=300000


def bar(t,h,l,o=None,c=None,close_t=None):
    return {"t": t, "end": t+STEP if close_t is None else close_t,
            "o": (h+l)/2 if o is None else o,"h":h,"l":l,
            "c": (h+l)/2 if c is None else c}


def audit(bars,left=2,right=2,confirmed=True,enabled=True):
    if not (enabled and confirmed) or len(bars) < left+right+1:
        return None,None
    window=bars[-(left+right+1):]
    cand=window[left]
    for j,x in enumerate(window):
        if x is None or not all(k in x and x[k] is not None for k in ("t","end","o","h","l","c")):
            return None,None
        if x["end"] != x["t"]+STEP or x["h"]<max(x["o"],x["c"]) or x["l"]>min(x["o"],x["c"]):
            return None,None
        if j>0 and x["t"]-window[j-1]["t"]!=STEP:
            return None,None
    high=all(cand["h"]>x["h"] for j,x in enumerate(window) if j!=left)
    low=all(cand["l"]<x["l"] for j,x in enumerate(window) if j!=left)
    event=lambda value: {"value":value,"origin":cand["t"],"known_at":window[-1]["end"]}
    return event(cand["h"]) if high else None,event(cand["l"]) if low else None


class Phase33PivotProbe(unittest.TestCase):
    def setUp(self):
        self.start=1794355200000
        self.rows=[bar(self.start+i*STEP,h,l) for i,(h,l) in enumerate([(106,103),(108,104),(111,99),(109,101),(107,102)])]

    def test_strict_pivot_both_extrema_at_one_origin(self):
        high,low=audit(self.rows)
        self.assertEqual((high["value"],low["value"]),(111,99))
        self.assertEqual(high["origin"],self.start+2*STEP)
        self.assertEqual(high["known_at"],self.start+5*STEP)
        self.assertGreater(high["known_at"],high["origin"])

    def test_high_tie_rejected(self):
        rows=[dict(x) for x in self.rows]
        rows[1]["h"]=111
        self.assertIsNone(audit(rows)[0])
        self.assertIsNotNone(audit(rows)[1])

    def test_low_tie_rejected(self):
        rows=[dict(x) for x in self.rows]
        rows[4]["l"]=99
        self.assertIsNone(audit(rows)[1])
        self.assertIsNotNone(audit(rows)[0])

    def test_requires_all_right_bars(self):
        self.assertEqual(audit(self.rows[:4]),(None,None))

    def test_missing_bar_blocks_a_pivot(self):
        rows=[dict(x) for x in self.rows]
        rows[3]["t"]+=STEP
        rows[3]["end"]+=STEP
        self.assertEqual(audit(rows),(None,None))

    def test_duplicate_timestamp_blocks_a_pivot(self):
        rows=[dict(x) for x in self.rows]
        rows[3]["t"]=rows[2]["t"]
        rows[3]["end"]=rows[3]["t"]+STEP
        self.assertEqual(audit(rows),(None,None))

    def test_nonstandard_interval_blocks_a_pivot(self):
        rows=[dict(x) for x in self.rows]
        rows[2]["end"]+=1
        self.assertEqual(audit(rows),(None,None))

    def test_bad_ohlc_blocks_a_pivot(self):
        rows=[dict(x) for x in self.rows]
        rows[4]["c"]=1000
        self.assertEqual(audit(rows),(None,None))

    def test_disabled_and_forming_are_non_events(self):
        self.assertEqual(audit(self.rows,enabled=False),(None,None))
        self.assertEqual(audit(self.rows,confirmed=False),(None,None))

    def test_alternative_parameters_keep_confirmation_cutoff(self):
        shifted=[bar(self.start+i*STEP,h,l) for i,(h,l) in enumerate([(106,103),(111,99),(109,101),(107,102),(105,103)])]
        h,l=audit(shifted,left=1,right=3)
        self.assertIsNotNone(h)
        self.assertIsNotNone(l)
        self.assertEqual(h["known_at"],self.rows[-1]["end"])

    def test_no_early_confirmation_with_partial_prefix(self):
        self.assertTrue(all(audit(self.rows[:n])==(None,None) for n in range(5)))
        self.assertIsNotNone(audit(self.rows)[0])

    def test_source_release_identity_and_lesson08_preserved(self):
        match=re.search(r'const string BUILD_ID = "(L08-0\.1\.2-([0-9a-f]{12}))"',SOURCE)
        self.assertIsNotNone(match)
        canonical=SOURCE.replace(match.group(1),'__BUILD__',1).encode()
        self.assertEqual(hashlib.sha256(canonical).hexdigest()[:12],match.group(2))
        self.assertEqual(SOURCE.count('request.security('),1)
        self.assertIn('[time[1], time_close[1], close[1]]',SOURCE)
        self.assertNotIn('strategy(',SOURCE)
        self.assertNotIn('alertcondition(',SOURCE)
        self.assertIn('const string SYMBOL = "BINANCE:PAXGUSDT"',SOURCE)
        self.assertIn('"R2-B provisional · R2-A comparator"',SOURCE)

    def test_source_pivot_gates_and_data_coverage(self):
        self.assertIn('pivotProbe and barstate.isconfirmed',SOURCE)
        self.assertIn('highKnownUTC := time_close',SOURCE)
        self.assertIn('lowKnownUTC := time_close',SOURCE)
        self.assertIn('highOriginUTC := time[pivotRight]',SOURCE)
        self.assertIn('lowOriginUTC := time[pivotRight]',SOURCE)
        self.assertIn('candidateHigh > high[offset]',SOURCE)
        self.assertIn('candidateLow < low[offset]',SOURCE)
        self.assertIn('time[offset] - time[offset + 1] == STEP',SOURCE)
        self.assertIn('time_close[offset] == time[offset] + STEP',SOURCE)
        self.assertIn('pivotProbe = input.bool(false',SOURCE)
        self.assertEqual(SOURCE.count('label.new('),3) # existing L08 markers only
        self.assertEqual(SOURCE.count('request.security('),1)

if __name__ == '__main__':
    unittest.main()
