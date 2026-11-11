# M02–M06 — Source-Aligned Top-Down Entry Gates, Candle Reaction, EMA/RSI, and Risk (research v0.1)

**Status: INDEPENDENT FORMALIZATION PROPOSALS, NOT APPROVED PINE OR EXECUTED STRATEGY.** 2026-11-09 Asia/Manila. Sole Coach source: [PDF pp6,9–10,17–25,31–32](../../sources/coach%20trading%20lessons.pdf). Sources remain distinguished from new models; [causal structure spec](01-causal-market-structure.md), [full traceability](00-source-to-rule-traceability.md), [cross-lesson register](../METHODOLOGY_RECONCILIATION.md).

## A. Coach's original sequence and conflicting contexts

**COACH_EXPLICIT PDF p9:** trend + zone + signal; engulfing used as one simple example. **p10:** assess HTF trend and support/resistance, WAIT for price to reach the zone; if price doesn't reach it, **NO TRADE**. Only then seek LTF **engulfing OR long-wick rejection plus follow-through OR strong body candle**. One strong confirming candle can suffice; **entry after confirmation candle CLOSES**. SL outside support/resistance, TP next level **OR** 1:2 / 1:3 RR. **p6/p24:** HTF context and LTF reaction separated, not chase.

**COACH's contextual exceptions:** p9 generally discourages sideways, pp12–13 gives conditional range setups; pp17–18 describes a countertrend SOL scalp versus HTF UP; p31 uses 30m OB + 5m confirmation with RSI bounce40–50 (different from p21 bounce above50); p32 bearish 4H can coexist with 15m range and mutually conditional SHORT rejection / LONG breakout. These cannot be silently forced into one universal source rule.

**OPEN source gaps:** exact zone geometry, candle confirmation formulas, “same contact candle or later candle”, RSI-bounce arithmetic/timeframe, stop buffer, eligibility of countertrend/range profiles, thresholds, setup expiry. Our labels and formulas below are NOT Coach terminology.

## B. Proposed information contract and WAIT states (INDEPENDENT)

An analysis snapshot reports separately: feed identity and quality; confirmed HTF structural bias; pre-known zone location and age; zone contact timing; LTF reaction and close state; EMA/RSI readings and timeframes; disconfirming events; risk proposal; and current decision eligibility.

| Proposed decision status | Preconditions / reason | Source relationship |
|---|---|---|
| DATA_INSUFFICIENT | instrument, bar finality, timestamp or OHLC history untrusted | necessary independent safeguard |
| CONTEXT_INSUFFICIENT | trend/swing evidence not established | structure-first, PDF p9/15 |
| ZONE_INSUFFICIENT | no verifiable eligible zone | p10 requires known area |
| WAIT_ZONE | known context+zone, price not yet touching | p10 explicit NO TRADE |
| CONTACT_PENDING | apparent touch is intrabar or ambiguous | independent temporal caution |
| WAIT_CONFIRMATION | zone reached but eligible closed LTF reaction absent | p10 wait for confirmation |
| RISK_INCOMPLETE | potential setup confirmed, but entry/SL/TP or contract unknown | source p10 entry and risk elements |
| CANDIDATE_FOR_REVIEW | all known gates plus risk proposal | **not an order, alert or probability claim** |
| REASSESS | opposing structural break or invalidated premise | p25 CHoCH possible change |
| EXPIRED | zone/signal validity period ended by a later rule | source leaves expiry missing |

**Proposed precedence:** untrustworthy data → invalidation → missing context/zone → wait for contact → wait for closed reaction → risk incomplete → candidate. Display detailed coexisting timeframe observations even when a top-level decision says WAIT. An unavailable macro calendar is NEWS_UNKNOWN, never NO_NEWS.

## C. Proposed M02 zone lifecycle (not Coach-specified mathematics)

A candidate zone record contains: exact exchange+symbol+product; timeframe; category (S/R, Order Block, FVG, EMA retest, Fibonacci); price interval low/high and quote; source/formation candle IDs; **defined_at and known_at**; eligible direction; invalidation/expiry policy; status and contact time. A zone whose full geometry was defined after the historic contact must NOT become an eligible prior-known area by retroactive drawing.

**Alternative zone touch models:**
- Z0: provenance-tracked discretionary/manual drawing with actual known-at time.
- Z1: a **completed** LTF candle's high-low overlaps the already-known interval.
- Z2: the completed candle's body overlaps the already-known interval.
- Z3: wick touches/rejects zone and later follow-through closes.
These disagree on wick-only probes; no candidate is certified by Coach as the universal definition.

**Same-bar ambiguity:** The source says wait until price reaches zone then seek confirming lower-TF candle. It does NOT specify whether the very candle whose wick first contacts the zone may qualify at close. Conservative sequential candidate A requires a *later* closed bar. Candidate B allows same completed bar touch+reaction if the zone pre-existed, but acknowledges that OHLC alone does not reveal all intrabar event order. Compare, don't silently pick a source-exclusive rule.

## D. Proposed M04 reaction grammar (source alternatives, independent geometry)

Let a valid completed candle have open O, high H, low L and close C. Define **body** B=|C−O|, **range** R=H−L, **upper wick** U=H−max(O,C), **lower wick** W=min(O,C)−L. If R=0, body/range ratios are undefined and must not be evaluated by division.

**COACH_EXPLICIT:** p10 engulfing (preferred), rejection wick plus follow-through, **or** strong candle. p21 bullish rejection long example. p31 bullish engulfing/rejection plus RSI/EMA considerations. p32 bearish wick, engulfing or failed breakout.

**INDEPENDENT alternatives:** body engulf of preceding candle's real body vs entire-candle engulf (wicks included); wick-body ratio threshold for rejection; body/range threshold for strong candle; follow-through as one or more later final closes. No thresholds, integer delays or Boolean combination have been chosen, so a score of “3/3 confirmed by Coach” is not warranted. Intrabar signals are PROVISIONAL, and one candle satisfying multiple descriptions is not three independent pieces of evidence.

## E. M03 exact EMA mathematical dependence — independently proved

For a **close-based** EMA with constant smoothing 0<α<1:
\[
E_t=\alpha C_t+(1-\alpha)E_{t-1}.
\]
Then
\[
E_t-E_{t-1}=\alpha(C_t-E_{t-1}),\qquad
C_t-E_t=(1-\alpha)(C_t-E_{t-1}).
\]
Since both coefficients are strictly positive, the sign of the **one-bar EMA slope** and **current close minus that same EMA** is exactly the same (assuming the same bars, source, initialization and no missing data). They are **not independent binary confirmation votes**. Multi-bar slope, different price source, timeframe or degenerate α=1 must be evaluated separately.

**COACH_SOURCE p22–24:** RSI14 common, above50/below50 is momentum context, >70 overbought and <30 oversold, NOT instant trades. EMA20/50/200 common periods, price position and EMA slope relevant. p24 example separately lists above EMA50 and EMA rising; the one-bar binary simplification above explains a *specific mathematical redundancy*, not a claim Coach intended a one-bar slope definition.

**Contextual RSI hypotheses** (all OPEN): RSI holding above50, RSI rebounding while within 40–50, RSI recovering across50, RSI rejecting below50. Lesson16/19 continuation and Q&A2 scalp have **different source wording**; time window, slope and exact bounce boundaries not specified.

## F. Model branches, not one universal signal

| Branch | Original pages | Source-consistent research gate | Crucial distinction |
|---|---|---|---|
| TREND_CONTINUATION | 9,10,21,24 | known HTF trend → previously known zone → closed LTF confirmation → risk review | clearest minimal source sequence |
| CONDITIONAL_RANGE | 12–13 | sideways range boundaries + lower-TF reversal at boundary | lesson07 cautions sideways; do not declare universally valid |
| COUNTERTREND_SCALP | 17–18 | explicitly short against bullish 4H with smaller horizon/conditional reaction | not HTF-aligned swing |
| PULLBACK_SCALP | 31 | Coach new 30m OB + 5m reaction, RSI40–50 consideration | not the student's already-open long |
| REVERSAL_WATCH | 25,32,34–35 | tentative local CHoCH/reaction vs higher reversal state | temporary bounce ≠ global reversal |

Initial *research* preference: TREND_CONTINUATION as basic causal baseline with qualitative comparisons to all four others; not a production strategy or decision to discard any example.

### F1. Important SOURCE distinction — range breakout trigger vs Lesson08 close (2026-11-10)

Original **PDF p10 Lesson08** explicitly says entry **after confirmation candle closes** for its trend/zone/LTF workflow. Original **PDF p13 Lesson10 sideways-range example** instead says **“entry sa break ng confirmation”** in both SELL and BUY setups. The latter leaves open whether the proposed entry is a later stop-trigger break of a completed confirmation candle, an intrabar threshold breach, or a closing break. It is **not accurate** to treat “after candle close” and “on break of confirmation” as automatically the same event or to impose the Lesson08 close rule universally across every Coach setup. Preserve a context-specific research branch with exact event timing and order semantics still OPEN.

The distinction is material for historical simulation: a breakout stop order may be placed only after its prerequisite confirmation is known; OHLC cannot establish the within-bar sequence of a touch, confirmation and order fill. Until this policy is chosen and tested, report a conditional candidate, **not** a verified filled entry.

## G. M06 gross-risk and execution distinction

The [M06 conceptual specification](09-m06-risk-and-execution-uncertainty.md) extends this early gross-risk sketch with source traceability, account units, as-of eligibility, product constraints and execution uncertainty. The earlier examples below remain contextual.

For a **LONG proposal** \(S<E<T\), per-unit price risk \(d=E-S\), gross reward \(g=T-E\), and gross RR \(g/d\). For a **SHORT proposal** \(T<E<S\), \(d=S-E\), \(g=E-T\), with \(d>0\). Require specified entry, stop and target before a unique gross RR; reject inverted or zero distances. A tick size and actual contract quantity are additionally necessary for a physically feasible order. No order mechanics are designed at this stage.

**Account risk** for simple linear fully filled quantity Q before costs is Qd in the quote currency; movement-to-stop as a percent of entry is d/E, **not percent of account equity**. A predeclared maximum account loss budget B gives nominal bound Q≤B/d in the same quote units, ignoring costs and gap/slippage/liquidation; actual tradable quantity must be constrained more carefully. Leverage changes margin/notional, not the underlying quoted per-unit stop distance.

**Rechecked Coach case arithmetic:** Q&A3 student SHORT E79419 S79918 T78423 → d499, g996, RR996/499≈1.995992, correctly rounds to 1:2. Q&A2 student's reported LONG E0.2436 S0.2385 → d0.0051 (about 2.0936% of entry) but no account risk inferred. Coach *different proposed plan* E0.238–0.240 and S strictly below0.231 has **no uniquely determined gross RR**.

The source does NOT choose order type, next-bar fill, trail algorithm, partial target division, intrabar stop/TP order, contract funding or fees. Official TradingView [strategy broker emulator](https://www.tradingview.com/pine-script-docs/concepts/strategies/) describes historical fill assumptions; no simulation has been performed.

## H. Falsification and discrimination matrix — designed only, NOT executed

| ID | Constructed case | Expected result or unresolved difference |
|---|---|---|
| D01 | HTF bullish, no evidence-based zone | ZONE_INSUFFICIENT, no long |
| D02 | Known zone, price never arrives | WAIT_ZONE / source NO TRADE |
| D03 | Zone touch on developing 5m candle | CONTACT_PENDING, not closed confirmation |
| D04 | Strong bullish engulfing away from valid zone | Not an eligible Lesson08-style entry |
| D05 | Contact + closed reaction, missing stop | RISK_INCOMPLETE |
| D06 | Opposing HTF event after setup developed | REASSESS; no stale bullish assumption |
| D07 | Only wick overlaps zone, body does not | Z1 contact yes; Z2 contact no |
| D08 | One candle both touches zone and engulfs | Sequential A versus same-bar B differs |
| D09 | Sideways gold at defined range boundary with bounce | conditional RANGE, not asserted trend continuation |
| D10 | SOL short against bullish 4H context | COUNTERTREND_SCALP, not aligned swing |
| D11 | RSI 47 to49 | in-band bounce maybe; strict above50 false |
| D12 | RSI 47 to52 | crossover variant possible, separate from in-band bounce |
| D13 | Close above same current EMA and one-bar EMA slope positive | exactly redundant sign for α in (0,1) |
| D14 | RSI equals70 exactly | not strictly above70 |
| D15 | Exact stop only constrained S<0.231 | gross RR incomplete |
| D16 | Student 1:2 RR but no 15m rejection in consolidation | WAIT on source Q&A3 timing logic |
| D17 | 15m bullish CHoCH while 4H still bearish | separate timeframe statuses; no global reversal |
| D18 | Missing macro event calendar | NEWS_UNKNOWN, no assumed calendar status |
| D19 | Gold derivative XAUUSDT vs backed token XAUTUSDT | distinct feed, no price-level transfer |
| D20 | More EMA/RSI gates reduce trade frequency | improvement unknown until after-cost holdouts |

These are **constructed expected cases**, not automatic tests or actual chart observations. Selecting thresholds, states, tick logic, simulation fills, risk budget or a Pine strategy remains OPEN.

## I. Next specification steps

The dependency path is: **M00/M01 causal market structure** → **M02 specific zone formation and expiry** → **M04 candle geometry and timing** → **M03 EMA/RSI contexts and redundancy tests** → **M05 state machine and conflicting style branches** → **M06 cost-/tick-aware order-proposal rules** → **M07 research evaluation/ablation**. This document sketches the interfaces without falsely declaring M02–M07 complete.

**Completion claim limited to:** written source-aligned conceptual state/risk research and formally derived EMA redundancy, with 20 candidate tests specified. No Pine script, TradingView chart verification, crypto backtest, alerts, deployment, or actual financial outcome.
