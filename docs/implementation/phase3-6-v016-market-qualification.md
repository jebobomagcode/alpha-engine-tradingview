# v0.1.6 market qualification and native lifecycle verification

**2026-11-13 UTC · D-032/D-033 · Draft PR #2.** Starting main `319459863fc138e8d347a1b00bc1de56fabb114c`. Starting PR head `5a75f639a2216e769842b1e235783062fbe030d5`. The original Coach PDF, PCSS studies, frozen research, standalone Lesson 08 v0.1.3 source, and accepted v0.1.4/v0.1.5 audit records are preserved. Chart qualification, tick arithmetic, and HTF continuity are **AI-INDEPENDENT EXPERIMENTAL** mechanics. Coach and PCSS provenance remains in the [integrated methodology record](ai-only-integrated-candidate.md).

## Source and candidate scope

| Item | Exact value |
| --- | --- |
| Candidate source commit | `0cd16934a203d894d2164f83a376d03eff2afd19` |
| Candidate Git blob | `12504758e6b4febedc07b4ce3aea760faf6923bb` |
| Candidate SHA-256 | `9376df68e43cb76d260ab109ca69b1b2813366a75072856b506ae2397f76fcec` |
| Candidate build | `AE-0.1.6-00d26a21011a` |
| Rollback source | v0.1.5 commit `5a75f639a2216e769842b1e235783062fbe030d5`, blob `6271d1e25ffe41a927f76fab6a509a65fe666f8c`, SHA-256 `f29e7980db347dd9cfd4e799a4c3b807ccf6ed2e5d05bc709281f96eacdaa452`. The existing private saved version 5 was read back with this exact SHA-256. Version 4 and v0.1.3 remain previous rollback anchors. |

The five supported chart identities are explicit. The experimental module requires Pine’s standard 5m OHLC flag, USDT and a 0.01 tick. Native positive acceptance used Candles. Pine’s standard flag also includes line and bar styles backed by standard OHLC. The module requests 1H/4H on the exact chart feed. Pine supplies the previous closed HTF open, close and EMAs to the 5m opening snapshot. Context additionally requires the expected UTC boundaries and the last 50 HTF opens spanning 49 intervals. That span check assumes the provider returns strictly ordered, distinct, on-grid opens. It does not independently authenticate every HTF value or the EMA seed before the 50-bar window. Only a closed 5m decision updates the panel's retained context. The support band, close-through, departure and wick clearance compare integer ticks. Existing R1-A/R1-B structure mechanics and manual inputs are retained. The manual Lesson 08 state and declaration panel remain scoped to PAXGUSDT Spot. Unsupported chart identity, quote/tick and chart style/interval withhold analysis. The displayed clean ticker on synthetic charts is a label only.

TradingView's native XAUUSDT perpetual returned an empty `syminfo.basecurrency`, type `crypto`, quote `USDT` and tick `0.01`. The first build withheld analysis. The corrected gate accepts an empty or exact `XAU` base **only** for `BINANCE:XAUUSDT.P`; Binance exchange metadata identifies its base. A different nonempty base, quote or tick is still rejected. Heikin Ashi initially displayed TradingView's modified ticker ID with an identity reason. The final build prioritizes the chart-style reason and normalizes the displayed identifier only.

- [TradingView chart information](https://www.tradingview.com/pine-script-docs/concepts/chart-information/)
- [TradingView higher-timeframe requests and repainting](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/)
- [TradingView nonstandard chart data](https://www.tradingview.com/pine-script-docs/concepts/non-standard-charts-data/)

## Public Binance evidence

Read-only retrieval on November 13 UTC used Spot `/api/v3/exchangeInfo` and `/api/v3/klines`, plus USDⓈ-M `/fapi/v1/exchangeInfo` and `/fapi/v1/klines` for XAUUSDT. All five listings reported TRADING at retrieval. `PRICE_FILTER.tickSize` determines the 0.01 price grid. Spot base/quote precision fields were 8, and the gold perpetual's price precision was 2 and margin asset USDT. Binance Spot returned `-1121 Invalid symbol` for `XAUUSDT`. The chart candidate does not admit other perpetuals or other venues. This scope uses product trade-price candles. It makes no inference about funding, fees, contract sizing, fills, or tradability for a particular account.

| TradingView exact chart ID | Binance listing | Receipt | Final native result |
| --- | --- | --- | --- |
| `BINANCE:PAXGUSDT` | PAXG/USDT Spot | 48 / 4 / 1 | **PASS**, standard 5m, 04:40 and 04:45 UTC cutoffs, native historical OHLC sample |
| `BINANCE:XAUTUSDT` | XAUT/USDT Spot | 48 / 4 / 1 | **PASS**, standard 5m, 04:45 UTC cutoff |
| `BINANCE:BTCUSDT` | BTC/USDT Spot | 48 / 4 / 1 | **PASS**, standard 5m, 04:45 UTC cutoff |
| `BINANCE:ETHUSDT` | ETH/USDT Spot | 48 / 4 / 1 | **PASS**, standard 5m, 04:45 UTC cutoff |
| `BINANCE:XAUUSDT.P` | XAUUSDT USDⓈ-M `TRADIFI_PERPETUAL` | 48 / 4 / 1 | **PASS**, standard 5m, 04:45 UTC cutoff, exact contract label |

The [265-bar receipt](../research/evidence/binance-market-qualification-v016.json) covers 2026-11-12 00:00–04:00 UTC exclusive (08:00–12:00 PHT) and includes exact OHLC fields and inclusive exchange close milliseconds. SHA-256 `e7215e4cc7c74b947d58a6b3980e95b795a8bc6369e5aad194e8fa6bd57f479e`. The checks verify every price on grid and every scheduled bar present, then reconstruct and match all 25 hourly/four-hour OHLC tuples from their constituent 5m rows. The Python research model also checked 30 prefixes across five tapes and both R1 policies. Four hours of source evidence cannot independently reproduce either EMA50 context; the Python runs withheld all HTF-qualified reactions. Historical OHLC establishes neither native receipt order nor physical touch. At 2026-11-12 00:00 UTC (08:00 PHT), the native TradingView candle matched all four exchange fields for each product. This comparison covers one sampled 5m candle per product. Full-window TradingView parity remains **INSUFFICIENT**.

| Product | Native O / H / L / C at 00:00 UTC |
| --- | --- |
| PAXGUSDT Spot | 3974.28 / 3974.83 / 3971.23 / 3971.61 |
| XAUTUSDT Spot | 3972.35 / 3972.50 / 3968.47 / 3969.09 |
| BTCUSDT Spot | 74015.20 / 74126.01 / 74010.01 / 74025.00 |
| ETHUSDT Spot | 2056.35 / 2060.77 / 2055.96 / 2058.26 |
| XAUUSDT perpetual | 3985.43 / 3985.62 / 3980.85 / 3981.26 |

- [Binance Spot public market data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints)
- [Binance USDⓈ-M exchange information](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information)
- [Binance USDⓈ-M kline data](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data)

## Native v0.1.5 edge audit

[The generator](../../research/phase3_6/native_v015_lifecycle_audit.py) adds read-only observations to the exact v0.1.5 source and changes the temporary default to R1-B. The generated unsaved Pine SHA-256 `e9f14240a0e6878a9f61246feaaed019aa9146fa3481162ad2981e3846ac7256` matched the copied-back editor. Width was 2 and the wick alternative remained OFF. The first scan evaluated 5,235 chart bars from 2026-10-26 00:00 to 2026-11-13 04:35 UTC at one tick. The 50-tick sensitivity scan evaluated 5,236 bars through 04:40 UTC. These counts describe chart evaluations, including the initial bar, and do not assert exchange-feed continuity across the full chart history.

| Gate | Native evidence |
| --- | --- |
| Same-close in-band support consumption | **PASS** for a real historical transition at 50 ticks. Twelve matches. Latest at 2026-11-12 04:30 UTC, HL 3973.65, close 3973.48, inside [3973.15, 3974.15]. The episode ended on that close and reaction was false. Display remained WAIT for 1H/4H bullish alignment under the existing precedence. No one-tick match or bullish-context REASSESS observation, both **NOT RUN** natively. The existing Python fixture covers that REASSESS reason. |
| R1-B reset and eligible re-cross | **PASS** historically. Ten reset-to-armed transitions and one tracked re-cross at the one-tick setting. HH 4093.84 originated 2026-11-05 23:40 UTC, armed on 2026-11-06 00:15 UTC, then crossed at 00:20 UTC. The last reset in the window belongs to a different reference and is excluded from this example. |
| Constant-memory retirement watermark | **PASS** in a native helper injection. Older/equal/newer proposed origins yielded RETIRED / CONSUMED / ARMED. An older origin naturally re-entering after a newer terminal origin remains **NOT RUN** on market history. It is excluded by the fixed-width monotone selection invariant in the [prior audit](phase3-6-v015-lifecycle-audit.md). |

The [15-bar event receipt](../research/evidence/binance-paxgusdt-v015-lifecycle-windows.json) independently corroborates the observed price and adjacent-bar geometry. The re-cross predecessor closed 4093.65, followed by a close of 4100.00. The in-band predecessor closed 3975.38, followed by 3973.48. Its checksum is `a35b63e0bd1fcbe95e72236699b36fdbe23bd341749de285141856ed58c5c3b4`. The Pine state evidence is reconstructed from chart history. Neither receipt supplies native Pine state or exchange arrival timestamps.

## Candidate acceptance ledger

| Gate | Status and evidence |
| --- | --- |
| Full local suites and CI | **PASS**. 127 standard tests locally, 21 separate structural tests, and [CI run 43367393774](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43367393774) logged 127 tests and OK for the exact candidate source commit. Python is a separate model and source QA. |
| Exact candidate editor and native compilation | **PASS**. Committed Raw source and copied-back unsaved editor matched complete normalized bytes. Native chart showed exact build on all five products. |
| Closed HTF / native coverage | **PASS** for the sampled 1H/4H 04:00 UTC pair across all five feeds and the live PAXGUSDT rollover bracket. At 04:59:27 UTC, the original panel showed 1H 04:00 and the integrated cutoff was 04:55. At 05:00:13 UTC, the original forming 5m panel showed confirmed 1H 05:00 / 3905.26 and last 5m close 05:00. The integrated 05:00 decision correctly retained 04:00 for both HTFs because that evaluated bar opened at 04:55. Integrated adoption at the subsequent 05:05 close and the other markets’ live rollover remain **NOT RUN**. Full EMA parity is **INSUFFICIENT**. |
| Unsupported product, interval, or candles | **PASS** for BTCUSD Spot, XAUUSDT perpetual at 15m, and PAXGUSDT Heikin Ashi on the final build, each with a withheld decision cutoff. BTCUSDT perpetual was additionally rejected by the immediately preceding candidate. |
| PAXGUSDT default parity and controls | **PASS**. At 04:45 UTC both v0.1.5 and the exact final candidate showed UNKNOWN with BOS candidate up at 01:20 UTC / 3892.41, no active references, down 1H/4H, mixed momentum RSI 41.9, WAIT, gap 3905.50–3908.99 and open demand 3887.22–3891.60. All 24 displayed pre-save controls matched. |
| Enabled manual Lesson 08 v0.1.6 native fixture | **PASS** for documented revision 31. At 04:50 UTC, M01 ON and OFF retained REASSESS, geometric overlap, contact Nov 11 14:50 UTC, both R2 records at 15:00 UTC and Strict UNKNOWN. The ON panel reported latest pivots and the OFF panel withheld all three M01 rows. The fixture is retrospective. All 24 default controls were restored in the test tab after the comparison. |
| Realtime closed-bar advancement | **PASS** on PAXGUSDT, 04:45 → 04:50 UTC with 1H/4H held at 04:00 UTC. The live 5m transition is separate from any durable save or hourly rollover. |
| Realtime-to-normal-reload at one cutoff | **PASS** at 05:00 UTC. After the live boundary the candidate’s exact build, standard PAXGUSDT Spot 5m and sampled research state restored at the same cutoff. This is browser-session chart persistence. |
| Named v0.1.6 private save and durable saved-source/input restoration | **NOT RUN**. The candidate compiled from an untitled buffer. The existing named private version 5 still read back exact v0.1.5 bytes. No new account save limit was exercised. |
| Original layout restoration | **PASS**. Reloading the second chart tab surfaced the temporary v0.1.6 chart instance even though the named script stayed v0.1.5. Removed the temporary chart instance, reattached the exact named v0.1.5, checked all 24 controls, saved the original layout, and reloaded. The resulting chart showed v0.1.5 alone on standard PAXGUSDT Spot 5m with the same 05:00 UTC cutoff. No named-script save was used during restoration. |
| GitHub PR #2 integration | **Open draft**, GitHub reported clean/mergeable. Accepted main has been preserved. The draft status and integration authorization are separate from CI. |

## Integration and release decision

The three candidate commits qualify the five feeds, handle the native gold-contract metadata and provide the lifecycle audit, and clarify nonstandard chart rejection. The PR is mechanically mergeable and source CI is green. Browser-session restoration propagated the temporary chart instance across two tabs on the same layout. The rollback restored the saved layout and the named private script remained at version 5 throughout. Private v0.1.6 persistence remains the release gate. Keep the existing named version 5 until the project can establish private candidate durability under the replacement safeguards. The bounded next acceptance should verify exact named source and build after script save, layout save and same-cutoff reload, and compare all 24 controls. No new indicator functionality is required for that gate. No private screenshot, account detail or chart identifier is stored in this repository.
