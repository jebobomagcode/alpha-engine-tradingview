# Phase 3.5 independent code and evidence review

**Date** 2026-11-12 (Asia/Manila) · **Repository** `jebobomagcode/alpha-engine-tradingview`

**Disposition: ACCEPTABLE FOR NATIVE TESTING.** Keep the draft PR and the existing private v0.1.2 save. The positive-price correction and code-level Lesson 08 isolation passed this review. Strengthen candidate-specific regression tests and finish the native gates before promotion.

## A. Exact reviewed checkpoint

| Item | Verified identity |
| --- | --- |
| Accepted main | `3458ff6854e9c349aef10a30e487a908a3648441` |
| Draft PR #1 head | `51cf1a9fc94de1bb0f5693b6913b68102afe207a` on `feat/phase3-5-m01-validity-freshness-20261112` |
| Candidate code commit | `4065e3b422fa5d2a5b4a92e12bbd364cea2a56f5`. The later PR head changes the implementation record only. |
| Accepted Pine | v0.1.2, build `L08-0.1.2-3b9eb3065294`, blob `dd1691072e3f81d18217c50efa87c4d6fa6b43e3` |
| Candidate Pine | v0.1.3, build `L08-0.1.3-3e3d909ba9f5`, blob `218e54cf573d6dfcc7b3306d22a0a34f966db160`, SHA-256 `8d168c72506b8bc6b4f1595598d8743070675509e79dcee6574dddacc586fe4a`. Masking only the build literal with `__BUILD__` and recomputing SHA-256 reproduces its 12-character suffix. |
| Push CI | Run `43212688894`, job `131164033285`, executed 50 tests at `4065e3b422fa5d2a5b4a92e12bbd364cea2a56f5`, all passed. |
| Latest PR CI | Run `43213331667`, job `131166206870`, executed 50 tests on GitHub's synthetic merge ref `de907062c97dff9ef15854f7a87e087c44716a73` for the exact reviewed head and base, all passed. The PR remains a draft. |

All five changed files were read in full or compared in full against main: `pine/lesson08-diagnostic.pine`, `tests/test_phase3_3_m01_probe.py`, `tests/test_phase3_4_toggle_isolation.py`, `tests/test_phase3_5_m01_evidence.py`, and `docs/implementation/phase3-5-m01-data-validity-and-evidence-status.md`. CI workflow, original Coach PDF, PCSS lesson records and prior acceptance evidence remain outside the PR diff. The repository PDF SHA-256 remains `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`.

[PR #1 diff](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/1/files) · [Candidate source](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/51cf1a9fc94de1bb0f5693b6913b68102afe207a/pine/lesson08-diagnostic.pine) · [Push CI](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43212688894) · [PR CI](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43213331667)

## B. Original defect and minimum reproduction

Use the allowed `L=R=1` setting, three consecutive 5m bars, exact 300,000 ms durations, and the following prices. Let the first bar open at time `t`.

| Open time | O | H | L | C |
| --- | ---: | ---: | ---: | ---: |
| `t` | 2.5 | 3 | 2 | 2.5 |
| `t+5` minutes | 2 | 4 | **0** | 2 |
| `t+10` minutes | 2.5 | 3 | 2 | 2.5 |

The center strictly dominates both neighbors on each side of its range, and the geometric inequalities hold. Running the predicate mechanically translated from each pinned Pine function gives v0.1.2 **both pivots** at `t+15` minutes and v0.1.3 **enough history, invalid window, neither pivot**. Lowering the center low to −1 also fails v0.1.3. Changing only the center low from 0 to 1 restores both valid pivot events. Three bars are minimal under the supported input bounds. These synthetic bars demonstrate a software-domain issue. [Phase 3.4 defect record](2026-11-12-work-resumption-phase3-4.md#c-independent-technical-findings)

## C. Candidate code review

**Patch A — ACCEPTED BEHAVIOR.** For a finite, defined bar, the intended exact-domain invariant is 0 < L ≤ min(O,C) ≤ max(O,C) ≤ H. Pine evaluates the corresponding comparisons using its float rules. Therefore all OHLC values are positive, and a geometry-consistent bar with positive OHLC satisfies the added inequality. It checks every required offset, including both sides of the pivot and the decision bar. Clock validity needs both exact bar length and consecutive opens. Pine v6 `and` is lazy, so missing local timestamps and prices fail the early guards. If the adjacent older open is missing, timestamp subtraction yields `na` and the comparison cannot pass. The returned four members are booleans, while price and timestamp record variables have explicit float/int types. The minimum and maximum window lengths are **3 and 17**, with **5 at the default 2/2**. The candidate handoff's “five (or more)” wording is a minor documentation error.

**Precision — DESIGN TRADEOFF.** TradingView documents rounding float operands to nine fractional digits for comparisons. Under that comparison model, an off-grid low of 10⁻¹⁰ can compare equal to zero, a high advantage of 4 × 10⁻¹⁰ can become a tie, and an open 10⁻¹⁰ below its stated low can round equal and pass geometry. These differences were reproduced in the narrow source translation with the documented comparison rule. They are outside the pinned PAXGUSDT Spot order-price increment of 0.01 and were absent from the archived trade-price rows. The strict positivity guarantee still holds for finite operands because a low rounding strictly above zero forces the compared body prices and high to round above zero. Feed tick membership and native handling of malformed off-grid data are separate gates. Avoid broadening the domain or snapping the research prices to ticks without an explicit data contract.

**Patch B — ACCEPTED BEHAVIOR.** The tuple separates enough history, window validity, and high/low events. State changes are inside `chartOK and pivotProbe and barstate.isconfirmed`. An invalid window clears neither retained price nor its original timestamps. On recovery, a full admissible window with no pivot changes the evidence label and keeps both records. The table has 16 rows indexed 0–15. The new row has precedence OFF, wrong chart, then committed evaluation status. The last-bar render can run during formation, but it reads the evidence already committed at a previous close. The detector receives no future values. Confirmed-chart-bar time is modeled evidence time.

**Display — DESIGN TRADEOFF.** `VALID · new pivot` may remain visible for the entire next forming candle and through a feed pause. Its tooltip scopes it to the latest evaluated closed bar. A reader who misses the tooltip and chart clock could read it as a fresh intrabar event. A gap becomes `INVALID` when an evaluated close actually spans the missing interval. The script cannot report a missing bar as it is happening without a separate heartbeat. Toggle and L/R input changes re-evaluate loaded history. Pivot records reconstructed after such a change describe that run with the selected parameters. They do not establish that the toggle or those parameters were present historically. Identical results after reload require matching source, inputs and relevant loaded chart data. The candidate has no exchange receipt clock.

[TradingView types and float comparisons](https://www.tradingview.com/pine-script-docs/language/type-system/#float) · [Pine v6 booleans and lazy evaluation](https://www.tradingview.com/pine-script-docs/migration-guides/to-pine-version-6/) · [Pine bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/#barstateisconfirmed) · [Pine execution and rollback](https://www.tradingview.com/pine-script-docs/language/execution-model/) · [Pine tables](https://www.tradingview.com/pine-script-docs/visuals/tables/) · [Pinned market identity and metadata](../research/phase2-m07-frozen-market-evidence.md)

## D. Independent testing and falsification

**Repository run:** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v` returned **50/50 PASS** on the exact draft head. The prior record's grouping of “historical 39” is imprecise. The 21 original Lesson 08 checks read the **current** source. They exercise a subset of translated Pine functions, source assertions and frozen Binance integrity. Only the 13 Phase 3.3 and five Phase 3.4 checks pin earlier Pine. The eleven Phase 3.5 tests use a Python mirror, archived inputs and source assertions. The mirror labels both event and no-event windows simply VALID. Its retention test reuses the same cutoff with altered prices, so it does not demonstrate progression across closes or recovery.

**Source-derived verification:** Separately executed a narrow translation of the pinned `strictPivots` blocks with explicit history indices, missing values and, where relevant, documented nine-place comparison. Checked the minimum counterexample, 18 individual missing-field variants, 21 invalid price/body/clock mutations, gap, duplicate, partial history, both tie directions, and **512 complete windows or truncated prefixes across all 64 L/R pairs**. All **30** admissible 2/2 windows from the existing 34-bar receipt agreed between versions, including the five previously reported extrema. A sequential 1/1 prefix with a real timestamp gap went from insufficient → new dual pivot → invalid for two closes → valid/no pivot. The exact record update guards preserve the original event across those steps. These are independently formulated deterministic inputs and source-driven checks by the same reviewer. The translated functions and record-guard analysis are bounded models rather than a full runtime emulator.

**Mutation checks — TEST COVERAGE GAP.** Ran all 50 tests on each of the following in-memory candidate mutations, recomputing its source-derived ID so the hash test checked the mutated source correctly. Every mutant stayed **50/50 green**. The actual checked-in candidate has none of these mutations.

| Mutation | Expected error the current suite misses |
| --- | --- |
| Replace `and low[offset] > 0` with `and (true or low[offset] > 0)` | The intended guard is bypassed. Retaining the string is enough to satisfy the source assertion. |
| Swap `VALID · new pivot` and `VALID · no new pivot` | The two valid outcomes display the reverse meanings. The Python mirror checks a generic VALID label. |
| Set table height to 15 with row index 15 still rendered | The new evidence cell is out of bounds. The source check does not validate the table index contract. |

Before promotion, require a candidate test to kill all three mutants. A minimal source-linked predicate check, explicit status truth table, and indexed row-count assertion address different failure modes. Extend the retention fixture across a later bad bar and the first fully valid recovery window. Keep the pinned historical tests as evidence of what shipped. [Candidate test file](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/51cf1a9fc94de1bb0f5693b6913b68102afe207a/tests/test_phase3_5_m01_evidence.py)

## E. Lesson 08 compatibility and provenance

**PASS — exact source isolation.** Mechanically replacing only the changed M01 predicate/tuple and adapter block, reverting the table size and release strings, and removing row 15 recovered the entire accepted v0.1.2 Pine file byte-for-byte (SHA-256 `a6e624777d792ec528389746da86d54bacc58f412d7ab8040c84fde325b78dd2`). Confirmed 1H mapping, setup and contact identity, availability, geometric overlap, body engulf, R2-B/R2-A, Strict receipt uncertainty, invalidation, expiry, REASSESS, retained R2 history, nominal risk and rows/labels are unchanged in source. The visible Build value intentionally identifies v0.1.3. M01 still has no dependency path into Lesson 08 decisions.

**COACH_EXPLICIT:** PDF pp. 8–10 describes engulfing around significant S/R and a closed confirmation in context, with alternative confirmation forms on p. 10. **INTERPRETATION:** PCSS treats context, zone and reaction as separate evidence gates. **INDEPENDENT_EXTENSION / EXPERIMENTAL:** a closed-5m strict local pivot with default 2/2, positive Spot domain and evidence display. No BOS/CHoCH or source-fidelity claim is inferred from a pivot match. [Coach PDF](../../sources/coach%20trading%20lessons.pdf#page=10) · [Lesson 08 PCSS](../lessons/08-trading-entry-workflow.md) · [M01 candidate research](../methodology/01-causal-market-structure.md)

## F. Native TradingView verification

Opened a separate **Untitled script** from TradingView's new indicator template. Pasted the canonical source and copied the full editor text back. The copy had 239 CRLF line endings and matched all 239 source lines exactly after CRLF → LF normalization. Used **Add to chart**, which TradingView documents as a temporary draft operation. Both v0.1.2 and v0.1.3 were initially visible. Their tables share a position, so I temporarily hid the v0.1.2 chart instance to capture the candidate by itself. [TradingView temporary draft workflow](https://www.tradingview.com/support/solutions/43000711497-how-to-create-a-new-script/)

| Native gate | Result and scope |
| --- | --- |
| Exact draft compilation and chart execution | **PASS.** Qualified `BINANCE:PAXGUSDT` Spot standard 5m displayed build `L08-0.1.3-3e3d909ba9f5`, intact Lesson 08 panel and the new M01 evidence row. |
| Default OFF and enabled valid/no-event | **PASS.** At the 14:20 UTC last-closed cutoff, OFF displayed in all three M01 rows. ON at 22:22:46 PHT, with 2/2 and the same 14:20 cutoff, showed `VALID · no new pivot`, retained high 3895.46 known 14:15 and low 3885.00 known 14:05. |
| Sampled live 5m confirmation | **PASS, one observed rollover.** At 22:24:52 PHT the 14:20 UTC cutoff still showed `VALID · no new pivot`. At 22:25:04 PHT the 14:25 UTC cutoff showed `VALID · new pivot`, low **3883.33 known 14:25**, and retained high **3895.46 known 14:15**. The panel already showed the following 5m candle forming. This brackets the visible closed-bar change and does not identify the platform's exact tick or exchange receipt. |
| Lesson 08 current-source native compatibility | **PASS, bounded.** Disabled setup fields matched the accepted chart at the same 14:20 cutoff apart from release identity. The already pinned revision 31 was then reconstructed on the candidate. At the same 14:25 cutoff, captures at 22:26:29 and 22:27:01 PHT showed identical original fields with only M01 toggled. Both showed `REASSESS · episode ended`, contact November 11 14:50 UTC, retained R2-B and R2-A at 15:00 UTC and Strict receipt order UNKNOWN. All 19 UI input values were read back and only M01 changed. This exercises reconstructed state and the terminal history display. |
| Native malformed OHLC, clock gap, short history, or wrong-chart status | **NOT RUN.** These were not observed in the qualified chart run. Deterministic window tests are separate. |
| Native hourly rollover or original Lesson 08 transition-cutoff equivalence | **NOT RUN.** The displayed 14:00 UTC confirmed 1H reference stayed fixed across the observed 5m rollover. |
| Candidate realtime-to-reload or durable saved-script parity | **NOT RUN.** The test intentionally used an unsaved temporary draft. Actual exchange receipt and physical-touch evidence remain **INSUFFICIENT**. |

Removed the temporary v0.1.3 chart instance and restored v0.1.2 visibility. The final chart showed only the accepted build with its original disabled setup and M01 off. Neither Save Script nor Publish was used. The private v0.1.2 source and saved script were preserved.

## G. Ponder findings and H. decision

1. **Accepted behavior, retain.** An invalid recent window and a valid older pivot can coexist. Retaining that record is valuable if the original close is shown. Clearing it after a bad window loses valid historical evidence. The next test should require the old timestamp to survive both invalidation and recovery.
2. **Design tradeoff, clarify if needed.** An always-visible “Last closed M01” label or explicit cutoff would reduce the chance of treating a prior event as current during formation. If native observation shows that users reliably associate the existing chart clock and tooltip with the M01 status, the shorter row remains defensible. A wall-clock feed-staleness alarm is a separate question.
3. **Test coverage gap, prioritize.** Repository tests need to reject wrong *candidate source* even when pinned baselines remain green. The three surviving mutants give concrete acceptance criteria. Simulated gap and malformed-price checks complement native compile, stable panel state, and an observed close. Wait for native market evidence before making feed-level claims.
4. **Open / insufficient evidence, defer.** Keep historical pivot information outside automated decisions. A future consumer would need an explicit as-of clock, historical event ID, admissible evidence contract and stale-data policy. The “VALID” label alone supplies none of those conditions.

**Decision: ACCEPTABLE FOR NATIVE TESTING.** The source-derived comparisons show the correction works under the qualified Spot assumptions, and exact source recovery establishes Lesson 08 isolation. The evidence row uses the most recent evaluated close and retains older records. The surviving mutations show that green CI alone cannot guard future revisions. A separate rewrite or a wider research phase would add scope without addressing the next failure modes.

## I. GitHub review checkpoint

This dated review is recorded on the dedicated `audit/phase3-5-independent-review-20261112` branch from the reviewed head. Accepted main and the draft PR retain the exact checkpoints in §A. The candidate, tests and earlier records remain intact. See the ref readback and exact documentation commit in the accompanying review report.
