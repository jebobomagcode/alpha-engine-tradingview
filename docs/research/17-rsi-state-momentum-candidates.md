# Lesson 17 — RSI Descriptive States and Candidate Confirmation Research

**Status:** OPEN RESEARCH ONLY. No Pine coding, chart acceptance, backtest, trade or deployment. 2026-11-09 Asia/Manila.
**Coach's sole source:** [Original PDF p22](../../sources/coach%20trading%20lessons.pdf), [PCSS source audit](../lessons/17-rsi-relative-strength-index.md). All proposals below are independent and must not be passed off as Coach-written rules.
**Scope:** crypto including different venue-qualified XAUUSDT, XAUTUSDT, PAXGUSDT products.

## Source truth

Usual RSI length 14; reference lines 70 overbought, 30 oversold, 50 momentum bias; RSI above 70 strong buying pressure, below 30 strong selling pressure, above 50 bullish and below 50 bearish momentum. Strong trends can maintain high/low readings. Do **not** blindly short overbought or buy oversold. Best uses: confirmation, momentum, confluence. Price action/market structure priority. Divergence deliberately not taught.

## Independent numerical reference, not a Coach formula

With G,D the nonnegative Wilder-smoothed average gain/loss values, use RSI=100*G/(G+D) when G+D>0. State seeding/warmup, price input and missing bars. Values 0,50,100 are mathematical boundaries with applicable assumptions, not source trade triggers. At both G=D=0, behavior must be decided/tested rather than inventing a Coach value.

TradingView official [RSI](https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/) documents length 14 and price source Close as UI defaults (separate from Coach), and [repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) describes live RSI value changes.

## Two descriptive dimensions, never an automatic BUY/SELL button

- Midpoint state: RSI>50 = bullish-momentum reading, RSI<50 = bearish-momentum reading, RSI=50 = **SOURCE_UNSPECIFIED_EQUALITY**.
- Extreme state: RSI>70 = overbought condition, RSI<30 = oversold condition, RSI 30–70 inclusive = *not strict Coach-labeled extreme*, with equality explicitly noted.
- The states overlap. RSI 75 = bullish momentum + overbought, not automatic SHORT. RSI 25 = bearish momentum + oversold, not automatic LONG.
- A separate structural state must remain available, especially if 4H trend contradicts 15m RSI.
- Distinguish real-time provisional reading from closed-bar confirmed reading, and record known-at timestamps.

## Four competing bounce/rejection definitions for future evaluation

1. STRICT_CROSS: completed RSI moves <=50 to >50 for bullish, >=50 to <50 for bearish.
2. MIDPOINT_HOLD: RSI remains on its trend side, approaches 50 within a parameterized margin and turns away.
3. FAILED_RECLAIM: midpoint temporarily crossed then rejected within N bars.
4. MOMENTUM_SLOPE: RSI above/below 50 and rising/falling without a midpoint touch.

These definitions are **not equivalent**; none is explicitly chosen by Coach's Lesson 16 or 17. No N, margin, or RSI source has been approved. Avoid the “five confirmations = independent probabilities” mistake because RSI, EMA and structure derive from overlapping OHLC.

## Research baselines and planned disconfirming cases — NONE RUN

- Minimal structural+zone+confirmed-candle baseline without RSI; compare to addition of RSI midpoint or extreme conditions in separate held-out datasets.
- RSI=75: overlapping >70/>50; no automatic short. RSI=25: overlapping <30/<50; no automatic long.
- RSI=50, 30, 70 exactly: equality policy must be explicit.
- Stable 4H bullish structure with 15m RSI=45: timeframes disagree without forcing bearish HTF.
- RSI sequence 47→52 vs 54→50.5→53: cross versus hold-and-bounce differ.
- RSI sequence 46→49→44 vs 48→52→47: rejected midpoint versus failed reclaim differ.
- Forming RSI momentarily >70 or >50 then closing below: do not claim confirmed alert at the earlier time.
- Very few bars, missing data or flat constant close where G=D=0: return INSUFFICIENT or explicit computational rule.
- Cross-product feed substitution: RSI from XAUTUSDT or PAXGUSDT is not the same history as an XAUUSDT perpetual.
- Strong trends with RSI continuously extreme: any RSI-only countertrend idea can fail repeatedly.
- Coach's Lesson 13 countertrend short was multi-factor; do not falsely present it as an RSI-only exception.
- Divergence as a possible *external enhancement* must never be attributed to Coach.
- Evaluate after-cost net expectation, false signals, lag, sample counts, robustness across crypto symbols and out-of-sample intervals before calling anything superior.

**Ponder direction:** Prefer an RSI *descriptive pane* with confirmed/provisional states and source-qualified extremes. Compare its additional value against no-RSI baseline before making RSI an execution gate. Method parameters, risk management and final indicator-vs-strategy choices remain open.

**Next owner-directed study:** Lesson 18 — EMA, starting at original PDF p23.
