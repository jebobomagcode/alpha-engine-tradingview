# Lesson 13 — Countertrend versus HTF Alignment; Risk/RR Formalization Candidates

**Status:** OPEN RESEARCH ONLY — no Pine Script, chart-runtime test, backtest, orders or deployment.
**Source:** [Coach PDF pp.17–18](../../sources/coach%20trading%20lessons.pdf), [Lesson 13 source-complete PCSS](../lessons/13-manage-your-risk-sol.md). 2026-11-09 (Asia/Manila).
**Crypto-only scope:** separate venue/product identity for SOLUSDT example and future XAUUSDT, XAUTUSDT and PAXGUSDT. No other trading project reused.

## Exact source observations

4H UP HH/HL, resistance near 87, support 85.2–85.5, no down BOS. 1H still bullish but weaker, potential CHoCH, bearish FVG 86.4–86.8, demand 85.6–85.8. 15m lower highs, declining RSI, possible CHoCH, small bearish OB 86.5–86.7.

SHORT: E in [86.4,86.7], S=87.2, T1=85.8, T2=85.3, T3=84.8 if full pullback, countertrend intraday/scalp. LONG alternative: wait for demand 85.2–85.6, 15m CHoCH and bullish displacement; entry after confirmation; S<84.9, T1=86.5, T2=87+, HTF-aligned swing. Full source images show 15m/1H/4H, but do not establish exact executed orders or a live exchange.

## 1. Mathematical audit and conditional risk

For linear short quote-unit price distance:
\[
R=S-E,\qquad G_i=E-T_i,\qquad \rho_i=G_i/R.
\]
With E varying between 86.4 and 86.7 and S=87.2, risk varies between 0.8 and 0.5. Since \(d\rho_i/dE=(S-T_i)/(S-E)^2>0\), endpoint RRs are valid extrema:

| Target | E=86.4 | E=86.7 |
| --- | ---: | ---: |
| TP1 85.8 | 0.75R | 1.8R |
| TP2 85.3 | 1.375R | 2.8R |
| TP3 84.8 | 2.0R | 3.8R |

**These are not achieved profits, win probabilities or actual account PnL.** Multi-target realized RR cannot be computed absent quantity fractions, fills, time sequence and costs. Hypothetical weighted all-target outcome \(\sum_i w_i\rho_i\) would require \(w_i\ge0\), sum weights 1 and all exits filled as assumed; those assumptions are not in Coach's document. TP3 is below stated 4H support 85.2–85.5.

For LONG, E unknown, S strictly below 84.9 and TP2=87+ not a unique exact number; ratio \((T-E)/(E-S)\) **cannot be uniquely evaluated**. Do not silently replace “below 84.9” with 84.9.

## 2. MTF classification candidates — not executable Coach rules

- **HTF_UP, 1H_WEAKENING, 15M_BEARISH_POSSIBLE_CHANGE:** report all three, not one absolute market state.
- **COUNTERTREND_PULLBACK_WATCH:** 4H UP, LTF short context and zone contact with qualifying bearish evidence; user may study a short but no automatic order.
- **HTF_ALIGNED_PULLBACK_WATCH:** 4H UP, lower demand reached, subsequent 15m bullish CHoCH/displacement condition; potential trend-aligned long.
- **WAIT / INSUFFICIENT:** missing HTF, zone, close, protected swing, actual entry/SL/TP or data quality issue.
- **UNKNOWN_RR:** no exact entry/stop, position size, target or allocation; do not invent.
- **NO_VALIDATED_EDGE:** qualitative “safer” or “higher probability” is Coach's claim, never a calculated metric without evidence.

**Competing simpler baseline:** manual multi-timeframe observation with no signal label. It could be safer until CHoCH/OB/FVG criteria become precise.

## 3. Important ambiguities

- Source simultaneously says 15m “possible CHoCH already” and Coach “respect ... CHoCH confirmation”. Exact structural break threshold and known-at timestamp unprovided.
- “Near overbought” 4H RSI≈63.88 is below conventional Wilder 70 threshold. Official explanation: https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/ . Dedicated RSI lesson occurs later; no project RSI cutoff selected.
- The FVG and OB numeric bands are in Coach's prose, not clearly annotated/deterministically derived from cropped screenshots.
- 4H support [85.2,85.5], 1H demand [85.6,85.8], long demand [85.2,85.6] are different context bands; never pretend they are identical.
- The 15m and 1H can be locally bearish/weaker despite bullish 4H. HTF precedence, conflict policy and short eligibility need explicit source-wide audit.
- “Scalp/intraday only” is qualitative, not a specified maximum bars-held parameter.
- Perpetual contract maintenance, liquidation, quantity, funding, spread and slippage not provided by Coach.
- The source screenshot dates/exchange are not fully verifiable; do not market example as current opportunity.

## 4. Planned disconfirming fixtures — NONE EXECUTED

1. 4H bullish and 15m bearish: keep source trend and countertrend label distinct.
2. Weak 1H CHoCH formation without confirmed break: provisional not confirmed.
3. Short price in supply zone but no qualified rejection: WAIT.
4. Long price reaches demand but lacks 15m bullish CHoCH or strong displacement: NO SETUP.
5. Confirmation candle forming then reversing: do not backdate confirmed event.
6. Short entry 86.4 TP1 85.8: report 0.75R before fees, not 1R.
7. Short entry 86.7 TP3 84.8: report 3.8R only if price actually reaches TP and fills.
8. TP3 84.8 is beyond 4H support: report obstacle, not a guaranteed full pullback.
9. Multiple TPs with no quantities: refuse single aggregate RR.
10. Long zone touched, unspecified exact entry/SL: return RR unknown.
11. No false “overbought” source-coded at RSI=63.88 with 70 threshold.
12. Unconfirmed 4H candle and known confirmed 15m bearish candle: preserve separate completion times.
13. A screenshot with no actual FVG/OB annotations: retain written claims as Coach assessments only.
14. Swap SOL to a gold-related crypto product: recompute tick, feed, quantity and costs, never copy source levels.

## 5. Future verification boundary

Once coding and tests are separately authorized: test time-causality in Pine, 4H/1H/15m source alignment, realistic fills, multi-target quantities, remaining position stops, funding and commission. Official TradingView: https://www.tradingview.com/pine-script-docs/concepts/strategies/ ; repainting: https://www.tradingview.com/pine-script-docs/concepts/repainting/ .

Use predeclared market history and holdouts to evaluate whether HTF-aligned setups actually outperform countertrend cases; avoid selection bias from a single attractive screenshot. No empirical edge established.

**Ponder direction:** do not impose a blanket no-countertrend rule, because Coach explicitly describes a countertrend short; instead mark it as conditional and higher-risk context while preserving no-trade uncertainty and objective risk arithmetic. No numerical parameters or final strategy rules accepted.

**Next on owner instruction:** Lesson 14, Fibonacci Retracement, PDF page 19.
