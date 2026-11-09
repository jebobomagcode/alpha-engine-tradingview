# Lesson 16 — Long/Short Continuation: Research Specification Candidates

**OPEN RESEARCH, not executable Coach specification, no Pine/chart tests/backtests/trading**. 2026-11-09 (Asia/Manila). Coach sole source [PDF p21](../../sources/coach%20trading%20lessons.pdf); full [PCSS Lesson 16](../lessons/16-long-short-setup.md). Owner's market focus: crypto, separate venue-qualified XAUUSDT, XAUTUSDT and PAXGUSDT feeds. Older repositories out of scope.

## Fixed source distinctions

LONG HTF: bullish structure + price above EMA + RSI above 50. LONG LTF: retraces to EMA/FVG + RSI bounces above 50 + bullish rejection candle. Output “continuation longorbuy”.

SHORT HTF: bearish structure + price below EMA + RSI below 50. SHORT LTF: retraces to EMA resistance + RSI rejects below 50 + bearish confirmation candle. Output “continuation short”.

Text says *example* not a documented exhaustive strategy. There is no exact indicator period, cross rule, required event-time sequence, explicit AND/OR syntax for EMA/FVG, entry price, SL/TP, timeframe pair or empirical performance.

## A. Three candidate representations

**M0 qualitative source dashboard:** show the six listed observations and unknowns independently, not machine trade labels. Highest fidelity to ambiguity but manual interpretation.

**M1 minimal baseline:** structural direction + relevant known location + closed directional candle confirmation; show EMA and RSI as non-mandatory context. Simpler, preserves Lesson 08 reasoning but is a separately declared research baseline, not identical to Lesson 16.

**M2 explicit six-gate continuation candidate:** require valid HTF structure, HTF EMA side, HTF RSI side, LTF contact, LTF RSI event and candle confirmation, with all time, expiry and geometry fixed. More reproducible but user/independent numerical decisions required; may reduce opportunities with no proven performance benefit. A distinct countertrend/range mode remains available as source-cited alternatives from Lessons 13 and 10.

No model is selected as final indicator or strategy. Compare with predeclared tests.

## B. Alternative RSI midpoint behavior definitions

LONG:
- CROSS_ABOVE: RSI previous completed <=50 and current completed >50.
- HOLD_ABOVE_BOUNCE: remains >50 but approaches to a predeclared tolerance and then rises.
- TEMP_DIP_RECOVER: goes below then returns above within N completed bars.
- RISING_ABOVE: RSI >50 and increasing for K bars.

SHORT:
- TEST_REJECT_BELOW: approaches 50 from below and turns lower, never exceeds midpoint.
- FAILED_ABOVE_RECLAIM: moves above 50 then returns below.
- CROSS_BELOW: previous >=50, current <50.
- FALLING_BELOW: RSI stays <50 and declines, without touching 50.

All are **independent hypotheses**, not the source's formal definitions. Distinguish RSI=50 equality, forming candles and missing/under-warmed RSI series. If RSI period unknown, source exact calculation is undefined.

## C. EMA/FVG location policies

LONG source “EMA/FVG” can mean:
- either EMA or FVG qualifies,
- both must overlap,
- both are context and user interprets,
- EMA primary, FVG optional.

SHORT source only specifies EMA resistance. Symmetric short FVG should be marked independent or sourced from a different specific Coach lesson, NOT falsely read from p21.

EMA is dynamic; contact alternatives include wick touch, body overlap, close cross, positive tick/ATR tolerance, or bounce/rejection after crossing. FVG requires a separately specified three-candle or alternative geometry; current page gives none. No parameter selection is Coach-prescribed here.

## D. Time-causal evidence fields

For each observation track:
- exchange-qualified symbol/product, timezone, HTF and LTF, bar IDs and close timestamps;
- swing origin and prior confirmation time; source HTF structure as-of moment;
- EMA period/source/warmup and RSI length, source and completed values;
- EMA/FVG touch interval and detection timing;
- RSI event classification, first/bounce/rejection bar and timeout;
- confirmation candle geometry, completion time, trigger policy and invalidation state;
- final status WAIT/CONFLICT/INSUFFICIENT/RESEARCH_CANDIDATE, never invented fill or fixed RR.

HTF values from a developing bar can change; TradingView docs describe confirmed HTF requests with offset plus lookahead_on; chart-timeframe barstate.isconfirmed is not a substitute inside request.security. External references:
https://www.tradingview.com/pine-script-docs/concepts/repainting/
https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/
https://www.tradingview.com/pine-script-docs/concepts/bar-states/

## E. Discriminating synthetic fixtures — NOT EXECUTED

1. HTF bullish structure, close above EMA, RSI 56, LTF EMA touch, RSI 47->52 and bullish rejection: passes CROSS_ABOVE variant; literal Coach bounce equivalence unproven.
2. LTF RSI 54->50.5->53 passes HOLD_ABOVE_BOUNCE but not CROSS_ABOVE.
3. HTF bearish and LTF RSI 46->49->44 passes TEST_REJECT_BELOW but not CROSS_BELOW.
4. LTF RSI 48->52->47 illustrates FAILED_ABOVE_RECLAIM; may not satisfy a strict never-above-50 rule.
5. Price reaches FVG but not EMA: OR and AND interpretations differ.
6. Price reaches EMA but no FVG: optional and mandatory overlap interpretations differ.
7. Short EMA not reached, short FVG touched: do not mark faithful to p21 SHORT example.
8. HTF HH/HL but close below EMA and RSI 44: conflict, do not force a universal signal.
9. HTF RSI >50 forming, closes <50: no confirmed prior bullish momentum.
10. LTF candle initially bullish rejection but closes bearish: provisional event invalidated.
11. RSI exactly 50: neither literal strict greater nor less comparison holds; equality open.
12. Swing is confirmed later than apparent historical LTF contact: prohibit backdated signal.
13. Old EMA touch, RSI bounce many bars later: timeout threshold required, source silent.
14. EMA-derived trend and HH/HL/RSI all agree on same price trend: correlated evidence, not independent probabilities.
15. Lesson 13 4H bullish plus lower-timeframe bearish scalp opportunity: maintain countertrend source mode distinct from p21 continuation example.
16. Missing stop, target and exact trigger: RR unknown, no order claim.
17. Switching between XAUUSDT gold derivative and XAUTUSDT/PAXGUSDT token products: require fresh levels/fees and no cross-feed copying.

## F. Ponder research direction

Preserve source-observation dashboard (M0) and simple structural baseline (M1); later test M2 only after exact parameters are independently formalized. Evaluate event frequency, confirmation lag, signal ambiguity, missing data, repeatability under Pine reload, false positives, sample selection and *out-of-sample after-fee* outcomes. Higher complexity is not presumed to improve performance.

**Next source:** Lesson 17 — RSI, PDF p22, user-directed only. No code or backtest authorized.
