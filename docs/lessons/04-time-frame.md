# Lesson 04 — Time Frame: Higher- and Lower-Timeframe Workflow

**Status:** COMPLETE for full PDF page-6 PCSS study, textual/visual audit, independent explanation, and preliminary design research.  
**Project:** Alpha Engine TradingView — independent crypto-focused research; **no Pine implementation, backtest or live order**.  
**Study date:** 2026-11-09 (Asia/Manila).  
**Original Coach source:** [coach trading lessons.pdf, PDF page 6 (lesson 04)](../../sources/coach%20trading%20lessons.pdf).  
**Coach PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`.  
**User PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`.

## Source-order item audit — original, not reconstruction

A full rendered page-6 image was inspected against the PDF's native extracted text. **Page 6 is prose-only** (no source diagrams, historical chart images, tables, assigned exercise or quantitative proof). We separately provided a supplementary mathematical timeframe-aggregation schematic and hypothetical BTC example.

| ID | Exact page-6 source item (paraphrase preserves order) | Status |
| --- | --- | --- |
| 04-01 | Heading: “04. Time Frame” | Covered |
| 04-02 | “HTF (1H/4H)”: Zone + trend; “no need overconfirm” | Covered; ambiguity documented |
| 04-03 | “LTF (5m/15m)”: wait for confirmation (entry trigger) | Covered |
| 04-04 | When the basis is 1H or 4H, entry can be on 5 minutes | Covered; explicit 5m illustration does not exclude 15m |
| 04-05 | “1. Higher Timeframe (1H / 4H)” | Covered |
| 04-06 | HTF: trend (up/down), key levels (support/resistance) | Covered |
| 04-07 | “2. Lower Timeframe (5M / 15M)” | Covered |
| 04-08 | LTF: await setup (pullback/bounce) | Covered |
| 04-09 | LTF: confirmation candle | Covered; no source definition on this page |
| 04-10 | LTF: actual entry + stop loss + take profit | Covered; stop/target algorithms not supplied here |

**Coach source contains no numerical thresholds**, no mandatory hierarchy between 1H and 4H, no exact HTF zone calculation, no exact confirmation-candle definition and no indicator formula on this page. Do not present our ideas below as Coach-explicit.

## 1. Coach's rule and meaning

**COACH_EXPLICIT (PDF p. 6):**
- HTF 1H/4H: analyze the zone and trend only, “no need overconfirm”.
- LTF 5m/15m: wait for confirmation as entry trigger.
- Specific example: use 1H or 4H as HTF basis and enter on the 5-minute timeframe.
- Numbered summary: HTF trend (rising/falling) plus support/resistance; LTF pullback or bounce, confirmation candle, entry, SL and TP.

**INTERPRETATION:** Analysis is organized by decision role, not by assuming one candle pattern defines everything. The HTF determines *where/under which directional context* to watch; the LTF determines *whether/when* a suitable reaction materializes, and supports considering entry/SL/TP.

**QUALIFICATION:** “No need overconfirm” is not a formal numerical rule. It should not be translated as “the HTF can be unconfirmed” or “never check HTF data quality.” An ambiguous HTF context must remain ambiguous.

## 2. Timeframe aggregation — prerequisite explanation

For aligned continuous periods:
- 4H = four 1H bars = sixteen 15m bars = forty-eight 5m bars.
- 1H = four 15m bars = twelve 5m bars.

The same underlying price series is aggregated differently; it is not an independent market. For HTF aggregation of ordered constituent bars:
\[
O_\mathrm{HTF}=O_\mathrm{first},\quad
H_\mathrm{HTF}=\max H_i,\quad
L_\mathrm{HTF}=\min L_i,\quad
C_\mathrm{HTF}=C_\mathrm{last}.
\]
The numbers of available component bars can differ with venue calendars, missing candles and market sessions. In addition, a plotted HTF bar's high and close may change before its period ends.

**Consequences:** A 4H candle may summarize a complicated intra-period rise, drop and rebound; the 5m chart reveals more detail but also more noisy swings. Lower timeframes do not automatically supply more *predictive information*, only more granular observations.

## 3. Higher timeframe: trend and support/resistance

**COACH_EXPLICIT:** “Dito mo titingnan: -Trend (pataas o pababa) -Key levels (support/resistance).”

**Independent clarification:** A directional trend is an inference from price structure over multiple bars, not merely whether the last HTF candle is green. Possible higher highs and higher lows / lower highs and lower lows belong to later market-structure lessons; do not finalize the swing detection here.

**Support/resistance caution:** a relevant zone may be a range of prices, not a magic exact tick. Its boundaries, detection timing, confirmation/invalidating behavior and priority cannot be derived from this lesson alone. Lessons 09–10 cover the source's S/R treatment later; Lesson 07 adds structure/confluence.

**Unresolved:** choose HTF 1H or 4H, or combine both? What if 1H and 4H disagree? Coach's page 6 allows HTF alternatives but provides no precedence, no requirement for both to align, and no weighted score.

## 4. Lower timeframe: reaction, confirmation, entry

**COACH_EXPLICIT:** “Hintayin setup (pullback / bounce)”; “Confirmation candle”; then “entry + SL + TP” on 5m/15m.

**Independent explanation:** a pullback temporarily moves against the preceding direction; a bounce is movement away from an observed level. Neither independently guarantees reversal/continuation. The source does not define what exact candle qualifies as confirmation, how many bars to wait, or when a stop/target is considered valid.

**Relation to earlier lessons:** Lesson 02 showed hammer/shooting star/doji morphology but expressly required context; Lesson 03 established that risk:reward affects modeled payoffs. These are separate layers: candle shape alone ≠ valid setup; positive planned RR ≠ statistical edge.

## 5. One complete hypothetical crypto illustration — NOT Coach's historical chart

**Purpose:** demonstrate decision sequence, not provide market advice or a strategy rule.

1. On a hypothetical BTCUSDT chart, previously **confirmed** 4H data appears upward and shows a candidate support range 100,000–100,200 USDT.
2. On a 5m chart, price declines into that area. We watch instead of automatically buying.
3. Price appears to bounce. Only once a suitably defined LTF candle is complete and later Coach rules are formalized might this qualify as confirmation.
4. A hypothetical planned long entry = 100,300 USDT; stop = 100,100; target = 100,700 (not mechanically justified by the source; stop lies within the illustrated support band).
5. Gross price-distance risk = 200 USDT per base unit, target = 400 USDT; planned gross risk:reward = 1:2 before fees, slippage and contract-specific sizing.
6. **Caveat:** favorable arithmetic does not establish that the entry/stop/zone is structurally sound. This is solely a teaching example.

**For XAUUSDT, XAUTUSDT and PAXGUSDT:** the page-6 top-down principle can be studied across all three as *research candidates*, but product/feed details, session behavior, tick precision and liquidity differ. Do not merge data or assume a gold perpetual contract behaves identically to physically backed token markets. Consult [market scope](../MARKET_SCOPE.md).

## 6. Precise temporal causality — independent research and technical verification

**Pivotal question:** At what clock time could the HTF trend or zone have been known *while a particular LTF candle was being evaluated*?

Consider a hypothetical 4H period from 08:00 to 12:00 in the chart's reference timezone. During 09:10, its final 4H high and close are **not knowable**. A 5m signal at 09:10 cannot legitimately depend on the final 12:00 close or a zone requiring a pivot confirmed after 09:10.

**Technical references, official TradingView Pine documentation (accessed 2026-11-09):**
- [Other timeframes and data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/)
- [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/)
- [Other data and timeframes FAQ](https://www.tradingview.com/pine-script-docs/faq/other-data-and-timeframes/)
- [Bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/)

Their contracts support the following cautions:
- A normal `request.security()` call for **forming HTF** data can produce values that change in real time and display differently after reload.
- For HTF values whose historical/live reproducibility is important, TradingView documents accessing **previously confirmed HTF data** by offsetting each requested expression by one HTF bar and using `barmerge.lookahead_on`. The tradeoff is latency. This is a *technical research requirement*, **not an already coded algorithm**.
- Using `barmerge.lookahead_on` without the historical offset can leak future HTF values into earlier historical LTF bars. **Avoid**.
- `barstate.isconfirmed` can indicate confirmation for the **chart's current timeframe**; it is not a reliable solution when used within a `request.security()` expression for another timeframe.
- A 15m/4H chart requesting full 5m event history should not assume ordinary single-value `request.security()` returns all intrabars; TradingView provides `request.security_lower_tf()` arrays for that specialized problem.

**Suggested architecture (not accepted as final):** run the future chart-side decision state machine on the intended entry-LTF (5m or 15m), request HTF context separately, and make zone/context observation timestamps explicit. Alternative: manual HTF/LTF chart inspection; simpler but less automated.

## 7. Ponder: alternatives, uncertainty and falsification

**Candidate approach A — strictly confirmed HTF:** only previously completed HTF bars feed the context and alerts. Advantage: reproducible historical/realtime results; drawback: delayed response to real developing reversals.

**Candidate approach B — forming HTF provisional context:** present evolving HTF structure with a prominent PROVISIONAL label, but do not backdate its final value. Advantage: timely exploratory information; drawback: can change and repaint.

**Candidate approach C — dual channel:** confirmed HTF drives stable research signals while provisional HTF is shown as diagnostics only. More informative but more complexity and potential visual clutter.

No approach is Coach-explicit and none is chosen as fixed system behavior. Do **not** assert “non-repainting” until actual Pine runtime acceptance.

**Competing research hypotheses:**
- HTF zone plus valid LTF confirmation outperforms LTF-only geometry after costs on predeclared crypto/gold instrument/timeframe samples.
- Apparent benefit disappears after time-of-knowledge correction, transaction costs, and realistic delay.
- A simpler one-HTF configuration outperforms combining 1H and 4H due to conflicting signals/overfitting.

**Future controlled tests:** mark every HTF zone's known-from timestamp, compare historical and realtime/reload captures, force conflicts, test symbol changes and session gaps, check no future pivots, examine 5m/15m trade frequency and slippage separately, compare source-baseline to extensions and a minimal LTF-only baseline, and report negative results.

## 8. Constrained decision sketch (NOT software)

`INSTRUMENT_VERIFIED → HTF_CONFIRMED_OR_PROVISIONAL → HTF_TREND_AND_ZONE → LTF_APPROACH → LTF_REACTION → LTF_CONFIRMATION_PENDING → ENTRY/SL/TP_EVALUATION → RISK_REVIEW → RESEARCH_SIGNAL_OR_WAIT`

A useful evidence-rich research companion should distinguish `NO_ZONE`, `HTF_UNCONFIRMED`, `HTF_CONFLICT`, `PRICE_NOT_AT_ZONE`, `NO_REACTION`, `LTF_UNCONFIRMED`, `RR_INSUFFICIENT`, and `DATA_INSUFFICIENT` rather than fabricate confidence.

These names are illustrative, not approved interface requirements or claims about the original PDF.

## Coverage verdict / next source item

**Lesson 04 source coverage COMPLETE:** checked all 10 source items of PDF page 6 in sequence; inspected the rendered page; verified no original drawings/figures or original calculations were omitted. Mathematical timeframe aggregation and example were clearly identified as additions.

**OPEN_UNRESOLVED:** HTF choice/priority/conflicts; trend and zone algorithms; concrete LTF confirmation; stop/target rules; temporal nonrepainting policy; exchange-qualified feeds and contract distinctions. These are not grounds to declare methodology implementation complete.

**Next on owner instruction:** **Lesson 05 — Leverage and Margin, PDF page 7**, retaining original crypto-vs-forex comparison even though our implementation target remains crypto.
