# PCSS Lesson 07 — Market Structure and Confluence

**Status:** COMPLETE — original page-9 source-order text and three illustrated panels manually audited, taught in the conversation, independent examples and critical qualifications documented; 2026-11-09 (Asia/Manila).  
**Coach authority:** [coach trading lessons.pdf, original PDF page 9](../../sources/coach%20trading%20lessons.pdf) — sole Coach-origin source.  
**Source PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`.  
**Original PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`.  
**Implementation:** NOT STARTED. No Pine code, compilation, actual chart signal tests, backtests, trades, or deployment.  
**Owner market scope:** Crypto including XAUUSDT, XAUTUSDT, PAXGUSDT separately; the original source's FXOpen gold spot/US dollar chart is not evidence for any crypto gold instrument.

## Exact-order source inventory

The full original PDF page 9 was rendered at 2x and examined visually alongside fitz-extracted native text. **Three identifiable illustrated panels** are present: upper-right trading chart, center-right orange-outline combined structure schematic, lower-right dual uptrend/downtrend illustration. Some first-paragraph text appears repeated at bottom of the source page following the final SELL line; this is a visible/extracted duplication, *not an additional distinct trading rule*. There is no original numerical probability, source OHLC worked dataset, coded algorithm, proof, or standalone exercise.

| ID | Source element in page order | Status/qualification |
| --- | --- | --- |
| 07-01 | Heading “07. MARKET STRUCTURE and CONFLUENCE” | Covered |
| 07-02 | Intro recalls engulfing and S/R; shifts to “context” of chart | Covered; prerequisites Lessons 04 and 06 |
| 07-03 | Coach lists 3 foundations: 1. Trend (direction/price bias), 2. Zone (support/resistance), 3. Signal (engulfing) | Covered in order |
| 07-04 | TREND heading | Covered |
| 07-05 | Uptrend = rising, pattern Higher High + Higher Low | Covered |
| 07-06 | Downtrend = falling, pattern Lower High + Lower Low | Covered |
| 07-07 | Sideways = no direction; avoid trades unless viewing a higher TF | Covered with nuance |
| 07-08 | “Paano maging valid ang entry”: engulfing alone is not enough; need Trend, Support/Resistance, Engulfing | Covered |
| 07-09 | “Valid Trade”: Uptrend + at support + bullish engulfing → “HIGH PROBABILITY BUY” | Covered as Coach's qualitative assertion; no empirical probability supplied |
| 07-10 | Downtrend + at resistance + bearish engulfing → “HIGH PROBABILITY SELL” | Covered; same evidence limitation |
| 07-11 | Last line restarts heading/intro text | Recorded as repeated text in original page, not a new independent concept |
| 07-F1 | Upper-right dark trading screenshot | Gold Spot/U.S. Dollar, 1H, FXOpen chart; descending trendline, LH/LL labeled swing structure, resistance/red line and support/green levels, live-style price bars. **This is not Binance XAUUSDT or tokenized gold** | Visually inspected |
| 07-F2 | Middle-right orange-bordered zigzag figure | Continuous left-to-right uptrend (higher HH/HL), sideways swing highs/lows in near-level bands, then downtrend (LH/LL). Shows transitions, not precisely detected timestamps | Visually inspected |
| 07-F3 | Lower-right dual-panel illustration | Green uptrend swing highs/lows and red downtrend swing highs/lows, comparison of HH/HL versus LH/LL | Visually inspected |

## 1. The three foundations

**COACH_EXPLICIT:** Trend = direction/bias; Zone = support/resistance; Signal = engulfing. Coach says these are the three principal foundations he uses to read a market, explicitly recalling Lessons 06 and earlier S/R mentions.

**PCSS intuition:** Trend asks “in which direction?”, zone asks “where might a relevant reaction happen?”, signal asks “what reaction is visible?”. A candle shape at an unrelated location lacks the same contextual relevance as a shape reacting to a preexisting zone within a compatible trend.

**Important separation:** The three terms describe different roles, not statistical independence. A zone derived from swing highs and lows can share nearly all its input data with the trend detector, so blindly counting them as three independent confirmations would overstate evidence.

## 2. Uptrend: higher highs and higher lows

**COACH_EXPLICIT:** Uptrend is paakyat; pattern HH + HL.

**INDEPENDENT EXPLANATION:** Consider a sequence of *already identified and confirmed* swings \(H_1,H_2,\dots\) and \(L_1,L_2,\dots\), each ordered within the same timeframe. A minimal comparative definition has:
\[
H_2>H_1,\qquad L_2>L_1.
\]
Example, not Coach data: highs 100 then 110 then 118 USDT, lows 90 then 95. The rising sequences fit the sketch. However, this assumes which extrema qualify as **swings** is already known and uses the appropriate chronological alternating sequence. The source does **not** define pivot lookbacks, minimum swing size, equal-high handling, wick/close reference or pivot-confirmation delay.

**Subtlety:** A down candle inside an uptrend is not automatically structural reversal; the degree and location of the move matter.

**Visual source:** In the combined orange diagram, rising peaks and retracements are shown to the left; the lower figure independently shows rising swings labeled higher high/higher low.

## 3. Downtrend: lower highs and lower lows

**COACH_EXPLICIT:** Downtrend is pababa; pattern LH + LL.

**INDEPENDENT EXPLANATION:** With confirmed relevant swing values, one candidate definition is
\[
H_2<H_1,\qquad L_2<L_1.
\]
Illustrative highs 120 → 113 → 105, lows 110 → 103 → 95 (USDT) show progressively declining comparable swing values.

**Visual source:** the upper-right dark screenshot shows an apparent 1H downward gold market, annotated trendline, LH/LL levels and S/R; it is an illustrative snapshot of **FXOpen Gold Spot/U.S. Dollar**, and cannot establish that all gold-backed crypto assets follow the same candles. The central schematic transitions from sideways to declining peaks/troughs. Lower-right pane shows the simple downtrend HH/LL contrast.

**Critical observation:** A single lower high is not by itself a complete downtrend; one must define the structure and lower lows coherently. Neither this page nor the diagrams resolve borderline mixed sequences.

## 4. Sideways: weak directional structure

**COACH_EXPLICIT:** Sideways = no direction; Coach advises avoiding trading unless looking at the higher TF.

**INDEPENDENT EXPLANATION:** Roughly repeated swing highs and lows, overlapping swings, or no consistent higher-high/higher-low or lower-high/lower-low sequence can indicate a range or uncertainty. The center diagram depicts a banded oscillation between the up- and downtrend segments. Ranges are not guaranteed to remain contained; breakouts and failed breakouts occur.

**Nuance:** “Sideways on 5m” is not inherently “sideways on 4H”. Higher-TF context may reveal a broader uptrend or downtrend. Coach's exception refers to seeking higher-timeframe context, **not automatic permission to trade sideways without a signal**.

**OPEN:** exact definition/threshold of sideways, how many swings are needed, mixed structures, equal highs, different timeframe structures.

## 5. Coach's valid-entry confluence requirement

**COACH_EXPLICIT:** Engulfing alone is insufficient. Valid entry needs all three: trend, S/R, and engulfing. His two illustrated rules are:

- Uptrend + at support + bullish engulfing = **“HIGH PROBABILITY BUY”**.
- Downtrend + at resistance + bearish engulfing = **“HIGH PROBABILITY SELL”**.

**SOURCE-INTEGRITY LIMIT:** “High probability” is Coach's emphatic description, **not a verified numerical win rate**. The PDF does not give the conditional success frequency, data distribution, trade management criteria, fees, entry timestamp or validation threshold. Never translate the phrase to, for example, 70%, 80%, or guaranteed positive expectancy.

**INDEPENDENT FORMAL REPRESENTATION (only as a schematic):**
\[
B_\mathrm{candidate}=T_\mathrm{up}\land Z_\mathrm{support}\land E_\mathrm{bull},
\]
\[
S_\mathrm{candidate}=T_\mathrm{down}\land Z_\mathrm{resistance}\land E_\mathrm{bear}.
\]
The letters are predicates to be **defined and measured later**, not completed indicators. The scheme respects Coach's conjunctive statement without guessing definitions. Even if all are true, actual entry timing, SL/TP and trading costs remain necessary. Lesson 08 is next, and may add conditions; do not treat page 9 as a fully executable order rule.

## 6. Prerequisite integration and independent crypto teaching example

- Lesson 02: single-candle shapes, including hammer/shooting star/doji; not all are Coach's engulfing signal here.
- Lesson 03: planned gross risk/reward and actual costs; good confluence does **not** remove stop risk.
- Lesson 04: HTF for trend/zone, LTF for confirmation; time-of-knowledge matters.
- Lesson 05: leverage/margin; apparent setup quality must not imply collateral safety.
- Lesson 06: bullish/bearish engulfing geometry; “strong/weak” remains numerically unspecified.

**Hypothetical example — NOT a real BTC chart or Coach's own trade.** A confirmed 1H BTCUSDT swing structure has rising highs and rising lows. A support zone is established *before* a subsequent 5m price approach. The newly closed 5m candle engulfs the preceding red body. This is a candidate according to Coach's conceptual BUY alignment, provided all three conditions were knowable and context definitions validated. A nearby bearish engulfing away from the relevant support would not meet the same candidate alignment. We still cannot infer a numeric probability or entry/SL/TP rule.

**Counterexample for overconfidence:** Suppose a bullish engulfing occurs at support in an uptrend but soon breaks down as broader volatility spikes. The three visually satisfied conditions did not ensure future success. Confluence is a selection heuristic, not a logical implication that markets must rise.

## 7. What “valid” means in different senses

1. **Geometrically valid**: a previously defined candle shape objectively matches OHLC.
2. **Structurally valid**: a causal, confirmed trend label matches the directional requirement.
3. **Spatially valid**: price interacted with a support/resistance region previously knowable.
4. **Coach-aligned candidate**: all three Coach concepts are satisfied according to explicit operational interpretations.
5. **Execution-valid**: entry, stop, target, size, costs, product mechanics and time states are acceptable under later rules.
6. **Empirically supported**: independent datasets show reliable, statistically defensible after-cost performance.

These are our analytical distinctions, not separate original Coach definitions. In this lesson, Coach asserts a qualitative *candidate alignment*, not independently verified financial performance.

## 8. Ponder audit of source ambiguities

- Swing detection: fixed left/right-bar pivots vs adaptive price excursions vs structural high/low breaks, all yield different labels.
- **Pivot known-at time:** a peak visible on historical charts may be validated only after additional bars. Plotting a swing marker at its physical peak is not the same as having that information when the peak formed.
- Comparison equalities and alternation: higher high vs equal high, lower low vs equal low, outside bars producing both a new high and new low, skipped/overlapping swings.
- HTF conflict: a 1H uptrend inside a 4H sideways range (or vice versa). Page 9 does not prescribe precedence.
- Zone quality: support and resistance are discussed but not numerically constructed; later Lessons 09–10 provide original source context.
- Confluence dependency: swing-based zones and swing-based trends use common evidence; naive “three independent confirmations” is unjustified.
- Label reliability: source screenshot uses FXOpen gold spot chart rather than requested crypto XAUUSDT, XAUTUSDT or PAXGUSDT; do not silently treat them as the same feed.
- Empirical assertion: if out-of-sample success probability conditioned on the three factors is not elevated above a suitable baseline *and* after costs, “high probability” would not be supported for that market/test design.

## 9. Official Pine technical findings — independent research, not Coach teaching

TradingView's official [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) page warns that many pivot scripts **draw labels into the past once a future-confirmed pivot becomes known**, making an unrealistically predictive historical chart. Its example confirms a pivot several bars later and places the label at the earlier peak; this is a display choice that must not be confused with signal availability.

The [Strategies](https://www.tradingview.com/pine-script-docs/concepts/strategies/) page details lookahead bias, selection bias, overfitting, and the importance of market fees/realistic assumptions. These documents inform our research constraints; **no Pine code was written or tested** in this milestone.

## 10. Future formalization candidates — not approved

The methodology could eventually be expressed as separate auditable detectors:

- **SWING_EVENTS:** confirmed peaks/troughs with source bar index and known-at index.
- **STRUCTURE_STATE:** UP / DOWN / SIDEWAYS / MIXED / INSUFFICIENT, with reasons and timeframe.
- **ZONE_STATE:** SUPPORT / RESISTANCE / NONE / UNKNOWN, with price bounds and known-from timestamp.
- **ENGULFING_STATE:** bullish/bearish geometry confirmed only after candle close, with prior pattern-ambiguity provenance.
- **CONFLUENCE_STATE:** aligned BUY_CANDIDATE / SELL_CANDIDATE / WAIT_CONTEXT / NO_ZONE / NO_ENGULF / CONFLICT.
- **RISK_REVIEW:** source-aligned setup is not execution authorization; require appropriate entry/SL/TP and product-specific risk data.

These terms are descriptive proposals. No algorithms, default thresholds, orders, alerts, or score weights have been authorized.

## Coverage, verification and checkpoint

- Original page 9 fully inspected as rendered PDF and native text; 10 unique text concepts, 1 repeated text fragment, 3 original illustrated panels catalogued.
- The dark actual chart is expressly **Gold Spot / U.S. Dollar on FXOpen 1H**, not one of the user's target crypto gold products.
- Qualitative high-probability claim preserved **as Coach's claim**, with no invented numerical probability.
- Original figures show trends, sideways structure and swings, but provide **no pivot lookback, S/R boundary, or quantitative confluence threshold**.
- Detailed independent reasoning and test ideas recorded in [research specification](../research/07-market-structure-confluence-candidates.md).
- **Lesson 07 complete for PCSS source study; no software implementation or financial validation.**
- **Next user-directed source:** Lesson 08 — Trading, original PDF page 10, including HTF marking, waiting for zones, LTF confirmation, entry and risk steps. Do not auto-advance.
