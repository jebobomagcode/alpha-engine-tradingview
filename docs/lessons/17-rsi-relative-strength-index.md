# PCSS Lesson 17 — RSI (Relative Strength Index)

**Status:** Complete for original-source PCSS study only; 2026-11-09 (Asia/Manila). Original PDF page 22 was checked visually and with native text extraction. No Pine Script, chart acceptance, backtest, deployment or actual trade.
**Sole Coach-origin source:** [coach trading lessons.pdf, p22](../../sources/coach%20trading%20lessons.pdf), original SHA-256 `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`. Private PCSS SHA-256 `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56` (not published).
**Market scope:** Separate venue-qualified crypto instruments including XAUUSDT, XAUTUSDT and PAXGUSDT; earlier projects remain outside scope.

## Complete source-order page inventory

The original page contains text only, with no screenshot, graph, performance study, source RSI formula, trade ledger or exercise. The following 21 items cover its heading, prose, settings, bullets and closing note.

| ID | Original element in order, rendered/paraphrased | Audit qualification |
|---|---|---|
| 17-01 | Heading RSI (Relative Strength Index) and repeated red-circle subheading | Concept/title |
| 17-02 | RSI measures strength of market movement | Momentum interpretation |
| 17-03 | Does not directly show trend direction; interpreted as buying/selling pressure | Price proxy, not direct order-volume measurement |
| 17-04 | Usual settings: length 14, overbought 70, oversold 30, momentum bias 50 | Usually is not fixed all-case proof |
| 17-05 | RSI above 70 = strong buying pressure | Coach language, not automatic short |
| 17-06 | RSI below 30 = strong selling pressure | Coach language, not automatic long |
| 17-07 | RSI above 50 = bullish momentum | Not the same as HTF bullish market structure |
| 17-08 | RSI below 50 = bearish momentum | Strictly below, equality unspecified |
| 17-09 | Overbought does not imply immediate SELL | Explicit warning |
| 17-10 | Oversold does not imply immediate BUY | Explicit warning |
| 17-11 | In strong trends RSI can stay high/low long; RSI-only countertrading dangerous | No quantified duration |
| 17-12 | Best usage: confirmation, momentum reading, confluence | Three items in exact order |
| 17-13 | Not good used alone for entries | Explicit warning |
| 17-14 | Common mistake: buy immediately at RSI 30 | Mistake 1 |
| 17-15 | Common mistake: sell immediately at RSI 70 | Mistake 2 |
| 17-16 | Common mistake: ignore market structure | Mistake 3 |
| 17-17 | Common mistake: ignore trend direction | Mistake 4 |
| 17-18 | Common mistake: use RSI alone | Mistake 5 |
| 17-19 | RSI divergence deliberately not discussed; prioritize possible market bias | Source scope exclusion |
| 17-20 | Then look for BOS, CHoCH, rejection candle confirmations | Examples, not mandatory simultaneous gates |
| 17-21 | RSI only confirms relative buying/selling pressure; price action and structure priority | Closing source principle |

## 1. Definitions and source settings

**COACH EXPLICIT:** RSI is a momentum indicator, not a direct market-structure/trend detector; Coach describes it as a proxy for buying or selling pressure. His **usual** setting is RSI length **14**, with reference levels **70 (overbought)**, **30 (oversold)** and **50 (momentum bias)**. RSI >70 is described as strong buying pressure; RSI <30 as strong selling pressure; RSI >50 bullish momentum; RSI <50 bearish momentum.

**PCSS clarification:** These regimes overlap. RSI 75 is both above 70 and above 50; RSI 25 is below 30 and below 50. Exact readings 30, 50 and 70 do not satisfy the source's strict “above/below” phrases; source provides no explicit equality rule. RSI does **not** measure actual market order identities, exchange depth or directly observed order-book pressure.

The word “usually” qualifies length 14 as a source-supported baseline, not proof that every original chart or optional configuration must use it. The page does not give a price source (Close vs another series), RSI smoothing initialization, or crossover/hold thresholds. External TradingView [RSI documentation](https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/) uses 14 and Close as software defaults; that does not prove every Coach screenshot setting.

## 2. Mathematical supplement — NOT from Coach

For Wilder-smoothed average gains G and losses D, where G,D≥0 and G+D>0, the RSI expression is

```text
RSI = 100 * G/(G+D)
```

equivalent to 100−100/(1+G/D) if D>0. Equal positive gains and losses yield RSI 50. **Independent worked illustration:** G=1.5,D=1 → RSI=60. If G=0,D>0 then RSI=0; if G>0,D=0 then RSI=100. If both G and D are zero, an explicit software convention is needed. These formulae and edge cases are *independent explanations*, not verbatim Coach definitions or an implemented calculator.

To reproduce a numerical RSI series, separately specify data source, length, Wilder-type smoothing/warmup, timeframe, missing-data treatment and whether values are from completed candles.

## 3. Strong-trend counterexamples and source warning

**COACH EXPLICIT:** overbought ≠ immediate SELL; oversold ≠ immediate BUY. Strong trends can maintain high/low RSI for extended periods, so RSI-only countertrend execution is risky.

**Independent illustration, not a backtest:** oscillator readings [64,72,77,74,81,78,83,76,79,73] contain a prolonged period >70. An entry rule “short every RSI>70” would ignore ongoing upward momentum and other required structure/zone/confirmation evidence. Similarly RSI=25 during a downtrend of LH/LL does not guarantee a bullish reversal.

## 4. Correct use, mistakes and deliberate exclusions

Coach's three uses (in source order) are **confirmation**, **momentum reading**, **confluence**. He explicitly says RSI alone is not suitable for entries.

Coach's five named mistakes: buy immediately at RSI 30; sell immediately at RSI 70; ignore market structure; ignore trend direction; use RSI alone.

Coach deliberately states he is **not discussing RSI divergence**. He recommends checking possible directional bias first, then looking for BOS, CHoCH or rejection candles. It would be inaccurate to claim RSI divergence or an exact divergence detector was supplied as a Coach trading rule. These named confirmation types are examples, not a complete Boolean gate.

The final source statement makes **price action and market structure** the priority, while RSI remains a confirmation/relative buying-selling pressure observation.

## 5. Cumulative PCSS links and unresolved operational criteria

Lesson 15 introduces RSI >50/<50 directional momentum. Lesson 16 uses HTF RSI on either side of 50 and lower-timeframe “bounces above 50” / “rejects below 50”, but does not define exact crossing, touch, hold, retracement or bar-count rules. This Lesson 17 supplies a usual RSI **length 14** and overbought/oversold reference lines, but **does not solve those event semantics** or define EMA length.

Lesson 13's 4H screenshot RSI≈63.88 is numerically **below** overbought reference 70 despite Coach's qualitative “near overbought” description. Do not silently redefine 63.88 as satisfying RSI >70.

**Independent design direction:** Treat RSI midpoint bias, extreme state and candle-confirmation state separately. Preserve HTF/LTF disagreement, data timestamps and source/independent provenance; never manufacture a numerical signal-confidence percentage.

TradingView [repainting documentation](https://www.tradingview.com/pine-script-docs/concepts/repainting/) confirms that RSI on open realtime candles can change; HTF requests also need careful confirmed-data selection. Source data from unfinished HTF candles must not be presented as past-confirmed observations.

## 6. Ponder: open questions and falsifiability

Unresolved research: exact price input, smoothing seed, equality at 30/50/70, precise meaning of bounce/rejection, timeframe choice, overbought-duration interpretation, whether divergence is a useful *independent* addition, and incremental explanatory/predictive value over market-structure and confirmation-only baselines. None of those enhancements is validated or authorized as executable rules.

See [independent RSI candidates](../research/17-rsi-state-momentum-candidates.md), which keeps the intended Coach/source distinctions and lists disconfirming fixture ideas.

**Coverage verdict:** All 21 original source units audited in order; no figure or original numerical worked example was present. RSI mathematical explanation and synthetic numbers labeled independently. **Lesson 17 COMPLETE as PCSS study; zero Pine scripts/backtests.** Next: **Lesson 18 — EMA**, beginning on original PDF page 23, only when owner asks to proceed.
