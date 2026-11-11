# M05–R4 — Multi-Timeframe Evidence, Context Conflicts and Decision States

**Phase 2 methodology research | 2026-11-11 Asia/Manila | INDEPENDENT PROPOSAL, NOT FINAL INDICATOR OR PINE CODE.**

## Scope and source authority

**Sole Coach source:** [coach trading lessons.pdf](../../sources/coach%20trading%20lessons.pdf), SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. The following original pages were read directly in this increment: **p6, p9, p10, p18, p21–28, p30–32, p33–35**. Related source studies: [Lesson04](../lessons/04-time-frame.md), [Lesson13](../lessons/13-manage-your-risk-sol.md), [Lesson19](../lessons/19-rsi-ema-topdown-analysis.md), [Q&A3](../lessons/qa-03-btc-consolidation-retest-and-breakout.md), [N-02](../lessons/note-02-bpi-bsp-stock-charting.md). Original p17 is mainly a visual setup; p18 has detailed source text. Do NOT infer image-only exact prices from text alone.

**COACH_EXPLICIT — p6:** HTF 1H/4H for direction and zones, LTF 5m/15m for setup/confirmation, with an example 1H/4H → 5m. **p9–10:** trend + support/resistance zone + signal; in the source-style continuation setup do not trade if the price never reaches the zone; look for a closed confirming LTF candle before entry. **p18:** SOL 4H bullish with weakening 1H, 15m bearish/short scalp against HTF; separately offers a safer HTF-aligned long after demand and 15m CHoCH/green displacement. **p21/p24:** example of HTF EMA/RSI + LTF pullback and reaction; p24 names HTF 4H, Daily, 1H. **p27–28:** TON 4H very bullish but RSI highly overbought; recommended action still WAIT for pullback to support/FVG/OB instead of chasing. **p30:** bullish structure + EMA respected + RSI near overbought favors continuation *in Coach's example* unless strong bearish confirmation. **p31:** 30m OB zone and 5m confirmation in FARTCOIN example. **p32:** BTC HTF bearish while 15m consolidates; conditional short rejection OR long breakout after separate conditions. **p35:** 4H BPI possible temporary rebound with Daily bearish/no CHoCH. These are examples, not source-defined universal timeframes or probabilities.

**Coach does not supply:** a mandatory one-size HTF ladder; exact hierarchical weights; numerical “higher probability”; mechanical veto of every countertrend candidate; how conflicting signals are ordered; which newly closed HTF bar a same-timestamp LTF bar may use; freshness/expiry; whether a temporary LTF CHoCH automatically changes 4H bias (it does not follow from his statements).

Everything below, including state names, identifiers, causal invariants, matrices, and comparison policies, is **INDEPENDENT_FORMALIZATION**. No buy/sell system is operational.

## A. Core choice — do not flatten timeframes into a score

The most defensible research representation is a **vector of scoped observations**, NOT one unqualified market label. Proposed snapshot at decision time \(\tau\):

\[
S(\tau)=\{I,\, H_1,H_2,\,L_1,L_2,\,Z,\,R,\,K,\,D,\,Q\},
\]

where each active item independently retains feed/symbol/timeframe, source family, confidence limitations, **known_at**, and references:
- \(I\): qualified instrument and data/finality identity.
- \(H_1,H_2\): optional selected HTF structural regimes / zones; not necessarily 4H+1H if style differs.
- \(L_1,L_2\): optional selected LTF structural and momentum conditions, each labelled by timeframe.
- \(Z\): pre-known price zones with status and contact episodes from [M02/R2](05-zone-contact-reaction-timing.md).
- \(R\): pattern reaction and required subsequent confirmations from [M04/R3](06-candle-pattern-and-confirmation-grammar.md).
- \(K\): *conditional* scenario family (continuation / range / countertrend scalp / pullback scalp / reversal watch), never guessed from symbol alone.
- \(D\): explainable top-level diagnostic gate and reason-code set, NOT an order.
- \(Q\): entry/SL/TP risk completeness and quality context, not estimated live PnL.

**Crucial independence:** HTF structural trend, LTF momentum, LTF price structure, LTF candle reaction and trade readiness are different fields. A 15m bearish BOS within a 4H UP context may be a pullback or scalp-relevant event; it is **not** a 4H bearish BOS. A 4H CHoCH may be a **possible shift** but cannot retroactively rewrite the regime of already processed 5m candles.

**Evidence invariants:** no item may rely on a source record whose \`available_at > \tau\`; use stable source/feed identity; preserve indicator calculation context and its bar finality; preserve original Coach/example statement separately from independently inferred market state; do not infer institutional flow or quantified win probabilities from OHLC-derived indicators.

## B. Timeframe profiles — source examples versus candidate engine configurations

| Profile | Source anchor | Evidence hierarchy and scope | Research status |
|---|---|---|---|
| TOPDOWN_TREND | PDF pp6,10,21,24 | HTF 1H or 4H, optionally Daily in p24; LTF 5m or 15m confirmation; one p6 example says 1H/4H → 5m | Source-supported example family; exact pairing and selected rule OPEN |
| 30M_5M_PULLBACK | PDF p31 | 30m main OB location, 5m confirmation; a *Coach alternative plan* to student's existing FARTCOIN long | Context-specific, not globally mandated |
| COUNTERTREND_SOL | PDF p18 | 4H still bullish, 1H weakening, 15m bearish scalp; *separate* 4H-aligned long after demand and bullish 15m evidence | Two different conditional trade styles |
| BTC_CONSOLIDATION | PDF p32 | 4H bearish; 15m consolidation; wait for short rejection or breakout-confirmed long branch, with distinct invalidations | Conditional alternative paths, not simultaneous orders |
| BPI_EQUITY_NOTE | PDF pp34–35 | Weekly/Daily/4H PH-stock commentary; 4H temporary bullish ≠ Daily CHoCH; pesos are historical stock levels | Source case for hierarchy, **NOT crypto implementation timeframe requirement** |
| CRYPTO_EXTENSION | user scope, not Coach source | BTC/ETH plus distinct venue-qualified XAUUSDT derivative, XAUTUSDT, PAXGUSDT token feeds; continuous-hours mapping requires per-feed proof | Separate independent applicability study OPEN |

**Research constraint:** HTF/entry TF choices must be explicit inputs of a named scenario/profile. Do not silently replace a 30m OB with 1H EMA, or call a BPI equity weekly/4H exercise a crypto signal.

## C. The causal “what did we know?” contract

For a qualifying HTF record \(h\) and LTF decision time \(\tau\), admissibility requires both \(\mathrm{available\_at}(h)\le \tau\) and validity under the chosen *information-freeze* policy.

**MTF-T0 (conservative baseline):** when evaluating an LTF candle that opens at \(o\) and closes at \(c\), freeze its HTF context to the latest fully known, final HTF evidence **at or before \(o\)**. Evaluate the LTF candle only when it is completed and available. If HTF changes during that LTF candle, it is not silently substituted as if it governed the candle's entire evolution. A later candidate can use the new HTF context on a subsequent LTF candle. This can delay qualification.

**MTF-T1 (decision-close comparator):** at evaluation instant \(\tau\ge c\), admit any independently confirmed HTF record actually available by \(\tau\) when deciding whether a *new* candidate now exists; document that it was learned at/between reaction close and the decision, **not** historically available at LTF open. Same-timestamp events need deterministic availability ordering, or an explicit conservative delay if order cannot be verified.

**MTF-T2 (manual annotated source view):** preserve analyst-specified known-at context without implying the screenshot shows actual prior-time availability.

**Constructed timeline:** At PHT 11:55–12:00 a 5m candle completes just as a 4H bar is scheduled to end at 12:00. Under T0 it uses the last *earlier* confirmed 4H regime, even if the new 4H bar becomes final at 12:00. Under T1, it can include a new confirmed 4H regime only **at a verified decision instant after both feeds have become available**, never at 11:55. No same-timestamp ordering is presumed by equality of nominal bar-close timestamps.

**Independent official TradingView guidance, not Coach:** [Other timeframes and data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) warns about future-leaking HTF requests and describes a historical offset combined with lookahead-on for stable last-confirmed HTF values. [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) notes real-time and historical HTF values may diverge. [Bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/) notes \`barstate.isconfirmed\` inside a \`request.security()\` expression does **not** solve requested-timeframe confirmation. These sources constrain later engineering, NOT a Pine implementation claim. Exact technical mapping remains unverified until actual compilation/runtime tests.

## D. Distinct structure and momentum fields — no arbitrary priority overwrite

| Observation pairing | Source-compatible interpretation | Not justified |
|---|---|---|
| 4H UP / 15m DOWN | possible pullback and/or qualified countertrend scalp (PDF p18) | rename 4H trend DOWN |
| 4H DOWN / 15m RANGE | higher bearish context + local indecision; source p32 says wait | immediate universal SHORT at market |
| 4H UP / 15m bullish confirmation at pre-known support | potential continuation *after* zone and closed evidence | profitability or automatic fill |
| 4H DOWN / 15m bullish CHoCH | possible LTF shift, could be retracement/reversal-watch case | declared 4H UP without 4H evidence |
| 4H UP / RSI>70 | strong bullish momentum may coexist with overbought; Coach p27 says don't chase | automatic SELL or automatic BUY |
| Weekly and Daily bearish / 4H possible bounce in BPI p35 | temporary 4H recovery remains distinct from Daily reversal | applying peso levels to XAUUSDT |
| Indicator above EMA yet structure UNKNOWN | indicators are context, structure cannot be inferred as source-exact HH/HL | “BOS confirmed” inferred from EMA alone |

**No binary rule** “all 3 TFs must point the same direction” appears in Coach. It would exclude p18 countertrend and p32 conditional breakout branches. Nor does a score like 2 bullish TFs versus 1 bearish TF automatically measure probability.

## E. Scenario-conditional decision gates (research interface)

Every scenario is identified and evaluated **separately**. Candidate outcomes can coexist in a diagnostic research report, but no global opposite-side trades are asserted.

1. **TREND_CONTINUATION:** required HTF structure known, matching bias and pre-known eligible zone; price reached zone; eligible *closed* lower-TF confirmation branch (R2/R3); coherent risk. A temporary opposite-direction LTF pullback is not a fatal conflict. A newly confirmed HTF structural disconfirmation **forces REASSESS** for this scenario. RSI/EMA are source-consistent contextual evidence; mandatory thresholds are still OPEN.
2. **CONDITIONAL_RANGE:** explicitly range-qualified boundary and reversal evidence; p13 break-of-confirmation trigger is separately specified RB1/RB2. If range cannot be established, do NOT convert generic sideways into automatic BUY/SELL. Source p9 warns against sideways without HTF context.
3. **COUNTERTREND_SCALP:** separate observed lower-TF direction against explicit HTF regime, flagged \`AGAINST_HTF\`; do not downgrade original HTF bias. Additional risk/horizon terms are **proposed safeguards**, not original Coach's exact rule. Missing explicit style/risk parameters → only descriptive setup watch, not a fully risk-qualified candidate.
4. **PULLBACK_SCALP:** p31 Coach's *proposed* 30m OB + 5m lower TF reaction, not a reproduction of the student's already-existing LONG; RSI 40–50 bounce is context-specific.
5. **REVERSAL_WATCH/BREAKOUT:** a new lower-TF CHoCH may open possible-change monitoring. A higher-TF reversal must be qualified from its *own* confirmed structure. Source p32 conditional long needs breakout confirmation on 15m/1H; do not equate every 15m bullish engulf with a confirmed bearish-HTF reversal.

**Incompatibility:** when two active scenario candidates point in opposite directions, report \`CONDITIONAL_CONFLICT\` with both reasons. Do NOT silently choose a “winner”, report simultaneous executable BUY and SELL, or hide the contextual difference behind a confidence percentage. If styles are not selected, report scenario observations and leave action eligibility \`UNSELECTED_STYLE\`.

## F. Proposed status vocabulary, provenance and deterministic explanation

Keep **two orthogonal layers**:
- **Observations:** per-timeframe structural state \`UP/DOWN/RANGE/UNKNOWN\`; \`POSSIBLE_CHOCH_UP/POSSIBLE_CHOCH_DOWN\` events; EMA/RSI descriptions; zone state; contact and reaction state; provenance.
- **Decision gate:** one active case-specific blocker and all underlying reasons. This is a *proposed reporting contract*, not Coach's literal labels.

| State/label | When report | Why different |
|---|---|---|
| \`DATA_INSUFFICIENT\` | required source bars unqualified, missing, invalid or inconsistent feed | missing data is not neutral market state |
| \`CONTEXT_INSUFFICIENT\` | required selected HTF unavailable/unknown; no established structure | not the same as RANGE |
| \`UNSELECTED_STYLE\` | multiple possible branches and no active style | analytical description still possible |
| \`ZONE_INSUFFICIENT\` | no prior known eligible price zone for profile | unlike zone known but uncontacted |
| \`WAIT_ZONE\` | eligible zone not contacted | source p10 NO TRADE in this template |
| \`CONTACT_PENDING\` | overlap detected only intrabar / confirmation unavailable | not a completed touch |
| \`WAIT_CONFIRMATION\` | contact confirmed but no qualifying *completed* reaction | no entry yet |
| \`WAIT_BREAK\` | range reversal candle known but later requisite break unobserved | p13 branch, not p10 close-entry |
| \`REASSESS\` | later HTF/context change disconfirms setup or changes required references | no stale green label |
| \`INVALIDATED\` | zone or scenario invalidation under **declared** research hypothesis | cannot simply roll into a ready trade |
| \`RISK_INCOMPLETE\` | directional reaction exists but entry/SL/TP or contract mechanics inadequate | pattern signal ≠ trade |
| \`CANDIDATE_FOR_REVIEW\` | necessary case-specific gates and risk proposal satisfied | **not** order, fill, probability or recommendation |
| \`CONDITIONAL_CONFLICT\` | opposite scenario paths remain conditionally plausible | display alternative conditions, no global trade side |
| \`NEWS_UNKNOWN\` | supplementary external economic-calendar status absent | does not imply “no news”, not universal crypto veto |

**Display precedence** (independent report preference): data failure → invalidated/disconfirmed context → missing required profile/bias → missing/invalid zone → wait for contact → wait for completed reaction/break → risk incomplete → candidate. However **never erase** lower-level meaningful observations: even when the gate says WAIT_ZONE, retain 4H DOWN, 15m RANGE, and the exact reason no candidate exists. A single ranked status must not conceal two opposite scenario branches; report their individual statuses.

**“INSUFFICIENT” versus “WAIT”:** insufficient means *information needed to establish a condition is absent*; WAIT means the condition is known and we are observing whether a subsequent qualifying event occurs. \`RANGE\` means range-qualified price behavior under a declared model, **not** \`UNKNOWN\`. \`NEWS_UNKNOWN\` means no source evidence about calendar, not a bearish/bullish vote.

## G. Decision lifecycle and stale-signal safety

A setup episode is keyed by \`instrument_key + profile + anchor_htf_ref + zone_id + contact_episode_id + reaction_id\`, each with causal times. On a new qualified HTF event, freeze old scenario provenance; mark its eligibility \`REASSESS\` or \`INVALIDATED\` per explicit policy before declaring fresh setup. Never rewrite a prior alert as if the later HTF event already existed.

**Potential staleness cases to test:** zone created after touch; HTF 4H bar newly available at same 5m close; intrabar candle wick later retracts; old pivot reclassified by R1; source feed gaps; RSI measurement still forming; conflict between two scenario candidates; stale candidate remains “green” after fresh confirmed HTF reversal; distinct venues/quote units; 15m CHoCH in ongoing 4H downtrend; strategy target without stop.

**Thresholds OPEN:** no chosen minimum bars of persistence, accepted reaction window, minimum RSI bounce, number of EMA votes, structure pivot spans, profile invalidation timeout or actual executed RR. These are not Coach-exact.

## H. Predeclared research cases — manually adjudicated, NOT executed

Assume fictitious consistent feed/bar closure except explicitly changed; “eligible” refers to the selected R1/R2/R3 candidates; results are logical **expectations**, not backtest observations.

| ID | Constructed case | Expected source-grounded research interpretation |
|---|---|---|
| MTF-01 | 4H UP, 15m DOWN pullback, no demand contact | 4H UP retained; continuation WAIT_ZONE, not BUY or HTF reversal |
| MTF-02 | 4H UP, 1H weakening, 15m bearish confirmation at resistance | descriptive countertrend SOL-like scalp branch; \`AGAINST_HTF\`, HTF UP unchanged |
| MTF-03 | 4H UP, demand contact, later 15m bullish reaction, coherent stop/target | potential continuation CANDIDATE_FOR_REVIEW under declared assumptions, not filled LONG |
| MTF-04 | 4H DOWN, 15m RANGE and no rejection | WAIT_CONFIRMATION or range-condition pending, not automatic SHORT |
| MTF-05 | 4H DOWN, 15m bullish CHoCH only | 15m POSSIBLE_SHIFT; 4H DOWN remains until its own evidence changes |
| MTF-06 | 4H DOWN, 15m short rejection confirmed at known resistance | conditional SHORT case; enforce zone/timing/risk, no automatic execution |
| MTF-07 | 4H DOWN, 15m local bullish engulf only, no breakout evidence | neither 4H UP nor automatic breakout LONG |
| MTF-08 | Same source p32 breakout long path achieves later confirmed 1H structural break | independent conditional LONG review, 4H remains DOWN if unchanged |
| MTF-09 | 4H UP, RSI 97 and price far above chosen demand zone | WAIT for retracement; RSI overbought not automatic SELL |
| MTF-10 | 4H UP, source 1H/15m TON figures missing from screenshot | distinguish Coach assertion from independently observed chart |
| MTF-11 | PDF p31 30m OB proposed, 5m reaction; chart profile not selected | no silent universal 4H/1H requirement; require explicit profile |
| MTF-12 | PDF p35 Weekly/Daily bearish but 4H possible recovery | no Weekly/Daily trend flip; do not transfer PHP BPI price levels to crypto |
| MTF-13 | 4H bar closes PHT12:00, 5m bar opens11:55 ends12:00 | T0 uses previous 4H; no new final 4H during 11:55 |
| MTF-14 | New 4H and 5m bars nominally close12:00; actual arrival ordering unknown | T1 same-timestamp acceptance UNCERTAIN; conservative delay |
| MTF-15 | New 4H known12:00:03, 5m known12:00:01, decision12:00:02 | no use of newly ending 4H at12:00:02 |
| MTF-16 | Decision12:00:04 with above confirmed arrivals | T1 may use both as-of decision; not rewrite their 11:55 context |
| MTF-17 | 4H event becomes available, earlier 5m signal already recorded | retain original as-of evidence; future context does not retroactively reclassify |
| MTF-18 | Previously qualified continuation long, new qualified HTF bearish structural disconfirmation | REASSESS current candidacy; never rewrite earlier historical signal |
| MTF-19 | Venue symbol XAUUSDT perpetual versus token XAUTUSDT spot | keep independent instrument keys and structural levels |
| MTF-20 | Price data missing required 4H history but RSI on 15m available | CONTEXT_INSUFFICIENT (or DATA_INSUFFICIENT for absent required 4H feed), not false “neutral” |
| MTF-21 | 4H RSI unknown, but setup profile only needs structure+zone+reaction | disclose missing optional RSI without an invented veto |
| MTF-22 | 4H RSI unknown in profile explicitly requiring RSI for gating | required-condition INSUFFICIENT, not a bearish vote |
| MTF-23 | LTF close above EMA50, 1-bar EMA slope upward same EMA | one redundant sign fact, not two independent confirmations |
| MTF-24 | Multiple active scenarios support opposite directional candidates | CONDITIONAL_CONFLICT with per-branch conditions, not global BUY/SELL |
| MTF-25 | No style/profile selected while contradictory structures are observed | UNSELECTED_STYLE and descriptive observations, no default trade |
| MTF-26 | Known HTF DOWN with invalidated resistance zone, bearish engulf on 15m | INVALIDATED or ZONE_INSUFFICIENT, not source-style SHORT |
| MTF-27 | 15m bearish engulf still forming | PROVISIONAL; WAIT_CONFIRMATION for closed-bar candidate |
| MTF-28 | PSE weekly historical setup copied to crypto venue with different sessions | invalid cross-market calibration; require venue-qualified test |
| MTF-29 | Range conditions on 15m but HTF direction unknown, profile explicitly requires HTF filter | CONTEXT_INSUFFICIENT, not unconditional range LONG |
| MTF-30 | 4H UP, 1H DOWN, 15m bullish candle at support but no risk numbers | preserve 4H/1H disagreement and potential reaction; RISK_INCOMPLETE not order |

**30 manually enumerated cases. No fixture runner was executed.** They cannot demonstrate non-repainting runtime behavior or profitability.

## I. Ponder comparison: alternative architectures

| Candidate model | Mechanism | Advantage | Failure mode / what would change decision |
|---|---|---|---|
| **M05-A stratified event ledger** | per-TF states, per-branch gated candidates, explicit provenance and known-at | best causal auditability; preserves p18/p32 conflict | more complex UI and potentially delayed signals; compare against source-manual cases |
| **M05-B one directional voting score** | collapse e.g. 4H/1H/15m to one bullish fraction | compact dashboard | ignores conditional scalp/reversal branches, correlated price features and missingness; not Coach-exact, no win-rate guarantee |
| **M05-C unanimous HTF/LTF agreement** | block if timeframe directions differ | easy rule, fewer candidates | incorrectly discards documented pullback and countertrend situations, may miss legitimate p32 conditional cases |
| **M05-D source-annotated manual analysis** | human frames chart context and key zones | highest fidelity to discretionary examples, useful benchmark | not automatic, quality depends on reference annotation timing |

**Research recommendation:** carry M05-A as the *working conceptual architecture* and M05-D as reference benchmark, use B and C only as explicit sensitivity comparisons. Do not select production parameters or claim model A has better trading expectancy without later data and user-authorized tests.

## J. Next incomplete methodological gates

1. Cross-module \`known_at\` and invariants need a formal **validation protocol** and later executable synthetic fixtures (no permission to code has been inferred).
2. M03 RSI/EMA precise contexts and overlap-ablation design remain partially specified.
3. M06 cost, tick and execution-specific risk modeling, plus M07 outcomes, must be defined before any strategy backtest is meaningful.
4. Source-human interpretation and algorithmic candidates should be compared **blindly and causally**, with explicit unclear/ambiguous labels and negative results retained.
5. Pine input mapping, chart-swap/reload acceptance, MTF consistency and alert conditions are future implementation, **not accomplished here**.

**Status:** written M05 research increment complete for the current scope; Phase 2 overall remains OPEN, all 35 Coach PDF pages remain source-studied, no Pine source or actual market backtest deployed.
