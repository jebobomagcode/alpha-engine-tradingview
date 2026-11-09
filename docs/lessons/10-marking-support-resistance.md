# PCSS Lesson 10 — Marking a Support and Resistance on a Time Frame

**Status:** COMPLETE at source-study level — original PDF pages 12–13 visually inspected, text extracted, every source example and numerical price verified, independent critical analysis prepared, 2026-11-09 Asia/Manila.

**Coach source:** [coach trading lessons.pdf, pages 12–13](../../sources/coach%20trading%20lessons.pdf). This is the only Coach-origin authority. **PDF SHA-256:** 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. **User PCSS SHA-256:** 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56.

**Project scope:** eventual crypto TradingView analysis including separate XAUUSDT, XAUTUSDT and PAXGUSDT products. **Original illustrated price feed is Gold Spot / U.S. Dollar on FOREX.com, 1H and 5m — not Binance gold perpetual or backed gold tokens.** Do not transfer numeric levels to crypto symbols. **Implementation:** zero Pine scripts, live acceptance, backtests, deployments or trades.

## Exhaustive source-order inventory and visual audit

Rendered both original PDF pages and independently checked native page text. **Page 12 has two dark chart screenshot panels, stacked one-hour and five-minute, marked resistance/support bands and arrows; page 13 is prose only**. No original mathematical derivation, exact entry fill, executed trade result, numerical win rate, or formal assigned exercise.

| ID | Original PDF content and order | Coverage |
| --- | --- | --- |
| 10-01 | p12 1H Gold Spot / U.S. Dollar FOREX.com chart with green support 4,670–4,680 and red resistance 4,730–4,750, multiple annotated tests | Inspected |
| 10-02 | p12 5m same gold spot feed, matching annotated bands, price near 4,710.70 at snapshot | Inspected |
| 10-03 | p12 Lesson heading “10. Marking a support and resistance on a time frame”; “so if e interpret natin ang chart” | Covered |
| 10-04 | “sa 1H” and support around 4,670–4,680 | Verified |
| 10-05 | Repeated support bounce; Coach's “Strong buyers area” | Qualitative, not order flow proof |
| 10-06 | Resistance around 4,730–4,750 | Verified |
| 10-07 | Multiple rejection at resistance; Coach's “Strong sellers area” | Qualitative |
| 10-08 | 1H sideways bias, no clear uptrend/downtrend, price ranges between levels | Covered |
| 10-09 | “Buy sa baba (support); Sell sa taas (resistance)” | Conditional location guidance |
| 10-10 | “sa 5m”, price near 4,710 in middle, not ideal entry | Covered |
| 10-11 | p13 SELL: wait for 4,730–4,750 | Covered |
| 10-12 | SELL: bearish engulfing or shooting star; “entry sa break ng confirmation” | Covered; break trigger undefined |
| 10-13 | SELL SL above resistance, 4,755; TP support 4,670–4,680 | Verified |
| 10-14 | p13 BUY: wait for 4,670–4,680 | Covered |
| 10-15 | BUY: bullish engulfing or hammer; “entry sa break ng confirmation” | Covered; break trigger undefined |
| 10-16 | BUY SL below support, 4,665; TP resistance 4,730–4,750 | Verified |
| 10-17 | p13 No bullish/bearish reversal (hammer, shooting star or engulfing) = invalid setup, no trade to avoid fakeouts | Covered, no zero-risk guarantee |

**No exact entry price or executed order is given in the original lesson.** Coach's proposed stop prices are about 5 original price units outside the far zone boundary, but this example does not establish a universal 5-unit stop buffer for other symbols or products.

## 1. One-hour context: two zones and a sideways bias

**COACH_EXPLICIT:** Support 4,670–4,680 has shown many bounces; resistance 4,730–4,750 has shown multiple rejection; Coach calls them strong buyers/sellers areas. Overall 1H price is sideways, not distinctly upward or downward. General location intuition is BUY near support and SELL near resistance.

**Interpretation:** The bands are intervals, not guaranteed reversal points. Two chart screenshots show the same forex gold spot context at differing granularity. Neither screenshot demonstrates whom the underlying buyers/sellers were or proves that a repeated reaction predicts a future profitable one.

**Cross-source tension:** Lesson 07 cautioned against sideways markets unless higher-timeframe context helps; Lesson 10 explicitly describes possible conditional range trades in a sideways 1H market. **Do not silently erase this tension**. It may be a case-specific exception, a schematic example, or require additional 4H context; source does not explicitly resolve.

## 2. Five-minute observation

**COACH_EXPLICIT:** Price around 4,710, in the middle, “not ideal entry”.

**Independent computation, from stated zones:** Distance to support upper edge = 4,710 − 4,680 = 30 price units. Distance to resistance lower edge = 4,730 − 4,710 = 20. These numbers explain why neither preselected zone is currently reached; they are NOT original calculations by Coach or a live quote.

Lesson 08 gate: if price has not reached the qualifying zone, wait/no trade. An appealing candle in the middle does not by itself fulfill that requirement.

## 3. Conditional SELL setup (source order)

**COACH_EXPLICIT:**
1. Wait until price rises to resistance 4,730–4,750.
2. Find bearish reversal: bearish engulfing or shooting star.
3. “Entry sa break ng confirmation.”
4. SL above resistance: 4,755.
5. TP in support: 4,670–4,680.

**Crucial missing data:** Coach has not specified confirmation candle OHLC or the exact break/entry price; one cannot derive a unique realized or planned RR from the source alone. What level must break (wick low/body low/close) is not defined.

**Independent hypothetical illustration, NOT a Coach trade:** If short entry E=4,740, stop S=4,755 and target T=4,680, price-distance risk 15, reward 60; gross reward/risk = 60/15 = 4 (risk:reward 1:4), before fees. A different confirmation break/fill changes the ratio.

## 4. Conditional BUY setup (source order)

**COACH_EXPLICIT:**
1. Wait for price to decline to support 4,670–4,680.
2. Find bullish reversal such as engulfing or hammer.
3. “Entry sa break ng confirmation.”
4. SL below support: 4,665.
5. TP resistance: 4,730–4,750.

**Independent hypothetical illustration, NOT a Coach trade:** Assume long entry E=4,675, stop S=4,665 and target T=4,730. Price-distance risk 10, reward 55; gross reward/risk 55/10 = 5.5 (risk:reward 1:5.5). The actual break trigger price is unspecified and can alter RR substantially.

In a linear product with valid long S<E<T, RR=(T-E)/(E-S); with valid short T<E<S, RR=(E-T)/(S-E). Product contract size, settlement currency, spread, fee/funding and fill behavior determine account-currency outcomes and are NOT in this source.

## 5. Final no-reversal = invalid setup

**COACH_EXPLICIT:** If no suitable bullish or bearish reversal pattern (hammer, shooting star, engulfing) is present, the setup is invalid; don't trade to avoid fakeouts.

**Interpretation:** Candlestick confirmation is necessary in this example but not sufficient for guaranteed profitability. A qualifying pattern can itself fail and turn into a losing trade.

**Cross-lesson nuance:** Lesson 08 also mentioned a strong large-body candle or a long-wick rejection plus follow-through. Page 13 highlights reversal patterns only. Whether the broader Lesson 08 options can qualify in this special sideways range scenario is **OPEN**, not decided by the source.

## 6. Ponder — previously unstated implementation questions

**Entry after confirmation close vs on break of confirmation.** Lesson 08 says entry only after confirmation candle closes; page 13 says “entry sa break ng confirmation”. One causal hypothetical reconciliation is (a) completed confirmation, then (b) price breaches a defined extreme and (c) later order may fill. But this is an **independent interpretation**. Coach does not establish wick/break level, how long to wait, entry order type, or whether a break can happen during the confirmation candle.

**Proposed interval-touch alternatives (not Coach):** For a known band Z=[a,b], candle OHLC (O,H,L,C), wick-range overlap holds if L<=b and H>=a; body overlap if min(O,C)<=b and max(O,C)>=a; close inside if a<=C<=b. They differ on wick spikes and price gaps. No variant approved.

**Future crypto mapping:** The illustration is FOREX.com Gold Spot USD, not XAUUSDT reference derivative nor XAUT/PAXG spot/token products. Source example prices may not fit actual crypto feeds; transfers should preserve logical process and verify venue-qualified units, zone provenance and timestamp. Distinguish prices quoted USD vs USDT and venue liquidity.

**Trade and backtest honesty:** Actual fill after a candle close can differ from observed closing price; TradingView default strategy broker emulator normally fills market orders created on a closing bar's next available tick. Source: https://www.tradingview.com/pine-script-docs/concepts/strategies/ . Confirmed HTF zones must become knowable before LTF contact; TradingView repainting docs: https://www.tradingview.com/pine-script-docs/concepts/repainting/ .

**Statistical uncertainty:** Source shows a hand-selected snapshot, not realized trade distributions, empirical positive expectancy, proof of a 1:4 or 1:5.5 opportunity, or current market instructions. All sample entries are explicitly independent.

## 7. Future evaluation blueprint (NOT implemented)

Potential stages: INSTRUMENT_VERIFIED -> HTF_ZONES_AND_BIAS -> PRICE_MIDRANGE/AT_SUPPORT/AT_RESISTANCE -> WATCH_REVERSAL -> CONFIRMATION_CLOSED -> ENTRY_BREAK_POLICY -> ENTRY_PRICE_KNOWN -> SL/TP/RR_REVIEW -> RESEARCH_CANDIDATE or NO_TRADE.

**OPEN_UNRESOLVED:** sideways permission/higher 4H requirement; strict vs broad confirmation taxonomy; exact confirmation-break trigger; zone-contact and expiry; target edge; stop padding scaled to asset; risk model; HTF temporal confirmation; actual orders. No numeric confidence claims. See the [separate research spec](../research/10-range-entries-and-confirmation-break.md).

## Source study completion

Both original annotated page-12 chart panels visually checked, full page-13 wording audited in order, numerical zones and stops verified, 2 independent hypothetical risk calculations checked. No original source exercise/formal proof omitted because none appears on pp. 12–13.

**Lesson 10 COMPLETE as a PCSS study, not as a coded or validated trading method.** **Next source:** Lesson 11 — Order Block; BOS vs CHoCH (PDF p. 14) on user instruction.
