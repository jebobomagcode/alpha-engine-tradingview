# Phase 3.3 — Opt-in M01-P1 confirmed 5m swing audit (Pine v0.1.2)

**Date:** 2026-11-12 (Asia/Manila)  
**Authorized repository:** `jebobomagcode/alpha-engine-tradingview` ONLY  
**Source:** [Pine v0.1.2](../../pine/lesson08-diagnostic.pine), SHA-256 `a6e624777d792ec528389746da86d54bacc58f412d7ab8040c84fde325b78dd2`; Git blob `dd1691072e3f81d18217c50efa87c4d6fa6b43e3`  
**Reproducible build:** `L08-0.1.2-3b9eb3065294`  
**Prior native-accepted rollback:** [Pine v0.1.1](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/74e7814e308a40f769d9b57607ebde145f492b8d/pine/lesson08-diagnostic.pine), build `L08-0.1.1-7fbb3eb381b6`  
**Status:** SOURCE COMMITTED / 13 NEW LOCAL CHECKS PASS; NATIVE PINE COMPILE AND CHART ACCEPTANCE NOT RUN.

## Authorization and purpose

After [Phase 3.2 owner-assisted persistence acceptance](phase3-2-persistence-interruption-handoff-2026-11-12.md), the owner said **"lets proceed"**, explicitly invoking Ponder and GitHub. This authorizes the next bounded research indicator increment, **not** broad production trading functionality or external project integration. The existing Spot `BINANCE:PAXGUSDT` 5m Lesson 08 diagnostic is preserved in the same repository; prior 26 source-study units and all research receipts are unchanged. New code has **not** been installed in the owner's private TradingView saved script.

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

The illustrative `left=right=2` default is an **independent M01 paper-case choice**, not a Coach threshold. The two new panel rows show **M01 high** and **M01 low**: price and confirmation time (“known”) at the rightmost completed 5m bar. Hover information identifies the original pivot bar. No historical origin-bar labels are backplotted. The chart retains the single preexisting confirmed-1H request and the Lesson 08 contact/reaction markers. Disabled mode shows both audit rows as Off.

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

`origin_at` is the selected candidate's bar-open UTC; `known_at` is the **rightmost confirming bar's close UTC**. Since the script cannot verify actual venue receipt time, `known_at` denotes **modeled chart-bar confirmation**, not exchange delivery. The state updates **only** under `chartOK and pivotProbe and barstate.isconfirmed`. A swing first appears when confirmed; the displayed origin is explanatory, never an earlier actionable timestamp.

No HH/HL, LH/LL, BOS, CHoCH, trend classification, structural orders, stops, signal alerts, backtesting or live trading are implemented by this new probe.

## Local tests and boundaries

The new test file is [`tests/test_phase3_3_m01_probe.py`](../../tests/test_phase3_3_m01_probe.py). The exact candidate source blob `dd1691072e3f81d18217c50efa87c4d6fa6b43e3` was used for a locally executed Python semantic mirror and Pine-source static assertions:

**13 / 13 PASS locally** (Python `unittest`, not native Pine). Cases cover strict extrema and simultaneous high/low at a candidate; equal highs and lows; insufficient right bars; missing/duplicate timestamps; inconsistent 5m close boundaries; impossible OHLC; disabled/forming-bar non-events; alternate left/right; no early confirmation; reproducible build digest; static retention of Lesson 08 request and guards.

The initial alternative-\(\ell/r\) fixture expectation failed because it moved the candidate origin; the **test fixture** was corrected to a proper \(\ell=1,r=3\) local extremum and all 13 then passed. No Pine logic was changed in response to that test error.

**Existing 21 Phase 3.1 tests were not independently re-run in this chat**; the older `assess`, `barFacts`, `nominalRisk`, source identity, risk and setup-identity implementations remain textually unchanged by the small patch. Do not claim 34/34 executed. The code has **not been compiled on native TradingView**, so the next acceptance gates remain NOT RUN. Local Python mirror is not proof of Pine execution, external data parity, or financial performance.

## Native TradingView acceptance plan — owner-assisted

1. Preserve exact v0.1.1 rollback from GitHub. Use the **existing single private saved script**, not a second script; do not touch unrelated projects.
2. In Pine Editor open the named saved `Alpha Engine TradingView — Lesson 08 Diagnostic` and load the exact v0.1.2 source. **Do not publish**. Verify complete editor text and the new build `L08-0.1.2-3b9eb3065294` before updating the saved script.
3. On `BINANCE:PAXGUSDT` **Spot standard 5m**, compile and add or update the saved instance. Verify all existing 12 user inputs and new 3 defaults. An earlier declared setup may remain EXPIRED; that does not affect the independent M01 probe.
4. With `Show confirmed 5m pivots` OFF, the two new panel rows must say `Off · research`. Existing Lesson 08 reason, 1H prior-close, R2-B/R2-A cutoffs and nominal geometry should remain unchanged under identical chart inputs.
5. Turn the pivot probe ON, keep \(\ell=r=2\) initially. Compare the latest `M01 high/low` price and known-at cutoff with five consecutive chart candles. Incomplete realtime 5m must not emit a newly confirmed event.
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

## Phase 3.3 owner-assisted native pivot acceptance — 2026-11-12, ~17:09 PHT

The owner provided two screenshots: the v0.1.2 Pine panel on the standard Binance PAXGUSDT Spot 5-minute chart, and the `Inputs` dialog with **Show confirmed 5m pivots** enabled, **Strict pivot left bars = 2**, **Strict pivot right bars = 2**. The panel shows exact build `L08-0.1.2-3b9eb3065294`, M01 high `3961.97 · known 11-12 08:10` (UTC), and M01 low `3952.13 · known 11-12 07:45` (UTC). The Lesson 08 setup was not enabled, so `INSUFFICIENT · setup declaration` is expected.

**Independent external corroboration, read-only:** Queried Binance Spot public PAXGUSDT 5m klines covering `2026-11-12T07:10:00Z` through `08:25:00Z` (16 rows). Applying the independent strict `left=2, right=2` high/low comparisons to that returned OHLC yielded:

| Swing | Price USDT/PAXG | Origin 5m open UTC | Last right-bar close / earliest modeled confirmation UTC | Compared to TradingView |
| --- | ---: | --- | --- | --- |
| High | **3961.97** | 07:55 | **08:10** | MATCH |
| Low | **3952.13** | 07:30 | **07:45** | MATCH |

**PASS (bounded native + Binance candle comparison):** The two observed native pivot prices and known-at labels agree with independently retrieved exchange-candle data and causal two-right-bar timing. The chart rendered the v0.1.2 panel and the opt-in controls; the earlier screenshot independently showed the two M01 rows OFF by default.

**Still not verified:** Full-session pivot output, realtime developing-candle behavior, future data revisions, native receipt timestamps, v0.1.1 versus v0.1.2 identical-setup parity, exact saved-source v0.1.2 contents, saved-chart reload, and trading performance. Do not infer these from a two-pivot match.

**Next:** Update the existing sole private TradingView script in Pine Editor to the exact verified v0.1.2 source (preserve v0.1.1 rollback in GitHub), save to the **same script slot**, reopen it and verify build / source / chart restoration. Do not create a second script or add full BOS/CHoCH before acceptance.

## Owner-assisted v0.1.2 saved-build reload and third pivot — 2026-11-12, approximately 17:16 PHT

The owner supplied a TradingView screenshot following the previously instructed hard refresh and reopened-script check. It shows **Binance PAX Gold / TetherUS Spot 5m** (no perpetual marker), the active chart indicator title `Alpha Engine | Lesson 08 Research v0.1.2`, and on-chart build `L08-0.1.2-3b9eb3065294`. The Pine Editor displays the named `Alpha Engine TradingVie...` document and source lines `//@version=6`, `indicator("Alpha Engine | Lesson 08 Research v0.1.2", ...)`, and `const string BUILD_ID = "L08-0.1.2-3b9eb3065294"`. This supports the **visible build/editor restoration** result after the owner's reported reload. It does **not** prove exact saved-source byte parity, since no complete v0.1.2 editor export was supplied. It also does not establish an independent remote TradingView storage/API readback.

The M01 panel remained active and showed **high 3961.97, known 08:10 UTC**, while the most recent qualifying low had advanced from 3952.13 to **3922.30, known 09:15 UTC**. The expected `INSUFFICIENT · setup declaration` remained present for the separately disabled Lesson 08 setup, and this is not an indicator defect.

**Independent corroboration:** A public read-only Binance **Spot PAXGUSDT 5m** query for `2026-11-12T08:40:00Z` through `09:20:00Z` yielded the relevant candles. The pivot-origin bar opened at **09:00 UTC** with low **3922.30**; the two later completed 5m bars opened 09:05 (low 3924.79) and 09:10 (low 3926.20). Both earlier neighboring 5m bars opened 08:50 (low 3931.67) and 08:55 (low 3926.02). Therefore `3922.30` is a strict low among two preceding and two following bars. The **09:10–09:15** final right-hand candle gives a modeled earliest confirmation at **09:15 UTC**, exactly matching the panel.

| Acceptance gate | Status | Scope and limitation |
| --- | --- | --- |
| v0.1.2 build visible on Spot 5m after owner's reported hard refresh | **PASS (visual)** | Correct v0.1.2 build, non-perpetual symbol and source header in named Pine Editor |
| Reopened named Pine Editor header/build | **PASS (visual)** | Only first source lines inspected, not all bytes |
| M01 pivot low 3922.30 / 09:15 UTC | **PASS (native + independent Binance OHLC)** | Third specific pivot corroborated; origin 09:00 UTC, 2+2 strict comparison |
| Prior high 3961.97 / 08:10 UTC still displayed | **PASS (visual)** | Previously independently corroborated |
| Complete saved v0.1.2 source hash equality | **NOT VERIFIED** | Requires owner copy/export of complete named editor source |
| Native v0.1.2 all-input reload parity and full-session/realtime behavior | **NOT VERIFIED / NOT RUN** | Screenshot does not show all settings across refresh, native receipt times or forming-bar behavior |
| Full Coach structure, BOS/CHoCH, strategy, trading performance | **NOT IMPLEMENTED / NOT RUN** | Beyond current opt-in research probe |

**Next:** Complete **same-saved-script** source equality without creating another script. From the reopened named Pine Editor, copy the entire source to `.pine` or `.txt`, upload it, and compare raw and LF-normalized SHA-256 against GitHub. Optionally check pivot audit ON and left/right=2 after another refresh. Do not claim the whole Phase 3.3 is accepted solely on the screenshot or develop further detector logic yet.

## Stop and follow-up

Stop this increment at the **v0.1.2 candidate awaiting native TradingView acceptance**. Do not auto-enable pivot audit for signals, auto-arm BOS/CHoCH, claim source-verified structural trend or expand to new symbols. If the prototype fails compile or parity, fix the specific defect against v0.1.1 rollback and retain both records. Native acceptance must precede any broad feature expansion.
