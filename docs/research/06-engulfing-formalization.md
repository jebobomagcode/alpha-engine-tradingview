# Lesson 06 research — source-grounded engulfing and candidate formalization

**Date:** 2026-11-09 (Asia/Manila)  
**Status:** OPEN / RESEARCH ONLY — no authorized or executed Pine code, script compilation, signal backtest or trading.  
**Primary source:** [Coach PDF p. 8](../../sources/coach%20trading%20lessons.pdf), [Lesson 06 full audit](../lessons/06-engulfing-pattern.md).  
**Owner scope:** crypto market focus, including XAUUSDT, XAUTUSDT and PAXGUSDT separately.

## A. What Coach actually gives, and what he leaves open

**COACH_EXPLICIT:** bullish = BIG green after red engulfs previous candle at support; buyers enter, possible rise. Bearish = BIG red after green engulfs previous candle at resistance; sellers enter, possible fall. Three image panels illustrate pairs near turns, bearish continuation after the pattern, and stronger vs weaker bullish engulfing silhouettes.

**NOT SPECIFIED:** full real-body vs wick-range engulfing, inequality strictness, min relative body size, pattern strength threshold, minimum trend, zone quality, number of previous bars, volume requirement, confirmation delay, entry/SL/TP placement, HTF-LTF mapping for this exact pattern, specific fees, or actual odds of reversal.

## B. Proposed competing geometric interpretations

Let \(O_1,H_1,L_1,C_1\) be the previous candle, \((O_2,H_2,L_2,C_2)\) the current one. Require finite valid OHLC for both; candle colors determined from actual opening and closing prices, not chart style.

| Variant | Bullish candidate | Bearish candidate | Note |
| --- | --- | --- | --- |
| A — real-body engulfing | \(C_1<O_1\), \(C_2>O_2\), \(O_2\le C_1\), \(C_2\ge O_1\) | \(C_1>O_1\), \(C_2<O_2\), \(O_2\ge C_1\), \(C_2\le O_1\) | Need equality vs strict containment policy |
| B — full candle / shadows | Variant A plus \(L_2\le L_1\), \(H_2\ge H_1\) | Same extra constraints | More restrictive, not Coach-determined |
| C — partial/weak | Overlap, relative size and directional price close subject to predeclared thresholds | Symmetric counterpart | Inspired by PDF's “weak engulfing” illustration; **not source-defined as an algorithm** |
| D — no pattern | Do not require engulfing | Do not require engulfing | Necessary negative control for empirical value |

For strict *larger body*, require at least one containment inequality strict; do not necessarily require a price gap. No threshold chosen.

### Derived normalized features for future tests — purely experimental

Body \(B_i=|C_i-O_i|\), range \(R_i=H_i-L_i\), with \(R_i>0\) for valid normalization.

- Body-size ratio: \(\beta=B_2/\max(B_1,\delta)\), where \(\delta\) is a well-defined tick-scaled floor; avoid zero division and note that any floor choice can bias illiquid markets.
- Bullish normalized body extension beyond previous high body boundary: \(\epsilon_{\mathrm{bull}}=(C_2-O_1)/R_2\).
- Bearish normalized extension: \(\epsilon_{\mathrm{bear}}=(C_1-C_2)/R_2\).
- Candle body fraction: \(\gamma=B_2/R_2\).
- Optionally overlap fraction / current range volatility normalization; no predictive confidence assigned.

**Caution:** a large body ratio does not guarantee *containment*. Example source audit: prior red \(O_1=102,C_1=100\), new green \(O_2=100.5,C_2=103\) has \(B_2>B_1\) but fails body engulf because \(O_2>C_1\). The lower-right **weak** original drawing appears similar: it does not necessarily meet strict Option A. Keep a separate shape flag rather than mislabeling.

## C. Synthetic fixture matrix (NOT historical validation)

| ID | Prior O,C | Current O,C | Expected |
| --- | --- | --- | --- |
| BULL-1 | 102,100 | 99.5,103 | strict bullish body engulf |
| BULL-EQUALITY | 102,100 | 100,103 | inclusive bullish, may fail gap-strict alternative |
| BULL-PARTIAL | 102,100 | 100.5,103 | larger green, not full engulf |
| BEAR-1 | 100,102 | 102.5,99 | strict bearish body engulf |
| DOJI-PREV | 100,100 | 99,102 | prior candle not red/green; cannot meet strict 2-color rule |
| DOJI-NOW | 102,100 | 100,100 | current doji, cannot meet strict bullish rule |
| WICK-ONLY | previous range larger than second range but body included | — | body true, full-range false |
| FORMING | provisional 2nd green becomes red at close | — | provisional only; no final confirmed engulf |
| MISSING | NaN/NA / impossible OHLC | — | UNKNOWN, not false confident classification |

No fixture represents a funded user trade or a verified exchange candle.

## D. Context and time-of-knowledge tests

- Pattern detector must know the previous completed candle and current **closed** candle before marking confirmed pattern.
- A support/resistance zone derived from pivots must have a recorded *known-from* time, not be backdated with hindsight.
- Requiring a zone and HTF bias is Coach-contextual; numerical implementation of zone and trend remains pending Lessons 07, 09–12 and source-specific confirmation.
- Distinguish an engulfing geometry flag from “trade confirmed” and “profitable expectation.”
- Do not conflate source's right-panel *later downtrend* with confirmation available at the engulfing candle's close.

Official TradingView implementation references (independent):
- [Bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/) — `barstate.isconfirmed` becomes true on the realtime bar's closing update and historical bars; not reliable inside `request.security()`.
- [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) — realtime high/low/close update while a bar forms, and incorrectly requested higher-timeframe data can leak future information.
- [Execution model](https://www.tradingview.com/pine-script-docs/language/execution-model/) — current realtime bar calculations can roll back; confirmed OHLC persists after close.

## E. Planned discriminating evaluation

**H0:** engulfing + location has no incremental predictive/decision utility over zone and trend without engulfing.

**H1:** strict body engulf with independently documented zone definition improves relevant out-of-sample outcomes compared with absence of the pattern, after transaction costs.

**H2:** relaxed/weak classifier improves sensitivity but degrades precision; overly strict full-shadow engulf may eliminate too many genuine cases.

Design: fix exact symbol/venue/product, 5m/15m chart and previously confirmed 1H/4H context; predefine target and stop rules from later lessons, holdout periods and realistic fee/slippage assumptions; measure false positives, number of setups, classification consistency, realized P&L, drawdown, stability by regime, and uncertainty. Analyze XAUUSDT derivative vs XAUT/PAXG token markets separately. A visually convincing chart is not proof of future edge.

**Alternative:** simpler detector only reports shape, no entry decision or enhanced labels until zone+confirm methodology formalized. This could be the safest version.

## F. Open questions / checkpoint

- Body vs wick engulfing.
- Equality boundary/tick normalization.
- “Strong”/“weak” image interpretation and whether partial overlap merits a separate label.
- How to define valid preceding trend or tested support/resistance.
- Candle close vs confirmation after subsequent bars.
- Whether volume/ATR/regime additions help or merely overfit.
- Correct handling of Heikin Ashi/nonstandard bars, gaps and vendor feeds.
- Cross-symbol data availability and contract identity, particularly gold-linked tickers.

No parameter values, code implementation, or trading claims approved. **Next PCSS:** Lesson 07 — Market Structure and Confluence, PDF p. 9, when the owner directs.
