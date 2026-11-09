# Lesson 18 — EMA Observations, Slope Redundancy and Sideways-Market Research

**Status:** OPEN INDEPENDENT RESEARCH PROPOSALS; not implemented, compiled, deployed or backtested. Date 2026-11-09 Asia/Manila.
**Sole Coach-origin evidence:** [PDF page 23](../../sources/coach%20trading%20lessons.pdf); [complete source-first PCSS Lesson 18](../lessons/18-ema-exponential-moving-average.md). Owner focus: crypto including XAUUSDT derivatives, XAUTUSDT and PAXGUSDT backed tokens as exchange/product-specific different data feeds. Older repositories out of scope.

## Coach source contract — exact source roles

- EMA used for trend direction, dynamic support/resistance, momentum continuation and market bias.
- Common EMA20 = short-term momentum, EMA50 = medium trend, EMA200 = overall trend/macro bias.
- Price above EMA = bullish environment; below EMA = bearish environment.
- During uptrend EMA acts as potential dynamic support for pullbacks; during downtrend EMA can act as resistance for rejection.
- EMA sloping upward = bullish momentum; downward = bearish; flat = ranging or weak.
- In sideways conditions, fake signals/price recrossings occur; Coach regards EMA as most useful in trending markets.
- **Missing:** mandatory EMA mix, length selection per HTF/LTF, crossover rule, price source, period-to-timeframe mapping, close vs wick, strict trend definition, slope horizon/magnitude, retest tolerance, empirically quantified performance.

## 1. One-step EMA recurrence and verifiable exact redundancy

Define same-timeframe, close-based period n>1, alpha=2/(n+1) with 0<alpha<1:
E_t=alpha*C_t+(1−alpha)*E_(t−1).

Two derived identities:
(1) E_t−E_(t−1)=alpha*(C_t−E_(t−1)).
(2) C_t−E_t=(1−alpha)*(C_t−E_(t−1)).

Thus the signs of close-minus-current-EMA and current-EMA-minus-previous-EMA are the SAME, including equality. For those exact conditions:

**C_t > E_t ⇔ E_t > E_(t−1).**
**C_t < E_t ⇔ E_t < E_(t−1).**

Consequently a six-factor confluence model that uses both **price above EMA** and **EMA one-bar upsloping** on the same close and timeframe as two supposedly independent confirmations will double-count the same mathematical fact. This holds regardless of chosen n>1, seed (once the recurrence holds), and actual price history. The result is stronger than an empirical correlation: it is algebraic identity.

**Counter-boundaries:** The equivalence may fail when slope is over k>1 bars, compared price is wick/high/low while EMA uses Close, the EMA series is drawn with offset, comparisons use different timeframes, or missing/irregular data/historical warmup yields inconsistent series. Do not generalize to chart “angle” or multi-bar macro trend without checking the definition.

**Tiny arithmetic fixtures (independent, no actual market candles):**
- Eprev=100, C=105, n=20 ⇒ E=100+10/21=100.476190..., C>E and E>Eprev.
- Eprev=100, C=95, n=20 ⇒ E=100−10/21=99.523809..., C<E and E<Eprev.
- Eprev=100, C=100 ⇒ E=100, C=E and unchanged slope.

## 2. Candidate EMA representations — no final selection

**A. Observation-only overlay (closest to source ambiguity):** show EMA20/50/200 separately, price position, one-bar directional change, multi-bar normalized slope where selected, source/known-at timestamp, and textual caution if conflicting structure or sideways. No BUY/SELL.

**B. Regime-gated analytical state:** independently define a sideways regime (e.g. adaptive pivot ranges, directional movement index, trend efficiency metric, ATR-normalized EMA movement), then track EMA retests only in a qualifying regime. Every metric/threshold is an external enhancement, not supplied by Coach. Failure risk: overfitting, suppressing valid source-described range/countertrend cases (Lessons 10/13).

**C. EMA confluence scoring:** assign relative roles to EMA20, EMA50 and EMA200 and add RSI/structure. Danger: every EMA is derived from same price data, and one-bar price-side and EMA-slope evidence are algebraically redundant; a naive weighted score can be falsely confident.

**D. Minimal baseline:** EMA20-only or no-EMA structure+S/R+closed-candle confirmation baseline for ablation; lower complexity, potentially fewer false “confluences,” may miss informative smoothing.

Working preference for future research: **A vs D**, then B/C only if measurable evidence warrants complexity; no final architecture approved.

## 3. “Angle” is not numerically invariant

Displayed angle depends on panel dimensions, zoom and price scale. To obtain an objective measurement, independently consider:
- one-bar change Δ1=E_t−E_(t−1);
- k-bar slope Δk=(E_t−E_(t−k))/k;
- normalized slope Sk=(E_t−E_(t−k))/(k*E_(t−k)) for strictly positive prices;
- ATR-scaled change as a separate hypothesis.

The word “strong” in Coach's slope labels does **not** define a numerical threshold. Even an ATR-normalized slope threshold could fail if volatility spikes or if short history distorts ATR.

**Slope and price location must not be presented as two independent checks if Δ1 and same close EMA are selected.**

## 4. EMA dynamic support/resistance: competing event definitions

- Wick touch: bar Low<=EMA<=High.
- Closing cross: a completed Close crosses EMA and returns to one side.
- Rejection: bar wick touches candidate EMA but closes with directional body; geometry/tolerance must be defined.
- Approximation: |price−EMA|<=epsilon, with predeclared epsilon in ticks, ATR or percent.
- Multi-bar pullback: price moves against HTF structure for several bars before revisiting EMA, followed by context-specific confirmation.

All are independent alternatives. **Coach gives no exact wick-vs-close touch rule, buffer, timeout or EMA length mapping.** A plotted moving average at the moment of evaluation is not a previously guaranteed fillable order price. Recording source/timeframe/EMA at actual event time prevents hidden re-anchoring.

## 5. Whipsaw and changing market conditions

Synthetic source-independent range: closes alternate 99,101,99,101 about a smoothed center near 100. Depending on starting EMA and length, completed prices can alternate above/below EMA repeatedly even with no structural uptrend/downtrend. A mechanical crossover system would risk churn and costs.

Potential research approaches to a sideways detector (all external):
- Confirmed swing-width/directional-progress measurement.
- EMA slope/volatility ratio.
- Trend-efficiency ratio of net displacement to cumulative absolute changes.
- Explicit unresolved/WAIT when conflicting structural timeframes or insufficient history.

A flat EMA can be caused by balance of price changes but cannot certify no future directional movement. A steeper EMA can lag an imminent reversal. These are candidate hypotheses, not empirically verified trading relationships.

## 6. Multiple EMA lengths and source/provider distinctions

Given n20,n50,n200 on the same completed close series: alpha20≈0.095238, alpha50≈0.039216, alpha200≈0.009950. The three reflect different smoothing horizons but share underlying price data. Their agreement is correlated and does not justify arbitrary multiplication of hit rates.

**Source nuance:** Coach lists common 20/50/200, while TradingView's standard EMA interface can have its own default length 9 and source Close, according to official documentation. Never interpret the UI default as Coach's chosen setting, or assert the 20/50/200 set is globally optimal without tests.

Official references:
https://www.tradingview.com/support/solutions/43000592270-exponential-moving-average/
https://www.tradingview.com/support/solutions/43000502589-moving-averages/

The exact venue-qualified TradingView feed and product are material: crypto perpetual XAUUSDT EMA may diverge from XAUTUSDT and PAXGUSDT token market EMAs even at similar nominal prices.

## 7. Causal multi-timeframe and live-candle safeguards

For a future EMA overlay, distinguish:
- completed candle source P_t versus forming realtime P_t;
- HTF 4H or Daily completed EMA from current HTF developing EMA;
- lookahead/offset settings of requested HTF data; timeframe identity and close time;
- EMA computation warmup and valid bar-count.

TradingView officially documents that unconfirmed HTF values can repaint after reload, and recommends an offset expression with lookahead_on to retrieve last confirmed HTF values, at the cost of delayed availability:
https://www.tradingview.com/pine-script-docs/concepts/repainting/
https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/

These are *future implementation constraints*, not actual Pine test results. A current forming EMA is not a source-proven confirmed EMA.

## 8. Proposed discriminating tests — none executed as Pine or market study

1. The mathematical sign-identity holds at n=20,50,200 for valid same-series EMA recursion, including equality case; symbolic derivation above.
2. One-bar price-side EMA and one-bar EMA slope claimed as two independent confluence votes: reject.
3. Multi-bar slope negative while latest close is above current EMA: possible; record distinct signal horizon.
4. Chart zoom changes apparent EMA angle without changing calculated prices: pixel-angle method rejected as invariant criterion.
5. Price touches EMA by wick but not by Close: different candidate retest rules disagree.
6. Price crosses EMA briefly intrabar but finishes on original side: provisional versus confirmed state.
7. 4H structural uptrend, 15m close below EMA20: HTF structure must not be overwritten.
8. Repeated EMA crossings in alternating closes range: whipsaw scenario, candidate NO_TRADE/WAIT.
9. EMA20 and EMA200 disagree: keep period-specific evidence rather than force an ungrounded majority decision.
10. Initial history too short for EMA200/seed: return WARMUP/INSUFFICIENT instead of fabricated stable macro bias.
11. Source Price differs Close vs HL2: EMA value and sign comparisons may change; provenance required.
12. Missing bars or instrument change: reset source/warmup interpretation; no cross-feed reuse.
13. XAUUSDT derivative vs XAUTUSDT or PAXGUSDT spot/token history: different EMA levels; no forced equality.
14. Source's “trend works best” compared to no-EMA structural baseline in precommitted holdout regimes with realistic cost/slippage; performance not assumed.
15. Capturing last confirmed HTF EMA on 15m chart: no future-values leak; test Pine reload once coding authorized.
16. Price exactly equal current EMA, slope should exactly 0 under same close-based same-period model; tolerance policy for floating-point rounding remains open.
17. EMA period order and spacing in a long sustained uptrend could show EMA20>EMA50>EMA200; this stacking is NOT a required Coach lesson-18 condition.
18. Source Lesson 19 begins next page and contains EMA50-specific top-down example; preserve it for subsequent study rather than preapply to this lesson.

## 9. Ponder decision and evaluation stop point

**Decision at study stage:** Source-faithful 20/50/200 EMA context with no ungrounded crossover execution or reliability score; mathematically eliminate duplicate one-bar price/EMA-slope “votes”; leave slope horizon, retest event, sideways-regime definition, 3-length combination and timeframe policy OPEN_UNRESOLVED. Compare simpler baseline against enhancements after entire source study and technical execution authorization.

**Verification boundary:** The one-bar redundancy is a proved algebraic identity given explicit assumptions; no Pine code, live behavior, simulated fills, exchange data or net financial returns have been tested. Do not conflate analytic proof with an empirically profitable rule.

**Next source on user's instruction:** Lesson 19 — RSI + EMA Application Using Top Down Analysis, original PDF page 24.
