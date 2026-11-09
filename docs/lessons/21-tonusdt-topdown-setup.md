# PCSS Lesson 21 — 4H/1H Chart Setup with BOS, CHoCH, RSI, EMA, FVG and OB

**Completed as original-source PCSS study and research, NOT Pine implementation, backtest, deployment or live trading.** 2026-11-09, Asia/Manila.
**Coach's sole source:** [original PDF pages 26–28](../../sources/coach%20trading%20lessons.pdf); SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. Original private PCSS file SHA-256 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56, personal file not published.
**Independent project:** crypto TradingView, XAUUSDT, XAUTUSDT, PAXGUSDT separate by venue/product; prior projects untouched.

## Full page and figure inventory

Original **p26** has two mobile TradingView TON/TetherUS screenshots side by side (BOTH marked 4H) and three 4H structural remarks. **p27** has 4H EMA/RSI remarks, a separate written 1H assessment, an ambiguous 15m reference, proposed zones and entry. **p28** contains stop, target, trailing-stop and wait conclusion. **p29** starts Q&A1, a new source unit. The two 4H images were inspected enlarged and compared with all native PDF text. No underlying historical OHLC dataset, 1H screenshot, 15m screenshot, actual trade fill, calendar date, quantified win rate, formula or assigned calculation is supplied.

| ID | Original item in order | Audit observation |
|---|---|---|
| 21-01 | p26 heading, 4H/1H setup using BOS, CHoCH, RSI, EMA, FVG and OB | Title is an illustrative chart case, not a backtest |
| 21-02 | p26 screenshot 1, TON/TetherUS 4H, EMA20/50/100/200, RSI14, volume | Image-observed ~2.731 price and RSI97.45 |
| 21-03 | p26 screenshot 2, TON/TetherUS 4H, Auto Fib Retracement 3 10, RSI14 | Image-observed ~2.736 price and RSI97.46; auto-Fib bands do not verify later OB+Fib levels |
| 21-04 | p26 4H strong bullish market structure | Coach qualitative assessment |
| 21-05 | p26 higher highs and higher lows | Exact eligible pivots not provided |
| 21-06 | p26 no major break of structure | Major and direction of break undefined |
| 21-07 | p27 price above EMA20/50/100/200 | Four source-named EMA periods |
| 21-08 | p27 interpreted very bullish | Source directional judgement |
| 21-09 | p27 RSI around 97 extremely overbought | Source near screenshot RSI97.45 |
| 21-10 | p27 trend very strong but chasing risky; high chance pullback | No probability supplied |
| 21-11 | p27 section: on the 1H | Only text supplied, no 1H screenshot |
| 21-12 | p27 1H continuation after consolidation | Coach assertion |
| 21-13 | p27 several bullish BOS | Coach assertion without 1H structure chart |
| 21-14 | p27 break above 2.48 | Textual level |
| 21-15 | p27 break above 2.60 | Textual level |
| 21-16 | p27 continuation toward 2.73+ | Textual level |
| 21-17 | p27 no confirmed bearish CHoCH yet | Time/pivot rule unknown |
| 21-18 | p27 1H RSI around 79 still bullish | Unverified by provided 4H images |
| 21-19 | p27 EMA20 respected as dynamic support | Source statement |
| 21-20 | p27 EMA20 support 2.40–2.45 | Historical level; timeframe matters |
| 21-21 | p27 EMA50 support 2.14 | Historical level |
| 21-22 | p27 Yung sa fart sir / 15m | Ambiguous asset reference; no 15m screenshot |
| 21-23 | p27 FVG 2.58–2.62 | No OHLC geometry to verify |
| 21-24 | p27 FVG 2.48–2.52 | No OHLC geometry to verify |
| 21-25 | p27 FVG 2.38–2.44 | No OHLC geometry to verify |
| 21-26 | p27 possible retracement zones | Not guaranteed support |
| 21-27 | p27 bullish OB 2.45–2.50 | Candles not provided |
| 21-28 | p27 resistance 2.75 psychological | Coach category |
| 21-29 | p27 resistance 2.80 possible rejection | Coach category |
| 21-30 | p27 resistance 3.00 major psychological | Coach category |
| 21-31 | p27 support 2.65 minor | Coach category |
| 21-32 | p27 support 2.58–2.62 FVG | Coach category |
| 21-33 | p27 support 2.45–2.50 OB+Fib | Textual claim; chart does not validate same retracement anchors |
| 21-34 | p27 support 2.38–2.40 stronger | Coach category |
| 21-35 | p27 safe to wait for pullback | Behavioral instruction |
| 21-36 | p27 entry around 2.58–2.62 | Conditional candidate, not fill |
| 21-37 | p27 bullish engulfing or strong rejection wick | Confirmation sought; no precise pattern specification |
| 21-38 | p28 stop-loss strictly below 2.52 | No exact price/buffer |
| 21-39 | p28 take profit 2.75 up to 3, trailing stop | Trailing activation and distance undefined |
| 21-40 | p28 very bullish near top: best action WAIT for support/FVG/OB pullback before LONG | Original final decision |

**Audit:** 40 source-ordered items, including both embedded screenshots and every numerical region. No figure or source numerical detail skipped. Image-only text and narrative claims remain separately attributed; inventory completeness is page-limited.

## 1. Source images: what is visible, and what is not

**Left screenshot (p26)**: TON / TetherUS, 4H, EMA 20/50/100/200, TON volume, RSI 14 close. Approximate visible price 2.731 (+11.29%). RSI purple value approximately 97.45; yellow RSI-related line about 93.92. Four visible moving-average price tags roughly 1.993, 1.680, 1.525, 1.430. Although indicator name lists four periods, screenshot does not independently verify each colored tag-period mapping through settings.

**Right screenshot (p26)**: TON / TetherUS, 4H, Auto Fib Retracement 3 10, RSI 14 close. Approximate price 2.736 (+11.62%), RSI 97.46 and yellow line around 93.92. Colored auto-Fibonacci regions at an older price base roughly 1.3–1.6 are visible. No selected swing anchors or custom Lesson14 manual 0.618–0.705 rule are demonstrated. This image does not verify Coach's later textual 2.45–2.50 OB + Fib confluence.

**Crucial boundary:** BOTH screenshots are 4H. Neither displays the stated 1H RSI around79, precise 1H BOS levels, nor a 15m FVG/OB. No venue-qualified exchange metadata or unambiguous date is supplied. Do not assert all observations were simultaneous or actually tradable in real time.

## 2. 4H context — Coach first

**COACH EXPLICIT:** Overall market structure strong bullish, higher highs / higher lows, “walang major break of structure”. Price is above EMA20/50/100/200; Coach calls it “very bullish”. RSI around 97, extremely overbought. Trend strong but chasing a high entry is risky; Coach thinks a pullback has a high chance before continuation.

**PCSS interpretation:** Source wording “no major break” may mean no opposing major invalidation, but does not formally specify protected swing, BOS threshold or direction. The explicit EMA100 is an important new case-specific input (earlier Lesson18 mentioned common 20/50/200). RSI>70 is NOT automatic SELL (Lesson17), and a very high reading is NOT an evidenced statistical probability of future pullback. Source screenshot shows price substantially above the four displayed moving averages, but chart color mapping and exact bar completion cannot be confirmed.

## 3. 1H written assessment — not independently screenshot-verified

**COACH EXPLICIT:** 1H remains bullish because recent candles continue after consolidation. Several bullish BOS:
- price breaks above 2.48;
- price breaks above 2.60;
- continuation toward 2.73+.
Coach says “No confirmed bearish CHoCH yet”. RSI about 79; bullish momentum. Price respecting EMA20 as support; suggested EMA20 band 2.40–2.45 and EMA50 2.14.

No 1H image or underlying bar data is included. These numerical/structural statements are author commentary only, not separately inspected 1H chart readings. The 4H EMA values in p26 naturally differ from the claimed 1H EMA support values because timeframes and sample histories differ. Lesson20 CHoCH definition remains qualitative; no objective pivot/close rule is supplied here.

## 4. Lower-timeframe content and unresolved asset reference

The source's literal transitional words include **“Yung sa fart sir”** followed by **“15m”**. This could indicate a separate FARTCOIN discussion or a transcription/informal reference; the text does not unambiguously establish the 15m instrument. Do not silently assign the subsequent FVG/OB ranges to the TON screenshots or to FARTCOIN. Mark **SOURCE_ASSET_UNVERIFIED**. No corresponding 15m image or OHLC series exists in this lesson.

**Coach FVG levels:** [2.58,2.62], [2.48,2.52], [2.38,2.44]. These are *possible retracement zones*, not guaranteed reactions.
**Coach bullish OB:** [2.45,2.50].
**Resistance:** 2.75 psychological, 2.80 possible rejection, 3.00 major psychological.
**Support:** 2.65 minor; [2.58,2.62] FVG; [2.45,2.50] OB+Fib (not independently confirmed by screenshot); [2.38,2.40] stronger.

**Independent interval intersection:** The middle FVG [2.48,2.52] overlaps the OB [2.45,2.50] over [2.48,2.50]. The low FVG [2.38,2.44] contains the stated stronger support [2.38,2.40]. No geometric rule or originating candles establish FVG or OB validity; overlapped price-derived zones are not independent evidence votes.

## 5. Original conditional trade plan and limits

**COACH EXPLICIT:** Wait for pullback. Candidate entry zone **2.58–2.62** after a **bullish engulfing or strong rejection wick**. **Stop LOSS strictly below 2.52**, **take-profit from 2.75 until 3.00**, potentially with trailing stop. Final source conclusion: very bullish but near recent top, so best action is **WAIT** for retracement toward support/FVG/OB before considering LONG.

No actual entry, fill, stop-trigger, exact tick-buffer, leverage, size, target allocation, exit/trailing rule or profitable outcome is supplied. Exact reward/risk is **UNKNOWN**. A source screenshot price ~2.736 to entry region corresponds to about 4.24%–5.70% hypothetical retracement, not an outcome prediction.

### Independent arithmetic example, NOT Coach's selected stop

For LONG entry E and stop S<E and target T>E, gross RR=(T−E)/(E−S). Coach says S<2.52; he does NOT select exact S.

Choose synthetic S=2.51 solely for illustration (before spread/slippage/fees/funding):

| Entry E | Target T | Risk E−S | Reward T−E | Gross RR |
| ---: | ---: | ---: | ---: | ---: |
| 2.58 | 2.75 | 0.07 | 0.17 | 2.43:1 |
| 2.62 | 2.75 | 0.11 | 0.13 | 1.18:1 |
| 2.58 | 3.00 | 0.07 | 0.42 | 6.00:1 |
| 2.62 | 3.00 | 0.11 | 0.38 | 3.45:1 |

These gross ratios vary, so **no fixed 1:2 or any other RR is source-established**. A trailing stop further makes realization contingent on its unspecified rule.

### Critical independent distinction: setup versus market invalidation

A stop just below 2.52 for the upper FVG entry could trigger **before** price tests deeper proposed bullish OB [2.45,2.50] or strong support [2.38,2.40]. Hence invalidation of **this upper FVG trade** is not proof of a full 4H bearish reversal. Track trade-specific failure separately from higher-timeframe structure and unused lower zones.

## 6. Integration and verification boundary

Earlier Lessons 07/12/20: BOS continuation and CHoCH possible reversal must use previously confirmed structural swings. Lessons 14/19: dynamic area of interest and HTF-first context; actual location and later LTF confirmation distinct. Lessons 17/18: overbought RSI and price above EMA do not independently generate orders; EMA readings can be correlated with structure/RSI.

Future indicator research should record instrument/venue/product/timeframe and each observation's known-at time; 4H/1H/15m confirmed versus developing data; source screenshot versus written Coach assertions; zone formation/contact and exact candle confirmation; RR unknown until stop/entry/target and fee/contract assumptions. Never invent simultaneous historical evidence from two 4H screenshots.

**External technical documentation (not Coach):** https://www.tradingview.com/pine-script-docs/concepts/repainting/ and https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/ explain real-time changes and higher-timeframe lookahead.

For alternative hypotheses, case disconfirmations and data-integrity research see [Lesson21 research](../research/21-tonusdt-topdown-case-provenance-and-risk.md). No Pine script or empirical chart tests were executed.

**Completion:** All 21 numbered lessons now studied in original source order, but **the 35-page Coach PDF is NOT finished**. Still pending: Q&A activity 1 pp29–30, Q&A2 p31, Q&A3 p32, Important Note on Location and Time p33, BSP charting notes pp34–35. Next **Q&A activity 1**, only on owner instruction.
