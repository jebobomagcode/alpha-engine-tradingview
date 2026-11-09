# Lesson 07 — Formalizing Market Structure and Confluence

**Status:** OPEN RESEARCH SPECIFICATION ONLY, 2026-11-09; no code, Pine chart tests, backtest results, trading orders or empirical edge established.  
**Original basis:** [Coach PDF p.9](../../sources/coach%20trading%20lessons.pdf) and [PCSS Lesson 07](../lessons/07-market-structure-confluence.md).  
**Market mandate:** crypto, including distinct XAUUSDT, XAUTUSDT and PAXGUSDT products.  
**Provenance:** Coach explicitly gives trend + S/R + engulfing; all formula choices below are *independent candidate formalizations*, not direct Coach rules.

## A. Source-constrained high-level predicate

For a user-selected instrument/timeframe context:
\[
B = T_\mathrm{UP}\ \land\ Z_\mathrm{SUPPORT}\ \land\ E_\mathrm{BULL},\quad
S = T_\mathrm{DOWN}\ \land\ Z_\mathrm{RESISTANCE}\ \land\ E_\mathrm{BEAR}.
\]
The conjunction is logical, **not** a calculated predictive probability. A historical bar with all three conditions does not automatically establish a valid order or positive expected return.

**Probability falsification question:** does \(\Pr(\text{predeclared favorable outcome}\mid T,Z,E)\) exceed relevant baseline conditions after realistic transaction costs, with meaningful samples and uncertainty? Outcome horizon, SL, TP, fees, funding and sample must be established first. Do not invent a numeric “high probability” from Coach's language.

## B. Swing definition candidates and causal timing

### Option 1: symmetric left/right window pivots

A swing high candidate on bar \(t\) can be compared to neighboring high values over \(L\) bars to the left and \(R\) to the right. But it is **not confirmable until at least bar \(t+R\)** closes. Tie/equality rules need specification. Symmetric low pivots are analogous.

Pros: interpretable, reasonably stable offline. Cons: confirmation lag, sensitivity to \(L,R\), failure on plateau highs/ties. In Pine, drawing the label at historical bar \(t\) can mislead users about the bar when the pivot was actually known. TradingView official [repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) specifically warns about retroactive pivot plotting.

### Option 2: causal directional-change / deviation swing

A swing extreme updates provisionally until price reverses by a predeclared absolute, percentage, or volatility-scaled threshold. The swing event becomes confirmed at reversal detection time, not the original extreme. Threshold may behave differently across BTC, altcoins and gold-related token products.

Pros: adapts to market price excursions. Cons: threshold sensitive and a historical extreme can be retroactively relabeled if not properly timestamped.

### Option 3: rolling channel/excursion

Track confirmed break of prior \(N\)-bar high/low ranges, with clear treatment of overlapping breaks and candidate swing lows. Pros: causal and straightforward; cons: not necessarily equivalent to visually labeled alternating HH/HL sequences or Coach's illustration.

**No option chosen.** Compare on fixture correctness, time-of-knowledge, label stability, density and actual controlled outcome utility. Allow a **MIXED/UNKNOWN** state rather than inventing uptrend/downtrend labels.

## C. Strict structural state proposal

For a temporally alternating sequence of confirmed swing highs \(H_i\) and lows \(L_i\) with valid comparisons:

- \(H_i>H_{i-1}\), \(L_i>L_{i-1}\) → **UP** candidate;
- \(H_i<H_{i-1}\), \(L_i<L_{i-1}\) → **DOWN** candidate;
- otherwise **SIDEWAYS, MIXED or INSUFFICIENT** according to separately specified range/ambiguity rules.

This alone does **not** solve minimum number of pivots, reversal threshold, tie behavior, transition state, equal HH/HL, dual-breaking candles, inside bars or zone anchoring. Avoid returning DOWN just because an UP candidate fails.

**Temporal invariance:** the signal at time \(t\) must use only swings whose **confirmation time** is \(\le t\). Display labels may optionally show the historical extreme but must disclose the detection lag and never backdate trade eligibility.

## D. Trend and zone share input data

S/R is often derived from swing extrema, so \(\text{Trend}\) and \(\text{Zone}\) are statistically dependent. Engulfing also shares underlying OHLC data with trend and zone.

**Therefore:** counting trend, zone and engulfing as 3 *independent* confirmations to multiply imagined probabilities is invalid without a justified conditional model. More restrictive conditions may reduce setup frequency but need not increase winning probability or profit factor.

**Counterfactuals:** compare T+Z+E against T+Z, T+E, Z+E, E-only, and a minimal predeclared nonpattern baseline; use out-of-sample and regime segmentation. Infer only the incremental utility actually supported by evidence.

## E. Context placement and timeframes

Lesson 04 allows 1H or 4H higher-timeframe context and 5m or 15m lower-timeframe entry. Page 9 does not specify mandatory simultaneous 1H-and-4H agreement or precedence when they conflict.

Future requirements:
- store instrument/venue/spot-vs-derivative identity, candle time and timezone;
- store HTF structural event's known-from timestamp, finalized/provisional state and whether the HTF price zone was knowable;
- validate zone contact using a predeclared wick/body/close rule; exclude zones formed only after the signal bar;
- ensure LTF engulfing uses two bars, second closed, and agreed strict/relaxed variant from Lesson 06;
- handle bullish engulf at bearish resistance and other misaligned observations explicitly as WAIT/NO_SETUP, not auto-buy/sell;
- handle incomplete or contradictory HTF context as MIXED/INSUFFICIENT.

## F. Proposed state flow and classifications

Inputs: exchange-qualified symbol and product type, chart timeframe, confirmed OHLC, source method for swings and zones, two-candle engulfing rules, timing and risk inputs.

Possible output statuses:
- `INSUFFICIENT_DATA`: incomplete bars or not enough confirmed swings.
- `CONTEXT_UP`, `CONTEXT_DOWN`, `CONTEXT_SIDEWAYS`, `CONTEXT_MIXED`.
- `ZONE_SUPPORT`, `ZONE_RESISTANCE`, `ZONE_NONE`, `ZONE_UNCONFIRMED`.
- `ENGULF_BULL`, `ENGULF_BEAR`, `ENGULF_ABSENT`, `ENGULF_PROVISIONAL`.
- `BUY_CANDIDATE`, `SELL_CANDIDATE`, `WAIT`, `NO_SETUP`, `UNVERIFIED`.

No performance confidence score or “high probability 80%” display until an appropriate statistical estimate is separately validated. Future execution decisions depend on later lessons.

## G. Synthetic planned fixture cases (NOT run)

1. Confirmed rising HH/HL + known support + closed bullish engulf → conceptual BUY candidate.
2. Confirmed falling LH/LL + known resistance + closed bearish engulf → conceptual SELL candidate.
3. Bullish engulf without support → NO COACH-ALIGNED setup.
4. HTF UP + LTF DOWN pullback → report timeframe disagreement without flattening into absolute market state.
5. Equal swing highs, rising lows → mixed/sideways until rule resolves tie.
6. One outside bar makes higher high and lower low → ambiguous; do not classify UP and DOWN simultaneously without priorities.
7. Chart pivots confirmed 4 bars after extreme: historical label may mark old bar, signal available only at confirmation bar.
8. Support zone discovered after engulf occurs → cannot retroactively validate old signal.
9. Gold FXOpen 1H screenshot compared to actual Binance XAUUSDT or token PAXGUSDT → not feed-equivalent.
10. Sideways LTF and clear higher TF uptrend → do not automatically declare both invalid or valid; must define context policy.

No fixture is executed or marked passed at this stage.

## H. Research design and failure criteria

**Research hypotheses:**
- H0: three-way confluence provides no incremental after-cost predictive/decision value versus suitable simpler baseline.
- H1: it improves quality or interpretability but at a cost of reduced signal count and later confirmation.
- H2: additions overfit specific historical gold/crypto regimes or appear predictive due to delayed pivot labels/lookahead.

Before comparing outcomes: predeclare exact market, exchange, product, date range, regimes, bar resolutions, source-grounded setup/entry/SL/TP, commission, spread, slippage, funding if applicable, holding period, walk-forward or out-of-sample window and model uncertainty. Use negative/neutral cases as well as attractive annotated past examples. Report sample counts and confidence limits.

Official independent TradingView sources:
- [Repainting and pivots](https://www.tradingview.com/pine-script-docs/concepts/repainting/): retrospective pivot labels and HTF security context can mislead.
- [Strategies and testing limitations](https://www.tradingview.com/pine-script-docs/concepts/strategies/): lookahead, selection bias, overfitting and cost realism.

**Priority direction:** Preserve source baseline with explicit provenance; prototype none until permitted; prefer chronological correctness and clear reasons over visually attractive hindsight structure lines.

**OPEN:** pivot model/strength, tie and transition rules, zone algorithms, candle geometry definitions, HTF conflict policy, quantitative “high probability” claim, execution risk, verified market-specific feed conditions.

**Next PCSS on owner's instruction:** Lesson 08 — Trading, PDF page 10.
