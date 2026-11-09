# Lesson 20 — CHoCH: Causal Swing Reference, Break Semantics and Reversal Qualification

**Status:** OPEN INDEPENDENT RESEARCH only. No Pine code, TradingView chart runtime, synthetic Pine unit tests, market backtests, orders or deployment. Date 2026-11-09 Asia/Manila.
**Coach-origin authority:** [original PDF p25](../../sources/coach%20trading%20lessons.pdf); [PCSS study and all four source diagram panels](../lessons/20-choch-change-of-character.md).
**Market scope:** distinct exchange-qualified crypto instruments including XAUUSDT derivatives, XAUTUSDT and PAXGUSDT token markets; other repositories excluded.

## A. Coach exact source claims

- CHoCH = “possible reversal or shift ng trend”, not certain trend reversal.
- An established DOWN structure breaks the previous **Lower High (LH)** → possible bullish reversal.
- An established UP structure breaks the previous **Higher Low (HL)** → possible bearish reversal.
- F1 Market Structure schematic: bullish BOS → bearish CHoCH → bearish BOS → bullish CHoCH.
- F2 Change of Character Trading Strategy: LH/LL, prior bearish BOS, lower LL near a demand zone, later upward CHOCH horizontal break, HH and subsequent advance; green/red trade-area shading but no price levels, fills or backtested performance.
- F3 “Bearish CHOCH” and F4 “Bullish Choch” directional zigzags; each illustrates a break against prior BOS direction.
- Four interpreted diagram panels across three physical embedded graphic regions; no numeric algorithm, source-specified break type or timeframe.

**No source basis** for declaring a pivot size, a required break candle close, a guaranteed new trend, fixed confirmation BOS, order price, take-profit or stop from the diagrams.

## B. Source-consistent event typing; independently proposed

Given a prior directional regime R (UP/DOWN) known as of a particular time and an eligible prior structural level Q:

- If R=DOWN and a subsequent qualified break above a previously confirmed LH level occurs, mark BULLISH_CHOCH_CANDIDATE.
- If R=UP and a subsequent qualified break below a previously confirmed HL level occurs, mark BEARISH_CHOCH_CANDIDATE.
- If R already UP and it breaks a prior high in the direction of UP, that is a possible bullish BOS; if R already DOWN and it breaks lower lows, possible bearish BOS.
- If prior regime, pivot level or event completion is unknown, return INSUFFICIENT/UNKNOWN or provisional breach, not fabricated BOS/CHoCH.

This is semantic formalization of Coach's words, **not a numerically specified Coach algorithm**.

## C. Materially different candidate detector policies

**M0 discretionary/manual:** user-selected LH/HL with screenshot/source provenance; no automatic pivot hierarchy. Maximum transparency, low automation; manual cherry-picked pivots may bias results.

**M1 close-confirmed detector:** select an eligible previously confirmed swing LH/HL and require closed candle on opposite side; potentially less noisy than wick-only, but delayed and may miss fast signals. The exact pivot left/right bars, buffer and close condition are independently imposed.

**M2 wick-breach detector:** if bar high exceeds LH in prior downtrend or low dips below HL in prior uptrend, show PROVISIONAL_BREAK. Earliest observations but can reflect liquidity sweeps and reverse by candle close. Cannot present a wick breach as Coach-certified confirmed change.

**M3 two-stage detector:** candidate CHoCH on qualified level break, then separately await a follow-through BOS/displacement/retest for stronger context. More selective, but delay and new parameters; Coach p25 does NOT mandate follow-through BOS or retest.

**M4 dual structural scale:** internal swing CHoCH vs external/HTF CHoCH, with exact level/timeframe tagging. More faithful to multi-timeframe ambiguity but more opportunities for hindsight/hierarchy ambiguity.

No final detector has been chosen; keep alternatives falsifiable, explain how a given marker was established, and preserve simpler M0 baseline.

## D. Precisely what time is knowable? — anti-repainting contract

For each potential pivot or event, preserve:
- instrument and venue, product category, timeframe, OHLC candle integrity;
- turning point bar/time and its price, whether HIGH/LOW;
- left/right span or other pivot criterion, and **pivot confirmed/known-at bar/time**;
- prior trend classification known-at time, protected/reference swing identity and eligibility;
- potential break bar/time, wick breach vs confirmed close, exact buffer/tick and equality handling;
- first CHoCH candidate knowability and any future follow-through confirmation separate from candidate;
- HTF-context known-at time, no leaking developing HTF swing information into earlier LTF events.

**Invariant:** a marker attributed to a pivot at time t_p cannot be claimed as knowable before confirmation time t_k if the algorithm needs later right-side bars. An event meeting condition t_break < t_k is not a historically actionable confirmation based on that pivot. A visual label can optionally be drawn at the turning point, but it must disclose later detection; source fidelity does not authorize hindsight signals.

Official TradingView v6 repainting:
https://www.tradingview.com/pine-script-docs/concepts/repainting/
Official HTF request:
https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/

## E. Edge cases that can refute a naïve universal CHoCH rule

1. A downtrend LH is wicked through but bar closes back below; wick-only and close-only policies disagree.
2. A prior uptrend HL briefly pierced then close reclaims; do not automatically equate with sustained bearish regime.
3. A small internal LH breaks during a still-bearish external structure; preserve timeframe and pivot scale.
4. Last visual LH formed only two bars ago and a right-bars pivot policy has not yet confirmed it; no earlier known level.
5. Multiple eligible LH levels (minor and major) imply different CHoCH timing; pivot-selection rule cannot be silently skipped.
6. Equal LH/HL and ticks at level produce no strict break; equality and tick tolerance choices matter.
7. Price gaps across reference level; break observed but no proof of fill at level.
8. A bullish CHoCH candidate occurs and later price makes new LL; it failed as sustained reversal.
9. CHoCH candidate later bullish BOS confirms further structure; if M3 used, distinguish both known-at timestamps rather than backdate BOS to CHoCH.
10. BOS event and CHoCH occur on different timeframes in same minute; no contradiction if each timeframe is tagged.
11. Historic pivot plotted on turning bar with detection after several right bars; forbid action labeling on earlier pivot time.
12. If first confirmed bar after pivot is already beyond swing level, document whether event detection is retrospective or too-late, no manufactured earlier opportunity.
13. No prior coherent HH/HL or LH/LL regime: one broken high should not automatically become CHoCH.
14. Venue/product change from XAUUSDT to XAUTUSDT or PAXGUSDT: never reuse structural levels or price units without distinct feeds.
15. Top-right original figure shaded green reward/red risk but no numbers; RR must be UNKNOWN.
16. Price returns to original demand zone but no CHoCH and later rallies: zone contact and structural break are different events; do not require both without source justification.
17. 15m bearish CHoCH during 4H UP pullback: keep 4H UP as potentially still valid; no automatic HTF reversal.
18. Historical tests with reversal figures selected after successful move may produce survivorship/selection bias; use unbiased chronological samples and negative cases.
19. Discontinuous exchange candles due to illiquid crypto token feed can produce false swings; data integrity and minimum history need checks.
20. A source F1 transitions through CHoCH and then BOS: do not assume every CHoCH always followed by BOS.

These are **planned tests**, none executed in Pine or real market. Numeric choices (left/right pivot bars, stop distance, price tolerance, confirmed-candle rule) are not yet selected.

## F. Comparative research and future validation

Compare source-visible/manual swing labels against:
- M1 confirmed close detector; M2 wick provisional; M3 two-stage follow-through; M4 dual-scale structural context.
- On the same predeclared completed crypto OHLC test sets, record marker time versus information arrival, missing pivots, rejected/missed candidates, false-break frequency, number of discretionary swing choices, and chart legibility.
- Use separate held-out histories with transaction costs and actual entry/stop rules only if later pursuing strategy profitability. CHoCH counts and pretty diagrams alone are not evidence of edge.
- Maintain source tags: COACH_EXPLICIT / PCSS_INTERPRETATION / INDEPENDENT_HYPOTHESIS / TESTED (only after actual tests).

## G. Ponder recommendation, not a code decision

**Current best research direction:** preserve a visibly **PROVISIONAL vs confirmed-level-break** distinction; maintain a **prior regime + reference LH/HL + detection-time** event record. Show that CHoCH is a possible shift, and do not turn it into an automatic BUY/SELL or confirmed lasting reversal. Investigate M0 (manual) and M1 (close-confirmed) first; retain M2 wick as early-warning presentation, M3/M4 later if they justify complexity.

**Unresolved:** swing hierarchy and pivot method, wick/close/volume/displacement, thresholds, BOS-follow-through requirement, entry/stop/TP, multi-timeframe semantics and empirical performance. No implementation or actual test results exist.

**Next user-directed PCSS lesson:** Lesson 21, original PDF pp26–28 on 4H/1H TON/USDT case; include screenshots and all text, then proceed to the document's Q&A/notes rather than stopping at the 21 numbered lessons.
