# Lesson 12 — BOS (Break of Structure) | PCSS source study

**Status:** COMPLETE at source-study level, 2026-11-09 (Asia/Manila); no executable Pine code, backtests, deployment, trading, or verified market performance.  
**Sole Coach source:** [coach trading lessons.pdf, pages 15–16](../../sources/coach%20trading%20lessons.pdf). **Source PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`. **User PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`.  
**Market scope:** Crypto including distinct XAUUSDT, XAUTUSDT and PAXGUSDT venue/product feeds; no other project accessed or modified.

## Full page-order source audit

Both original PDF pages were inspected as rendered images **and** extracted PDF text. Page 15 has **four embedded illustrations**, two of which are two-panel composites; page 16 has **one additional embedded chart**, for five embedded illustrations. No original BOS numeric threshold, OHLC table, formal proof, exercise, realized trade, measured win rate or exchange-specific signal is supplied.

| ID | Original source item | Audit finding |
| --- | --- | --- |
| 12-01 | p15 heading “12. BOS (Break of structure)” | Covered |
| 12-F1 | p15 top left: paired “BULLISH BOS” and “BEARISH BOS” candlestick diagrams | HH/HL and upward BOS in bullish panel; LH/LL and downward BOS in bearish |
| 12-F2 | p15 top right: paired “Bullish Order Block Candle / Bearish Order Block Candle” diagrams | Repeats previous Lesson 11 image, same-direction colored OB candle 1, “1→3 GAP”, shaded zones and checks; NOT proof that every BOS requires OB/FVG |
| 12-02 | “before natin i-identify ang BOS is tignan natin ang trend or takbo ng market” | Prior trend first, not arbitrary crossing |
| 12-03 | “Uptrend -> Higher Highs (HH) + Higher Lows (HL)” | Covered |
| 12-F3 | p15 rising green zigzag, HH/HL/BoS labels and legend | Multiple upward BOS labels based on preceding highs; not quantitative detection |
| 12-04 | “Downtrend -> Lower Highs (LH) + Lower Lows (LL)” | Covered |
| 12-F4 | p15 “Change of Character Trading Strategy” candlestick screenshot | Bearish LH/LL plus earlier down BOS and later **CHOCH**, demand zone and large upward recovery; NOT a pure downtrend-only image |
| 12-05 | “dito palang alam na natin ang bias if buy ba or sell” | Directional bias, not an automatic order |
| 12-06 | “BOS means continuation ng trend or tuloy ang pagtaas or pagbaba ng price” | Continuation meaning |
| 12-07 | “Sa uptrend nabreak ang previous High (HH) ibig sabihin: tuloy ang akyat” | Previous HH breakout described; threshold unspecified |
| 12-08 | p16 “downtrend nabreak ang previous Low (LL)” | Previous LL breakout described |
| 12-F5 | p16 “Break of structure Example” descending candlestick graphic, several LL/BOS tags | Visually inspected repeated bearish continuation illustrations |
| 12-09 | p16 “ibig sabihin naman ay tuloy ang baba” | Downtrend continuation |

**Scope boundary:** page 17 starts Lesson 13 “Manage your risk”; it is not part of the BOS criteria in this study.

## 1. Coach-explicit rules and prerequisite recall

From Lesson 07: an UP trend involves progressively higher swing highs and higher swing lows, while a DOWN trend involves lower highs and lower lows. Lesson 11 defines BOS as trend **continuation**, CHoCH as **possible reversal**.

**COACH EXPLICIT (pp15–16):** Check trend first. If the established market is in an uptrend, breaking the previous HH means bullish continuation. If it is in a downtrend, breaking the previous LL means bearish continuation. Trend analysis helps determine BUY/SELL directional focus.

**PCSS interpretation:** Price breaking a number alone is not BOS. We must identify the relevant *previous structurally significant* high or low on a specified timeframe and know the trend prior to the break. An up-candle in a downtrend is not automatically bullish BOS. Bias does not satisfy entry, support/resistance, confirmation, stop or TP rules from Lessons 07–10.

## 2. Bullish BOS — original interpretation and added numerical example

In the original green zigzag chart, a sequence of HH/HL movements is accompanied by labels “BoS” near extensions beyond earlier peaks.

**INDEPENDENT teaching example, not Coach data:** Assume a relevant high H* = 110 USDT has already been confirmed and a recent higher low is 95 USDT; a later completed candle closes at C = 112 USDT. Under **one candidate close-break rule**, 112 > 110 marks a bullish continuation candidate, conditional on an UP prior state. Coach does not say a closing-price break is compulsory. An intrabar high break is a competing definition.

## 3. Bearish BOS — original interpretation and added numerical example

The p16 image shows a lower-high/lower-low downtrend and repeated break markers below prior LL levels.

**INDEPENDENT teaching example:** Last confirmed relevant low L* = 90 USDT; later closed C = 87 USDT; 87 < 90 meets a *candidate* close-break comparison if the prior state was DOWN. It would not necessarily be a bearish BOS if the market was previously UP: a low-side break in that setting might represent a possible CHoCH.

**No original numerical price chart** or contractual quote/settlement data accompany the figure. The image is an illustrative historical sequence, not measured trading performance.

## 4. Distinguishing the source CHOCH illustration

The source graphic under the “Downtrend” bullet on p15 is titled **Change of Character Trading Strategy**. It illustrates lower lows, a downward BOS, a separately marked CHOCH, a demand zone and later substantial bullish movement. This is a **mixed transition example**, not evidence that every red continuation break is eventually reversed.

Do not conflate the initial trend state with the later possible change. In particular, a bullish move against the former downtrend is not automatically an established new bullish BOS: its classification requires the pre-break structure and which structural reference broke. The exact protected swing, CHoCH confirmation rule and later-trend transition criteria are **not defined by Lesson 12**.

The separate top-right OB figure repeats the preceding lesson. Its inclusion does not establish that an OB, imbalance, or "1→3 GAP" is a mandatory BOS prerequisite.

## 5. Mathematical formalization alternatives — explicitly NOT Coach rules

Let prior *confirmed* structure be S_(t−1) ∈ {UP, DOWN, SIDEWAYS, MIXED, UNKNOWN}, previously confirmed relevant high H* and low L*, and the current candle (O_t,H_t,L_t,C_t).

**Candidate A — candle closing break:**
- S_(t−1) = UP and C_t > H* => bullish BOS candidate.
- S_(t−1) = DOWN and C_t < L* => bearish BOS candidate.

**Candidate B — wick penetration:**
- S_(t−1) = UP and H_t > H* => bullish crossing candidate.
- S_(t−1) = DOWN and L_t < L* => bearish crossing candidate.

**Counterexample:** Prior high H*=110; candle O=108,H=112,L=107,C=109. It traded above the prior high but closed below. Wick-break: yes; close-break: no. Source simply says “nabreak”; it does not choose a rule or an equality/tick buffer.

**Further gaps:** swing method and confirmation latency; whether a local peak or last major structural high qualifies; multiple candidate swing levels; break of both sides in an outside bar; 1H/4H conflict; repeated labels after the same level breaks; fakeouts, gaps, missing candles and volume/cost filters.

## 6. Temporal integrity — independent engineering research

An apparent historical swing at candle k can need subsequent candles to confirm. If a BOS event depends on that swing, the swing must have become **knowable** before the BOS event. A marker drawn at the old swing's occurrence should not be mistaken for when a trader could have used it.

Keep `swing_origin_time`, `swing_known_at_time`, `break_event_time` and `break_confirmed_time` separate. A forming candle's wick may cross HH and then close back below; a closing-break strategy cannot classify it as confirmed earlier.

TradingView official technical sources (independent, not Coach):
- https://www.tradingview.com/pine-script-docs/concepts/repainting/
- https://www.tradingview.com/pine-script-docs/concepts/bar-states/
- https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/

For confirmed HTF `request.security()` values, the documented technique offsets the requested expression and uses `barmerge.lookahead_on`; unoffset future-looking requests can mislead historical signals. This is a possible implementation constraint, not code already written.

## 7. Complete-methodology context and falsification

BOS is structural evidence; it is **not a self-sufficient BUY/SELL trigger or proof of positive expectancy**. Lessons 04, 07–10 still require HTF/LTF context, zone relevance, candle confirmation, defined entry, stop, target and actual risk checks.

Future tests should compare close, wick and buffered break variants with a simpler baseline on predeclared crypto markets. Examine false breaks, event delay, missed events, stale pivot use, signal density, after-cost utility and out-of-sample stability. An illustration emphasizing successful continuation cannot establish win rate.

**Ponder conclusion:** Preserve Coach's trend-first, high/low continuation concept while keeping pivot algorithms, break conditions, event chronology and CHoCH distinction as open hypotheses. Prefer explicit WAIT/INSUFFICIENT over forced labels.

## Completion

All text and **all five image blocks** across the two PDF pages were inspected. No source examples, proofs or exercises omitted. Exact source data are qualitative only; numerical OHLC examples above were invented for teaching and labeled accordingly. **Lesson 12 COMPLETE as PCSS study, not implemented or tested.**

**Next on owner direction:** Lesson 13 — Manage Your Risk (PDF pages 17–18), including a SOL trade analysis with source numbers. Stop here.
