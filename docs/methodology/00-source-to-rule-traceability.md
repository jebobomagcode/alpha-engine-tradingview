# Phase 2 — Coach-source to formal methodology traceability (v0.1)

**Status:** RESEARCH SPECIFICATION IN PROGRESS; no Pine code, brokerage integration, alerts, historical market backtests, or deployed chart. Date: 2026-11-09 Asia/Manila. This is a conceptual document, not an approved automated rulebook.

## Sources, scope, and order

- Sole Coach source: [original 35-page PDF](../../sources/coach%20trading%20lessons.pdf), SHA-256 **481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730**. [All original PCSS studies](../LESSON_COVERAGE.md) and [coverage reconciliation](../SOURCE_STUDY_COMPLETION_AUDIT.md).
- Personal PCSS standard is source for teaching rigor, NOT published in public repository.
- Future *implementation* only crypto: separately venue/product-qualified BTC/ETH, XAUUSDT, XAUTUSDT, PAXGUSDT as user specified. Forex and PSE equity examples are source study, not authorization for separate forex/equity implementations.
- Methodology provenance: COACH_EXPLICIT (original PDF); STUDENT_ASSERTION (Q&A only); INTERPRETATION (inferred formal meaning); INDEPENDENT_EXTENSION (new proposal); OPEN_UNRESOLVED (missing rules); TESTED_FORMAL_EXAMPLE (arithmetic/constructed fixture only); LIVE_VALIDATED requires real TradingView verified test, currently NONE.
- Rule/figure inventory is **not** performance data. A study document can be COMPLETE while its machine-readable methodology remains OPEN.
- This matrix has **26 original source units**, in their original PDF order; its destination column lists module allocation, not proof that every module is already formally specified.

## Phase boundary and requirements

**Current milestone:** (1) create complete source-to-concept index, (2) register consequential cross-lesson tensions, (3) write an exact *research* specification for the causal bar/pivot/structure foundation, (4) design finite counterexamples. We do not select production parameter values or implement Pine. Additional methodological modules will be specified incrementally.

**Requirements that no future variant may erase:** source attribution; original meaning retained even if corrected mathematically; time known-at; exchange-qualified feed identity; non-hindsight pivots; source Lesson08 NO TRADE outside the chosen zone for the trend-location-confirmation setup; confirmation candle closes before that source-style entry; source “possible reversal” is not proof of regime reversal; trade-risk completeness; no unearned performance or confidence claims.

## Source-order traceability map

| Source unit | Original PDF | Key source concepts | Assigned research modules / unresolved choices |
|---|---:|---|---|
| 01 Trading101 | 1 | crypto/forex/stocks scope, discipline | M00 instrument identity; M06 risk; no performance inference |
| 02 Candles | 2–3 | hammer, shooting star, doji, location | M04 reaction geometry (wick/body ratio missing) |
| 03 Risk Reward | 4–5 | 1:2 examples, compounding | M06 gross vs net risk/expectancy; cost model missing |
| 04 Time Frame | 6 | HTF1H/4H trend+zone, LTF5m/15m entry | M00 bar known-at; M05 pairing and delayed confirmation |
| 05 Leverage & Margin | 7 | capital, notional, leverage, liquidation warning | M06 margin/exposure and sizing; venue risk policy unknown |
| 06 Engulfing | 8 | bullish/bearish body engulfing descriptions | M04 candle rule geometry and source ambiguity |
| 07 Structure & Confluence | 9 | HH/HL, LH/LL, sideways caution, trend+zone+signal | M01 structure; M05 branch eligibility |
| 08 Trading | 10 | HTF→zone→LTF close confirmation→entry, NO TRADE if no contact | M05 sequential state machine, M04, M06 |
| 09 Support & Resistance | 11 | zones and role reversal | M02 zone rules, prior touch/flip evidence |
| 10 Marking Support/Resistance | 12–13 | sideways gold range and conditional zone entries | M02 range, M05 range exception; Forex price values NOT crypto |
| 11 Order Block | 14 | last candle before large move, no defined threshold | M02 OB formation without institutional-identity claim |
| 12 BOS | 15–16 | trend first; up breaks prior HH, down breaks prior LL | M01 causal pivots and structural continuation |
| 13 Manage Your Risk | 17–18 | SOL countertrend scalp and HTF-aligned conditional long | M05 style-specific branch, M06 separate invalidations |
| 14 Fibonacci | 19 | swing anchors, 0.5–0.618 and later 0.618–0.705 | M02 anchor freeze & alternative bands, M04 confirmation |
| 15 Reliability | 20 | price action, EMA, RSI, FVG/OB, candles | M03 indicator redundancy; M05 score alternatives |
| 16 Long/Short Setup | 21 | structural + EMA/RSI context, pullback, reaction | M03 RSI/EMA; M05 ordered continuation templates |
| 17 RSI | 22 | RSI14, 30/50/70, not signal alone | M03 oscillator levels; contextual bounce alternatives |
| 18 EMA | 23 | EMA20/50/200, slope/location and range caveat | M03 exact EMA/candle warmup/redundancy |
| 19 Top-Down RSI+EMA | 24 | HTF context → pullback → LTF confirmation | M05 event provenance and optional context filters |
| 20 CHoCH | 25 | DOWN breaks prior LH; UP breaks prior HL; possible reversal | M01 countertrend break then reassessment |
| 21 Setup | 26–28 | 4H TON screenshots; claimed 1H/15m inputs, FVG/OB/RSI context | M00 case evidence provenance; M05 unknown context |
| Q&A 01 | 29–30 | bullish HTF EMA/RSI, wait retest, possible bearish challenge | M03 signals vs bias; M05 WAIT |
| Q&A 02 | 31 | existing FARTCOIN long vs Coach NEW preferred 30m OB/5m bounce40–50 | M03 RSI context, M05 position vs candidate, M06 stop inequality |
| Q&A 03 | 32 | 4H bear/15m consolidation, SHORT rejection OR breakout LONG | M01/05 independent branches, M06 example RR |
| N-01 Location/Time | 33 | forex Tue–Thu, London/NY PHT, macro calendar | M00 optional timezone/news context; no crypto veto without evidence |
| N-02 “BSP” Charting | 34–35 | actual PSE:BPI Weekly/Daily/4H, EMA20/50/200, local bounce vs Daily CHoCH | M00 market ID, M01 time-relative reversal, M03 |

## Module dependencies and stage of work

| ID | Module | Depends on | Formalization state | Immediate next evidence |
|---|---|---|---|---|
| M00 | Instrument, bar timestamps, source quality and causal availability | none | Foundational research spec in [01](01-causal-market-structure.md), sections A–B | verify example clocks/HTF |
| M01 | Market structure, swing selection, BOS/CHoCH, regime | M00 | Foundational research spec in [01](01-causal-market-structure.md), sections C–H | alternative pivots and synthetic cases |
| M02 | S/R, range, OB, FVG, Fibonacci zones | M00,M01 | OPEN; only previous lesson research | source-to-zone grammar |
| M03 | EMA, RSI and momentum/confluence | M00,M01 | OPEN; source disagreements inventoried | algebra and alternative RSI bounce |
| M04 | Candle reaction, rejection, engulfing, confirmation | M00,M02 | OPEN; source confirms close for Lesson08 | exact OHLC geometry |
| M05 | HTF/LTF and setup eligibility, WAIT, directional conflicts | M00–M04 | concept flow only; not formalized | state transition table |
| M06 | SL/TP, sizing, margin and strategy-evaluation contract | M00,M02,M05 | OPEN; examples audited | cost-/tick-aware quantities |
| M07 | Validation/ablation, venue/regime and evidence reporting | M00–M06 | research protocol only | predeclare holdouts and benchmarks |

**Phase 2 is NOT complete.** Completion requires individual rule IDs with formal constraints, alternative definitions, counterexamples, source traceability, decision records and a coherent cross-module interface. The first increment does not close M02–M07.

## Scope of the first formalization

M00/M01 will produce:
1. Explicit bar record including exchange-qualified ticker, market product, timeframe, open/close time, OHLCV and finality/available-at timestamp.
2. Swings that cannot be used before confirmation. A historical drawing at the pivot origin is NOT an alert then.
3. Candidate trend taxonomy and structural event taxonomy while preserving unresolved pivot and break thresholds.
4. A finite fixture set with manually evaluated expected outcomes and assumptions (not executed automated tests).
5. No source claim that “more confluence” implies a win rate.

See [cross-lesson reconciliation](../METHODOLOGY_RECONCILIATION.md) for unresolved choices and priorities and [M00/M01 research specification](01-causal-market-structure.md).
