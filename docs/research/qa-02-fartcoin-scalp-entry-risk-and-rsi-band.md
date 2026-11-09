# Q&A 02 — FARTCOIN Scalp: Independent Timing, Stop Geometry and RSI Band Research

**Status:** OPEN PROPOSED RESEARCH, not implemented, backtested, deployed or confirmed with actual exchange price candles. 2026-11-09 Asia/Manila.
**Source of Coach claims:** [original PDF page31](../../sources/coach%20trading%20lessons.pdf), [PCSS full source audit](../lessons/qa-02-fartcoin-scalp-pullback.md). **Original page is text-only; there is NO supplied FARTCOIN screenshot**, despite an earlier mistaken coverage label referring to a FART chart.

## 1. Fixed, source-grounded observations

**Student reports existing LONG:** FARTCOIN (exchange/quote/product unknown), 1H two red candles rejected support then a solid green candle, E=0.2436, S=0.2385, scalping. Requests TP.

**Coach qualitative response:** “mas healthy yan for scalp continuation”; “below supp and liquidity zone” phrase without the referenced drawing; alternative preferred WAIT for E range 0.238–0.240, confirmation bullish engulfing or rejection wick and RSI bounce 40–50, price above EMA50, S strictly <0.231, TP 0.258–0.279 with trailing stop; patience and price coming to entry zone. **30m OB main zone, 5m for entry confirmation**.

No chart/OHLC, filled-order evidence, venue, exact stop placement, indicator period/timeframe for EMA or RSI, realized PnL or statistical evidence. Different source statements should not be mashed into one certified trade.

## 2. Critical new RSI research direction

Earlier Lesson16 bullish continuation says RSI bounces **above 50**, whereas p31 Coach's scalp pullback says RSI bounce **40–50**. These contexts differ, and source text does not formally specify that all long entries require RSI>50.

Candidate *independent* event definitions:
- BAND_TOUCH_RECOVER: RSI enters 40–50, reaches a local minimum, then rises with a completed bar (possibly still <50);
- BAND_RECLAIM_50: RSI dips into 40–50, then returns above50 by confirmed bar;
- BAND_REJECTION_LOW: reaches near 40 from above and holds above40 before recovering;
- PRICE_CANDLE_CONFIRMATION_ONLY: RSI reported as descriptive context, not a hard gate.

Source does not choose a single event definition, window N, oscillator price source, smoothing, tolerance, or exact bar close. Never label these as Coach-certified numeric algorithms. Research should compare signal populations and avoid hindsight using future local minima.

## 3. Existing position and new candidate are different tasks

**Existing-position assessment:** source reports E=0.2436, S=0.2385 and no actual position quantity/order receipt. Original question is “where TP?”, but Coach's response pivots to his separate entry plan. Do not assume Coach explicitly ordered stop modification or instructed exit and re-entry.

**New pullback candidate:** source describes E range 0.238–0.240 *only if price returns and qualifying reaction occurs*. This setup may never appear; no automatic limit buy. A stop <0.231 may lie below another separately unverified 30m OB reference; no source chart to confirm.

## 4. Independently verified arithmetic

Student: price risk 0.2436−0.2385=**0.0051**, stop movement ~**2.093596%** of entry. If independently applying Coach's targets only as an illustrative comparison:
- T0.258: price reward0.0144, gross RR **2.823529:1**;
- T0.279: price reward0.0354, gross RR **6.941176:1**.

Coach's text has stop **strictly below0.231**, so RR is **not unique**. For one hypothetical valid S=0.230:
- E0.238,T0.258: risk0.008, reward0.020, RR **2.5:1**.
- E0.240,T0.258: risk0.010, reward0.018, RR **1.8:1**.
- E0.238,T0.279: risk0.008, reward0.041, RR **5.125:1**.
- E0.240,T0.279: risk0.010, reward0.039, RR **3.9:1**.

Coach's proposed entry is 0.0036–0.0056 below student entry, approximately **1.48–2.30%** relative to student E. Under S0.230, Coach's stop distance is **0.008–0.010** per unit, wider than student's 0.0051, with nominal movement to stop 3.36%–4.17% versus student's 2.09%. This does not prove either is higher expectancy or safer; it illustrates a valid counterexample to "lower entry means higher RR."

Formula for linear long gross RR=(T−E)/(E−S) and percent price stop (E−S)/E; actual account risk additionally needs quote currency, position size, leverage exposure, margin mode, bid/ask spread, fees, possible slippage, funding and fill policy.

## 5. Alternative research models

**M0 source-context assistant:** show student’s *reported* trade separately from Coach’s preferred wait-for-pullback idea. Show all price/zone/timeframe uncertainty, no machine label or order. Highest source fidelity, non-automated.

**M1 minimal zone+candle reaction:** select venue-qualified asset, confirmed 30m OB region using independently declared geometry, 5m completed bullish engulf/rejection after contact, stop selected by explicit risk policy; 1H bias and RSI/EMA context displayed. Simple, but multiple unsourced parameters remain.

**M2 RSI-band + EMA gate:** add chosen precise 40–50 bounce semantics and selected EMA50 timeframe/price source; more selective, but may exclude valid Coach discretionary interpretations, lag and overfit.

**M3 multitimeframe structural risk model:** independent 1H structural regime, 30m zone, 5m micro confirmation, trade invalidation distinct from 30m OB and HTF bias, risk per fixed capital and cost estimate. Richer but higher complexity and false confidence from correlated price signals.

Research preference: first M0 + M1, then use M2 as falsifiable enhancement. No implementation chosen.

## 6. Causal and correctness requirements, future-only

- Exchange-qualified symbol, spot/perpetual product, ticker decimals/tick size, OHLC source history and timezone.
- 1H student support-rejection claim is not an image-confirmed observation; if needed source/audit tag STUDENT_ASSERTION.
- 30m OB must have independently declared pivot/displacement/last-opposite-candle logic and formation/known-at time, not a static future-selected rectangle.
- 5m wick and bullish candle confirmation must identify completed/provisional bar state and relationship to known 30m zone.
- 5m RSI bounce within 40–50 vs crossing50 requires separate hypothesis IDs and explicit lookback/expiry; no future local minima leaked into past.
- The source's EMA50 timeframe unspecified; do not silently assume 5m from adjacency in prose.
- Actual source text says “SL below 0.231” not at0.231, and trail stop mechanics unknown.
- Protect against live versus historical HTF/MTF lookahead/repainting. Official external:
  https://www.tradingview.com/pine-script-docs/concepts/repainting/
  https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/

## 7. Planned falsification tests — none executed on market prices

1. Student E0.2436 and S0.2385: absolute distance0.0051, percentage2.093596.
2. Comparison with Coach E0.238–0.240, sample S0.230: lower entry yet larger stop and possibly lower RR.
3. RSI 47→49 after prior dip: satisfies some band-bounce definitions but not strict cross above50.
4. RSI 44→52: passes reclaims-above50 variant; both may be observed after bounce.
5. RSI 39→45: entered band from below without prior above-band test; require explicit temporal syntax.
6. RSI 52→49→47→50.5: crossing and local minima known only after later bar; no backdating.
7. Price returns to 0.239 but no qualifying bullish candle: WAIT.
8. 5m bullish engulf intrabar becomes bearish at close: reject confirmed-candle classification.
9. EMA50 below current price on 1H but above on 5m: timeframe conflict, no fabricated one-state rule.
10. 30m OB computed retrospectively after 5m bounce: reject historical eligibility.
11. A lower wick touches zone and immediately rebounds without full body contact: geometry variants differ.
12. Student already long with no fill receipt: no claim that a particular exit or TP was realized.
13. Support/liquidity commentary “below supp” ambiguous: don't assign exact support line.
14. Student tight S0.2385 is crossed temporarily, then price rallies: higher nominal RR not proof better execution.
15. Missing tick/fees/funding: do not claim gross RR is net RR.
16. Price never falls to Coach desired area: source permits no new entry rather than forced buy.
17. Trailing stop might capture less/more than planned terminal TP; activation/offset required.
18. FARTCOIN product differences or later crypto gold products: never transfer level units between unrelated feeds.
19. Price closes above EMA50 while RSI remains around43: discretionary acceptance unknown; keep conflict visible.
20. Backtest structure+30m OB+5m candle vs RSI-band + EMA gating with held-out samples: improvement may vanish after costs.

**No synthetic Pine fixtures, historical market execution or strategy backtest have been run.** The arithmetic is checked, but the trading edge is unverified.

## 8. Ponder recommendation and next source

Preserve the **two different questions** (student already in position versus Coach future opportunity) as separate evidence objects. An indicator should prioritize explicit zone status and 5m confirmation evidence, with RSI-bounce-in-40–50 clearly labeled as a candidate rule rather than an assumed universal RSI>50 requirement. Track dynamic stop placement and quantity separately.

**Next on user instruction:** Q&A activity no.3 original PDF p32 (4H to 15m BTC; compare student 1:2 RR claim against arithmetic), then original note p33 and BSP section pp34–35. Whole PDF remains incomplete until those units are studied.
