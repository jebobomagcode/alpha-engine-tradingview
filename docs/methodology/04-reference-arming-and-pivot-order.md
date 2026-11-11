# Phase 2 M01-R1 — Structural Reference Arming, Pivot Ambiguity and Event Admissibility

**Status: INDEPENDENT RESEARCH SPECIFICATION, not Coach-exact or approved Pine.**
**Checkpoint:** 2026-11-11 Asia/Manila. Supersedes the *interpretation of* audit counterexample AUD-C01, not the original source and not the rest of M01.
**Scope:** source-first study of PDF pp9,14–16,25 and the existing [M00/M01 contract](01-causal-market-structure.md), [2026-11-10 audit](../audits/2026-11-10-phase2-preimplementation-audit.md). No Pine, trading, backtest, or automated structural detector.

## 1. Original Coach boundary

**COACH_EXPLICIT:** UP = HH/HL; DOWN = LH/LL; BOS is a continuation break of a previous structurally relevant high or low after trend is identified (PDF pp9,14–16). CHoCH is a *possible* change when a preceding LH is broken in a downtrend or a preceding HL is broken in an uptrend (p25). The PDF does not prescribe fractal left/right spans, when a pivot becomes usable, whether a breakout requires a close, equality/buffer, reference re-arming, or how outside bars are ordered. Everything operational below is **INDEPENDENT_FORMALIZATION**.

## 2. Correction: earlier AUD-C01 is impossible under strict high-fractal confirmation

In M01-P1, a high pivot at origin bar \(i\), value \(H_i=106\), is accepted only if \(H_i>H_{i+1},\dots,H_{i+r}\) (and left conditions) for chosen \(r\ge1\). If a required right bar \(j\in[i+1,i+r]\) instead **closes at 107**, its high \(H_j\ge C_j=107>106\). Therefore the candidate is **REJECTED**, not a confirmed high discovered after it was exceeded. This is a **mathematical impossibility proof**, not a market observation. The old audit's illustration AUD-C01 cannot serve as a valid strict P1 example.

**Actual late-eligibility problem:** A pivot may be fully confirmed at time \(t_0\), but the **corresponding trend/reference class**, imported source annotation, or a multi-timeframe context may become valid only at \(t_2>t_0\). Price may have crossed that pivot during \((t_0,t_2]\). We must not retroactively emit the crossing as BOS/CHoCH at \(t_2\). This problem can also occur for reference reinstatement after an explicit regime-selection change.

*Concrete causal scenario:* \(H^*=106\) is confirmed at 10:00 with right-side highs all at most 105; before the required contextual regime has been established, the next completed bar closes at 107 at 10:05. The relevant context does not become classifiable as UP until 10:10. At 10:10 the level is **pre-breached relative to its activation**, not a new 10:10 bullish BOS; the 10:05 move may be retained as unclassified historical price movement. (This is an intentionally **constructed** eligibility-delay example, not a reproduced trade.)

## 3. Separation of five timestamps (INDEPENDENT)

For an identified market/timeframe and a given candidate swing reference:

| Field | Meaning |
|---|---|
| \`pivot_origin_at\` | Original bar where the maximum/minimum is visually located |
| \`pivot_confirmed_at\` | Earliest time required right bars are fully available for this pivot hypothesis |
| \`regime_known_at\` | Earliest time sufficient ordered swing evidence establishes the relevant UP/DOWN context |
| \`reference_armed_at\` | Earliest permitted decision boundary after **both pivot and regime are available**, resolving any later contextual conditions |
| \`break_observed_at\` | Available-at time of the **first eligible new crossing** after arming, or NULL if none occurs |

\(\mathrm{reference\_armed\_at}\ge \max(\mathrm{pivot\_confirmed\_at},\mathrm{regime\_known\_at})\). A proposed *closed-bar, next-interval arming convention* starts eligibility on the next fully observed decision bar **after** both become known. Same-bar newly confirmed pivot plus break is **not** counted in the conservative research baseline. Do not equate a plotted origin coordinate with the alert/event time.

Reference identity contains instrument key, TF, pivot ID/level, swing degree, structural role (UP-HH / UP-HL / DOWN-LL / DOWN-LH), source hypothesis ID, and lifecycle state. If the eligible reference changes, freeze a new identity; never relabel an earlier event by applying a later state.

## 4. Three distinct reference policies: compare, do not conflate

**R1-A — CONSERVATIVE RESEARCH BASELINE (preferred for causal safety, not selected production):**
1. Require a final/available bar and a valid, unambiguous, *previously known* eligible pivot + regime before arming.
2. At arming, check the **most recently eligible completed close**. A close already beyond the threshold blocks this reference under R1-A. In the older cases, PRE_BREACHED denotes this at-arming observation. A historical crossing that already reverted is a separate fact. Wait for a new structurally eligible reference ID when the at-arming check blocks.
3. If on the correct side, allow only a **new, first completed-bar strict crossing** beyond a frozen threshold with valid prior-close evidence; emit once and atomically consume the reference.
4. A later oscillation across the same consumed reference is NOT a second event. A newly confirmed, independently eligible pivot can create a fresh reference.
5. CHoCH causes \`POSSIBLE_SHIFT\` status, **not** immediate opposite regime acceptance.

**R1-B — RE-CROSS AFTER RESET (independent comparator):** A reference already beyond threshold at arming can become eligible *only after* a later fully available close returns to the original, non-broken side, followed by a distinct subsequent closed-bar crossing. Preserve \`INITIAL_PREBREACH\` and \`RESET_AT\`; do not create an event at the old crossing. This yields more potential events but may recycle stale levels and diverge from Coach's discretionary choice of “previous” structure.

**R1-C — MANUAL STRUCTURAL ANCHOR (source-faithful comparator):** Analyst supplies exact eligible swing, role, and **actual known-at timestamp**. The same no-backdating rule applies. Supports source discretionary practice, but not fully automated and not a license to infer undocumented historical availability from a screenshot.

**Decision for ongoing research:** R1-A remains the latest-close comparator, R1-B the reset comparator, and R1-C the manual anchor comparator. A separate **pre-arm history comparator** can block a reference after any observed beyond-threshold close in a declared history window. The policies differ in coverage and information requirements. Production selection remains open.

**12 November clarification (E3):** A valid high 106 is confirmed at 10:00. Completed closes of 107 and 105 are known by arming at 10:10. A later eligible close of 108 qualifies as a new crossing under the literal latest-close policy and is suppressed by the history comparator if its window includes the 107 close. The 107 close remains pre-arm under both. Keep at-arming state and pre-arm history as distinct fields.

## 5. Pivot geometry: outside bar, equality and alternating order

- **Strict fractal ties:** equal adjacent highs prevent a strict high pivot, and equal lows prevent a strict low pivot. Tolerance/tick rounding is a separate hypothesis.
- **Both high and low on one candle:** a wide outside bar can strictly exceed surrounding highs AND fall below surrounding lows. Its OHLC alone does not establish which extreme formed first. **R1-P0 conservative comparator:** mark \`DUAL_EXTREME_AMBIGUOUS\`; do not insert this candle as two ordered alternating swings and do not derive a protected high/low reference whose relative order is unknown. Preserve both unsequenced observations.
- **R1-P1 separate-channel comparator:** track highs/lows separately, but restrict HH/HL and LH/LL trend classification until an unambiguous sequence can be constructed. May preserve more observations, still no invented within-bar path.
- **R1-P2 deterministic tie policy:** choose an ordering from an externally justified time-resolved feed. Without actual intrabar evidence, an arbitrary high-first/low-first assumption must be explicitly labeled *simulation*, never observed price path.
- A candidate with simultaneous high+low does not establish a trend by itself; a later clean swing may resolve structure or may require a new chain. No forced BUY/SELL.

## 6. Temporal event protocol and key invariants

For the **independent closing-break** hypothesis, let high reference \(h\) have threshold \(h+\varepsilon\), low reference \(l\) have threshold \(l-\varepsilon\), where tick buffer \(\varepsilon\) and its source are separately declared. At an eligible bar \(t\), compare the *previous eligible known close* to the frozen reference threshold, then require a **fresh** final close across it. Record the crossing bar interval, the first availability of all classification evidence, and the decision/publication time separately from the reference origin.

- Qualifying crossings occur only after arming. Declare which at-arming or pre-arm history evidence each comparator requires before evaluating its first eligible break.
- Do not use an unconfirmed/unknown regime to classify a past BOS/CHoCH.
- An event at time \(t\) cannot depend on a higher-timeframe final bar available at \(t+\Delta\).
- If pivot identity disappears under the candidate's right-hand confirmation window, classify \`PIVOT_REJECTED\`, not \`PIVOT_CONFIRMED_LATE\`.
- A reference is consumed after the chosen event; equal level is not a strict break.
- Gap crossing between final bar closes may qualify as a **closed-bar level-crossing event** in the alternative, but does not establish executable fill at the level.
- Candidate independent risk/entry gating remains downstream: a BOS alone does not authorize a trade.
- Backfilled drawings of older swing origins must carry delayed confirmation metadata; never use these locations as historical event times.

## 7. Constructed discriminating fixtures (MANUALLY ADJUDICATED; NOT RUN AS CODE)

All cases are **invented numbers**, final bars where stated, \(\varepsilon=0\). They are reviewed as logical expected outcomes, not market data.

| ID | Given causal sequence | R1-A expected | R1-B difference |
|---|---|---|---|
| ARM-01 | Candidate high106, next required right bar closes107 | PIVOT_REJECTED (strict P1); never a valid confirmed pivot | Same |
| ARM-02 | High106 confirmed10:00, close107 at10:05 before UP regime at10:10 | PRE_BREACHED at arming; **no historical BOS** | Requires later reset/re-cross |
| ARM-03 | High106 confirmed, UP context and armed at10:00, prior close104 then next final close107 | One bullish BOS candidate at new bar close | Same |
| ARM-04 | High106 armed, next final close106 exactly | No strict BOS | Same |
| ARM-05 | High106 armed, current wick107, close105 | WICK_TEST only in wick alternative; no close BOS | Same |
| ARM-06 | High106 triggers once; closes105 then107 using same consumed reference | No second BOS | Same unless independent new ref |
| ARM-07 | High106 prebreached, later close105 then107 | No event until new structural reference | Re-cross BOS possible after reset and distinct subsequent close |
| ARM-08 | UP context and confirmed HL94; prior close96 then final close93 | Bearish CHoCH candidate only, not full DOWN | Same |
| ARM-09 | DOWN context and confirmed LH106; prior close104 then107 | Bullish CHoCH candidate only, not full UP | Same |
| ARM-10 | Ambiguous outside candle = unique local high and low | DUAL_EXTREME_AMBIGUOUS; no fabricated alternating order | Same pivot policy separate from re-cross |
| ARM-11 | Right-hand candidate has tied high with origin | PIVOT_REJECTED under strict comparisons | Same |
| ARM-12 | 4H context only confirmed after a 5m decision already emitted | Future 4H evidence disallowed for earlier 5m event | Same |
| ARM-13 | A previously valid pivot is replaced retrospectively by a later more attractive origin | Reject history rewrite; new pivot ID only at its own known-at | Same |
| ARM-14 | Range/structure unknown, close crosses rolling 20-bar maximum | Generic breakout research event, NOT source-classified BOS | Same |
| ARM-15 | Wick breaks pivot during developing bar, then closes below | PROVISIONAL wick only; close breakout false | Same |
| ARM-16 | Price gap opens beyond level after eligible previous close below | Closed-bar level crossing may be recorded at close; no assumed level-price fill | Same |

## 8. Falsification obligations before code approval

The forthcoming *executable* fixture runner (not yet authorized) would need to prove: no event before pivot+regime known; no historical reclassification after reload; exact-once event consumption; stable previous-reference IDs; missing bars yield insufficiency; simultaneous pivots never imply undocumented order; source screenshot manual labels and computed pivots have different provenance; alternative arming policies produce transparently different counts.

**Mathematical audit conclusion:** AUD-C01 as originally worded was *mis-specified for strict fractals*. Corrected ARM-01 and ARM-02 separate pivot invalidity from late regime/reference eligibility. This correction changes **only the hypothesis and test-case interpretation**, not any Coach PDF wording or accepted prior study results.

**NEXT:** formalize M02/M04 zone-contact, confirmation timing, same-bar ambiguity and invalidation precedence in [R2 timeline specification](05-zone-contact-reaction-timing.md).
