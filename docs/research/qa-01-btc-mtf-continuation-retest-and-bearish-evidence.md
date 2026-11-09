# Q&A 01 — BTCUSD 4H/15m Evidence, EMA Retest and Conditional Bias Research

**OPEN INDEPENDENT RESEARCH ONLY; no code, signals, historical backtests, orders, deployment or market performance evidence.** 2026-11-09 Asia/Manila. Sole Coach source: [original PDF pp29–30](../../sources/coach%20trading%20lessons.pdf), [PCSS QA1 study](../lessons/qa-01-btc-htf-bias-and-confirmation.md).
Market identity **BTCUSD (source)**, not assumed BTCUSDT; future crypto implementation may include exchange-specific BTCUSDT, ETHUSDT and distinct XAUUSDT, XAUTUSDT, PAXGUSDT, always separate provider/product and candles.

## A. Three levels of evidence that must not be collapsed

**Observed on original screenshot p29 left (4H):** BTCUSD price~82,446; EMA20~80,596; EMA50~79,175; EMA100~77,804; EMA200~75,783; RSI14~69.91, yellow RSI smoother~65.86; strong upward pattern. No BOS label or selected swing reference.
**Observed on original screenshot p29 right (15m):** BTCUSD price~82,427; EMA20~82,103; EMA50~81,758; EMA100~81,447; EMA200~80,899; RSI14~63.10; yellow smoother~67.95; pullback candles after upward burst. Not evidence that 4H trend has reversed.
**Student/Coach text p30:** student says “May BOS”, EMA respected, trending/bullish, continuation and wait for retest/confirmation; Coach agrees and says continuation probability exceeds reversal *unless strong bearish confirmation*. Neither gives a quantified posterior probability, stop, target, entry or trade outcome.

A visual upward trend does not independently verify an objective structural BOS unless eligible pivot levels and breakout timing are specified.

## B. Important threshold and typo distinctions

4H RSI69.91 is above50, but **strictly below70** by 0.09; student says “near overbought”, not necessarily already overbought. 15m RSI63.10 is above50 but below70; yellow smoother ~67.95 sits above current 15m RSI. These do not create opposing trend states by themselves.

Student types “red line ema2” while chart indicator explicitly “EMA20/50/100/200”. Treat as likely missing zero *with source note*, do not rewrite source or claim EMA2 configuration.

The two screenshots have device time 8:24 but no verified candle-close alignment, year or complete OHLC; no certainty about simultaneous values or exact post-capture outcome.

## C. Distinct alternative causal models (not Coach mandated logic)

M0: Discretionary Coach context dashboard, independent labels for HTF bias, price-versus-EMA, 4H RSI, 15m momentum/retest and waiting state, no automatic order. Transparent but subjective swing labels.

M1: Minimal structural baseline: previously confirmed 4H trend, identifiable HTF/LTF support area, subsequent 15m completed bullish candle. EMA/RSI descriptive, no invented all-EMA eligibility requirement. Lowest complexity.

M2: EMA-respect explicit event: define EMA period, retest tolerance and wick-vs-close touch, subsequent confirmation candle, last-valid time, with separate strong bearish disconfirmation rules (confirmed pivot break/CHoCH or specific bearish reversal event). More reproducible but unapproved numerical choices and false signal risk.

M3: Multi-EMA + RSI gating/scoring, potentially filtering out countertrend/range scenarios and double-counting correlated price-derived indicators. Needs ablation and out-of-sample evaluation, not presumed better.

**Study-stage preference:** M0 plus M1 as falsifiable baseline; M2 only after exact event grammar selected; M3 only with incremental out-of-sample value beyond M1. No executable method chosen.

## D. Potential strong bearish confirmation: hypotheses, not source definitions

- 4H bearish CHoCH after a previously known 4H HL break; later bearish BOS optional (source Lesson20 prior structure).
- A closed rejection/engulfing bearish candle at a previously defined resistance level.
- Loss of meaningful support/EMA followed by a failed retest or lower-timeframe bearish continuation.
- RSI below50 might support bearish momentum on its own timeframe, but cannot alone supply “strong bearish confirmation”, especially while 4H structure remains bullish.

No single one is specified by Coach p30 as the mandatory “unless” condition. Any future threshold or event must be tagged INDEPENDENT_HYPOTHESIS and empirically evaluated.

## E. Falsification test plan, NOT EXECUTED

1. 4H close > EMA20>EMA50>EMA100>EMA200 and RSI69.91: bullish context, not >70 overbought.
2. 15m RSI63.10 but falling, price above EMAs: bullish-side momentum yet LTF pullback, not automatically short.
3. 4H bullish and no retest yet: WAIT, not instant buy.
4. Retest reached but no completed bullish candle: WAIT.
5. A green 15m candle during formation closes red: do not backdate confirmed continuation.
6. Current price above same close-based EMA and EMA one-bar upward are algebraically identical, not two independent votes.
7. Student “May BOS” without identified previous high: BOS unverified relative to a mechanical swing detector.
8. Student typed ema2; screenshot says EMA20: data conflict explicit, not EMA2 strategy.
9. 4H RSI 70 exactly versus 69.91: strict >70 threshold differs.
10. Same BTCUSD ticker traded on another venue or BTCUSDT pair: no casual carryover of EMA levels.
11. 4H HTF pivot confirmed only after earlier 15m retest: no hindsight structural confirmation.
12. Bearish 15m candle after peak but no 4H CHoCH: local pullback can coexist with HTF UP.
13. New confirmed 4H bearish structural shift: should trigger reassessment under explicit independently selected rule.
14. No selected timeframe or instrument feed: INSUFFICIENT.
15. Coach probability phrasing without a measured sample: cannot translate to 60%,70%,80% or fixed odds.
16. Student claims EMA respected but image shows one recent EMA touch or no obvious retest: distinguish actual touch evidence from EMA below price.
17. Multiple EMA alignment and RSI confluence from one price trend: do not assume statistical independence.
18. 15m RSI recovery above50 after retest, yet no stop/target: signal candidate cannot be called a fully risk-defined executable strategy.
19. Chart screenshot no visible date year or exchange: cannot reconstruct an exact time-series test fixture from these images.
20. Risk/commission/slippage missing: no after-cost expectancy claim.

## F. Ponder conclusion and next source

The distinctive practical lesson is conditional probability reasoning: bullish HTF and EMA-respect support continuation interpretation, **but bearish evidence could invalidate it**, while confirmation remains pending at the actual LTF entry location. The original case illustrates WAIT even when bullish. Future engine should report both *reason for bullish context* and *what new evidence would challenge it*.

Nothing here proves a success rate or creates Coach-certified numeric thresholds. Full source coverage still requires Q&A02 p31, Q&A03 p32, Important Note p33, and BSP charting pp34–35. Next only on user instruction: **Q&A activity no.2**.
