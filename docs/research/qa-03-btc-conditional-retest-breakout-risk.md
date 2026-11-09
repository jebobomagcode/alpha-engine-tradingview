# Q&A03 — BTCUSD HTF Bias, Consolidation, Conditional SHORT/ LONG and Risk Hypotheses

**Status: OPEN INDEPENDENT RESEARCH ONLY; not programmed, not backtested, not deployed, and not traded.** Original Coach-source [PDF p32](../../sources/coach%20trading%20lessons.pdf), [source-audited Q&A3 PCSS](../lessons/qa-03-btc-consolidation-retest-and-breakout.md).
Market ID from images: **Bitstamp BTCUSD** (4H,1H,15m) not Binance BTCUSDT. Venue and contract cannot be silently substituted. Independent gold-linked crypto products XAUUSDT, XAUTUSDT, PAXGUSDT are separate symbols/feeds.

## A. Source contract and evidence distinctions

- Three original BTCUSD/Bitstamp screenshot panels: 4H recent bearish leg following older uptrend, 1H decline and rebound, 15m decline and consolidation, approximate last prices 79,276/79,242/79,276. **No EMA or RSI overlay**, no drawn trendline, no marked evening-star or BOS/CHoCH reference levels.
- Student interpretation: 4H downtrend using trendline, 1H big bearish candle ~79,600 possible entry, 15m evening star. Proposed SHORT 79,419 stop 79,918 target 78,423, rounded 1:2 RR.
- Coach endorses HTF directional bias but warns 15m **currently consolidates**. WAIT for BOS/CHoCH or retest/rejection before entry.
- Coach conditional SHORT near79,850 if 15m rejection wick, bearish engulf or failed breakout above79.8k; stop around80,250; target near79k or lower; trail SL.
- Coach conditional LONG on breakout with BOS 15m or 1H, OR 1H candle closing above79,850–80k. No LONG stop/target or exact filled entry.
- Coach repeats HTF bias correct / LTF consolidation WAIT phrase at end; repetition is not independent market confirmation.

## B. Verified mathematics, independent from the Coach text

Student SHORT: 79,918−79,419 = **499** USD/BTC nominal risk; 79,419−78,423 = **996** potential nominal reward; RR=996/499≈**1.995991984:1**. Claim 1:2 is correctly rounded. Price stop movement ≈**0.6283%** of entry.

Coach reference ONLY if one assumes exact E79,850 S80,250 T79,000 despite “around” source wording: risk**400**, reward**850**, gross RR=**2.125:1**, stop distance≈0.501%, target move≈1.064%.

These are gross price ratios, not after-cost PnL/account-risk metrics. No actual order fills, bid/ask spread, fees, funding, tick size, slippage, leverage or position sizing is known.

## C. Competing candidate model designs (not approved Pine)

**M0 — Source transparency dashboard:** show source-attributed HTF interpretation, LTF consolidation, and opposing conditional scenarios, with WAIT and unknown detection thresholds. Closest to Coach discretion, least automation.

**M1 — Minimal trend/location/confirmation:** require independently identified prior HTF structural bias, LTF retest of known level and closed rejection candle for SHORT; separate breakout evidence for LONG reassessment. Source-faithful direction but independently chosen event semantics.

**M2 — Explicit two-branch research state machine:** at retest near a defined resistance, candidate rejection SHORT; at confirmed 1H breakout/BOS, candidate bullish LONG. Need explicit reference band, valid period, close criteria, event timeout and mutual exclusion when forming bars disagree. Higher complexity but captures Coach's conditional reasoning.

**M3 — Regime-aware classifier:** independently quantify 15m consolidation/trending, then evaluate event types. Potential better separation, higher parameter count and overfitting risk.

Research direction M0 first and M1 baseline; test M2/M3 only if simpler explanation and results require them. Do not assume complexity improves net trading returns.

## D. Critical falsification fixtures — planned, NOT executed

1. Student E79419 S79918 T78423 => exactly 499 risk, 996 reward, RR 1.995992.
2. Coach reference E79850 S80250 T79000 => 400 risk, 850 reward, RR 2.125.
3. Student 1:2 rounded is correct; do not falsely flag as error.
4. Coach says “around”; exact RR unknown.
5. 4H screenshot shows old rise and recent decline; trend horizon matters.
6. 15m short-term consolidation while 4H bearish; no automatic SHORT.
7. Price trades >79.8k then rejects on 15m: potential wick-failure branch, not guaranteed.
8. Price briefly trades >79.85k then 1H closes below: not confirmed 1H breakout.
9. 1H closes above80k after bearish bias: potential bullish branch, independent of prior bias.
10. 1H closes between79,850 and80,000: choose explicit above-band interpretation; source range ambiguous.
11. 15m bullish BOS with no 1H BOS: source lists 15m/1H possibilities; not necessarily HTF reversal.
12. Evening star student claims without marked candles: detector cannot be calibrated to source chart.
13. 1H big red candle near79,600 without source OHLC/time: cannot confirm executable event.
14. Several potential swings imply different BOS/CHoCH; select known-at pivot before break.
15. BOS pivot confirmed after candidate entry: disallow retroactive signal.
16. Rejection wick appears on open candle then closes bullish: provisional must not become certified.
17. Resistance retest near79,850 never occurs: WAIT, not forced entry.
18. Failed breakout and bullish continuation appear on different timeframes: show conflict, not arbitrary majority.
19. Swap Bitstamp BTCUSD to Binance BTCUSDT: verify feed history, do not reuse exact levels.
20. High gross RR but no historical after-cost profitability: do not claim an edge.

Future validation needs bar-known times, source instrument identity, separate rejection/breakout triggers, closed/provisional status, representative historical windows, robust out-of-sample and cost accounting, and genuine Pine chart-reload parity testing. Source p32 establishes NONE of those numeric implementation rules.

External TradingView documentation:
https://www.tradingview.com/pine-script-docs/concepts/repainting/
https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/

## E. Ponder takeaway and handoff

**Decisive result:** Even correct bearish HTF analysis plus approximately correct 1:2 SHORT RR does not make an entry timely in the current 15m consolidation. The same resistance region yields *two conditional interpretations*: rejection SHORT or validated bullish-breakout LONG, depending on evidence. WAIT remains informative.

Next source when owner says proceed: PDF **p33 Important Note on Location and Time** (originally about forex sessions/news, not crypto rules); then BSP/Philippine stocks notes pp34–35. Entire PDF source study still incomplete. No coding.
