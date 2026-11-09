# Lesson 19 — Time-Causal Top-Down RSI/EMA Confluence: Research Candidates

**OPEN RESEARCH ONLY; no Pine implementation, backtest, chart acceptance, trades, alerts or deployment.** 2026-11-09 Asia/Manila.
Coach-origin source: [original PDF p24](../../sources/coach%20trading%20lessons.pdf), [PCSS study](../lessons/19-rsi-ema-topdown-analysis.md). Market scope: crypto with separate venue/product identity for XAUUSDT, XAUTUSDT and PAXGUSDT. No legacy-project reuse.

## Exact source contract

STEP1: HTF (4H/Daily/1H) market structure, EMA direction, RSI momentum. Bullish example: price above EMA50, EMA sloping upward, RSI above50.
STEP2: do not chase impulses; wait for retracement, EMA retest, FVG revisit, key support/resistance.
STEP3: LTF (15m/5m) rejection candles, BOS/CHoCH, RSI holding momentum and EMA S/R respected.
LONG: HTF bullish/above EMA/RSI>50 and LTF EMA/FVG retrace, RSI bounce >50, bullish rejection.
SHORT: HTF bearish/below EMA/RSI<50 and LTF EMA resistance, RSI rejection <50, bearish confirmation.
LONG/SHORT examples are repeated from Lesson16 p21, not new empirical samples or a complete executable strategy.

**Source gaps:** exact HTF hierarchy, indicator source/timeframes, slope horizon, status of forming bars, location list AND/OR, slash BOS/CHoCH order, EMA/FVG logic, RSI-holding event, candle confirmation geometry, trigger/expiry and risk.

## Proposed architecture alternatives — not approved rules

**M0 descriptive dashboard:** full HTF trend and EMA/RSI context, pullback location, LTF confirmations and reasons for WAIT/INSUFFICIENT. Closest to discretionary source, little automated execution.

**M1 minimal causal baseline:** confirmed HTF structural bias + previously knowable S/R or qualified zone + closed LTF directional candle. EMA and RSI shown as independent fields, not mandatory gates. Fewer parameters.

**M2 strict continuation detector:** explicit instrument/timeframe choice, fixed EMA/RSI definitions, exact touch and rejection geometry, close/HTF confirmation and configurable expiry; requiring every specified condition is an independent formalization, NOT a source-stated hard six-gate rule.

**M3 multi-regime taxonomy:** source-distinguished HTF-aligned continuation, Lesson13 countertrend scalp, Lesson10 range and WAIT/CONFLICT; flexibility vs greater complexity and overfit risk.

Working research preference: M0 and M1 first; use M2/M3 as falsifiable alternatives after full source audit. No numerical thresholds chosen.

## Exact EMA redundancy under narrow assumptions

For n>1 with alpha=2/(n+1) and same close-based EMA on same bar:
E_t-E_(t-1)=alpha*(C_t-E_(t-1));
C_t-E_t=(1-alpha)*(C_t-E_(t-1)).
Both multipliers strictly positive, so **Close above current EMA iff one-bar EMA slope positive**; likewise both negative or zero. Thus scoring both EMA50 conditions in Coach's Step1 example as independent votes would double count under these definitions. Coach's “sloping upward” may instead refer to multiple bars; source does not define it. No blanket claim that all longer-horizon EMA trends or RSI readings are redundant.

## Multi-timeframe causal contract

Every observation should retain:
- exact TradingView symbol/venue/product/timeframe;
- HTF structure origin and known-at time of confirmed pivots; chosen EMA length/source/confirmed update; RSI length/source/confirmed update;
- location type EMA/FVG/SR, formation and contact timestamps, expiry and reaction policy;
- LTF RSI holding/bounce/rejection *hypothesis identifier* and bar state;
- BOS/CHoCH protected swing and event timestamps, rejection candle close;
- actual eligibility, unknown/WAIT/conflict reasons and separately sufficient risk parameters.

Avoid historical future leaks: confirmed higher timeframe request via source expression offset with lookahead_on is a documented method, whereas unoffset lookahead_on leaks future HTF readings historically. A forming LTF RSI/candle can repaint. Official:
https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/
https://www.tradingview.com/pine-script-docs/concepts/repainting/
https://www.tradingview.com/pine-script-docs/concepts/bar-states/

**Unresolved:** the causal pipeline can operationalize first HTF, then contact, then confirm, but no exact numerical maximum delay or mandatory combined event grammar exists in Coach source.

## Planned disconfirming fixtures — not run

1. HTF bullish above EMA50 and RSI56 but no pullback => WAIT.
2. Retracement to FVG but no EMA contact => slash policy matters.
3. Zone touched but no LTF rejection or RSI momentum => WAIT.
4. Bullish rejection appears intrabar then closes bearish => confirmed candidate invalid.
5. HTF RSI>50 intrabar then HTF closes<50 => prevent backdated context.
6. Daily UP and 1H DOWN => preserve timeframe conflict instead of forcing majority.
7. Same-close one-bar EMA50 price side and slope as separate votes => reject redundant score.
8. Close>EMA50 but EMA50 declines across 5-bar horizon => possible, tests differing definitions.
9. CHoCH without BOS, or BOS without CHoCH => alternatives must be tested separately, not assumed identical.
10. FVG and EMA aligned from same impulse => confluence dependence may add little incremental evidence.
11. LTF signal happens before selected HTF pivot confirmation => cannot claim earlier knowability.
12. EMA50 selected for p24 bullish example but source LONG generic EMA => don't fabricate universal length.
13. SHORT reaches FVG but not EMA resistance => not source-explicit SHORT setup.
14. Reused Lesson16/Lesson19 examples => not independent measured repetitions.
15. Missing entry, stop, target or position quantity => RR_UNKNOWN, no order claim.
16. Change symbol between XAUUSDT derivative and XAUTUSDT/PAXGUSDT tokens => no shared candles.
17. Unrealistic backtest of lookahead values => reject inflated historical results.
18. Increasing number of confluence filters reduces sample size with no after-cost holdout improvement => prefer baseline.
19. Flat/ranging regimes repeatedly touch EMA while HTF/RSI mixed => WAIT or source-specific range method; no automatic trend continuation.
20. Chart reload changes prior unconfirmed 5m marker => technical nonrepainting check fails.

## Ponder outcome and next source

Use distinct structural, EMA and RSI observations without inventing hard all-gates or confidence percentages. Evaluate time-causality and baseline redundancy before optimizing backtests or trading. No financial edge demonstrated, no Pine behavior verified.

Next owner-directed lesson: **Lesson 20 CHoCH** from original PDF p25 including multiple figures. Do not auto-advance.
