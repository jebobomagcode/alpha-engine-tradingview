# Phase 3.6 — M01 structural-reference readiness and falsification plan

**Continuation:** See the [Phase 3.6 source review and as-of structural-reference contract](../research/phase3-6-structural-reference-contract.md) for explicit boundary phases, ordered-segment policies and an adjudicated comparison scope. The original proposal below is retained as the audit baseline.

**Date:** 2026-11-13 Asia/Manila · **Status:** RESEARCH-ONLY DRAFT, not an approved BOS/CHoCH implementation.  
**Repository:** `jebobomagcode/alpha-engine-tradingview` **ONLY**.  
**Accepted baseline:** `main` at `319459863fc138e8d347a1b00bc1de56fabb114c`; Pine v0.1.3 build `L08-0.1.3-3e3d909ba9f5`, blob `218e54cf573d6dfcc7b3306d22a0a34f966db160`; 55/55 tested, native private library version 3.0 accepted.  
**Source:** only the original 35-page Coach PDF (SHA-256 `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`), corroborated against the repo source identity. Source prose AND figures on pp. 9, 14–16, 25 were inspected for this scope; previously accepted PCSS lessons are preserved rather than repeated.

## 1. Why this increment and not another indicator feature?

Phase 3.5 established a **research-only** strict local 5m pivot, confirmed no earlier than all right bars' close, with positive-price/clock validity and a last-closed-window status. It **did not** establish a qualified ordered swing sequence, UP/DOWN regime, eligible structural HH/HL/LH/LL, BOS, CHoCH, numerical accuracy, profitable signals, or actual market receipt order.

Moving immediately from the last displayed pivot high/low to a BOS/CHoCH label would skip the most consequential unproven dependency. The next increment is therefore a **source-scoped specification and falsification protocol for a structural reference**, not Pine v0.1.4.

**COACH_EXPLICIT:** p. 9 describes UP via HH/HL, DOWN via LH/LL, and a distinct sideways case. The figure illustrates ordered turning points. Pp. 14–16 say structure/trend comes first and BOS continues an established trend by breaking a previous HH (UP) or LL (DOWN); p. 14's OB diagrams are examples, not a formal pivot detector. P. 25 illustrates a possible shift: breaking a previous LH in DOWN or a previous HL in UP. The p. 25 diagrams do not specify a numeric left/right count, intrabar ordering, or automatic reversal confirmation.

**OPEN_UNRESOLVED in source:** which visible turn is a structural rather than micro pivot; ties; candidate significance/scale; alternating-order policy; wick vs close; tick buffer; protected reference; arm/rearm/freeze rules; whether changing HTF bias can reclassify an earlier LTF event; what establishes a completed new regime after CHoCH; actual quote-feed availability. These MUST NOT be represented as Coach-prescribed values.

**INDEPENDENT_EXTENSION:** the accepted M01-P1 strict 2/2 pivot is only a reproducible observational comparator. Its event known-at timestamp is a modeled completed-candle boundary, not an authenticated venue receipt timestamp.

## 2. Baselines and mutually competing options

| Candidate | Mechanism | Advantage | Main failure/tradeoff | Status |
| --- | --- | --- | --- | --- |
| **S0 Manual structural annotation** | Analyst declares eligible prior HH/HL/LH/LL, regime, origin, `known_at`, source evidence, and valid decision boundary | Source-faithful to the Coach's discretionary marking; creates a human reference comparator | Subjective; cannot backdate a historical analyst declaration from today's screenshot | **Primary qualitative baseline** |
| **S1 Strict P1 pivot sequence** | Accumulate strictly confirmed OHLC extrema with 1–8 L/R, then classify only an *unambiguously ordered* structural sequence | Reuses audited P1 data validity, is deterministic, testable and causal | Dual-extreme candles, consecutive same-side extrema, small swing significance and latency require new explicit policies | **Preferred first mechanization research candidate, NOT approved as Coach-exact or Pine** |
| **S2 Directional-change swings** | Confirm after a declared absolute/tick/volatility reversal, using only known bars | Different significance mechanism; useful falsification comparator | Thresholds, comparison clock, latency and intrabar ordering not source-given | **Independent challenger, not selected** |
| **S3 Rolling extremes** | Previous N completed bars' high/low | Simple chart-level break comparator | Does not by itself establish HH/HL regime or structurally eligible “previous” swing | **Negative/control baseline; never silently label Coach BOS** |

**Decision:** compare S0 vs S1 first because they test whether the audited P1 findings can represent the Coach's visually selected structure. Preserve S2/S3 as deliberately different challengers. No new automation yet.

## 3. Minimum causal reference record (proposed schema, not implemented)

A valid research reference must specify:

- `instrument_key` = **BINANCE:PAXGUSDT Spot, USDT quote** for the presently accepted chart; market product and venue are part of identity. Do not conflate PAXGUSDT, XAUTUSDT, and XAUUSDT.
- `timeframe`, data-source version, candle finality, validation outcome, any unavailable/irregular bar intervals, and quote tick rules.
- `pivot_id`, `pivot_origin_at`, `pivot_confirmed_at`, pivot side/value and origin-vs-known clock.
- `sequence_status` = ORDERABLE / DUAL_EXTREME_AMBIGUOUS / GAP_INSUFFICIENT / TIED_OR_UNCONFIRMED / OTHER_INSUFFICIENT.
- `regime` = UP / DOWN / UNKNOWN / RANGE_CANDIDATE (range is not automatically UP or DOWN); `regime_known_at` and supporting **ordered** swing IDs.
- `reference_role` = UP_HH / UP_HL / DOWN_LL / DOWN_LH only after a genuinely supported regime; `reference_armed_at`, level, explicit threshold/buffer and `source_policy_id`.
- `reference_lifecycle` = UNARMED / ARMED / PREBREACHED / CONSUMED / RETIRED / INSUFFICIENT, with frozen IDs and versioned evidence.
- `break_observed_at`, event type, previous eligible closed price, qualified crossing price, event decision cutoff and prior evidence set. Never infer within-candle touch/fill from OHLC.

**Invariant I1 (availability):** `pivot_confirmed_at >= max(available_at for every required left/center/right candle)`. Historical pivot origin is not decision time.  
**I2 (ordering):** OHLC cannot order the high and low inside the same bar; dual-extreme origin remains unsequenced unless finer authenticated evidence resolves it.  
**I3 (eligibility):** `reference_armed_at >= max(pivot_confirmed_at, regime_known_at, required contextual availability)`. Do not let the bar that newly establishes a premise generate a retroactively armed crossing; require a clearly declared next eligible decision interval.  
**I4 (fresh first break):** For the close-break hypothesis, compare eligible adjacent *closed* bars on either side of a **frozen** level and buffer. Require the prior bar on the unbroken side, current on the broken side and the reference already ARMED before that bar's eligible opening. Gaps/unknown predecessor → INSUFFICIENT, not BOS.  
**I5 (single use):** Once a reference produces an event, mark CONSUMED and do not count a second oscillation across it unless a separately justified new ID exists.  
**I6 (classification):** UP + qualified prior HH break → `BOS_CANDIDATE_UP`; DOWN + prior LL break → `BOS_CANDIDATE_DOWN`; DOWN + LH break → `CHOCH_CANDIDATE_UP`; UP + HL break → `CHOCH_CANDIDATE_DOWN`. A CHoCH candidate means *possible shift*, not automatic acceptance of reversed regime.  
**I7 (no false source promotion):** All pivot windows, alternating compression, buffers, close-versus-wick choice, reset and status names are **INDEPENDENT**, not Coach-exact. No action recommendation.

These requirements extend the existing [M00/M01 research](../methodology/01-causal-market-structure.md), [R1 arming audit](../methodology/04-reference-arming-and-pivot-order.md) and [cross-module causal clock](../methodology/08-cross-module-causal-reconciliation.md), rather than replacing them.

## 4. Critical structural choices to adjudicate before coding

**A. Dual-extreme and alternating sequence.** A fully confirmed strict P1 high AND low on the same origin bar is possible. Candidate `A0` quarantines both for sequential regime classification while keeping two independent *observation* records. Candidate `A1` keeps two side channels but still refuses unsupported high-first/low-first sequencing. Arbitrary high-first ordering is a simulation, not historical observation. Also resolve consecutive highs without an intervening low via a named policy, not silent future-dependent replacement.

**B. Significance and structural degree.** A strict P1 turn is local; Coach's structural HH/HL need not equal every tiny zigzag. Compare manual structural anchors with P1 at declared (L,R) settings and a separately proposed significance filter. Do not optimize L/R or thresholds based on winning trades. A lone recent high and lone recent low do not establish an UP or DOWN regime.

**C. Arming and prebreach.** Prior [R1-A](../methodology/04-reference-arming-and-pivot-order.md#4-three-distinct-reference-policies-compare-do-not-conflate) checks the **latest** known close at arming, not every pre-arm close. A separate pre-arm-history veto is more conservative but requires a declared and complete lookback. R1-B reset-and-recross and R1-C declared manual anchor are different policies. A prior critique's impossible “strict high pivot already breached by its required right bar” example must NOT be reused; a realistic late reference arises when regime/context becomes knowable **after** the pivot itself.

**D. Break and reference buffer.** Close-crossing and wick-breach are independent hypotheses. Equality and an epsilon of zero vs a declared whole-tick buffer change events. Neither is mathematically specified by Coach. Retain `WICK_TEST` as a non-BOS research comparator when OHLC alone cannot establish an executable intrabar sequence.

**E. Context/timeframe and zones.** A 5m candidate cannot silently imply 1H structural confidence. New 1H evidence does not change the as-of status published before its availability. A BOS/CHoCH research observation is not by itself an entry: Lesson 08 p. 10 requires a relevant pre-known zone and later confirmation under its trend-following workflow. The sideways Lesson 10 pp. 12–13 and p. 32 conditional breakout paths are **separate** scenarios.

## 5. Constructed adversarial cases — *paper expectations only; NOT Pine or market backtests*

All cutoffs are UTC and all prices are illustrative USDT/PAXG unless otherwise noted. These are specification tests, not market evidence.

**F01 — both pivot sides on the same origin.** Strict P1 `L=R=2`; consecutive standard 5m bars:

| Open UTC | Open | High | Low | Close |
| --- | ---: | ---: | ---: | ---: |
| 10:00 | 101 | 104 | 100 | 103 |
| 10:05 | 102 | 106 | 99 | 105 |
| **10:10** | **100** | **112** | **95** | **110** |
| 10:15 | 107 | 108 | 98 | 100 |
| 10:20 | 102 | 105 | 100 | 103 |

At **10:25 close**, strict high 112 and low 95 at the **same 10:10 origin** both become known for this candle-only model. Expected: two *unsequenced* observed extrema; **NO inferred high-before-low or low-before-high ordering**, no regime/BOS/CHoCH from this isolated sequence. Source technique: internal math, not a Coach signal.

**F02 — tie asymmetry.** Modify F01's 10:05 high to 112 (other OHLC unchanged). A strict 10:10 high is **not** confirmed; the low 95 still is. Expected one-sided low event only.

**F03 — missing middle 5m interval.** Omit the 10:15 bar and use 10:20/10:25 as the remaining right-side observations. The 5m window is not contiguous; expected **INSUFFICIENT / invalid window**, no new pivot. Later evidence cannot backfill the missing 10:15 decision.

**F04 — one extremum is not trend.** Even a valid, isolated confirmed high/low pair is insufficient to establish ordered HH/HL or LH/LL. Expected UNKNOWN, no BOS/CHoCH.

**F05 — late regime known while prebreached.** High 106 confirms at 10:00, close 107 at 10:05 (before UP context exists), context becomes available at 10:10; latest eligible close at arming is still 107. Expected `PREBREACHED`, not a newly invented bullish BOS at 10:10/arming.

**F06 — R1-A vs full pre-arm history comparator.** Same 106 reference confirmed 10:00; close 107 at 10:05, return to 105 by 10:10 and remain at 105 through 10:15. With regime known 10:10 and a new eligible decision bar 10:15–10:20 closing 108: literal R1-A latest-close arming can admit a fresh crossing at 10:20; a **declared, complete** history-veto comparator rejects because 10:05 exceeded 106. Expected POLICY_DISAGREEMENT, neither label “Coach exact.” A missing pre-arm-history interval invalidates a history-veto decision rather than silently treating absence as no breach.

**F07 — reference consumed once.** Once the 106 eligible HH has emitted an observed break, subsequent closes remaining above 106, or a later return and re-cross, must not re-emit under the same consumed reference ID. Expected one candidate event, not repeated BOS spam.

**F08 — close vs wick.** An eligible bar with H=108 but final close=105 against a qualified 106 high yields **WICK_TEST** under wick hypothesis, **NO CLOSE_BREAK** under close-first hypothesis; neither implies a fill or intra-bar ordering. Repeat with close=107 for close-cross candidate, provided prior eligible close was ≤106.

**F09 — same-bar new regime premise.** A newly qualified regime at a completed bar's close cannot retroactively arm a reference at that bar's open. Expected wait for a strictly eligible subsequent decision interval; never back-label that bar's break.

**F10 — CHoCH is possible shift only.** Under established DOWN, a qualified fresh break above a prior eligible LH is `CHOCH_CANDIDATE_UP`. It does **not** immediately assert new UP, a BUY, or a completed reversal. Opposite direction symmetric.

**F11 — contradictory TF evidence.** A confirmed 1H state arriving after the relevant 5m decision must not rewrite its past status. Preserve as-of decision evidence and allow a later reassessment only at a new cutoff.

**F12 — stale source ID.** Same numerical level from different venue/product/timeframe, or a screenshot created later than the claimed decision, does not make the old reference valid as-of then. Expected INSUFFICIENT / mismatched provenance.

**F13 — zone independence.** A structural break without any pre-known relevant Lesson 08 support/resistance contact is **not** an entry under the Lesson 08 workflow. No “BUY” or “SELL” from structural labels.

**F14 — valid price but ambiguous swing chain.** Two successive high pivots with no admissibly ordered low between them do not automatically complete HH/HL. Compare explicitly documented compression and quarantine policies before selecting one.

**Status:** F01's OHLC arithmetic is explicitly reproducible (dual strict extrema and 10:25 cutoff). F02–F14 are **planned discriminating specifications**, not claimed to have been executed or confirmed on native TradingView. These paper cases must later be encoded with independent expected outputs and tested against genuine source-derived code—not just mirrored assertions.

## 6. Ponder assessment and proposed next decision

**Prefer the smallest falsifiable bridge, not immediate BOS labels.**

1. **First gate — structure research adjudication:** Evaluate S0 manual annotated swing chains vs S1 5m P1 on fixed declared evidence, choose and freeze an explicit sequence/dual-extreme policy; document source-linked disagreements. Validate F01–F14 as formal fixtures with real cutoff/availability fields. Reject any case that inadvertently assumes knowing candle extremum order.
2. **Second gate — reference eligibility:** Evaluate R1-A latest-close versus history veto, R1-B reset and R1-C manual. Verify pre-arm crossings, late regime, one-time consumption, missing predecessor and threshold tick semantics. Keep a comparison matrix, not one secretly adopted universal rule.
3. **Third gate — controlled indicator proposal (SEPARATE authorization):** Only if the prior two gates pass, propose ONE opt-in **informational structure candidate** on the existing standard Binance PAXGUSDT Spot 5m chart. It must remain OFF by default, preserve the existing Lesson 08 and M01 outputs, avoid alerts/trading/backtests, and carry origin, confirmation, arming and decision clocks. Prepare source isolation, mutation tests and native persistence protocol before writing any Pine.
4. **Do not collapse scopes:** M02 zone formation, M04 alternative candle patterns and M05 context conflicts remain separate unfinished methodology work. Their research may proceed independently, but an M01 event cannot be marketed as a Coach-complete trade or a source-exact trading signal.

**Reversal triggers:** If many Coach-annotated swing references disagree with strict P1 even when correctly time-lagged, favor S0 or compare directional-change S2 rather than forcing source material into P1. If bar-close P1 repeatedly lacks the event ordering needed for HH/HL, quarantine it; seek finer evidence before converting the result into a deterministic structure state. If owner wants M02/M04 prioritized first, do that **without changing the accepted Phase 3.5 implementation**.

## 7. Acceptance ledger and scope

| Gate | Outcome |
| --- | --- |
| Original Coach PDF identity and relevant pages/figures inspected | **PASS — PDF SHA-256 matched source manifest; source-inspection research only** |
| Existing Phase 3.5 main Pine v0.1.3 acceptance preserved | **PASS — no Pine changes in this research branch** |
| Candidate alternatives and causal invariants specified | **RESEARCH DRAFT** |
| F01–F14 numerical/runtime fixture execution | **NOT RUN** (F01 logic can be hand-checked) |
| Qualified manual comparison against real source screenshots | **NOT RUN** |
| Automated M01 structural engine / BOS / CHoCH | **NOT IMPLEMENTED, NOT AUTHORIZED IN THIS INCREMENT** |
| TradingView native structure signals and saved-script changes | **NOT RUN / UNCHANGED** |
| Strategy testing, alerts, trade execution, edge/profitability | **OUT OF SCOPE** |

**Review handoff:** The research document should receive independent scrutiny (including a check that the proposed R1 event states cannot contradict the pre-existing lessons). Accepting this plan would NOT automatically authorize Pine coding, merging unrelated work, public TradingView publishing, or trading.
