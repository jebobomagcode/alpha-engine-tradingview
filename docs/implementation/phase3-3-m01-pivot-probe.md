# Phase 3.3 — Opt-in M01-P1 confirmed 5m swing audit (Pine v0.1.2)

**Date:** 2026-11-12 (Asia/Manila)  
**Authorized repository:** \`jebobomagcode/alpha-engine-tradingview\` ONLY  
**Source:** [Pine v0.1.2](../../pine/lesson08-diagnostic.pine), SHA-256 \`a6e624777d792ec528389746da86d54bacc58f412d7ab8040c84fde325b78dd2\`; Git blob \`dd1691072e3f81d18217c50efa87c4d6fa6b43e3\`  
**Reproducible build:** \`L08-0.1.2-3b9eb3065294\`  
**Prior native-accepted rollback:** [Pine v0.1.1](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/74e7814e308a40f769d9b57607ebde145f492b8d/pine/lesson08-diagnostic.pine), build \`L08-0.1.1-7fbb3eb381b6\`  
**Status:** SOURCE COMMITTED / 13 NEW LOCAL CHECKS PASS; NATIVE PINE COMPILE AND CHART ACCEPTANCE NOT RUN.

## Authorization and purpose

After [Phase 3.2 owner-assisted persistence acceptance](phase3-2-persistence-interruption-handoff-2026-11-12.md), the owner said **"lets proceed"**, explicitly invoking Ponder and GitHub. This authorizes the next bounded research indicator increment, **not** broad production trading functionality or external project integration. The existing Spot \`BINANCE:PAXGUSDT\` 5m Lesson 08 diagnostic is preserved in the same repository; prior 26 source-study units and all research receipts are unchanged. New code has **not** been installed in the owner's private TradingView saved script.

## Source-to-methodology chain

- **COACH_EXPLICIT, sole PDF pp9, 14–16 and 25:** market structure includes higher highs/lows, continuation BOS, and potential-reversal CHoCH in defined contexts. The original Coach source does **not** specify exact mechanical pivot search left/right lengths or an automated 5m trend state.
- **INDEPENDENT_EXTENSION / EXPERIMENTAL:** M01-P1 from [causal market structure research](../methodology/01-causal-market-structure.md#c-candidate-swing-methods-three-materially-different-models) defines a **strict, causally confirmed local fractal swing**. It is an optional descriptive comparator to manual M01-P0, not a claim to have implemented Coach's fully discretionary structural model.
- **OPEN_UNRESOLVED:** numeric pivot lengths, structural-vs-micro significance, BOS/CHoCH reference arming, ties under other variants, minimum market significance, predictive ability and event/market-data receipt times.

## New bounded interface

Added three **optional** inputs, appended after the preexisting 12:

| Input | Initial value | Meaning |
| --- | --- | --- |
| Show confirmed 5m pivots (research only) | OFF | Compute and display latest strict high and low; no entry gate or trade signal |
| Strict pivot left bars | 2, user-adjustable 1–8 | Number of already earlier 5m bars compared against candidate |
| Strict pivot right bars | 2, user-adjustable 1–8 | Number of later closed 5m bars required before confirmation |

The illustrative \`left=right=2\` default is an **independent M01 paper-case choice**, not a Coach threshold. The two new panel rows show **M01 high** and **M01 low**: price and confirmation time (“known”) at the rightmost completed 5m bar. Hover information identifies the original pivot bar. No historical origin-bar labels are backplotted. The chart retains the single preexisting confirmed-1H request and the Lesson 08 contact/reaction markers. Disabled mode shows both audit rows as Off.

### Formal candidate and timing

At closed 5m decision bar \(j\) and chosen nonnegative lookback offsets \(\ell,r\ge1\), the candidate origin is \(i=j-r\). Confirm a strict high at \(j\) iff:

\[
H_i>\max\{H_k : i-\ell\le k\le i+r,\ k\ne i\},
\]

and a strict low iff

\[
L_i<\min\{L_k : i-\ell\le k\le i+r,\ k\ne i\}.
\]

Equal highs or lows disqualify their respective strict extrema. Require \(\ell+r+1\) valid completed standard 5m OHLC bars; all consecutive opens must differ by exactly 300,000 ms; each close timestamp must equal open + 300,000 ms, with internally valid OHLC. Missing, duplicated, irregular or malformed windows produce no new confirmed pivot, never an invented swing.

\`origin_at\` is the selected candidate's bar-open UTC; \`known_at\` is the **rightmost confirming bar's close UTC**. Since the script cannot verify actual venue receipt time, \`known_at\` denotes **modeled chart-bar confirmation**, not exchange delivery. The state updates **only** under \`chartOK and pivotProbe and barstate.isconfirmed\`. A swing first appears when confirmed; the displayed origin is explanatory, never an earlier actionable timestamp.

No HH/HL, LH/LL, BOS, CHoCH, trend classification, structural orders, stops, signal alerts, backtesting or live trading are implemented by this new probe.

## Local tests and boundaries

The new test file is [\`tests/test_phase3_3_m01_probe.py\`](../../tests/test_phase3_3_m01_probe.py). The exact candidate source blob \`dd1691072e3f81d18217c50efa87c4d6fa6b43e3\` was used for a locally executed Python semantic mirror and Pine-source static assertions:

**13 / 13 PASS locally** (Python \`unittest\`, not native Pine). Cases cover strict extrema and simultaneous high/low at a candidate; equal highs and lows; insufficient right bars; missing/duplicate timestamps; inconsistent 5m close boundaries; impossible OHLC; disabled/forming-bar non-events; alternate left/right; no early confirmation; reproducible build digest; static retention of Lesson 08 request and guards.

The initial alternative-\(\ell/r\) fixture expectation failed because it moved the candidate origin; the **test fixture** was corrected to a proper \(\ell=1,r=3\) local extremum and all 13 then passed. No Pine logic was changed in response to that test error.

**Existing 21 Phase 3.1 tests were not independently re-run in this chat**; the older \`assess\`, \`barFacts\`, \`nominalRisk\`, source identity, risk and setup-identity implementations remain textually unchanged by the small patch. Do not claim 34/34 executed. The code has **not been compiled on native TradingView**, so the next acceptance gates remain NOT RUN. Local Python mirror is not proof of Pine execution, external data parity, or financial performance.

## Native TradingView acceptance plan — owner-assisted

1. Preserve exact v0.1.1 rollback from GitHub. Use the **existing single private saved script**, not a second script; do not touch unrelated projects.
2. In Pine Editor open the named saved \`Alpha Engine TradingView — Lesson 08 Diagnostic\` and load the exact v0.1.2 source. **Do not publish**. Verify complete editor text and the new build \`L08-0.1.2-3b9eb3065294\` before updating the saved script.
3. On \`BINANCE:PAXGUSDT\` **Spot standard 5m**, compile and add or update the saved instance. Verify all existing 12 user inputs and new 3 defaults. An earlier declared setup may remain EXPIRED; that does not affect the independent M01 probe.
4. With \`Show confirmed 5m pivots\` OFF, the two new panel rows must say \`Off · research\`. Existing Lesson 08 reason, 1H prior-close, R2-B/R2-A cutoffs and nominal geometry should remain unchanged under identical chart inputs.
5. Turn the pivot probe ON, keep \(\ell=r=2\) initially. Compare the latest \`M01 high/low\` price and known-at cutoff with five consecutive chart candles. Incomplete realtime 5m must not emit a newly confirmed event.
6. Check one strict tie, missing or irregular-bar case if available from native evidence; record NOT RUN otherwise. Do not manufacture a market event just to obtain a pass.
7. Save the **same** private script, refresh, and verify the exact build, input values and swing confirmation cutoffs. Separate editor equality, compiled panel and saved-instance restoration. Keep previous failures and Phase 3.2 acceptance intact.

### Acceptance gate ledger (as of this commit)

| Gate | Result |
| --- | --- |
| GitHub v0.1.2 source / reproducible build SHA | PASS — exact local candidate blob |
| 13 new Python mirror / static checks | PASS |
| Previous 21 regressions re-executed against v0.1.2 | NOT RUN |
| Native Pine v6 compile and no runtime errors | NOT RUN |
| Native chart 5m pivot known-at/origin correctness | NOT RUN |
| Native unchanged Lesson 08 baseline and inputs | NOT RUN |
| Same saved private script source equality and reload | NOT RUN |
| Profitability, exchange receipt, physical touch, execution | NOT RUN / INSUFFICIENT |

## Stop and follow-up

Stop this increment at the **v0.1.2 candidate awaiting native TradingView acceptance**. Do not auto-enable pivot audit for signals, auto-arm BOS/CHoCH, claim source-verified structural trend or expand to new symbols. If the prototype fails compile or parity, fix the specific defect against v0.1.1 rollback and retain both records. Native acceptance must precede any broad feature expansion.
