# Authorized market scope — crypto-first, including gold-linked crypto products

**Status:** OWNER DIRECTIVE — 2026-11-09 (Asia/Manila)  
**Decision:** D-013 in [DECISIONS.md](DECISIONS.md).  
**Scope:** The eventual TradingView indicator/optional strategy must focus on cryptocurrency trading environments, including the three explicitly named gold-related tickers. This market decision supersedes Lesson 01's open question about whether the system should target forex/CFD or Philippine equities. It does **not** alter the original 35-page Coach PDF or remove those topics from PCSS coverage.

## Required instrument families

| Priority | User-specified notation | Initial product distinction | Required treatment |
| --- | --- | --- | --- |
| Core | Cryptocurrency symbols generally (exact list not yet selected) | Spot or derivatives, exchange-specific | Support the crypto ecosystem as the intended target; instrument/product and venue must be explicit |
| Explicitly in scope | **XAUUSDT** | For example, Binance XAUUSDT USDT-margined cash-settled perpetual exposure to gold; **not physical-gold ownership and not the XAUT token** | Treat as a gold-reference-price derivative when using that Binance product; confirm the TradingView feed and exact instrument/venue |
| Explicitly in scope | **XAUTUSDT** | USDT quote for XAUT / Tether Gold, a physically backed gold token; an individual market may have spot or derivative variants | Treat token market price and issuer/product mechanics separately; do not equate to XAUUSDT |
| Explicitly in scope | **PAXGUSDT** | USDT quote for PAXG / Pax Gold, another physically backed gold token; market/product variant depends on venue | Treat token market price and issuer/product mechanics separately; do not equate to XAUTUSDT or XAUUSDT |

**The user's ticker strings specify the requested scope, not a promise that each instrument is listed on every exchange, in every region, or under the same TradingView symbol ID.** Actual support and feed availability must be verified against exact market, exchange, product type and contract specifications when building and testing.

### External identity checks — independent, not Coach-source claims

- Binance Academy, [How to Trade Gold and Silver on Binance Futures](https://www.binance.bh/en/academy/articles/how-to-trade-gold-and-silver-on-binance-futures): names **XAUUSDT** as a USDT-margined perpetual gold-reference-price contract, cash settled in USDT; not ownership of bullion.
- Tether, [Tether Gold: Digital Gold for the Modern Era](https://tether.io/news/tether-gold-digital-gold-for-the-modern-era/): **XAU₮** is a token backed by physical gold with product-specific ownership/redemption conditions.
- Paxos, [PAXG overview](https://docs.paxos.com/guides/stablecoin/paxg): **PAXG** represents tokenized physical gold, with one PAXG representing a fine troy ounce of allocated gold under issuer terms.
- These are instrument-identity descriptions from providers, not independent validation of pricing equality, current exchange listings, exchange liquidity or trading performance.

## Consequences for project design (proposals, not implemented)

1. **Instrument and venue metadata**: identify exchange-qualified TradingView symbol, underlying reference, token vs futures vs spot product, settlement denomination, session calendar, contract/tick size, and available price/volume data.
2. **Distinct feed handling**: do not merge candles, compare price values as if equivalent, or use XAUUSDT as automatic source for XAUTUSDT/PAXGUSDT trades. Permit cross-instrument comparisons only as clearly marked optional independent research with source/lag, liquidity and price-basis considerations.
3. **Crypto-relevant analytical context**: spread, liquidity, volatility, bar intervals, perpetual funding/mark-price phenomena where data is available, spot gaps/listing history, exchange-specific anomalies, and token-specific price dislocations. A Pine script cannot be presumed to access all these data natively.
4. **Gold-specific research**: distinguish global gold benchmark behavior from derivative market prices and each token issuer's backing and redemption mechanics. Prices can diverge due to venue, currency quote, liquidity and product effects.
5. **Evaluation matrix**: eventual testing should deliberately include liquid major crypto, other crypto markets when selected, XAUUSDT, XAUTUSDT, and PAXGUSDT; report data availability and historical coverage separately. No performance claim without appropriate tests.
6. **PCSS unaffected**: continue original lesson sequence and cover Forex/PH stocks in the source because they are part of Coach's complete teaching. For implementation implications, map those sections to crypto only where justified rather than adding Forex or PSE runtime support.

## Non-decisions and open checks

- Exact trading exchanges, exact TradingView prefixed symbols, spot vs futures preference for XAUTUSDT/PAXGUSDT, platform subscription/data availability and initial test universe remain undecided.
- No hardcoded equivalence, universal market superiority, exchange inclusion, constant fee/funding, or guaranteed cross-market arbitrage.
- No current Pine Script, no live data access audit, and no backtests exist in this new project.

## Ponder control

**Hypothesis:** a source-grounded Coach baseline plus explicitly marked crypto and gold-specific enhancements may improve usability and reliability. **Disconfirming evidence:** higher complexity, nonportable signals, data inconsistency, lookahead, poorer out-of-sample behavior, or a failure to distinguish instrument product mechanics. Preserve a baseline and keep improvements testable.
