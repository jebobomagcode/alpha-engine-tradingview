# Phase 3 Lesson 08 chart diagnostic v0.1.0

**Scope:** Binance Spot PAXGUSDT, standard 5m candles, one versioned bullish continuation setup. This indicator describes evidence and waiting states. It defines no trading operation, strategy, alerts or production rule.

- [Exact v0.1.0 Pine v6 source](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/387c425b24ee5bb9b56a3a1c464cd4d313d7cb74/pine/lesson08-diagnostic.pine) SHA-256 `9c0eb91b74054f236213ad58607fbb29ceb81cffc9277072f6d7668a478b60e6`
- [M07 acceptance protocol](../research/phase2-mtf-validation-and-falsification-protocol.md#i-bounded-m07-profile) · [Frozen Binance evidence](../research/phase2-m07-frozen-market-evidence.md) · [M06 risk specification](../methodology/09-m06-risk-and-execution-uncertainty.md)
- [Original decision-core and evidence checks](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/387c425b24ee5bb9b56a3a1c464cd4d313d7cb74/tests/test_lesson08_diagnostic.py)

## Source and interpretation

**COACH_EXPLICIT.** The original [Coach PDF](../../sources/coach%20trading%20lessons.pdf#page=10), 35 pages, SHA-256 `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`, is the sole Coach authority. Pages 6 and 10 describe higher-timeframe trend and zone, a lower-timeframe confirmation after price reaches the zone, waiting when it does not, and entry only after confirmation closes. Engulfing, rejection with follow-through, and a strong candle are alternative confirmations on p10. The page describes stops outside the relevant zone and next S/R or fixed RR alternatives for targets. The p13 range workflow has a separate break-of-confirmation condition. [Lesson 08 PCSS interpretation](../lessons/08-trading-entry-workflow.md)

**INDEPENDENT_EXTENSION / EXPERIMENTAL.** The one-sided profile, explicit clocks, inclusive OHLC interval overlap, strict opposite-color real-body engulfing, one-episode suspension, and R2-B/R2-A policies are project definitions. No new universal Coach threshold, candle order or observed trade is implied.

## Chart use

1. Open the standard-candle **BINANCE:PAXGUSDT** chart at **5 minutes** and add the Pine source to the chart in the editor. Pine guards the exact instrument, 5m interval and standard chart family. Select Candles for the accepted chart configuration. The source disables active setup processing until the declaration is enabled.
2. Enter the version, bullish 1H reference close, separately declared context and zone availability, support floor and ceiling, and exclusive expiry. TradingView displays input times in the chart timezone. Preserve the exact UTC instants in the setup record. The zone, levels and bias are analyst inputs. Use a new version for any changed declaration.
3. Keep a separate timestamped manifest if claiming contemporaneous analyst knowledge. A chart input only establishes the clock used by this calculation. Historical configurations and amended histories remain reconstructions.
4. The panel shows the most recent closed decision, current confirmed 1H reference, setup/contact IDs and first qualifying close under each policy. Two Data Window values expose the prior confirmed 1H close boundary (Unix seconds) and price for each chart bar. The display uses one zone box and at most three cutoff markers. A geometric overlap establishes range intersection. Physical touch remains unknown. Strict remains unknown for a later candidate because no receipt-order channel is available.
5. Optional nominal geometry requires a positive long entry reference, a positive stop below both entry and support floor, and target above entry. Output is loss distance in USDT/PAXG and gross reward divided by loss distance. No quantity, exchange order constraints, costs, rounding, fill or net payout are inferred by this script.

## Causal and lifecycle conventions

- **Opening premise.** The accepted 1H tuple is offset by one hourly bar, using TradingView's documented lookahead-on alignment. Its hourly open and close IDs must match the immediately preceding hour at the 5m open. The selected manual anchor must have been seen in loaded chart history. Activation is the later declared availability of zone and context, at or before the 5m open. A new hourly reference cannot affect an earlier candle. [TradingView higher-timeframe requests](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) · [Bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/)
- **Decision.** State mutates only on the confirmed 5m update. Under the chart model the exclusive bar end is the decision cutoff. It is distinct from observed wall time, venue receipt, physical touch and a chart label. A missing active bar, missing required hourly premise or incomplete active OHLC blocks subsequent first-event claims for that run. An unavailable adjacent predecessor blocks the current reaction. No missing interval is synthesized.
- **Identity.** Within the fixed profile and product, setup ID combines declared version, hourly anchor and activation. Contact ID extends it with the first accepted overlap-bar open. A changed declaration requires a new version. First cutoffs are write-once within a run. Inputs changing or reload can cause recalculation. External observations are the historical record of what the earlier chart showed.
- **End of episode.** A close strictly below the support floor invalidates an active setup. The exclusive expiry blocks any fresh qualification at or after its cutoff. An approach-side separator suspends the setup without automatic re-entry. The **first departure that itself completes an eligible later engulf** can issue that reaction at its close, then end the episode. This resolves the P11/P04 counterexample to unconditionally closing the episode before classifying the departure candle. It is an explicit Phase 3 interpretation of the M07 convention. Further bars cannot re-arm the version. [Pinned P04/P06/P07/P11](../research/phase2-frozen-prefix-timing-assessment.md)
- **Limits.** The source has no ordered receipt input and no persistent archive across runs. Revisions or after-the-fact analyst changes require externally saved earlier records and a new version. Pine does not reconstruct as-issued data from a provider's overwritten history.

## Deterministic acceptance

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
```

**PASS — 19 tests.** The suite executes the exact Pine decision functions via a narrow Python syntax adapter. It checks the chart integration guards statically, including one offset HTF request and one confirmed-bar state mutation path. Tests cover P01, P04, P06–P12 where applicable to the fixed nominal bar clock, and targeted risk, missing-data, equality and repeat-event cases. P05's out-of-order receipt experiment and P12's actual as-issued revision archive are outside this chart's capabilities. Fixture tests check the two P12 snapshots separately. The suite also verifies the original three Binance payload hashes, all 288 × 5m and 48 × 1H time boundaries, and 216 exact Decimal aggregate comparisons. The syntax adapter does not emulate TradingView's runtime or feed.

## TradingView acceptance observations

All UTC and PHT times below are 12 November 2026 unless a row explicitly names 11 November. PHT is UTC+8. The observed chart was authenticated and live. TradingView identified `BINANCE:PAXGUSDT` and 5 minutes, with standard Candles selected. The new diagnostic was the only script edited. The final source was copied back from Pine Editor and matched the submitted text exactly. The compiled instance displayed its own distinctive provisional-policy label and both new Data Window fields. No public TradingView publication was used.

### Frozen historical market input comparison

An exact-symbol public Binance refresh at 05:55:35.714 UTC returned `PAXGUSDT`, `TRADING`, `isSpotTradingAllowed=true`, base PAXG, quote USDT and tick 0.01. It did not replace the pinned evidence. The chart Data Window was read on the **final build** at the two adjacent 5m opens below. All 12 fields shown (eight 5m prices, two prior hourly close boundaries, two hourly close prices) matched the pinned receipt and the T0 mapping. The hourly boundary is the inclusive Binance close timestamp plus 1 ms, as defined by M07.

| 11 November bar open UTC / PHT | TradingView and frozen Binance O / H / L / C | TradingView and expected prior 1H close UTC / Unix seconds / USDT |
| --- | --- | --- |
| 00:55 / 08:55 | 4027.22 / 4027.84 / 4026.51 / 4026.51 | 00:00 / 1794355200 / 4033.79 |
| 01:00 / 09:00 | 4025.95 / 4030.82 / 4025.00 / 4029.00 | 01:00 / 1794358800 / 4026.51 |

These are chart display observations at tick precision. They establish sample agreement only. Native venue receipt timestamps, a full-window TradingView export and a live hour-change capture were not obtained.

### Native retrospective fixture

Version 2 declared an intentionally broad **hypothetical** zone of [4000, 4060] USDT/PAXG. It used 11 November UTC 00:00 as the 1H anchor, 00:40 for both availability inputs, and 01:10 as exclusive expiry. The 00:40 and 01:00 5m candles in the frozen receipt meet the independent body inequality against their adjacent predecessors. This was a deliberately selected software fixture, with no claim of contemporaneous analyst knowledge or historical trading eligibility.

The final chart displayed setup `L08/2/1794355200000/1794357600000`, contact `L08/2/1794355200000/1794357600000/1794357600000`, **R2-B 00:45 UTC**, **R2-A 01:05 UTC**, **Strict UNKNOWN**, and current **EXPIRED**. For hypothetical entry/stop/target references 4030/3996/4080, it showed loss distance **34 USDT/PAXG** and gross **1.471R**. This was geometry only.

### Native prospective capture and draft persistence

| Time PHT | Observation |
| --- | --- |
| 14:03 | Before activation, version 1 was entered with 14:00 anchor, 14:05 context and zone availability, 14:40 expiry and test zone [3900, 4050]. |
| 14:06:01 and 14:09:42 | On the final build the 14:05–14:10 bar was forming. Last closed cutoff 06:05 UTC, prior hourly close 06:00 UTC at 3974.23, WAIT for availability, no contact and no R2 first time. |
| 14:10:21 | On the final build last cutoff became 06:10 UTC. WAIT for closed confirmation, contact `L08/1/1794463200000/1794463500000/1794463500000`, physical touch UNKNOWN, and no qualifying R2 time. |
| 14:11:10 | The browser was actually reloaded. The restored chart showed the same contact and cutoff, but displayed the earlier draft's labels and lacked the new Data Window fields. It was not a same-source parity result. |
| 14:15 | Editor copy-back still matched the final source, 9,784 UTF-8 bytes. Only this diagnostic's older chart instance was removed and the exact current draft was added as a fresh instance. |

TradingView reported the account was on Basic with a limit of one saved script and blocked private saving of this new draft. No paid upgrade or removal of another script was attempted. Editor text persistence and the chart's compiled-instance persistence were checked separately.

### Same-build realtime-to-reload comparison

Version 3 was set before activation at approximately 14:17 PHT, with a 14:00 anchor, 14:20 context and zone availability, 14:55 exclusive expiry, and the deliberately broad test zone [3900, 4050]. This was a new declaration on the final build added as a fresh chart instance.

| Time PHT | Native observed output |
| --- | --- |
| 14:19:44 | Last closed cutoff 06:15 UTC. WAIT for availability, no contact. |
| 14:20:33 and 14:23:50 | 14:20–14:25 candle forming. Last closed cutoff 06:20 UTC. WAIT for availability, no contact and no R2 first time. |
| 14:25:06 and 14:25:22 | After the nominal boundary the panel still showed the 06:20 UTC last decision. It issued no decision using the clock alone. |
| 14:25:51 | TradingView had processed the closed 5m bar. Last decision cutoff 06:25 UTC, WAIT for closed confirmation, geometric overlap, physical touch UNKNOWN, neither R2 first time. |
| 14:26:18 after actual browser reload | The same final-build panel showed the same 06:25 UTC cutoff, WAIT reason, setup/contact IDs, prior 1H time and price, and blank R2 cutoffs. |
| 14:26:32 after reload | The two final-build Data Window fields remained present. They reported prior 1H boundary 1794463200 (06:00 UTC) and close 3974.23 USDT/PAXG. |

Matched setup ID `L08/3/1794463200000/1794464400000` and contact ID `L08/3/1794463200000/1794464400000/1794464400000`. This is a genuine **same-build PASS for one live cutoff and reload**, with the manifest held fixed. Both the initial draft-restore failure and this fresh-instance pass remain part of the record.

A separate public Binance Spot 5m lookup begun at 06:25:44.488 UTC returned the completed 06:20 bar (O/H/L/C 3973.12/3974.24/3972.17/3974.24) and the then-forming 06:25 bar. It did not replace the frozen receipt or establish what TradingView had received at any earlier instant. The 06:25 UTC panel time is a modeled decision cutoff. The wall-clock observations bound when the change was seen, with native venue receipt and the exact execution instant unavailable.

## Acceptance disposition by layer

| Gate | Status | Scope |
| --- | --- | --- |
| S · Coach source and provenance | PASS | PDF hash and selected pages checked. The independent geometry and timing choices are labelled. |
| L · Decision logic and lifecycle | PASS | Exact-core fixture checks passed for same/later qualification, missing inputs, invalidation, expiry, no duplicate cutoffs, and no terminal revival. |
| T · Chart-clock causality | PASS | Pinned no-backdating checks plus live forming/closed contact observations and two native historical boundary observations. |
| T · Native receipt and correction provenance | INSUFFICIENT | Historical OHLC and Pine execution do not supply exchange receipt ordering or independently archived prior versions. Strict stays UNKNOWN when it is relevant. |
| D · Product and bounded input integrity | PASS | Verified chart identity, public Binance metadata, all pinned input hashes and aggregate checks, and two native chart comparisons. |
| D · Full-window TradingView feed comparison | NOT RUN | Two inspected bars are the cross-provider coverage. |
| R · Nominal geometry | PASS | Exact-core geometry checks and one explicit native hypothetical. |
| R · Order sizing and quantization | NOT RUN | M06 retains these separate future checks. The chart has no quantity or order model. |
| U · Geometric touch distinction | PASS | P10 and the native panel preserve range overlap and unknown physical touch separately. |
| U · Actual cost and execution | INSUFFICIENT | No fill, fee, venue event order or realized payout evidence is available. |
| P · Native compile and chart execution | PASS | Exact final Pine compiled and ran on the qualified chart. The retrospective R2 comparison, sampled HTF rollover, and prospective close behavior were observed. |
| P · Fresh final instance, same-build realtime-to-reload | PASS | Version 3 at the 06:25 UTC closed decision, with matching IDs, reasons, cutoffs and final-build fields. |
| P · Updated unsaved instance after reload | FAIL | The first reload restored the earlier compiled instance while the editor retained the final text. |
| P · Durable saved script and paired live hourly rollover | NOT RUN | The Basic plan blocked a new private script save. The exact build's hour-boundary comparison was historical. |
| E · Empirical performance | NOT RUN | No authorized empirical performance study. |


**Next verification.** Use a visible immutable build identifier when editing the draft, then repeat the saved-instance and live-hour-boundary checks when supported. Keep the same single-setup scope until the user authorizes a wider feature set.

## Phase 3.1 — v0.1.1 build identity and lifecycle, 12 November 2026

The v0.1.0 record above is retained as evidence for that version. Phase 3.1 began from verified main `168eabc645d3c94e1f0ec35a49966fbb3f28de18`. The tested release is [v0.1.1](https://github.com/jebobomagcode/alpha-engine-tradingview/commit/43b9a855cc5d8018b765375ee356046dec2c5ffb), build **`L08-0.1.1-7fbb3eb381b6`**, source blob `80cd5291507fcbb8c919ed02c0f56fb921299b98`.

### Source, editor, chart and saved identity

| Layer | Identity and verification |
| --- | --- |
| Repository source | Exact UTF-8 bytes SHA-256 `1bb0613634f6cd941853552aaa5bab605b2296a541007ffb6c70f24f20b73c91`, 11,164 bytes. |
| Reproducible build ID | Replace only the value of the `const string BUILD_ID` declaration with `__BUILD__`, keeping the quotes, other bytes and line endings. SHA-256 of those bytes is `7fbb3eb381b64b8fe5104fb07f15c25da80130c3f514e9499862279134957296`. Prefix the first 12 hex characters with `L08-0.1.1-`. The release test verifies this binding. |
| Editor | Copied back the complete pasted source. Its SHA-256 matched the repository bytes. The same bytes remained in the editor after the first reload. |
| Compiled chart | Identified by the displayed Build cell, the release title and the compiled panel fields. The Build cell is sourced from the constant, independent of inputs. The editor hash verifies the input bytes. TradingView exposes no independent compiled binary digest in this check. |
| Saved script | A private save attempt stopped at TradingView's Basic limit of one saved script. There is no v0.1.1 saved-script restoration result. |

### Lifecycle and declaration identity

The closed departure candle may still record a first qualification under the existing R2 rules. At that same cutoff, **Current state** shows **REASSESS · episode ended**, **At last cutoff** lists the newly recorded policy or policies, and **Recorded R2-B / R2-A** retains the first cutoffs. Subsequent bars retain REASSESS and the first cutoffs, with the new-record indication cleared. The existing contact, decision, terminal and confirmation predicates continue to govern the same evidence.

Setup identity is an ordered declaration key:

`L08/<revision>/<anchor UTC ms>/<context known UTC ms>/<zone known UTC ms>/<exclusive expiry UTC ms>/zone=<floor>/<ceiling>`

The panel wraps the zone component for readability. It displays contact open UTC, with the full contact ID in that cell's tooltip. The contact ID appends the contact open in UTC milliseconds to the setup key. The market and methodology are fixed for this profile. The key uses separate timestamps, so changing the earlier availability clock changes the identity even if the later clock and effective start remain the same. Zone values use the parsed Pine numeric values with up to 16 fractional digits in the key. Equivalent decimal spellings refer to the same numeric value. Optional nominal geometry inputs affect only that display. Enabled declarations use their full keys, and disabling the setup removes active processing. Re-enabling an identical declaration reconstructs the same identity. A new setup with an otherwise identical declaration needs a new revision. Pine recalculation still requires external records to substantiate earlier as-issued observations. [Pine numeric types](https://www.tradingview.com/pine-script-docs/language/type-system/) · [Pine input behavior](https://www.tradingview.com/pine-script-docs/concepts/inputs/)

**21 local checks passed.** The existing P11 test now verifies REASSESS and the new R2-A record on the same cutoff, prior R2-B retention, and no new event or revival on the following bar. P04 verifies the both-new case. The release and declaration tests cover the source digest, each material field, distinct sub-tick values, and equivalent decimal spellings. The Python adapter still executes the bounded Pine core separately from native Pine acceptance.

### Native compiled instance and historical chart checks

- At **14:48:40 PHT**, Native in-place **Update on chart** compiled v0.1.1 and showed its exact Build cell on standard 5m BINANCE:PAXGUSDT. Existing revision 3 showed last closed cutoff 06:45 UTC, WAIT for closed confirmation, contact 06:20 UTC and blank R2 cutoffs.
- At **14:49:03 PHT**, An actual reload restored the compiled v0.1.0 chart instance at the same cutoff. The editor still copied back the exact v0.1.1 bytes. The in-place update succeeded before reload. Its chart restoration failed. This is not a same-build state comparison.
- At **14:50 PHT**, TradingView's separate Basic cap of two chart indicators surfaced during re-attachment. Once removal of the stale Lesson 08 chart instance was confirmed, the verified v0.1.1 draft was added within the available slot. The existing other indicator and saved scripts were untouched.
- **Retrospective departure fixture, 11 November:** Version 31 used 22:00 PHT anchor, 22:50 PHT for both availability inputs, 23:15 PHT expiry and zone [4000, 4008]. In the frozen input, the 22:50 bar overlapped at low 4007.74 and the 22:55 strict engulf had low 4008.25. Native history showed both first cutoffs at **15:00 UTC**, Strict UNKNOWN and current **REASSESS**. The exact same-cutoff new-event display is also checked deterministically.
- **Native declaration edits:** With revision 31 held fixed, support floor 4000 → 4000.001 changed the zone component. Moving context-known time from 22:50 → 22:45 PHT changed the context clock component while zone-known stayed at 22:50. The build ID and observed departure cutoffs stayed stable.
- **Retrospective split fixture, 11 November:** Version 32 used the prior Phase 3 historical setup with the same inputs other than revision. The final build again showed R2-B **00:45 UTC**, R2-A **01:05 UTC**, Strict UNKNOWN and current EXPIRED.

### Genuine live hourly rollover and fresh-instance reload

On 12 November 2026, version 33 was declared prospectively at about 14:52 PHT. The anchor was 14:00 PHT, both availability inputs 14:55 PHT, exclusive expiry 15:20 PHT and the test support [3900, 4050]. Nominal risk display was disabled, with each optional price input zero. The standard BINANCE:PAXGUSDT 5m chart reported an open market. Before and after reload, the settings dialog showed exactly the same values in all 16 visible input controls.

| Observed PHT | Confirmed 1H UTC / price | Last closed 5m cutoff UTC | Compiled panel observation |
| --- | --- | --- | --- |
| 14:54:18 | 06:00 / 3974.23 | 06:50 | WAIT for availability, no contact. |
| 14:55:25 and 14:59:22 | 06:00 / 3974.23 | 06:55 | First eligible 5m bar forming. Previous WAIT decision retained, no contact or recorded R2 cutoff. |
| 15:00:09 | 07:00 / 3961.14 | 07:00 | New 15:00–15:05 PHT candle forming. The closed decision recorded geometric contact at bar open 06:55 UTC and showed WAIT for confirmation. Both R2 cutoffs remained blank. |
| 15:00:32, after actual browser reload | 07:00 / 3961.14 | 07:00 | Identical fresh build marker, setup declaration, cutoff, contact open, current WAIT reason, geometric evidence and R2 history. |

The declaration key was `L08/33/1794463200000/1794466500000/1794466500000/1794468000000/zone=3900/4050`. The contact-open component is `1794466500000`. The observed hourly reference advanced on the first forming 5m bar after the hour. The closed 5m decision and open-bar display were checked independently at the same boundary. These wall-clock observations give a sampled bracket on the visible change. Exact TradingView execution time and native venue receipt ordering remain unknown. [TradingView execution model](https://www.tradingview.com/pine-script-docs/language/execution-model/) · [Confirmed higher-timeframe data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/)

### Phase 3.1 gate disposition

| Gate | Status | Evidence |
| --- | --- | --- |
| Deterministic regression, release identity and material setup inputs | PASS | 21 local checks, including both qualifying-departure scenarios and single-field identity changes. |
| Exact editor bytes and native compilation | PASS | Source copy-back matched the repository SHA-256. The native panel showed the corresponding build ID. |
| In-place source update before reload | PASS | The linked update immediately displayed the v0.1.1 chart instance and build ID. |
| Native historical lifecycle, R2 timing and declaration identity | PASS | Retrospective departure and split R2 fixtures, plus native zone and availability edits with unchanged analyst revision. |
| Genuine live hourly rollover and closed 5m decision | PASS | Observed before and after the 15:00 PHT boundary with one identifiable build and setup. |
| Fresh-instance same-build realtime-to-reload | PASS | 07:00 UTC cutoff, exact input readback and observed panel matched. |
| In-place unsaved chart restoration | FAIL | Actual reload restored v0.1.0, while the editor retained the v0.1.1 text. |
| Private saved-script creation | FAIL | TradingView Basic blocked the attempt at its one-saved-script limit. |
| Durable saved-script restoration | NOT RUN | No saved v0.1.1 instance was available after the blocked save. |
| Native receipt, physical touch and execution evidence | INSUFFICIENT | Chart observations preserve the geometric-only claim. |

**Next verification gate.** When a private save slot is available, check saved editor source copy-back and restoration of the same compiled build with identical setup inputs. Keep the diagnostic bounded while the saved-script gate remains open.


## Phase 3.2 — owner-assisted saved-script restoration checkpoint, 12 November 2026

Additional screenshots from the owner's own TradingView session establish a named `Alpha Engine TradingView — Lesson 08 Diagnostic` entry under *My scripts*, the expected v0.1.1 source header when opened, and the correct build `L08-0.1.1-7fbb3eb381b6` on the chart after a hard refresh. One refresh initially restored the wrong `PAXGUSDT.P` perpetual chart, correctly producing `INSUFFICIENT · chart identity`. After the owner selected the non-`.P` Binance Spot instrument and repeated the requested refresh, the supplied chart screenshot showed Spot 5m, the same build, and `EXPIRED` under the already elapsed declaration. [Detailed evidence and remaining gates](phase3-2-persistence-interruption-handoff-2026-11-12.md#owner-assisted-tradingview-verification-after-work-interruption--2026-11-12-approximately-16121629-pht).

**Acceptance boundary:** Visual saved-script reopen and build-marker persistence are now observed in the owner-supplied screenshots. No full saved-source export or hash equality has yet been established. Exact saved-source bytes and complete input-state parity remain NOT VERIFIED. No new Pine source changes or new realtime methodology gates were attempted.
