# Lesson 21 — Multi-Timeframe Historical Case, Provenance, RR and Validation Alternatives

**OPEN INDEPENDENT RESEARCH; no Pine, TradingView runtime, real-market backtest, order or deployment.** Original Coach-only source [PDF pp26–28](../../sources/coach%20trading%20lessons.pdf); [Lesson21 PCSS](../lessons/21-tonusdt-topdown-setup.md). Crypto-focused new project. Historical example is not a current signal.

## 1. Evidence hierarchy and the critical cross-asset ambiguity

**Screenshot observed:** Two TON/TetherUS 4H images at ~2.731/2.736; left EMA20/50/100/200 and RSI14 ~97.45, right Auto Fib Retracement 3 10 and RSI14 ~97.46. Neither image confirms 1H RSI79/BOS 2.48/2.60 nor 15m zones, nor dates/exchange or realized trade.
**Coach written assessment:** 4H bullish HH/HL above four EMAs; 1H bullish BOS with no confirmed bearish CHoCH, RSI79, EMA20 2.40–2.45, EMA50 2.14.
**Ambiguous asset wording:** “Yung sa fart sir 15m” before 15m section could refer to another token. Price scale alone cannot resolve symbol attribution. Do not assign TON or FARTCOIN as independently verified. Mark SOURCE_ASSET_UNVERIFIED.
**15m/zone claims:** FVG [2.58,2.62], [2.48,2.52], [2.38,2.44], OB [2.45,2.50], support/resistance and conditional trade plan are Coach textual observations with no supplied 15m OHLC.

## 2. Source-faithful interpretation, not predictive validation

Coach teaches: strongly bullish trend with extreme RSI is not a signal to chase. Wait for pullback at previously relevant support/FVG/OB, then a bullish engulfing or rejection candle; entry region [2.58,2.62], stop **strictly below 2.52**, targets ~2.75–3.00 with trailing stop. No selected stop price, actual trailing mechanism, order type, quantity, fees, contract size, executed result or win rate.

A source screenshot captured near a dramatic positive move is vulnerable to *selection bias* if incorrectly presented as an unbiased signal sample. No later outcome given. It cannot be used to claim a proven trading edge.

## 3. Independent risk arithmetic and interval conflicts

For hypothetical S=2.51 (NOT Coach's specified level), sample gross RR:
- E=2.58,T=2.75: (2.75−2.58)/(2.58−2.51)=0.17/0.07≈2.43.
- E=2.62,T=2.75: 0.13/0.11≈1.18.
- E=2.58,T=3.00: 0.42/0.07=6.
- E=2.62,T=3.00: 0.38/0.11≈3.45.
Exact RR remains unknown because S can be any valid stop strictly below 2.52 and actual targets/trail differ.

Overlaps: middle FVG [2.48,2.52] and bullish OB [2.45,2.50] intersect [2.48,2.50]; lower FVG [2.38,2.44] and stronger support [2.38,2.40] intersect [2.38,2.40]. These may be correlated representations of the same structure, not separate independent evidence votes.

**Crucial trade-vs-structure distinction:** upper entry-zone stop <2.52 can fire while lower 2.45–2.50 and 2.38–2.40 supports remain untested. Reject the false inference that stopped upper-zone LONG = confirmed global downtrend.

## 4. Candidate research representations — none authorized as code

M0: preserve source screenshot and source commentary fields with labels SCREENSHOT_OBSERVED, COACH_ASSERTED, UNKNOWN_ASSET; manual education dashboard only.
M1: minimal time-causal model: venue-qualified instrument, confirmed 4H structure, one documented zone contact, completed LTF confirmation, WAIT/INSUFFICIENT otherwise. EMA/RSI reported separately.
M2: strict confluence: define RSI bounce, EMA periods, FVG/OB geometry, CHoCH/BOS pivots, verified 1H/15m timestamps, risk and alert expiry. These numeric rules are independent enhancements, not supplied by p26–28.
M3: multi-zone setup context: distinguish upper FVG trade status from lower OB/FVG and HTF regime state, with explicit invalidation. More informative but more complex.

Preference: source-qualified M0 and M1 first. Evaluate M2/M3 only after full source Q&A/notes and on independent market data.

## 5. Planned falsification cases — none executed

1. Both PDF charts are 4H even though title says 4H/1H: refuse visually verified 1H claims.
2. Unknown 15m ticker after “fart sir”: label source asset unresolved.
3. 4H RSI97 in developing bar later closes lower: distinguish provisional/confirmed.
4. 4H bullish with 1H bearish CHoCH after screenshot: don't backdate reversal.
5. 1H text EMA20 2.40–2.45 versus 4H EMA prices near 1.993 etc: correct timeframe separation.
6. Auto Fib screenshot shading at older price base cannot prove 2.45–2.50 Fib + OB match.
7. Price reaches FVG2.58–2.62 with no bullish engulf/rejection: WAIT.
8. Bullish engulf printed before retracement: not source-sequenced entry.
9. Price never retraces: WAIT remains valid, no automatic LONG.
10. Stop 2.51 triggers before OB2.45–2.50, preserving potential deeper bullish context.
11. Target2.75 with entry2.62 and S2.51 gross RR1.18, not fixed 2:1.
12. Trailing stop may realize less than stated target; execution parameters missing.
13. Different market feed TONUSDT spot/perpetual or XAUUSDT vs XAUTUSDT/PAXGUSDT: no reused candles.
14. No confirmed pivot when BOS/CHoCH marker drawn: prevent history backdating.
15. Missing full OHLC, exchange or date: no authentic empirical reproductions from screenshot.
16. Indicators EMA, RSI, FVG and OB derived from overlapping price swings: do not multiply confidence scores.
17. Representative winning chart selection can overstate edge; require unbiased chronological holdouts.
18. Price opens through stop level with a gap: stop price not guaranteed fill.
19. Mark support/resistance from source as historical, not current live zones.
20. Causality: HTF value known time must precede entry opportunity; distinguish 4H/1H/15m observations at nonmatching close times.

Official external implementation research: https://www.tradingview.com/pine-script-docs/concepts/repainting/ and https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/ .

## 6. Ponder conclusion and handoff

Strongest source-grounded takeaway is **WAIT until location plus confirmation**, not RSI/EMA automatic order. Keep source ambiguity and potentially contradictory timeframes visible rather than inventing perfect hindsight confluence. Source contains no successful actual order, fixed stop, RR or probabilistic edge.

All **21 numbered lessons complete**; **Q&A1 pp29–30, Q&A2 p31, Q&A3 p32, location/time p33, and BSP pp34–35 remain**. Next requested continuation must begin at Q&A1, not implementation. No Pine code or previous repository modification.
