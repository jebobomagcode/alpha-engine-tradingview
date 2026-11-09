# Lesson 04 research candidates — multi-timeframe context and causal signal timing

**Status:** PROPOSED / OPEN_UNRESOLVED. No Pine code, compilation, backtest or deployment.  
**Scope authority:** Coach PDF page 6 and [Lesson 04 PCSS](../lessons/04-time-frame.md).  
**Project market policy:** crypto including XAUUSDT, XAUTUSDT and PAXGUSDT, with distinct venue/product metadata.  
**Date:** 2026-11-09.

## What is actually Coach-explicit

- HTF 1H or 4H: trend plus zone/key support/resistance; no need to overconfirm.
- LTF 5m or 15m: wait for a pullback/bounce and confirmation candle, then evaluate entry, SL, TP.
- Specific narrated pairing: 1H/4H contextual basis and 5m entry example.
- No exact trend/zone/confirmation rules, no timeframe hierarchy on disagreements, no entry execution semantics on page 6.

## Mathematical and temporal data contract

For aligned complete periods of equal duration:
\[
N_{\mathrm{LTF}/\mathrm{HTF}}=\frac{T_{\mathrm{HTF}}}{T_{\mathrm{LTF}}},
\]
so one 1H bar contains 12 five-minute or 4 fifteen-minute bars; one 4H bar 48 five-minute or 16 fifteen-minute bars. Sessions, holidays, feed gaps, exchange timestamp conventions and account data limits can violate observed bar counts. Confirm timeframe relationships at configuration time rather than assuming any chart period is smaller.

OHLC aggregation over constituent bars:
\[
O_H=O_1,\ H_H=\max_i H_i,\ L_H=\min_i L_i,\ C_H=C_n.
\]
The finished HTF bar's final \(C_H,H_H,L_H\) are only finalized after the HTF period completes. A source-side zone algorithm can also have extra pivot confirmation delay. Each analytic output therefore needs at least:
- chart instrument identity and venue / trading product;
- source timeframe, bar open/close timestamps;
- **when the value became knowable** (available-from timestamp);
- confirmed / forming / invalid / missing source status;
- price-zone boundaries and validity/invalidation status;
- LTF event time and confirmation status;
- explicit reason if waiting / insufficient data / conflict.

## Viable system architectures (competing, no fixed selection)

**A. Confirmed HTF only:** last completed HTF context powers alerts/decision support. Avoids HTF repaint but lags current movements.

**B. Forming HTF context:** evolving context prominently marked provisional; may be useful visually but cannot be passed off as historical stable confirmation.

**C. Dual-channel:** confirmed reference state drives stable signal conditions; forming context rendered separately as diagnostic commentary, never silently blended. Tradeoff: extra complexity and potential chart clutter.

**Pragmatic option to investigate:** calculate entry logic on the chart's 5m or 15m timeframe and request 1H/4H context. A script running on a higher chart timeframe and sampling lower intrabars can omit events if implemented with single-value `request.security()`; arrays via `request.security_lower_tf()` address different requirements but have plan/runtime constraints.

## Official TradingView Pine constraints (independent technical evidence)

1. [Other timeframes and data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) warns about lookahead and explains confirmed HTF offsets and lower-timeframe intrabars.
2. [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) distinguishes live unconfirmed HTF behavior from historical results.
3. [FAQ: other data and timeframes](https://www.tradingview.com/pine-script-docs/faq/other-data-and-timeframes/) recommends the previous HTF expression (one-bar offset) plus `barmerge.lookahead_on` for confirmed HTF values, not an unoffset future-leaking `lookahead_on` call.
4. [Bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/) states `barstate.isconfirmed` does not solve HTF confirmation when placed inside `request.security()`.

**Reference semantics:** request only expressions that were knowable as of each LTF bar, with explicit lag policy. A script audit must find no future leak, including latent pivot detection and drawing zones backward in time. Use synthetic multi-TF OHLC fixtures plus actual Pine chart/reload evidence once implementation is authorized.

## Candidate model states (not agreed)

- No reliable market data / wrong product / missing timeframe history.
- HTF trend unknown or mixed; HTF zone absent or valid/expired/invalidated; confirmed/provisional context distinguished.
- LTF price outside or contacting relevant zone; pullback or bounce / rejection candidate.
- LTF confirmation pending / confirmed / invalidated.
- Entry/SL/TP present but risk-reward assumptions unverified; actionable research summary vs WAIT/INSUFFICIENT.

This section should not silently override Coach's “no need overconfirm”; additional risk filters are **independent extensions** and should be assessed for complexity vs accuracy.

## Evaluation plan (when later authorized)

- **Temporal tests:** HTF candle still forming, HTF candle closes, zone becomes knowable after pivot confirmation, delayed 4H information, mid-period conflict, chart reload consistency.
- **Timeframe tests:** 1H→5m, 1H→15m, 4H→5m, 4H→15m, HTF/LTF invalid or same TF, session and exchange gaps, timezone conversion and DST when relevant.
- **Market tests:** distinct venue/product feeds for BTC-like crypto, XAUUSDT derivative, XAUTUSDT and PAXGUSDT gold-backed token markets; do not transfer volume/funding/cost assumptions.
- **Ablations:** no HTF context, 1H only, 4H only, both, provisional diagnostics, with/without confirmation when explicitly defined later; compare after costs, predeclare markets/holdout periods to reduce overfitting.
- **Acceptance gate:** exact source fidelity, deterministic fixtures, actual Pine compilation and chart observations, historical/realtime consistency checks, real alert gating if permitted, and candid limits. No positive backtest implies guaranteed profitability.

## Unresolved until later source study

- HTF trend and support/resistance definitions.
- Which of 1H/4H takes precedence, and whether both are compulsory.
- LTF 5m/15m selection / confirmation-candle definition.
- How to set source-grounded entry, stop, target and invalidation.
- HTF confirmation delay vs reactivity tradeoff.
- Specific TradingView exchange IDs and available data for selected crypto/gold products.

**Next:** Lesson 05 (PDF page 7), Leverage and Margin. No code until owner authorizes it.
