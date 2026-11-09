# PCSS Lesson 13 — Manage Your Risk (SOLUSDT)

**Status:** COMPLETE, source study only, 2026-11-09 (Asia/Manila). Two original PDF pages and all three mobile screenshots visually inspected; original text independently extracted; Coach examples checked mathematically. Zero Pine scripts, code backtests, live orders or deployments.

**Sole Coach source:** [coach trading lessons.pdf, PDF pp. 17–18](../../sources/coach%20trading%20lessons.pdf), PDF SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. **Personal PCSS:** SHA-256 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56, excluded from this public repository. Our independent project targets crypto including distinct XAUUSDT, XAUTUSDT and PAXGUSDT products.

## Ordered source inventory — complete original pages

Page 17 consists of the heading and **two mobile screenshots**. Page 18 contains extensive Coach text on the left and **one 4H screenshot** at right. All three screens are labeled SOLUSDT Perpetual Contract, but the original does not establish a verified exchange, year, order timestamp or execution history. Page 19 begins Lesson 14, not included here.

| ID | Original source item and exact values | Coverage |
| --- | --- | --- |
| 13-01 | p17 “13. Manage your risk” heading | Covered |
| 13-F1 | p17 left SOLUSDT 15m candles, volume and RSI 14 close; price near 86.19, RSI around 49.06; another line about 63.12 | Visually inspected |
| 13-F2 | p17 right SOLUSDT 1H candles, volume, RSI; price near 86.20, RSI about 62.88; another line about 64.35 | Visually inspected |
| 13-02 | p18 short entry 86.4–86.7 at supply / OB / FVG area | Exact values preserved |
| 13-03 | Short stop loss 87.2, above HTF resistance | Exact value |
| 13-04 | Short TP1 85.8, TP2 85.3, TP3 84.8 “if full pullback” | All three values preserved |
| 13-05 | “quick analysis”: 4H bullish, HH + HL | Covered |
| 13-06 | Price recently touched approximately 87 resistance then rejected | Coach interpretation |
| 13-07 | RSI near overbought, momentum slowing | Source statement, not numerical rule |
| 13-08 | 4H support 85.2–85.5, last push base / demand | Exact band |
| 13-09 | No down BOS yet: still bullish but in a pullback | Crucial |
| 13-10 | 1H still bullish but weakening | Covered |
| 13-11 | 1H possible CHoCH forming, lower high + bearish push | “Possible”, not proven |
| 13-12 | 1H rejection candles near resistance interpreted as supply | Coach interpretation |
| 13-13 | 1H bearish FVG 86.4–86.8 | Exact band |
| 13-14 | 1H demand/support 85.6–85.8 | Exact band |
| 13-15 | 15m weakening (“humihina na”) | Covered |
| 13-16 | 15m clear lower highs | Coach assessment |
| 13-17 | 15m RSI dropping; Coach calls momentum shift confirmed | Covered with qualification |
| 13-18 | 15m “possible CHoCH already” | “Possible”, not deterministic |
| 13-19 | 15m small bearish OB 86.5–86.7 | Exact band |
| 13-20 | Coach shorted due to rejection and CHoCH confirmation | Retain claim; no fill ledger |
| 13-21 | SHORT is a pullback trade AGAINST bullish HTF, scalp/intraday only | Source constraint |
| 13-22 | Alternative “LONG for SOL (Safer but wait tayo)” | Qualitative comparative judgment |
| 13-23 | Long waits for demand 85.2–85.6 | Exact band |
| 13-24 | Long requires 15m CHoCH and strong bullish displacement, a large green candle | Both source conditions |
| 13-25 | Long entry AFTER confirmation, not blind buy; stop BELOW 84.9 | Open inequality, NOT exactly 84.9 |
| 13-26 | Long TP1 86.5, TP2 87+; Coach calls HTF-aligned setup higher-probability swing | Exact targets, unmeasured probability |
| 13-F3 | p18 right SOLUSDT Perpetual 4H screenshot, price near 86.20, RSI ≈63.88, other plotted line ≈55.88, strong rise then pullback | Visually inspected |

There is **no source trade fills dataset, final profit/loss, allocation percentages across TP targets, exact long entry, exact long stop, objectively stated RSI signal cutoff, or quantified trading edge**.

## 1. Prerequisites

Lessons 04/07: HTF structure and LTF confirmation, HH/HL vs LH/LL. Lesson 05: exposure, not merely leverage selection, determines dollar price risk. Lessons 08–10: wait for zone, then confirmation, then risk-defined entry; NO TRADE is a legitimate result. Lesson 11: CHoCH is a possible reversal; OB identifies a candidate reaction location. Lesson 12: BOS indicates continuation of the PREVIOUSLY established trend.

## 2. Higher timeframe: 4H bullish, no bearish BOS

**COACH EXPLICIT:** The 4H is bullish with HH/HL; price touched near 87 resistance and rejected. RSI near overbought and momentum slowing. Demand/support 85.2–85.5. **No BOS down yet**, thus still bullish overall but possibly in a pullback.

**Interpretation:** A smaller-TF bearish movement is not enough to reclassify the 4H as bearish. The distinction between pullback and primary-trend reversal governs the risk context of Coach's countertrend SHORT.

**Numerical qualification (independent):** Original 4H screenshot RSI ≈63.88, BELOW conventional Wilder overbought level 70, as explained by TradingView official reference https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/ . Coach's “near” is qualitative and no custom exact RSI threshold is specified. Do not hardcode 63.88 as a risk trigger.

## 3. MTF 1H and LTF 15m

**COACH EXPLICIT 1H:** Still bullish but losing momentum. Possible CHoCH forming with lower high and bearish push; rejection candles near resistance as supply evidence; bearish FVG 86.4–86.8; demand/support 85.6–85.8.

**COACH EXPLICIT 15m:** Clear lower highs, declining RSI, possible CHoCH already, bearish OB 86.5–86.7. Coach says he shorted because of rejection and CHoCH confirmation.

**Important source ambiguity:** “possible CHoCH already” and “CHoCH confirmation” are both on the page. The PDF does not define an exact protected swing, wick/close break or confirmation bar. Do not turn this discretionary statement into a binary confirmed CHoCH algorithm without independent definition and empirical testing.

The original screenshots contain candles/RSI, **not objectively annotated OB/FVG geometric bounds or complete OHLC history**. The written zones are source facts; their algorithmic construction cannot be verified from these screenshots alone.

## 4. Countertrend SHORT numerical audit

**COACH EXPLICIT:** Entry interval [86.4,86.7], SL 87.2, TP1 85.8, TP2 85.3, TP3 84.8 only if full pullback. Countertrend relative to bullish 4H; scalp/intraday intent.

**INDEPENDENT MATH:** For a valid linear short with entry E, stop S>E and target T<E, risk distance R=S−E, reward G=E−T, and gross reward/risk rho=(E−T)/(S−E).

| Assumed entry | Risk to 87.2 | TP1 reward / RR | TP2 reward / RR | TP3 reward / RR |
| --- | ---: | --- | --- | --- |
| 86.4 | 0.8 | 0.6 / **0.75R** | 1.1 / **1.375R** | 1.6 / **2.0R** |
| 86.7 | 0.5 | 0.9 / **1.8R** | 1.4 / **2.8R** | 1.9 / **3.8R** |

All arithmetic was recomputed exactly. Gross price-distance RR grows with E for this short when T<S; the source's entry range does **not** determine one fixed ratio. No source allocation at TP1/TP2/TP3, exchange fees, funding, slippage, trade size or actual fills; hence no realized aggregate RR.

**Extra observation:** TP3=84.8 is below Coach's 4H support 85.2–85.5. His “if full pullback” qualification matters: price may encounter support before the deepest short target. There is no empirical success probability for crossing that support.

A 0.5–0.8 quote-unit stop distance is **not** account-currency risk without base quantity/contract size. Executable stops can slip. Leverage changes posted margin and can influence liquidation risk; it does not set the gross price loss by itself.

## 5. Proposed HTF-aligned LONG — conditional, not immediate

**COACH EXPLICIT:** Wait for SOL to reach demand 85.2–85.6. Then require a 15m bullish CHoCH plus strong bullish displacement (large green candle). Enter **after** confirmation, not blind buy. SL strictly **below 84.9**. TP1 86.5, TP2 87+. Coach calls this “safer” and a “higher probability swing” because it aligns with HTF bullish trend.

**INDEPENDENT MATHEMATICAL LIMIT:** Long gross RR=(T−E)/(E−S) requires exact entry E, stop S and target T (S<E<T). Coach supplies neither exact E nor exact S, and TP2 “87+” is not one exact T. **Do not substitute S=84.9 or E=85.2/85.6**. A unique long RR is unknown.

**Timeframe-zone integrity:** The p18 4H support [85.2,85.5], 1H demand [85.6,85.8], and proposed long entry area [85.2,85.6] differ. They should not be silently merged or assumed identical because each belongs to a distinct context.

“Safer” is Coach's relative preference, not a risk-free condition. “Higher probability” is unmeasured in the source and should not be transformed into a numeric win probability.

## 6. PCSS interpretation and cross-lesson synthesis

Coach describes TWO different candidate trade classes in ONE bullish 4H regime:
- **Countertrend scalp/intraday SHORT:** LTF bearish reaction from upper supply/OB/FVG, still against HTF UP.
- **Trend-aligned conditional LONG:** price must first reach lower demand, then 15m bullish CHoCH and displacement must occur.

This qualifies, rather than deletes, Lesson 08's general advice to focus BUY in uptrend. Coach has introduced an explicit case-specific countertrend research opportunity. Still no permission for automatic trading without confirmation/risk.

**Ponder findings:** No realized entry or performance from static screenshots; TP3 below HTF support may be hard to reach; 4H RSI is below common overbought threshold; the long has insufficient exact price data for a numerical RR; CHoCH/FVG/OB source notes remain discretionary. A future algorithm should track disagreement and conditionality rather than flatten the 4H bullish and 15m bearish observations to one signal.

## 7. Source-grounded research handoff

See [independent research](../research/13-countertrend-risk-mtf.md) for hypotheses, alternatives and planned tests. A future explainable system could track HTF_ALIGNED vs COUNTERTREND, per-timeframe structural states, confirmed/provisional CHoCH, contact with previously knowable zones, and risk computations from actual specified entry, stop, quantity and TP allocation. No feature threshold accepted.

Official independent TradingView references: [Strategy order/exits](https://www.tradingview.com/pine-script-docs/concepts/strategies/), [repainting/HTF behavior](https://www.tradingview.com/pine-script-docs/concepts/repainting/), [RSI](https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/).

**Coverage verdict:** All pages 17–18 source bullets, exact values and three original chart panels inspected. No original exercise, theorem or source-computed RR to omit. Lesson 13 COMPLETE for source study, **not for software implementation, backtesting or verified profitability**.

**Next on owner instruction:** Lesson 14, Fibonacci Retracement, original PDF page 19. Stop here; do not auto-advance.
