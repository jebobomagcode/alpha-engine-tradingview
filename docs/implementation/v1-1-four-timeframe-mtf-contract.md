# v1.1 four-timeframe MTF specification — 4H / 1H / 15m / 5m

**Status:** OWNER REQUIREMENT RECORDED / PROPOSED ENGINEERING CONTRACT — 2026-11-14 Asia/Manila.
**Active decisions:** [D-038](../DECISIONS.md) (Binance USDⓈ-M USD-stablecoin perpetual-only, LONG/SHORT) and **D-039** (four-timeframe analysis).
**Acceptance:** NOT IMPLEMENTED / NATIVE NOT RUN. The accepted private TradingView v1 version 8.0, build `AE-0.1.11-0f4b3df98b90`, is preserved, with version 7 rollback. Do not present this specification as implemented functionality.

## User requirement and separation of product from methodology

The owner explicitly requires four timeframes in **multi-timeframe analysis: 4H, 1H, 15m and 5m**, while retaining D-038's exclusive Binance USDⓈ-M stablecoin-settled **perpetual** product scope and bidirectional LONG/SHORT research.

The four **timeframe identities** are owner-required. The detailed **roles** below are a recommended, independently specified engineering interpretation, not explicit numerical Coach prescriptions, and remain subject to falsifiable testing:
- **4H — macro regime/context:** broad swing context, source-qualified trend/regime, major supply/demand and conflicts.
- **1H — intermediate trend/structure:** HH/HL/LH/LL, recent confirmed reference, BOS/possible CHoCH, contextual locations and agreement/conflict with 4H.
- **15m — setup and area of interest:** nearest qualified candidate zones (OB/FVG/supply-demand), retracement/location context, emerging reactions, setup validity. A 15m event is not automatically a 5m confirmation.
- **5m — local trigger/confirmation:** causal bar-close contact, bullish/bearish reaction, reference consumption/invalidation and conditional **nominal** E/SL/TP/R. Qualify LONG and SHORT independently; no auto-trading.

No hardcoded majority vote among timeframes, no guarantee all four agree, and no undocumented assumption that a higher-timeframe trend makes a lower-timeframe setup valid. Explicit contradictions → WAIT / CONFLICT / REASSESS as warranted. Missing essential evidence → INSUFFICIENT. Optional countertrend rules would need separate objective definitions and tests.

## First chart integration — preserve v1 foundation

Use a **standard 5m TradingView chart of one positively qualified exact BINANCE USDⓈ-M PERPETUAL product** as the initial host chart. The analysis consumes native **completed 5m bars** and separately requests **15m/1H/4H confirmed data for that same ticker/feed**, never spot or a different product.

The current v1 `pine/alpha-engine-research.pine` permits only five exact Binance identities at 5m and uses 1H/4H prior-closed EMA context, **not a complete 15m MTF layer**. The 4H/1H/15m/5m target requires new independent work. If later enabling a 15m host chart, a 5m state cannot be reconstructed from a naive `request.security(..., "5", ...)` sample; use and validate true lower-timeframe intrabar handling (e.g. `request.security_lower_tf`) or gate the 15m host chart until feature-parity is demonstrated. 5m-only host initially is an **engineering sequencing recommendation**, not an owner refusal of four-timeframe MTF analysis.

## Causal evidence contract for each timeframe

Store/derive **per-product, per-timeframe**: source identity, exact bar open/close, confirming cutoff, data-known-at cutoff, feature values, warmup, source hash/provider where testable, validity/state and invalidation time. Distinguish a historical price pivot's origin from the later close that confirmed it; never place the discovery in the past.

At each closed 5m decision cutoff `T`:
1. Read the completed eligible 5m candle with cutoff `T`.
2. Use only **15m**, **1H** and **4H** bars already confirmed and available by `T`; never use the still-forming portion of a higher-period bar. Verify exact as-of behavior both at and between timeframe boundaries; report the *actual last confirmed close* for each layer.
3. Higher-timeframe Pine requests must use non-leaking confirmed values (typically history-offset expressions with `lookahead_on` when requesting strictly higher timeframes), with explicit warmup, gap and close-boundary tests. Validate behavior around 15m :00/:15/:30/:45, 1H and 4H rollover; do not use `barstate.isconfirmed` within a security request as a substitute for tested causality.
4. Missing 15m or HTF data/warmup → honest INSUFFICIENT/WAIT by feature; one layer's missing data must not be silently replaced with another layer's current value.
5. All four layers refer to the **same verified Binance USDⓈ-M perpetual's price feed**, consistent trade-price vs mark/index policy; no cross-symbol substitution. Preserve contract-status, tick precision and D-038 exclusions.

## Expected output and state policy

The dashboard should display four separate labelled panels or rows:
`4H: [context, latest confirmed close, source readiness]`,
`1H: [structure/context, latest confirmed close, readiness]`,
`15m: [zone/setup, latest confirmed close, readiness]`,
`5m: [reaction, last decision cutoff, readiness]`.
Show the relationship: `ALIGNED LONG`, `ALIGNED SHORT`, `MIXED/CONFLICT`, `WAIT`, `INSUFFICIENT`, or specific `REASSESS/INVALIDATED` *only when separately defined conditions justify the label*. Do not imply a numerical confidence score or statistical win probability without valid empirical calibration.

For SHORT, mirror the directional logic with separately tested bearish supply/resistance contact and stop-above-entry geometry; for LONG, preserve causal support/demand logic. A potential zone alone is not a trade signal. Disallow crossed or stale state/timestamps, expired/replaced references and future-borne FVG/Fib levels.

## Concrete new tests and evidence gates

- **Boundary as-of:** 5m close at 10:05 UTC uses latest confirmed 15m **10:00 UTC**, but no information from the 10:00–10:15 still-forming bar; at 10:15 the just-closed 15m data becomes eligible according to documented decision ordering. Repeat at 1H/4H cutoffs, including one 5m bar after rollover.
- **Frozen-prefix invariance:** append new bars to each timeframe and confirm every *earlier* 5m cutoff keeps identical MTF values, states and known-at times.
- **Full 4-way matrix:** 4H/1H up/down/mixed/missing × 15m ready/not-ready × 5m bullish/bearish/none, for both LONG and SHORT; selected rules must explain conflict/withholding and avoid majority voting.
- **Feed/contract adversaries:** BINANCE USDⓈ-M USDT and USDC PERPETUAL positive cases; Spot, COIN-M, dated futures and non-Binance negative cases; nonstandard OHLC and missing history negative cases.
- **15m feature parity:** test its pivot and AOI creation/retirement, timestamped FVG/OB/Fib lifecycles; adding 15m should not erase the accepted 1H/4H and 5m behavior.
- **Native+model audit:** validate Python source evidence against Pine as separately labeled model/model vs model/native comparisons. Existing `research/phase3_6/integrated_replay.py` has one externally supplied `confirmed_bullish_context` flag rather than a per-cutoff 4-timeframe ledger; extend without misrepresenting prior acceptance. Positive saved-script reload remains INSUFFICIENT until observed and is not a blocker to frozen tests.
- **Release isolation:** retain the 148 standard plus 21 separate historical structural regression acceptance, v1 source SHA and version 7 rollback. The successor requires new tests, native 5m chart checks, complete source identity, same-cutoff persistence and capability-specific failure explanations.

## References

- [Active Binance perpetual-only scope](v1-1-binance-usds-m-perpetual-qualification.md)
- [Work parity reconciliation](v1-1-work-parity-reconciliation.md)
- [v1 native release evidence](phase3-8-v1-stabilization.md#integrated-private-v1-release--2026-11-13-pht)
- TradingView [Other timeframes and data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) — confirmed HTF request technique and lower-timeframe intrabar caveat.
