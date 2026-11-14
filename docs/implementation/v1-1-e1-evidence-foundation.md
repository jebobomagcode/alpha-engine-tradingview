# v1.1 E1 — two-feed evidence and four-timeframe opening snapshots

**Scope.** D-041 product direction and the owner’s E1 engineering authorization. Stacked engineering branch `engineering/v1-1-e1-evidence-foundation`, based on PR #4’s `research/v1-1-crypto-universe-scope-20261114` at `2ec89ab28463a0f0342bf945dd39cf27b624c7f4`. Review its E1-only diff against that base. If the documentation base lands on `main`, verify the ancestry and E1-only diff before retargeting. This increment adds the evidence layer. Existing Python and Pine detectors, the Coach/PCSS records, `main`, accepted private v8.0 and v7.0 rollback are preserved.

## Contract candidates and evidence receipt

| Binance USDⓈ-M contract | Raw type/status in exchange snapshot | Base / quote / margin / settlement | `PRICE_FILTER.tickSize` | TradingView chart mapping |
| --- | --- | --- | --- | --- |
| `BTCUSDT` | `PERPETUAL` / `TRADING` | BTC / USDT / USDT / USDT | `0.10` USDT/BTC | `BINANCE:BTCUSDT.P` |
| `ETHUSDC` | `PERPETUAL` / `TRADING` | ETH / USDC / USDC / USDC | `0.01` USDC/ETH | `BINANCE:ETHUSDC.P` |

- [Exchange snapshot excerpt](../research/evidence/v1-1-e1/exchange-info-excerpt.json) preserves both unmodified Binance symbol records, including trading/size filters, plus `U_MARGINED`, UTC and the server timestamp. The Binance public connector returned it at `2026-11-14T01:46:05.265Z` (`09:46:05.265 PHT`). The payload’s `serverTime` was `2026-11-13T06:02:01.706Z`, about 19h44m older. The audit qualifies the **dated snapshot**. Current listing freshness must be reverified before release. The direct public web route returned HTTP 451, while the supported public connector returned the preserved data. The 48-hour audit window used in tests is a fixture setting. The model takes an explicit age limit and does not set a release freshness SLA.
- [Manifest](../research/evidence/v1-1-e1/manifest.json) pins both file hashes, settlement sources and TradingView mappings. Binance’s [linear contract specification](https://www.binance.com/en-BH/support/faq/detail/360033161972) establishes USDⓈ-M quote/settlement conventions, and its [ETHUSDC listing announcement](https://www.binance.com/en/support/announcement/detail/4ff3534898ab4ea09afb450a94f20afe) names USDC settlement for that contract. Use exchange `PRICE_FILTER.tickSize` for the price grid. Symbol suffix and display precision are insufficient admission evidence.
- [Trade-price candle receipt](../research/evidence/v1-1-e1/trade-klines-receipt.json) preserves all eight request envelopes and connector response texts from Binance `/fapi/v1/klines`. Window `2026-11-12 16:00` to `2026-11-13 04:00` UTC exclusive (`2026-11-13 00:00` to `12:00` PHT). Each contract has 144 closed 5m, 48 closed 15m, 12 closed 1H and 3 closed 4H bars. The two markets total 414 rows. All 126 higher-timeframe bars match 5m-derived OHLC on exact ticks, as a cross-check against separately returned native Binance intervals. Volume fields are retained in the receipt and unused by the model. Finality is bounded by the historical request window. Historical candles do not provide native realtime receipt times.
- TradingView’s public contract pages and their **Full chart** links identify Binance’s BTC/Tether and ETH/USD Coin perpetuals. A read-only chart check on November 14 PHT showed the exact exchange tickers, **5 minutes**, selected **Candles** and the market-open status on both. This is chart identity/rendering evidence. The [native Data Window sample](../research/evidence/v1-1-e1/tradingview-chart-sample.json) also matches all eight OHLC fields for one 5m candle per contract at `2026-11-12 16:00 UTC` (`2026-11-13 00:00 PHT`). This is a bounded price-series cross-check. Wider matched OHLC, `syminfo.mintick`, feed timing and Pine behavior are separate gates.

Primary references [Binance Exchange Information](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information) · [Binance trade-price klines](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data) · [TradingView BTCUSDT.P](https://www.tradingview.com/symbols/BINANCE-BTCUSDT.P/) · [TradingView ETHUSDC.P](https://www.tradingview.com/symbols/ETHUSDC.P/?exchange=BINANCE).

## Executable evidence contract

[Python model](../../research/v1_1/evidence_contract.py) · [Shared fixture](../../tests/fixtures/v1_1/e1-cutoffs.json) · [Regression runner](../../tests/test_v1_1_e1_evidence.py).

| Record | Fields and invariants |
| --- | --- |
| Market and chart | Exact venue, segment, symbol, raw contract type and trading status, base/quote/margin/settlement, exact decimal tick, approved mapping, metadata server time and native gate status. Chart carries ticker, price basis, standard-OHLC flag, timeframe and tick evidence. Product, mapping-field checks and native acceptance are independent results. The two-symbol manifest supplies the reviewed inputs. |
| Candle and source | Exact trade `series_id`, provider `source_id`, immutable `receipt_id`, timeframe, UTC epoch-ms open and exclusive close, positive integer price ticks, finality, revision, modeled availability and optional observed first-seen. For `/fapi/v1/klines`, `close_ms = raw[6] + 1`. Off-grid OHLC and malformed/non-final records are rejected by the receipt normalizer. Candle origin is its open and candle confirmation is its exclusive close. Derived detectors will need their own origin and confirmation later. |
| Snapshot and decision | For a host interval `[o,T)`, calculate expected HTF closes as `floor(o / step) × step` and look them up as of `o`. The 5m candle is due at `T`, and must be final and available by `T`. Each layer reports the expected and latest visible close, selected revision and contiguous usable history when ready, plus a distinct reason when withheld. Aggregate readiness is independent of trade direction or detector output. |
| Availability modes | `modeled` permits a completed HTF packet at exact modeled open. `observed` requires independently observed availability strictly before open. Equal observed ms values alone do not resolve arrival order. A missing observed time stays unknown and never falls back to modeled time. An observed 5m close may be used at the cutoff only if available by that cutoff. A packet arriving during a 5m interval can first participate at a later opening if it is still the expected packet. |
| Warmup, revisions and gaps | Read explicit contiguous warmup lengths by timeframe. A missing expected bar with an older visible bar is stale. Do not forward-fill. Select the highest valid revision number visible at the applicable boundary. Conflicting payloads at that revision fail the layer. Identical payload and clock values with multiple receipt IDs are deduplicated by stable receipt-ID order. A correction available later cannot revise the earlier as-issued state. Keep earlier receipt versions for reconstruction. |

This E1 clock uses continuously scheduled UTC bars for the two chosen crypto perpetuals. Session-aware expected closes and the separate TradFi product qualification are future work. Immutable pinned inputs can arrive in arbitrary iterable order. Ordering is determined by declared availability and revision, with contradictory final evidence surfaced rather than silently sorted into a winner. Retain the manifest and receipt IDs in any model-to-native comparison.

## Frozen cases and gate results

The hand-authored fixture gives explicit timestamp offsets and verdicts for a simultaneous 15m/1H/4H rollover, two positive products, exclusion cases, gaps, stale/late evidence, conflict and a version change. The expectations are independent of the Python selection implementation. A future Pine harness can read or transcribe this fixture without running the Python logic. The frozen Binance receipts remain distinct from the synthetic schedule.

| UTC decision cutoff | 5m confirmed close | 15m / 1H / 4H selected confirmed closes |
| --- | --- | --- |
| 2026-11-13 00:00 | 00:00 | 23:45 / 23:00 / 20:00 on November 12 |
| 2026-11-13 00:05 | 00:05 | 00:00 / 00:00 / 00:00 on November 13 |
| 2026-11-13 00:10 | 00:10 | 00:00 / 00:00 / 00:00 on November 13 |

At `00:05` the newly closed packets enter for the first time **under the historical model**. A synthetic 1H packet available at `00:02` instead misses the `00:05` decision and can first enter the `00:10` decision. The observed-clock case with equal host-open and packet-arrival milliseconds withholds that packet until a later eligible open. Future bars and revisions do not change the prior snapshot.

| Gate | Status | Evidence or gap |
| --- | --- | --- |
| Exact Binance product, units and ticks in dated snapshot | PASS | Public metadata records and settlement references. Release-time metadata freshness remains open. |
| Native TradingView exact chart identity and type | PASS | Both named chart tickers, 5m interval and Candles control observed. |
| Native TradingView historical 5m OHLC sample | PASS | Two bars at the same UTC open, eight OHLC fields matched. |
| Native TradingView tick and four-timeframe parity | NOT RUN | A wider matched capture and native `syminfo.mintick` remain open. |
| Four-layer receipt integrity and expected cutoff behavior | PASS | 414 Binance trade candles, 126 higher-timeframe OHLC aggregates, both markets checked at three cutoffs. |
| Model and fixture verification | PASS | 11 new E1 tests, including malformed/off-grid inputs, missing, stale and delayed evidence, warmup, revision, identity, reason codes, exact boundary and prefix invariance. |
| Standard and separate structural regressions | PASS | 159 standard tests and 21 structural checks passed locally under Python 3.12.14. |
| Native Pine snapshot parity, actual packet arrival, persistence | NOT RUN | Native Pine instrumented proof and actual realtime receipts remain open. No private script save or layout change. |

`PASS` means the scoped gate has evidence. `FAIL` means a supplied constraint was contradicted or the evidence was invalid. `INSUFFICIENT` means required evidence is absent, stale or not yet usable. `NOT RUN` means the named verification was never executed. Synthetic negative verdicts are passing checks of the expected withholding behavior.

## Design consequences and next milestone

The Coach PDF and completed PCSS remain the authority for source interpretation, including Lesson 08’s top-down location and closed confirmation. D-041’s four-layer roles and the clock/admission implementation are independent engineering. E1 applies neither detector parameters nor a market performance objective. The [approved-direction specification](../product/v1-1-candidate-specification.md) keeps the other Coach branches in coverage. This implementation leaves the accepted v1 and its fixtures untouched.

Next, build a **disposable native clock diagnostic** using three same-contract previous-HTF-bar requests and a closed 5m decision. Compare chart tick and the four native close/price packets to the pinned Binance window first, then exercise a real boundary and reload with the same version and inputs. Preserve provider differences and runtime timing evidence as distinct results. Use the verified packet contract for a minimal LONG/SHORT continuation slice once the native clock gate is understood. [TradingView timeframe requests](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) · [Execution model](https://www.tradingview.com/pine-script-docs/language/execution-model/).
