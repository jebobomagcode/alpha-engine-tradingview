# PCSS Lesson 15 — Reliability on Charting

**Status:** COMPLETE at original-source PCSS study level, 2026-11-09 Asia/Manila; all page-20 statements preserved in their actual order, visual page inspected and native text checked; independent mathematical explanations and critique labeled separately. **No Pine code, market-data backtest, actual chart acceptance, deployment, trades or empirical win-rate evidence.**

**Only Coach-origin source:** [coach trading lessons.pdf, PDF page 20](../../sources/coach%20trading%20lessons.pdf), original SHA-256 `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`. Private PCSS standard SHA-256 `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56` (do not publish personal PCSS). Scope: fresh independent TradingView project focused on crypto, including separately identified XAUUSDT, XAUTUSDT and PAXGUSDT products. Do not access/modify previous trading projects.

## Complete source-order inventory and original-page audit

Page 20 was extracted through native PDF text and rendered at high resolution for direct manual inspection. **Page 20 has only text**, mostly near its upper-left corner. No figure, chart, diagram, table of measured reliability, EMA length, numerical trade, worked computation, formula, proof, question or exercise.

| ID | Original page-20 item in strict order | Source-preserving interpretation |
| --- | --- | --- |
| 15-01 | Heading “15. Reliability on charting” | Lesson title |
| 15-02 | “mas reliable long term” introduction | Qualitative preference for the listed charting components, **no statistical reliability measure or specified hierarchy** |
| 15-03 | “-structure / sup and resistance” | Market structure and support/resistance (previous Lessons 07, 09, 10, 12) |
| 15-04 | “-EMA trend” | EMA used for trend reading; **no period, source price, crossing or slope rule given** |
| 15-05 | “-RSI momentum” | RSI used for momentum reading |
| 15-06 | “-FVG / OB / liquidity” | Names Fair Value Gaps, Order Blocks and liquidity together; no deterministic boundaries, volumes or mandatory confluence count |
| 15-07 | “-confirmation candles” | Retains candle-confirmation prerequisite from previous lessons; no new candlestick patterns defined |
| 15-08 | “RSI is more useful in momentum of market.” | Explicit emphasis on momentum rather than stand-alone trend or trade decision |
| 15-09 | “If above 50 usually bullish momentum, below 50 bearish momentum” | **Strict above and below 50 as qualitative directional interpretation**, not guaranteed forecast; equality not specified |
| 15-10 | “Pero hindi rin enough gamitin mag isa kaya importante parin structure at S&R” | Explicitly warns against standalone RSI use; emphasizes structure and support/resistance |

**Next-page boundary:** Original page 21 begins *Lesson 16 — Long and Short set-up*, where additional EMA and RSI conditions appear. Those are **not part of Lesson 15** and have not been taught or formalized in this study. Page 22 begins the dedicated RSI lesson; do not import its settings into page 20 and claim they originated here.

## 1. Coach's reliability components, preserving source order

**COACH EXPLICIT:** “mas reliable long term” followed by five unweighted, unranked components:
1. Structure / support and resistance.
2. EMA trend.
3. RSI momentum.
4. FVG / OB / liquidity.
5. Confirmation candles.

**PCSS interpretation:** They describe different *roles* in contextual chart reading: structural direction and zones; smoothed price trend; recent momentum; possible price reaction/liquidity regions; visible confirming candle behavior.

**Do not misstate source:** Coach provides neither a numerical “reliability score” nor a requirement that all five must pass as mandatory boolean gates, and does not claim this exact sequence is an executable strategy. The listed order is source order, not a measured descending priority. Last sentence explicitly says RSI is insufficient on its own; that does not mathematically prescribe weights for all elements.

## 2. Structure and support/resistance first

From source order, Coach lists structure and S/R first and returns to them in the closing sentence. Previous Lessons 07, 09 and 12 define HH/HL vs LH/LL, support/resistance zones, and BOS continuation meaning. These provide context for interpreting the other components, especially in conflicting 4H/15m cases like Lesson 13.

**Independent conceptual example, NOT Coach market data:** HTF remains bullish HH/HL while LTF RSI<50. This may reflect a pullback rather than a confirmed HTF reversal. The HTF structural observation and an LTF momentum reading can both be true on their own timeframes. Do not force them into one bullish/bearish boolean.

## 3. EMA trend — what the source does and does not define

**COACH EXPLICIT:** only “EMA trend” appears on page 20.

**INDEPENDENT MATHEMATICAL EXPLANATION:** For EMA period \(n>0\) and closing price \(C_t\), a common form is:
\[
\alpha=2/(n+1),\qquad \mathrm{EMA}_t=\alpha C_t+(1-\alpha)\mathrm{EMA}_{t-1}.
\]
For illustrative \(n=20\), \(\alpha=2/21\approx 0.095238\). The number 20 is **NOT from Coach's page 20**. Its initialization, selected price series, and repeated sampling must also be specified.

Different interpretations can disagree: current price above EMA, EMA rising versus falling, two EMA crossovers, EMA with source timeframe. This lesson provides no length, single/multi EMA decision, price source, slope calculation, crossover policy or timeframe precedence; these remain **OPEN**.

**Independent external technical authority:** TradingView's [EMA help](https://www.tradingview.com/support/solutions/43000592270-exponential-moving-average/) explains weighting and lag; do not mistake EMA for evidence of actual order identity or a predictive guarantee.

## 4. RSI momentum, midpoint and mathematical derivation

**COACH EXPLICIT:** RSI is especially useful for momentum reading, above 50 **usually** suggests bullish momentum and below 50 bearish momentum, but RSI alone is inadequate.

**Independent math:** With Wilder-smoothed average gain G and average loss D>0, RS=G/D and RSI=100-100/(1+RS). If G=D then RSI=50; if G>D, RSI>50; if G<D, RSI<50. If G=1.5,D=1 (synthetic smoothed averages) then RS=1.5 and RSI=60. These are illustrative values, not a measured Coach chart. Edge cases with no gains/losses require implementation behavior rather than division by zero.

Source does **not** specify RSI period or exact zero/midpoint equality behavior on page 20. A potential neutral state at exactly 50 is a reasonable independent convention, not literal Coach instruction. The dedicated RSI lesson is later and must be audited in sequence. Official [TradingView RSI](https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/) documents the formula and default 14 separately (EXTERNAL, not page-20 source).

**Critical distinction:** RSI>50 does NOT imply next price candle rises or establish overall trend independently; momentum of smoothed recent gains versus losses is not a guaranteed directional forecast. A 4H bullish structure and a 15m RSI below 50 can coexist.

## 5. FVG, OB and liquidity — related, not identical concepts

**COACH EXPLICIT:** groups “FVG / OB / liquidity” without a numeric rule.

**INDEPENDENT CLARIFICATIONS:** FVG is a candidate imbalance depending on a chosen OHLC geometry; Order Block is a price region preceding strong displacement (Lesson 11 source); liquidity may mean actual resting market depth, stop/liquidation interest inferred from charts, or a proposed liquidity-sweep price pattern. **Chart OHLC does not reveal who placed orders or how many stops exist**. Do not equate these objects or pretend FVG/OB/liquidity detection is finalized.

Page 20 does NOT require every FVG to overlap an Order Block, nor make “liquidity” universally measurable from OHLC, nor state a minimum count of three or five confirmations.

## 6. Confirmation candles

**COACH EXPLICIT:** “confirmation candles” are included as a component, without any new type/threshold.

**Previous source recalled only as prerequisite:** Lessons 02, 06 and 08 discuss engulfing, rejection, strong bodies, hammer/shooting star and closing-event conditions. Lesson 10 emphasizes specific reversal candles in its range case. Their applicability to future arrangements remains scenario-sensitive; we should not impose a universally required engulfing candle for all regimes based on this page alone.

**Independent distinction:** a confirmed-looking candle in the middle of a range may fail the location gate from Lesson 08. Price-action classification and actual trade eligibility are separate concepts.

## 7. Interpretation — “reliability” is not demonstrated reliability

The page gives a qualitative preference, not a dataset or measurement:
- no asset universe, historical date coverage, timeframe, success definition, forward horizon or risk model;
- no backtest, commission/funding, drawdown or out-of-sample sample size;
- no indicator ablation comparing EMA/RSI to structural-only baselines;
- no defined confidence weights, votes or numeric reliability percentages.

**Ponder source-respecting conclusion:** treat the listed components as analytical context and candidate diagnostics, not proof that adding each indicator independently improves a signal's predictive power.

### Important dependence problem (independent)

EMA and RSI are both transformations of historical price data, whereas some structural/FVG/OB detections also depend on the same OHLC extrema. Multiple signals can therefore be highly correlated. It is **not** mathematically justified to multiply their purported “success probabilities” as if independent or to assume five agreeing components equal five independent votes. Quantify incremental information against baselines and avoid retrospective selection.

## 8. Proposed conceptual workflow — NOT a Coach binary checklist

Proposed **research-stage** arrangement: instrument/timeframe-qualified structural context -> price location (S/R and qualified FVG/OB/liquidity hypotheses) -> EMA trend and RSI momentum as supporting/conflicting observations -> a fully closed LTF confirmation candle -> independent entry/SL/TP review or WAIT/NO TRADE/INSUFFICIENT.

**This does not assert that Coach requires all five gates, nor that EMA is subordinate to structure as a formal mandated weighting.** Read the eventual next Lesson 16 before specifying exact long/short conditions.

**Synthetic contradiction case:** 4H structure UP, 4H EMA rising, 15m RSI=46, support approached, no LTF confirmation. A robust model should report disagreement and WAIT rather than automatic short or long. This is independently invented, not original case data.

**Time-of-knowledge:** EMA/RSI and current bar high/low/close may move during an unclosed bar. HTF data can repaint on LTF without correct confirmation handling. Official [TradingView Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) documents the need to distinguish provisional versus confirmed events. This is a potential future code requirement, not a tested property of our project.

## 9. Future validation gate

See [Lesson 15 independent research document](../research/15-indicator-reliability-confluence-ablation.md) for baselines, counterexamples, data sufficiency, ablation design, correlation checks, scoring-vs-gating comparisons and indicator configuration choices. Nothing has been implemented or tested on crypto data.

## Completion and handoff

All ten source-page items read in strict order, original page rendered and image inspected; no original figure, numerical result, formula or exercise exists to reproduce. Supplementary EMA/RSI formulas, neutral convention, flow and examples clearly marked independent. **Lesson 15 COMPLETE as a PCSS source study, NOT an implementation or validated strategy.**

**Next on owner instruction:** Lesson 16 — *Long and Short set-up*, original PDF page 21, which supplies additional HTF/LTF EMA and RSI combinations. Preserve page boundary; do not auto-advance.
