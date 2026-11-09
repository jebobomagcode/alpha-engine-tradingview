# PCSS Lesson 16 — Long and Short Set-up

**Status: COMPLETE for source-based teaching and research only, 2026-11-09 Asia/Manila.** Original PDF p21 inspected visually from rendered image and cross-checked with native text. No Pine code, TradingView runtime testing, backtesting, deployment, trading order or empirical signal-performance analysis.

**Sole Coach-origin source:** [coach trading lessons.pdf, PDF p21](../../sources/coach%20trading%20lessons.pdf). Original SHA-256: 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. **Personal PCSS SHA-256:** 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56 (not published in this public repo). Owner's new TradingView project is **independent of all older trading projects** and targets crypto including venue-qualified XAUUSDT, XAUTUSDT and PAXGUSDT as distinct markets.

## Complete source-order inventory: original page 21

Page 21 is text-only. It contains two directional examples with three HTF observations and three LTF observations each. It has **no chart, figure, table, source calculation, number besides RSI 50, EMA/RSI length, absolute price, position/order details, profit, test results, proof or assigned exercise**. PDF page 22 begins Lesson 17 RSI and is outside Lesson 16's source boundary.

| ID | Original source text in order | Qualification |
| --- | --- | --- |
| 16-01 | “16. Long and Short set-up” | Heading |
| 16-02 | “Example Long Setup” | First example |
| 16-03 | LONG HTF “Bullish structure” | Exact structure method not defined on this page |
| 16-04 | LONG HTF “Price above EMA” | EMA length/source not given |
| 16-05 | LONG HTF “RSI above 50” | RSI period not given on this page |
| 16-06 | LONG LTF “Price retraces to EMA/FVG” | Slash is ambiguous: either, both, or a loose illustrative grouping |
| 16-07 | LONG LTF “RSI bounces above 50” | “Bounce” has no precise crossing or retest rule |
| 16-08 | LONG LTF “Bullish rejection candle appears” | No exact candle geometry defined here |
| 16-09 | “= continuation longorbuy” | Coach conclusion, not an order fill |
| 16-10 | “Example Short Setup” | Second example |
| 16-11 | SHORT HTF “Bearish structure” | Source condition |
| 16-12 | SHORT HTF “Price below EMA” | Source condition |
| 16-13 | SHORT HTF “RSI below 50” | Source condition |
| 16-14 | SHORT LTF “Price retraces to EMA resistance” | SHORT text names EMA resistance; **does not mention FVG** |
| 16-15 | SHORT LTF “RSI rejects below 50” | “Rejects” not formally quantified |
| 16-16 | SHORT LTF “Bearish confirmation candle” | Not the exact mirror of named bullish rejection candle |
| 16-17 | “= continuation short” | Coach conclusion |

**Source inventory verified from actual page, not inferred from earlier study.** Two examples do not establish that all future valid Coach trades must pass one fixed 6-boolean checklist, have fixed indicator parameters or necessarily use the same triggering candle.

## 1. LONG example — meaning and prerequisite recall

**COACH EXPLICIT:** HTF bullish structure; price above EMA; RSI above 50. LTF price retraces toward EMA/FVG, RSI bounces above 50 and bullish rejection candle appears. He names the result continuation LONG/BUY.

**Prerequisites:** Lesson 07 defines HH/HL bullish structural context; Lessons 04 and 08 distinguish HTF bias from lower-timeframe confirmation; Lesson 15 explicitly uses RSI>50 as a *usually bullish* momentum observation and cautions against RSI alone. Lesson 11 introduced OB; FVG was named elsewhere but complete geometry is not established by this page.

**PCSS interpretation:** monitor a lower-timeframe pullback within a known bullish higher-timeframe environment and evaluate a supportive reaction rather than buying blindly. An EMA/FVG “zone” is a *location candidate*, not a guaranteed price floor or automatic order.

**Open:** Is “EMA/FVG” logical OR, AND/overlap, or shorthand for optional confluence? Is RSI bounce a cross up through 50 or a test of 50 from above? What defines a bullish rejection candle and its completion? What is actual entry trigger and stop? None answered unambiguously by page 21.

## 2. SHORT example — meaning and original asymmetries

**COACH EXPLICIT:** HTF bearish structure; price below EMA; RSI below 50. LTF price retraces to **EMA resistance**, RSI rejects below 50, then a bearish confirmation candle. Coach labels continuation SHORT.

**PCSS interpretation:** an upward pullback within a structurally bearish market moves toward a moving-average resistance area, followed by an anticipated continuation downward supported by momentum and price-action observations.

**Source asymmetries are material:** LONG says “EMA/FVG” but SHORT says “EMA resistance”; LONG calls specifically for “bullish rejection candle,” SHORT says more generic “bearish confirmation candle.” Do NOT replace Coach's examples with one invented symmetric “EMA or FVG” and one invented pair of strict rejection candles. A short FVG research variant could be independently proposed, but not attributed to this exact page.

## 3. RSI midpoint event is the largest semantic gap

These **independent illustrative** RSI sequences can lead to different classifications:
- 47 -> 52: RSI crosses to above 50; one possible *bullish bounce* definition.
- 54 -> 50.5 -> 53: RSI tests near 50 from above and rebounds without crossing it; another possible *bullish bounce*.
- 46 -> 49 -> 44: RSI rises toward 50 while remaining below, then falls; possible *bearish rejection*.
- 48 -> 52 -> 47: failed move above 50, followed by recross below; a different bearish-rejection event.

Coach does not select crossing, touch, tolerance, bar lookback, RSI smoothing method, or completed-versus-forming bar status. Value equal to 50 is not classified by this source; do not silently force bullish or bearish.

**Important measurement fact:** EMA and RSI both derive from historical prices, as do many structural and FVG events. Their confirmations can be correlated; counting them as independent probability votes would not be valid without a supported joint statistical model.

## 4. Other missing technical specifications

- No exact HTF/LTF durations in this page. Prior lessons mention multiple candidate pairings but do not turn this page into one mandatory pairing.
- No specific EMA period or indicator source price. TradingView's stock EMA input default is not proof Coach selected that length.
- No RSI period on p21. The dedicated RSI lesson p22 provides additional background, but do not back-attribute its contents before studying it.
- No exact HH/HL, LH/LL pivot detector, wick/close break, trend conflict/sideways policy.
- No exact EMA contact tolerance, FVG geometry, invalidation, expiration, RSI-event timeout or candle wick/body ratio.
- No entry/stop/TP, fees, contract size, RR or actual output trade. It is an explanatory continuation example, NOT an executable strategy.
- No measured win rate or evidence that adding each EMA/RSI/structure check increases out-of-sample returns.

## 5. Cross-lesson reconciliation without erasing source cases

**Lesson 13** explicitly describes a countertrend short even though 4H structure remains bullish. **Lesson 10** also discusses conditional range setups. **Lesson 16** is specifically two *trend-continuation* examples. It does not automatically prohibit Coach's earlier countertrend/range cases. Treat each as a distinct source case until a full methodology-level hierarchy is defined.

Lesson 08 requires zone relevance, closed confirmation and risk evaluation; Lesson 10 in its range case adds “entry on break of confirmation”. This page gives neither an override nor a precise universal order trigger, so do not claim a fully specified entry rule.

## 6. Independent proposed state representation — NOT code

One possible descriptive sequence:
1. Known source venue/symbol/timeframe, confirmed HTF structure.
2. HTF price-versus-EMA and RSI-versus-50 observations, separately timed and with explicit indicator settings (currently unknown).
3. LTF EMA/FVG retracement contact as a provisional event.
4. LTF RSI midpoint-bounce or rejection event with the selected hypothesis label, not an unqualified source-exact event.
5. Fully closed LTF bullish rejection or bearish confirmation candle.
6. State output LONG_CONTINUATION_CANDIDATE / SHORT_CONTINUATION_CANDIDATE / WAIT / CONFLICT / INSUFFICIENT, distinct from actual order execution and RR.

**Source page does not define the state names, exact event grammar or an algorithm requiring all six to trigger simultaneously.** For future implementation a transparent state display and known-at time is preferable to “AI confidence 95%” invented from price-derived confluences.

## 7. Technical references and temporal safety

**External, NOT Coach-origin:** TradingView [EMA](https://www.tradingview.com/support/solutions/43000592270-exponential-moving-average/) discusses the exponential price weighting and its configurable length; [repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) and [HTF requests](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) explain changing unconfirmed HTF data and the confirmed-HTF offset approach. [Bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/) explains candle confirmation and cautions that barstate.isconfirmed inside request.security does not work as an HTF confirmation shortcut.

Never backdate eligibility when the HTF EMA/RSI or structural pivot was confirmed only later. A provisional RSI above 50 on a forming HTF candle may later close below 50. Source and timestamps must be preserved.

## 8. Ponder study conclusion

Coach provides two concrete but qualitative continuation *examples*, not an objective entry/exit machine or a tested edge. The material unresolved questions concern RSI event semantics, EMA/FVG slash, EMA periods, structural pivots, timeframes, candle threshold and complete trade management. Research alternatives and falsification fixtures are in [Lesson 16 research](../research/16-long-short-continuation-state-candidates.md).

**Coverage conclusion:** All 17 original items examined in page order, with no original figure/table/formula/exercise omitted (none exists). No code or actual tests. **Lesson 16 COMPLETE as PCSS study. Next: Lesson 17 — RSI (Relative Strength Index), PDF p22, only on owner instruction.**
