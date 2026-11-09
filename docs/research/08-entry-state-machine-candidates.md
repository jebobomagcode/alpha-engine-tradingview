# Lesson 08 — Gated Entry Workflow: Formalization and Validation Candidates

**Status:** RESEARCH-ONLY / OPEN_UNRESOLVED. No Pine code, compilation, backtests, deployment or trading.  
**Date:** 2026-11-09 (Asia/Manila).  
**Coach source:** [original PDF page 10](../../sources/coach%20trading%20lessons.pdf); [complete Lesson 08 PCSS](../lessons/08-trading-entry-workflow.md).  
**Owner implementation scope:** cryptocurrency markets with gold reference perpetual XAUUSDT and gold-backed token pairs XAUTUSDT / PAXGUSDT as **distinct** venue/product types.  
**Main new finding:** Original Coach Page 10 **gates LTF confirmation behind prior HTF zone contact** and offers **three alternative** confirmations, then allows **next structural target OR 1:2 / 1:3 RR**. Exact operation remains underspecified.

## A. Source-backed workflow requirements

Coach-explicit:
1. Use HTF 1H or 4H: find support/resistance, mark swing HH/HL or LL/LH, identify trend/bias (focus buy in uptrend; sell in downtrend).
2. Wait for price to reach the preidentified applicable zone; if it does not reach, **NO TRADE**.
3. After contact, inspect LTF (Lesson 04 specifies 5m or 15m).
4. Look for one of: bearish/bullish engulfing (preferred), rejection long wick followed by a follow-through candle, strong large-body candle. No need for "3 candles"; one qualifying strong confirmation is enough.
5. Do not enter before confirmation candle closes.
6. SL above resistance for short, below support for long.
7. TP at next support/resistance **or** 1:2 / 1:3 planned RR.

No "automatic buy" or bot order is authorized; this is a source interpretation for future research tooling.

## B. Candidate causal state model (not accepted code)

Potential immutable event attributes:
- instrument/exchange/product ID, chart time and data status;
- HTF context and zone **known-from timestamp**, price interval, invalidation condition;
- bias direction and confirmation time;
- LTF contact bar with known-at timestamp;
- geometry event type and completion bar;
- hypothetical entry decision timestamp **after** confirmation close, fill model;
- SL, TP, RR policy, tick/contract metadata, fees and limitations.

Illustrative transitions:
- `NO_HTF_CONTEXT/UNKNOWN_BIAS` -> `WAIT_ZONE`;
- when price actually reaches preexisting appropriate zone, `ZONE_CONTACT` -> `WAIT_CONFIRMATION`;
- only directionally aligned, completed qualifying event -> `CONFIRMED_SETUP`;
- next evaluate entry/SL/TP/realistic costs -> `RESEARCH_ELIGIBLE` or `NO_TRADE`;
- if price never reaches zone -> `NO_TRADE_ZONE_MISSED`, not a late BUY/SELL;
- if data is stale, zone or risk facts unknown -> `INSUFFICIENT`, not fabricated precision.

This can be seen as a causal state machine rather than a single conjunctive Boolean on a historical bar. Event ordering matters. Exact expiry/zone invalidation and recontact rules remain open.

## C. Zone contact — candidate mathematical definitions

Let prior-known support/resistance zone be interval \([z_L,z_H]\), a **subsequent** bar high \(H_t\), low \(L_t\) and close \(C_t\). Candidate modes:
- **Wick/range overlap:** \(L_t\le z_H\) AND \(H_t\ge z_L\). Captures a one-tick spike.
- **Close inside zone:** \(z_L\le C_t\le z_H\). Stricter, may miss fast reactions.
- **Body overlap:** intervals \([\min(O_t,C_t),\max(O_t,C_t)]\) and zone intersect.
- **Proximity/volatility-adaptive touch:** test distance against prior-known ATR or ticks; this is not Coach-explicit and may introduce more subjectivity.

These can disagree. Do not define a universally safe "touch" without source support; compare candidates later using sensitivity and false-event checks. Every zone must be established at a clock time **before** the alleged contact, avoiding hindsight.

## D. Confirmation alternatives — edge cases

### 1. Engulfing

Recall Lesson 06 candidate strict body engulf vs full-wick and weak partial variants. It requires two bars by geometry, even though the **confirmed event** can be registered at the second candle's close. Direction must match HTF bias and appropriate zone.

### 2. Rejection + follow-through

A long rejection wick candle PLUS later confirming candle. Unknown:
- wick length ratio, body size, which zone edge is rejected;
- follow-through directional close requirement;
- whether it must exceed rejection high/low or just close directionally;
- how many bars may intervene;
- whether confirmation must occur within zone, after leaving, or before invalidation.

The phrase "1 strong confirmation enough" does NOT compress this two-stage event to a single candle. Source language needs to be preserved, not overwritten.

### 3. Strong candle

Body large relative to what? Candidate comparisons: body/range, rolling median body, ATR multiple, volume-adjusted body, percentile by instrument and timeframe. None supplied by Coach. No default threshold selected or taken as equivalent to predictive power.

**Potential ordering for evaluation:** detect all three candidate types as alternative evidence, then record which one (if any) is *satisfied first as of its actual known-at time*. Do not require all, and do not count multiple correlated variants as independent confirmations or assign artificial probabilities.

## E. Entry and execution timeline

Coach: entry **after the confirmation candle closes**.

If signal bar closes at \(t_c\), decision is knowable no earlier than \(t_c\); actual simulated/live fill may be later and at another price.

Official TradingView:
- Bar state confirmation: https://www.tradingview.com/pine-script-docs/concepts/bar-states/
- Strategy broker emulator fills and lookahead: https://www.tradingview.com/pine-script-docs/concepts/strategies/
- Repainting / HTF requests: https://www.tradingview.com/pine-script-docs/concepts/repainting/

Do not assume a bar's final OHLC before it closes. Do not leak future-confirmed HTF pivots into an earlier LTF alert. Explicitly test what occurs if zone contact and confirmation appear in one LTF candle, since the source does not specify whether the same candle can serve both purposes.

## F. SL and TP conflict — important research choice

Coach says SL **outside** relevant zone (below support for buy, above resistance for sell). He allows:
- next structural support/resistance TP, OR
- 1:2 / 1:3 RR target.

**Counterexample, not actual market data:** Long entry 100,100, SL 99,750 gives risk 350; next resistance 100,450 yields 1R. Fixed 2R target 100,800 sits above next resistance. Coach does not specify:
- whether a 1R structural target is acceptable;
- whether to skip trade if structural next-level target violates minimum RR;
- whether to choose RR target irrespective of intervening resistance;
- whether partial exits, scale-outs or adjustments are valid.

Research alternatives to compare once permitted:
A. Next-level first (source's structural branch).
B. Minimum-reward-to-risk condition; skip if next level is too near (independent risk filter).
C. Fixed 2R/3R mode (source's arithmetic branch).
D. Separate hypothetical targets, report conflict and **do not claim a unique Coach entry**.

Default prudential design candidate: show both and mark `TP_POLICY_UNRESOLVED` until owner/empirical evidence selects a policy. Not a settled rule.

## G. Proposed test inventory (NONE RUN)

- HTF UP/support reached; closed bullish engulf -> directional candidate after close.
- HTF DOWN/resistance reached; closed bearish engulf -> candidate.
- HTF bullish but price never reaches support; bullish engulf elsewhere -> NO TRADE.
- Touch on wick only vs close inside zone: classification differs.
- Support discovered only *after* alleged contact -> reject as retroactive.
- Engulfing before touching zone -> not valid unless a separate post-contact confirmation occurs; precisely specify event sequence.
- Rejection candle plus timely follow-through -> potential confirmation event; wick alone insufficient under that variant.
- Large body candle before closing reverses by close -> no final strong-candle confirmation.
- “No need 3 candles” should not lead implementation to reject two-candle engulfing or rejection+follow-through.
- Entry order generated on bar close; emulator next-bar/tick fill; expected vs realized RR updated after fill.
- TP at next resistance yields 1R while 2R target beyond that resistance; unresolved target-policy alert.
- Stop within support (not below): violates Coach's outside-zone placement rule.
- HTF 1H UP, 4H DOWN; no invented precedence.
- Instrument data mismatched between FX gold chart, Binance XAUUSDT perpetual and PAXG/XAUT token venues; reject or clearly qualify.
- Persistent touch/zone invalidated/time elapsed and chart session gaps -> undecided expiration logic.
- Synthetic/Heikin Ashi bars vs standard OHLC must be explicitly controlled before claiming historical real-market fills.

Actual source fidelity, runtime, strategy, cost and empirical gates must be checked separately if implementation is later authorized. Source-study completion does not establish algorithm correctness or trading profitability.

## H. Ponder decision and constraints

**Working design direction:** event-driven evidence with explicit WAIT/NO TRADE, optional independent enhancements, and instrument-specific risk/fee caveats. Prioritize fewer but causally accurate candidate states over numerous repainted historical BUY/SELL labels. Preserve both Coach's original alternatives and the unresolved priority between target rules.

**No feature locked:** numerical trend/zone algorithms, touch type, confirmation ratios, stop buffer, RR target selection, position size, expiry, risk tolerance and alerting remain proposals. No Pine scripts created.

**Next study:** Lesson 09 — Support & Resistance, original PDF page 11, only at the next owner-directed continuation.
