> **SUPERSEDED PRODUCT TARGET (2026-11-14, D-038):** This file preserves the earlier, broader D-037 exploratory scope as historical context only. The owner subsequently narrowed Alpha Engine TradingView to **Binance USDⓈ-M USDT/USDC/verified USD-stablecoin-settled PERPETUAL contracts only**. No Spot, COIN-M, dated futures or other exchanges. Use the [current active v1.1 plan](v1-1-binance-usds-m-perpetual-qualification.md). The source study and accepted private v1 are not changed.

# v1.1 — Crypto-wide market coverage (product scope and qualification)

**Status:** OWNER REQUIREMENT RECORDED / RESEARCH PLAN ONLY — 2026-11-14 Asia/Manila  
**Decision:** D-037 in [DECISIONS.md](../DECISIONS.md).  
**Starting accepted v1:** `main` at `8e60a982385e46aa818acb49103f1dedbe856b77`; integrated Pine blob `6fe1f8718ba8b742be500262a1df84fbd933c871`; private TradingView saved version 8.0, build `AE-0.1.11-0f4b3df98b90`. Preserve v1 and version 7 rollback. No new native save or instrument qualification is claimed by this plan.

## Owner's intent — exact scope

Owner clarified that “all markets” means **all cryptocurrency markets**, including **spot, futures, perpetual swaps and other crypto derivatives**, not stocks, equity indices, forex or conventional commodities as standalone implementation targets. Cryptocurrency-related products are in scope regardless of venue or quote currency when a usable TradingView feed and adequate evidence exist. Gold-linked **crypto** instruments including PAXGUSDT, XAUTUSDT and XAUUSDT perpetual remain included as distinct products; this does not authorize standalone forex XAUUSD.

The product goal is a **chart-native, instrument-aware crypto research indicator** rather than a fixed list of five Binance tickers. “All” defines intended coverage and discovery; it is **not a promise** of verified support for every listed contract, every broker/feed, any arbitrary timeframe, or options whose chart cannot provide adequate OHLC evidence.

### Product families to investigate

| Family | Example kind | Distinct evidence/constraints |
| --- | --- | --- |
| Crypto spot | BTC/USDT, ETH/USD, SOL/USDC | Exchange/quote identity; venue-specific OHLC; tick size and session |
| Linear perpetual swaps | USDT/USDC margined | Mark/last/index price differences, funding and contract semantics (often not directly observable in Pine) |
| Inverse / coin-margined perpetuals | BTC collateral / inverse contracts | Contract denomination, nonlinear P&L; do not apply linear USDT risk assumptions |
| Dated / delivery futures | Quarterly and other dated crypto contracts | Expiry, roll/gap, changing contract identity, settlement |
| Other chartable crypto derivatives | As genuinely available | Explicitly identify product, coverage, session and risks; don't fabricate metadata or valuations |
| Tokenized gold on crypto markets | PAXG/XAUT spot, gold-referencing crypto perpetual where listed | Distinct underlying product, venue and quote; no price/feed substitution |

## Existing v1 constraints — verified source

`pine/alpha-engine-research.pine` integrated at v1 still hardcodes the five exact Binance identities, requires `syminfo.currency == "USDT"`, `syminfo.mintick == 0.01`, standard 5m OHLC and a fixed `STEP = 300000` clock. A separate manual Lesson 08 declaration remains PAXGUSDT Spot-specific. The research engine reads confirmed 1H and 4H context on the same chart feed. These are real constraints; they must not be bypassed without replacing the associated validation and assumptions.

## Proposed architecture — independent research, not Coach prescriptions

1. **Chart-native identity:** distinguish TradingView exchange prefix, exact symbol, asset/quote, product family, contract/expiry if available, price type, mintick, pointvalue and session. Do not classify solely from a ticker suffix; Pine metadata can be insufficient or atypical. Expose `UNKNOWN/INSUFFICIENT` when classification cannot be established.
2. **Eligibility vs qualification:** avoid a growing symbol whitelist. Use capabilities (standard real OHLC, sound price/time/precision, sufficient history and HTF availability) for chart eligibility. Keep explicit venue/product coverage records and a separate tested-qualification matrix; never imply all markets are empirically validated.
3. **Price and arithmetic:** replace 0.01 assumptions with symbol-relative tick arithmetic, rounding, bounds and numerical stability tests. Distinguish nominal geometric E/SL/TP from position sizing, P&L, inverse settlement, fees and funding.
4. **Bar-time semantics:** replace fixed 5m clock checks with timeframe-aware periods and confirmed prior-bar chronology; explicitly handle missing bars, exchange/feed interruptions, derivatives expiry and product-specific session boundaries. **Do not fill gaps** with invented candles.
5. **MTF causality:** for any new chart timeframe, select appropriate strictly higher confirmation horizons. Preserve as-of known-at semantics, confirmed HTF observations, no future leakage and no silent lower-timeframe substitution. Qualify each mapping before enabling it.
6. **State/UI:** explain exactly why an instrument or timeframe is eligible, qualified, insufficient, or unsupported. Keep all experimental structure, zones and reaction outputs source-labelled and WAIT/INSUFFICIENT informative. Preserve the optional, historically PAXG-specific manual Lesson 08 as a separate feature until deliberately generalized.
7. **Safety and scope:** informational research indicator only. No live trades, broker connection, auto-execution, claims of profitable edge, untested release promotion, public TradingView publication or deletion of existing rollback.

## Proposed incremental validation sequence

**R01 — capability contract.** Inventory every present whitelist and quote/tick/clock/PAXG assumption, then define an independent market-adapter specification and adversarial fixtures. Freeze the v1 SHA-pinned regression baseline.

**R02 — market-agnostic closed-bar research core.** Make source-safe crypto charts eligible without hardcoding symbols, with explicit detection of unsupported nonstandard OHLC and unknown product identity. Test extremely fine/coarse tick, non-USDT quote, missing candle, short history, unusual metadata and source prefix.

**R03 — derivatives and sessions.** Qualify representative linear perpetuals, inverse/coin-margined perpetuals and dated futures on at least two venues where feeds permit. Check quote/settlement vs nominal geometry, continuity and expiry/roll behavior. Record any unavailable category as NOT RUN/UNSUPPORTED rather than silently granting support.

**R04 — timeframe expansion.** Separately qualify 5m baseline, 15m and later timeframes with explicit HTF mapping and native chart-clock evidence. Any unqualified interval remains gated.

**R05 — native and release acceptance.** Re-run the 148/148 integrated standard regression baseline and 21 separate structural checks; test native Pine compilation, representative chart renders, causal parity, negative gates, same-cutoff reload, selected positive-state transitions and retained rollback before any private successor release. Additional tests should be added rather than replacing the baseline.

**Qualification matrix columns:** exact TradingView symbol/feed; exchange; product family; quote/settlement; tick; chart style/timeframe; bar/session clock; historical sample; HTF readiness; known-at/repaint checks; overlay/output checks; data limitations; source hash; CI/native status.

### Acceptance standard

“Runs” means a compatible chart is not arbitrarily excluded and the indicator produces a truthful status. “Qualified” requires reproducible evidence for that exact venue/product/timeframe class. “Validated profitable” is a separate research question and **not implied**. All v1 claims remain bounded to their original scope. 

### Primary references

- [D-013 historical crypto-only market scope](../MARKET_SCOPE.md)
- [Integrated v1 native release ledger](phase3-8-v1-stabilization.md)
- [Five-market qualification](phase3-6-v016-market-qualification.md)
- TradingView Pine Script documentation: [Chart information](https://www.tradingview.com/pine-script-docs/concepts/chart-information/), [Other timeframes and data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/), [Non-standard charts](https://www.tradingview.com/pine-script-docs/concepts/non-standard-charts-data/)
