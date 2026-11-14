# v1.1 — Binance USDⓈ-M perpetual-only qualification plan

**Status:** OWNER REQUIREMENT / DOCUMENTATION PROPOSAL — 2026-11-14 Asia/Manila.
**Active owner decision:** D-038 in [DECISIONS.md](../DECISIONS.md), superseding the broader D-037 target.
**Accepted v1 remains unchanged:** main `8e60a982385e46aa818acb49103f1dedbe856b77`; integrated Pine `6fe1f8718ba8b742be500262a1df84fbd933c871`; saved TradingView version 8.0 / build `AE-0.1.11-0f4b3df98b90`. Retain version 7 rollback.

## Exact new owner focus

**Only Binance USDⓈ-M linear perpetual swaps/futures that are quoted/settled in a USD-pegged stablecoin**, presently including USDT and USDC products, plus any other USD-stablecoin-settled Binance perpetual family that is explicitly verified and technically qualified later. Both LONG and SHORT *informational research* setups are required.

**Out of scope:** Binance Spot; COIN-M / inverse / coin-settled contracts, even if a ticker contains USD; delivery/quarterly/delivery-dated futures; options; other exchanges (Bybit, OKX, etc.); conventional forex, equities and PSE data feeds. A Binance USDⓈ-M gold-referencing perpetual such as XAUUSDT.P remains eligible if verified as a qualifying contract: the product is in scope by Binance **contract family**, not because its underlying is a cryptocurrency. No equivalence to tokenized spot gold is assumed.

The target is **all eligible contracts within that Binance perpetual family**, rather than an arbitrary five-symbol whitelist. "Eligible" and "verified/qualified" are distinct: no automatic claim that every listed contract works today, or that every related symbol can be reliably identified from Pine chart metadata alone.

## Instrument and data eligibility contract

1. **Venue and contract family:** exact TradingView BINANCE feed plus a positively confirmed Binance USDⓈ-M USD-stablecoin-settled `PERPETUAL` identity, not merely a ticker suffix, a 24/7 schedule or a quote containing `USD`. At qualification time, compare exact feed to Binance USDⓈ-M `exchangeInfo` contractType, quote/settlement/margin asset and status where available. Pine itself cannot be assumed to call Binance REST APIs or read all contract metadata; unresolved identity is `INSUFFICIENT`.
2. **Quotes and settlement:** USDT and USDC are initial targets. Other stablecoins require **positive confirmation of actual Binance USDⓈ-M perpetual support** and of price, quote, and settlement mechanics; do not assume FDUSD/other names are currently offered.
3. **Price inputs:** standard candles backed by the exact eligible contract's trade price. Mark price and index price are separate series, not interchangeable with trade OHLC; record what source is used. Do not mix Spot candles or COIN-M data into the analysis.
4. **Precision:** replace v1's `syminfo.mintick == 0.01` hard gate with validated symbol-relative tick arithmetic. Check min tick, price/quantity filters and numerical stability. E/SL/TP/R must remain **nominal research geometry** and never imply actual size, fee, funding, liquidation or fill.
5. **Market clocks:** preserve confirmed-closed-bar behavior and causal as-of timestamps, no lookahead. Initial existing research uses 5m with confirmed 1H/4H. Any higher chart timeframe is a separate validated extension; gaps and exchange interruptions must produce truthful status, not invented data.
6. **LONG and SHORT parity:** design directional support/demand and resistance/supply state machines with symmetrical readiness, contact, reaction, invalidation, risk geometry and provenance. The current v1 experimental reaction branch is bullish-only; do not describe v1 as a complete SHORT engine.
7. **Causal display:** retain reliable WAIT/INSUFFICIENT and qualification explanations; do not assume good trading outcomes. No live orders, automated trading, position sizing, guarantees or public TradingView publication are authorized.

## Owner-required MTF framework — D-039

The v1.1 research engine must analyze **4H, 1H, 15m and 5m** on the same qualified Binance USDⓈ-M perpetual product. Recommended role design: **4H macro regime**, **1H intermediate trend/structure**, **15m setup/AOI and zone lifecycle**, **5m close-confirmed LONG/SHORT reaction and nominal price geometry**. These roles are an independent implementation hypothesis; the four exact timeframes are owner-specified. Start on standard 5m host chart and request **confirmed** 15m/1H/4H data. For timeframes above the host chart, preserve known-at cutoffs, warmup/gaps and no-lookahead. Do **not** infer 5m events from one lower-timeframe sample on a 15m host. Mixed context remains informative; no forced majority vote. [Full four-timeframe contract and test matrix](v1-1-four-timeframe-mtf-contract.md). Current accepted v1 has 1H/4H research context on 5m but does not implement this four-layer model; new native work remains NOT RUN.

## Priority reconciliation with Work's v1.1 parity recommendation

Work proposed a read-only v1.1 model-vs-Pine parity audit starting from PAXGUSDT Spot 5m and the currently unverified positive Fibonacci/reference/contact/geometry reload states. The **causal timing and lifecycle audit remains worthwhile**, but Spot is only a **historical regression fixture**, not an active v1.1 product target after D-038. Do a bounded Spot oracle preflight, then prioritize exact Binance USDⓈ-M perpetual identity and positive qualified USDT/USDC samples. Perform full cutoffs/known-at/retirement parity on *perpetual* evidence; opportunistic positive-state native reload, not a dependency that blocks adapter work. The existing Python integrated replay does **not** model Fib or geometry and accepts one supplied bullish HTF context value, not a verified per-cutoff HTF ledger; extend evidence before claiming comprehensive parity. Read the [dedicated Work reconciliation and evidence matrix](v1-1-work-parity-reconciliation.md).

## Focused validation sequence

**P01 — evidence-bound adapter.** Inventory existing code: five exact Binance identities, `USDT` quote, `0.01` tick, 5m `STEP=300000`, and separate PAXGUSDT Spot manual Lesson 08 feature. Specify how to reject Spot, COIN-M, dated contracts, unknown venue, unsupported quote and nonstandard chart style. Preserve v1 baseline and SHA-pinned historical fixtures.

**P02 — USDⓈ-M positive sample.** Select verified Binance USDT and USDC linear perpetuals with different ticks and price scales. Prove exact contract/feed metadata, closed-bar monotonicity, qualified HTF data, no future leakage and correct display behavior.

**P03 — LONG/SHORT research symmetry.** Independently test both directional state machines and risk geometry on synthetic adverse cases and bounded actual data without inferring profitability or trade execution. Verify mixed HTF states and no-trade outcomes.

**P04 — native chart qualification.** Test qualified and disqualified products (including an allowed gold-linked Binance perpetual, Binance Spot, COIN-M and dated futures); source identity, same-closed-cutoff reload, positive/negative states, chart visibility and overlays. Keep every unsupported state informative.

**P05 — release gate.** Run existing 148 standard regression checks plus the separately maintained 21 structural checks and new contract/direction/clock cases. Confirm exact Pine compilation, native observations, source identity, chart layout restoration and retained rollback. Do not replace the owner-private version 8.0 until a separately accepted successor passes the release gates.

Qualification matrix: exact TradingView chart ID; Binance exchangeInfo identity; contractType; base/quote; settlement/margin asset; tick; chart style/timeframe; available OHLC history; 1H/4H evidence; as-of and parity checks; LONG/SHORT case; negative gate; source SHA; CI/native evidence; status = PASS / INSUFFICIENT / NOT RUN.

## Historical context and sources

- [Earlier broader D-037 exploratory plan](v1-1-crypto-universe-qualification.md): historical, superseded as target by D-038; retain for decision traceability, not implementation authorization.
- [Accepted private v1](phase3-8-v1-stabilization.md) and [five-market v0.1.6 qualification](phase3-6-v016-market-qualification.md).
- Binance [USDⓈ-M perpetual contract specifications](https://www.binance.com/en-BH/support/faq/detail/360033161972): linear, USDT/USDC quoted and settled; distinguishes COIN-M and dated contracts.
- Binance USDⓈ-M [Exchange Information](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information): metadata source to verify actual products, not a guaranteed Pine-accessible endpoint.
