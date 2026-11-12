# Phase 3.4 — Lesson 08 / M01 toggle-isolation regression

**Date:** November 12, 2026 (Asia/Manila)  
**Authorized repository:** `jebobomagcode/alpha-engine-tradingview` ONLY  
**Scope:** Regression and acceptance checks; **no changes to Pine trading/research logic**.  
**Starting main:** `144f16314c268e06a299e1a8f5cba0dad468b5fd`  
**Test implementation:** [`tests/test_phase3_4_toggle_isolation.py`](../../tests/test_phase3_4_toggle_isolation.py)  
**GitHub Actions:** [`phase3-4-regression.yml`](../../.github/workflows/phase3-4-regression.yml)  
**Passed CI run:** [43195302296](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43195302296), commit `70981d7ead5bcc284a32724e4129c81425c5debb`.

## Authorization and objective

The owner continued after the bounded Phase 3.3 M01 swing-audit acceptance with "lets proceed" and the Ponder and GitHub tools, in the context of the proposed Phase 3.4 regression test. Verify that M01 opt-in research calculations can neither change nor silently reinterpret the source-grounded Lesson 08 contact, R2-B/R2-A reaction, setup identity, invalidation, expiry, reassessment, nominal geometry or confirmed-hour context.

**Project isolation:** only `jebobomagcode/alpha-engine-tradingview`. Do not access old trading projects. No new Pine features, trading signals, orders, alerts, strategies, backtests, external sites or paid plans. Preserve the owner's one saved private TradingView script and v0.1.1 rollback.

## Baselines and method

- **Accepted v0.1.1 baseline:** Git commit `74e7814e308a40f769d9b57607ebde145f492b8d`, Pine Git blob `80cd5291507fcbb8c919ed02c0f56fb921299b98`, build `L08-0.1.1-7fbb3eb381b6`.
- **Installed native chart/repo candidate v0.1.2:** Git blob `dd1691072e3f81d18217c50efa87c4d6fa6b43e3`, build `L08-0.1.2-3b9eb3065294`. Prior native acceptance covered four individual strict M01 pivot prices and their modeled confirmation cutoffs.
- **Source isolation proof:** A mechanically constrained reverse patch removes only the M01 audit inputs, isolated `strictPivots` function, opt-in confirmed-bar state block, the two M01 informational panel rows, and the two release identifiers/table size change. The result is **the exact v0.1.1 Pine source**. No other code paths differ: the original `barFacts`, `assess`, lifecycle transitions, label emission, M06 nominal geometry, 1H `request.security` tuple, and old panel rows 0–12 are unchanged.
- **Deterministic scenario comparison:** The existing subset Pine-to-Python decision-core interpreter ran frozen cases `P01`, `P04`, `P09`, `P10`, `P11` over three availability/expiry policies, comparing the v0.1.1 and v0.1.2 decision snapshots across **15 replay configurations**. Source-level data dependency and identical core snapshots establish an isolation result at the frozen-model level, not native Pine or market performance.
- **Repeatable CI:** Added read-only GitHub Actions automation with full Git history to make the v0.1.1 baseline available for regression. Existing source/test suites are preserved, not reconstructed.

## Actual execution and correction

Initial CI: [43195172837](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43195172837) at `5abaac6211262c1411a3719438ba864e2d83edb5` — **38 passed, 1 failed**. The failure was in the new Python test helper, which assumed the substring `nominalRisk(` occurred only once, whereas the Pine source correctly contains both its function declaration and a later invocation. No Pine defect was indicated. Corrected the test extractor to anchor to the complete unique function declaration; the Pine source was unchanged.

**Verified CI:** [43195302296](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43195302296) at `70981d7ead5bcc284a32724e4129c81425c5debb`: **39/39 tests PASS** (GitHub Actions runner, `python3 -m unittest discover -s tests -p 'test_*.py' -v`).

| Component | Tests | Result |
| --- | ---: | --- |
| Prior Lesson 08 deterministic/source/receipt checks | 21 | PASS |
| Prior Phase 3.3 optional M01 pivot/model checks | 13 | PASS |
| New Phase 3.4 exact-source isolation/frozen-prefix comparison | 5 | PASS |
| **Total** | **39** | **PASS** |

### Important distinctions

**Supported:** For these exact source versions, turning the M01 audit on or off cannot feed new data into the unchanged Lesson 08 decisions: the new probe has no return path into the old state-machine variables. The original core functions and all original chart decision-path source sections are byte-identical except for unrelated release metadata. Existing and new deterministic Python tests run successfully on GitHub's CI.

**Not supported by this evidence:** Native TradingView ON/OFF comparison of the same activated Lesson 08 setup, intrabar tick execution parity, feed/venue receipt ordering, or profitability. Static code isolation and the frozen Python interpreter do not substitute for observing native Pine on the same evidence cutoff. There is still no BOS/CHoCH automation.

## Remaining native acceptance — cooperative owner chart test

Preserve the existing sole **privately saved v0.1.2** script, exact build `L08-0.1.2-3b9eb3065294`. Do **not** create another private saved script or change Pine.

1. On standard `BINANCE:PAXGUSDT` **Spot 5m**, use an already accepted, unchanged analyst-declared Lesson 08 setup where possible (the archived revision-33 reference with known times/zone is acceptable for descriptive replay). Keep all inputs except the M01 audit toggle identical.
2. Capture the full panel with **M01 audit OFF**: same decision cutoff, setup/contact IDs, current state, R2-B/R2-A first qualifying cutoffs, recorded event, strict status, confirmed-1H reference and nominal geometry.
3. Toggle only **Show confirmed 5m pivots** to **ON**, keep `left=2,right=2`, and capture the same fields before the next bar closes or by using a frozen historical cutoff. Record the exact chart clock and account for any bar rollover. All pre-existing Lesson 08 panel fields should match; only the new M01 rows may differ.
4. Test on a setup that has observed contact or reaction if available, rather than counting a disabled setup as full R2 parity. If no contact/R2 signal exists in the available authorized chart, record those branches **NOT EXERCISED**.
5. Optional: repeat OFF→ON→OFF at an identical cutoff. Never infer source-defined physical touch from OHLC overlap.

| Native gate | At this checkpoint |
| --- | --- |
| Repository v0.1.1/v0.1.2 decision-path isolation | PASS |
| Frozen-prefix L08 model snapshots across 15 configurations | PASS |
| Existing 21 + M01 13 + new 5 CI checks | PASS (39/39) |
| Native TradingView same-cutoff audit OFF/ON L08 panel comparison | NOT RUN |
| Native activated-setup contact/R2 branch parity | NOT RUN |
| Live realtime forming-to-closed bar parity | NOT RUN |

**Next:** Owner screenshot of OFF/ON at comparable cutoff on the correct saved-script v0.1.2 chart. Do not widen to production BOS/CHoCH or open a new feature sprint before recording this bounded acceptance result.

## Owner-assisted native M01 ON/OFF comparison — November 12, 2026, 18:12–18:14 PHT

The owner provided two screenshots of the *same* `BINANCE:PAXGUSDT` **Spot 5m** chart with active build `L08-0.1.2-3b9eb3065294`. The first capture at approximately **18:12:42 PHT** shows M01 research pivot audit **ON**, `left=2, right=2`. The second at **18:14:40 PHT** shows the M01 checkbox **OFF**, with unchanged left/right settings. Both screenshots display the **same last completed candle cutoff, 2026-11-12 10:10 UTC**; each also shows the *next* 5m candle forming. The changing current market price is not treated as a completed-bar decision change.

| Original Lesson 08 panel field | M01 ON | M01 OFF | Comparison |
| --- | --- | --- | --- |
| Instrument / timeframe | Binance PAX Gold / TetherUS Spot 5m | Same | MATCH |
| Build | `L08-0.1.2-3b9eb3065294` | Same | MATCH |
| Last closed 5m cutoff | `11-12 10:10` UTC | Same | MATCH |
| Current state | `INSUFFICIENT · setup declaration` | Same | MATCH |
| 1H / analyst context | `11-12 10:00 · 3940.63 · anchor unverified` | Same | MATCH |
| Setup ID | `Enable and declare context / zone` | Same | MATCH |
| Contact open UTC | `—` | Same | MATCH |
| Touch evidence | `No accepted overlap` | Same | MATCH |
| Recorded R2-B / R2-A | `— / —` | Same | MATCH |
| At last cutoff | `—` | Same | MATCH |
| Strict | `Waiting for later candidate` | Same | MATCH |
| Evidence model | `Declared availability · history reconstructed` | Same | MATCH |
| Nominal only | `Disabled` | Same | MATCH |
| Policy | `R2-B provisional · R2-A comparator` | Same | MATCH |
| M01 high | `3961.97 · known 11-12 08:10` | `Off · research` | EXPECTED AUDIT CHANGE |
| M01 low | `3938.08 · known 11-12 10:10` | `Off · research` | EXPECTED AUDIT CHANGE |

**PASS — bounded native same-cutoff toggle isolation for the disabled-setup branch.** All original Lesson 08 panel outputs are visually identical at the same *completed* 5m decision cutoff. The two optional M01 rows alone switch from displayed confirmed pivots to `Off · research`. This is consistent with the 39/39 automated source/model regression suite.

**Limits and unexercised branches:** The Lesson 08 declaration was disabled in **both** screenshots (`INSUFFICIENT · setup declaration`). Thus **no setup contact, active R2-B/R2-A reaction, invalidation, expiry or reassessment path was exercised by this native ON/OFF pair**. Those branch-specific native regression claims must remain **NOT RUN**, not PASS. The snapshots were taken approximately two minutes apart but show the same last completed cutoff, avoiding a completed-bar rollover; the forming candle's price changed. These are owner-supplied UI screenshots, not a TradingView API capture or realtime tick-by-tick equivalence proof.

### Updated Phase 3.4 gate ledger

| Gate | Updated status |
| --- | --- |
| Exact source isolation: reverse only M01 changes → baseline v0.1.1 | **PASS** |
| GitHub CI 21 original + 13 M01 + 5 Phase 3.4 tests | **PASS — 39/39** |
| Native same-cutoff M01 ON/OFF parity for disabled Lesson 08 declaration | **PASS — owner screenshots** |
| Expected M01 high/low rows ON and OFF | **PASS — owner screenshots** |
| Native activated setup contact and R2-B/R2-A toggle regression | **NOT RUN — branch unexercised** |
| Native terminal lifecycle states under toggle | **NOT RUN — branch unexercised** |
| Native realtime forming-to-close / venue receipt order | **NOT RUN / INSUFFICIENT** |

**Disposition:** The strictly bounded Phase 3.4 *code-level isolation plus disabled-setup native toggle test* passes. Full activated-setup contact/reaction parity remains an explicit follow-up acceptance task. Do not alter Pine, override historical source events, automate trades or label those unexercised branches as passed.

### Subsequent Work audit and bounded continuation — November 12, 2026

The [dated Work audit](../audits/2026-11-12-work-resumption-phase3-4.md) adds direct native same-cutoff M01 toggle parity for two pinned **enabled historical reconstructions** with retained contact and R2 records, one EXPIRED and one REASSESS. The earlier owner-assisted disabled-setup results above remain the original record. Toggle parity at original transition cutoffs, native invalidation and genuine live-to-reload parity remain NOT RUN. The current gate ledger is in the dated audit.
