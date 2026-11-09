# Lesson 15 — Component Reliability, Confluence Dependence and Ablation Candidates

**Status:** OPEN RESEARCH HYPOTHESES ONLY, 2026-11-09 Asia/Manila. No Pine code, chart test, backtest, empirical performance or trading.
**Sole Coach authority:** [original PDF p. 20](../../sources/coach%20trading%20lessons.pdf) with [PCSS source audit](../lessons/15-reliability-on-charting.md).
**Implementation scope:** independently new crypto TradingView project, including XAUUSDT, XAUTUSDT and PAXGUSDT as distinct venue-qualified product feeds. Other repositories must not be touched.

## Source fidelity boundary

Coach lists under “mas reliable long term”: structure/support/resistance, EMA trend, RSI momentum, FVG/OB/liquidity, confirmation candles. Then emphasizes RSI for momentum (usually bullish if above 50, bearish if below 50) and explicitly warns RSI alone is insufficient without structure/S&R.

**Not in Coach's page 20:** strict importance ranking, numerical reliability percentage, hit-rate statistics, EMA periods, multiple EMA crossings, RSI length, exact FVG/OB/liquidity geometry, candle completion requirement here, all-five-gates rule, five-vote confidence system, asset universe, timeframe settings or profitability.

Therefore source text should not be converted into a fully specified quantitative strategy without additional independent policy decisions or later source lessons. Lesson 16 (PDF page 21) is next and gives specific HTF/LTF setup components; do not silently incorporate its rules into Lesson 15.

## A. Competing system architecture candidates — no selection yet

**Option A — source-relative qualitative dashboard:** display structural regime/SR location, EMA orientation, RSI position vs 50, OB/FVG/liquidity candidates and candle confirmation separately, with clear source/independent provenance. Advantage: avoids inventing hard weights or signal conditions; disadvantage: discretion remains.

**Option B — hierarchical confluence gates:** define a sequence of required structural bias, relevant zone contact, trend/momentum conditions and confirmation, followed by risk. Advantage: reproducible; disadvantage: Coach page 20 does NOT require all five, and overly strict conditions can suppress valid discretionary setups (including Lesson 13 countertrend case).

**Option C — additive weighted score:** choose weights for independent components, output a score and optional threshold. Advantage: interpretable if weight calibration and uncertainty are defensible; disadvantage: arbitrary weights, double-counted price evidence, overfit and false confidence without rich out-of-sample data.

**Option D — minimal baseline:** only qualified structure and support/resistance plus relevant confirmation. Advantage: simplest, fewer parameters, closest to Coach's closing statement; disadvantage: potentially omits useful but unproven momentum context.

**Working research preference:** preserve A with D as baseline until all Coach lessons are audited, then compare B/C as separately labeled *independent enhancements* on predeclared historical crypto fixtures. Not final code direction or user-approved strategy.

## B. Why “more confirmations” does not mathematically mean higher reliability

EMA computed from closes and RSI computed from price changes share source information. Swing/BOS, OB, FVG and reaction patterns often use the same OHLC highs/lows. Their events are often statistically dependent.

A naive count of positive indicators cannot be interpreted as N independent pieces of evidence. Multiplication of independent likelihoods would require conditional independence or a justified joint probabilistic model, not established here.

**Example of dependence:** 4H price rising over many bars can produce both higher swing highs and an upsloping EMA, while RSI also shifts above 50. These may be different views of *the same underlying trend*. An extra indicator is useful only if it adds better calibrated information beyond the baseline, including potential disagreement and false alarms.

## C. Independent EMA/RSI formalization candidates, not Coach thresholds

**EMA:** choose period n, input source, warm-up and timeframe; for \(\alpha=2/(n+1)\), \(EMA_t=\alpha C_t+(1-\alpha)EMA_{t-1}\). Separate candidate orientation rules: price > EMA, slope \(EMA_t>EMA_{t-k}\), or multi-EMA arrangement; no n or k selected. Official https://www.tradingview.com/support/solutions/43000592270-exponential-moving-average/ .

**RSI:** Wilder RS=smoothed_gain/smoothed_loss, RSI=100−100/(1+RS). From Coach page 20, RSI>50 *usually* bullish momentum, RSI<50 *usually* bearish; RSI=50 is not specified. Candidate neutral equality policy or tolerance around 50 is independently introduced and not claimed as source. Choose period only after later Coach RSI page (Lesson 17) and entire PDF review. Official https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/ .

**Candle state:** must label 5m/15m forming vs confirmed data explicitly, especially EMA/RSI midbar. Official https://www.tradingview.com/pine-script-docs/concepts/repainting/ .

## D. Proposed ablation design (not executed)

Freeze source-compatible baseline and independent variants before accessing future outcome measurements. Use same chronological splits/holding rules/fee model. Compare:
- M0: qualified structural regime + S/R zone + closed confirmation candle;
- M1: M0 plus EMA-orientation condition;
- M2: M0 plus RSI-above/below-50 condition;
- M3: M0 plus both EMA and RSI;
- M4: M0 plus independent explicit FVG/OB/liquidity candidates;
- M5: full confluence (only if a final rule is specified);
- M6: continuously measured independent weighted-score alternative, calibrated only on train period.

Do NOT presume any is superior. If EMA and RSI only reduce sample count without improving out-of-sample after-cost outcome or decision clarity, retain the baseline.

Possible evaluation endpoints, to predeclare:
- complete setup count, rejection reasons, coverage, missing history and frequency of contradictory cases;
- out-of-sample net expectancy, drawdown, error bars/uncertainty intervals, transaction costs and opportunity tradeoffs;
- event known-at time, repaint/reload consistency, and price-feed identity;
- false positives, false negatives relative to a predeclared operational label, latency and number of unique opportunities;
- stratification by market regime, volatility, exchange-qualified spot/perpetual versus tokenized gold products.

Avoid cherry-picked examples, repeated testing over same holdout, label leakage, survivorship bias, double-counting a single trade across multiple partially overlapping signals or optimizing thresholds after viewing test results.

## E. Planned discriminator cases — NO execution

1. 4H HH/HL UP, 4H EMA rising, 15m RSI 46, LTF support approached, no confirmation: context disagreement + WAIT, not forced BUY/SELL.
2. 4H UP while 15m RSI<50: do not call 4H DOWN on RSI reading alone.
3. RSI=50 precisely: equality undefined by Coach, candidate NEUTRAL rather than arbitrary bullish/bearish.
4. RSI crosses 50 intrabar but closes back below: no historical confirmed crossing under close-based policy.
5. EMA slope rising while price below EMA: difference between candidate EMA definitions, not automatic model bug.
6. EMA source length n not specified: do not claim n=9/20/21 Coach-prescribed.
7. FVG and OB overlap because built from same strong move: cannot count as independent votes without evidence.
8. Liquidity-sweep marker drawn from OHLC does not establish actual exchange resting order volume.
9. Five candidate indicators agree on one bar but entry is at midrange rather than known zone: Lesson 08 says no zone contact, NO TRADE.
10. A confirmed candle appears at valid S/R but HTF structure is unknown or data missing: insufficient, not fabricated confluence.
11. Large increase in strict filter count raises precision on in-sample but reduces actual out-of-sample opportunities or worsens after-cost return: reject claimed proven reliability.
12. Two overlapping symbol feeds (XAUUSDT derivatives vs XAUTUSDT/PAXGUSDT) create disagreeing levels: keep different venue/product identities.
13. TradingView historical data and realtime forming bars differ: maintain provisional vs confirmed events, test reload behavior later.
14. Lesson 13 countertrend short with 4H UP and 15m bearish: do not unilaterally forbid a source-described candidate under an unjustified five-gates rule.
15. LTF support contact and RSI>50 but no candle confirmation: source does not authorize automatic BUY.

## F. Ponder conclusion

The source teaches a *set of complementary analytical roles* plus an explicit warning against standalone RSI. The most important measurable question is whether adding EMA, RSI, OB/FVG/liquidity truly improves a simpler causal structure+zone+confirmation baseline.

**Decision:** keep Coach's qualitative statement and separate components; prefer an explainable dashboard research candidate with NO TRADE/WAIT/INSUFFICIENT. Leave thresholds, mandatory confluence rules, scoring weights and code design **OPEN** until source-wide lessons and appropriately designed tests.

**Next user-directed PCSS:** Lesson 16, Long and Short set-up, PDF page 21; not yet studied. No coding, backtesting or deployment.
