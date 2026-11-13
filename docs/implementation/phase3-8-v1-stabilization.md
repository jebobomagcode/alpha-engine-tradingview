# v1 dashboard stabilization and runtime acceptance

**2026-11-13 PHT.** The [accepted private v0.1.10 release](phase3-7-complete-chart-overlays.md#named-private-release-acceptance--2026-11-13-pht) remains the named script. The chart readability correction is a disposable v0.1.11 candidate. This independent presentation change makes no new Coach-methodology claims.

## Dashboard correction

The accepted lower-left research table could be crossed by candles and the TradingView watermark could overlap its final row after reload. A native bottom-panel trial separated the tables from candles and left annotations on the chart. It reduced chart height and required scrolling through the manual table before the research rows. It remains a TradingView UI option for full chart clearance.

The candidate sets `behind_chart = false`, moves the research table to middle-left in Corners and Research only, and keeps the manual table at top-right in Corners. Both left retains the two left positions and adds a transparent two-line footer to clear the watermark. Only populated research cells receive the opaque background. This keeps the watermark visible. One trial lost the research table when both tables touched the same anchor during relocation. Moving the research table before the manual one resolved the collision. An intermediate footer inherited the table's opaque background and covered the watermark. Per-cell backgrounds resolved that regression.

The existing four Dashboard layout options, all 39 displayed controls, default values, data and annotation calculations are preserved. Both tables use their existing text size and retain every row. Research only reduces the display to one table. Hidden clears both tables and keeps the annotations. Filled tables cover the candles directly underneath them. The remaining candle area and annotation styles were readable in the sampled charts. A native floating toolbar can still cross the manual top-right table on a constrained pane.

| Identity | Value |
| --- | --- |
| Candidate parent | `7f9e288ed10f018074aa605030387e74e6d3d0ea` |
| Candidate build | `AE-0.1.11-0f4b3df98b90` |
| Pine SHA-256 | `eb82fd61ca02629b2eb7b80a9c6d2c574198c655c1dbb7e7d1b119b8ad4b60d8` |
| Pine blob | `6fe1f8718ba8b742be500262a1df84fbd933c871` |
| Named script | v0.1.10 version 7.0, `AE-0.1.10-148c152b12d2`, SHA-256 `4c01ea5b52cf7aeaa81b698b0286d0764ea7e113b569e8eb8489321dfd8ef21b` |
| Rollback | History retained versions 6 and 5. Version 6 is the previously byte-verified rollback. |

TradingView applies the declaration's visual-order settings on attach. The final editor was read back byte for byte, then the temporary study was removed and re-added with Add to chart. Native inspection used standard Binance PAXGUSDT Spot 5m at chart-canvas sizes **1192 × 827** and **891 × 827** CSS pixels. The narrower pane used the native watchlist. The final candidate rendered legible research rows and a clear watermark at both widths. Both left also showed legible market/HTF text above the watermark. Research only and Hidden behaved as documented, and the 15m chart withheld annotations. [TradingView visuals and declaration settings](https://www.tradingview.com/pine-script-docs/visuals/overview/#behind_chart) · [TradingView tables](https://www.tradingview.com/pine-script-docs/visuals/tables/).

At the shared 13:55 UTC cutoff the saved build and disposable candidate showed the same possible CHoCH at 10:35 @ 3887.63, confirmed 1H/4H down, RSI 45.7, reaction WAIT, Bear FVG OPEN 3876.65–3881.01 and Supply OB OPEN 3905.97–3909.38. Both showed the corresponding structure, zone and historical support-invalidation drawings. The candidate was removed and the original chart was restored, saved and reloaded. The named script picker still showed 7.0. Complete editor readback matched the original hash and the version history showed v6 and v5. The candidate was never saved as a named private version.

## Bounded live runtime evidence on the saved version 7

All cutoffs and captures in this table use 2026-11-13 UTC. The source was the actual saved build on Binance PAXGUSDT Spot standard 5m.

| Capture | Closed cutoff | Dashboard and chart evidence |
| --- | --- | --- |
| 13:38:44 and 13:39:37 | 13:35 | Forming price moved from about 3889.23 to 3892.49. Both panels retained 13:35. Bear FVG GEOMETRIC TEST 3874.17–3875.44 remained in the dashboard and its box and badge. |
| 13:40:15 | 13:40 | Both panels advanced to 13:40. Bear FVG was replaced by Bull FVG OPEN 3873.98–3884.31. The bullish box and badge appeared with the same state. RSI moved from 66.3 to 59.6. |
| 13:40:47, after reload | 13:40 | Saved build and same closed cutoff restored. Bull FVG OPEN and its bounds, confirmed HTF, structural event and observation reason matched. The chart also reproduced the v0.1.10 lower-left dashboard overlap. |

The live PAXGUSDT, BTCUSDT, ETHUSDT, XAUTUSDT Spot and XAUUSDT gold perpetual 13:40 UTC samples did not yield a positive current Fib, armed reference, reaction or nominal geometry suitable for reload. PAXGUSDT was sampled again later. Trying a historical 5m cutoff in the saved script showed TradingView's Basic-plan intraday replay upgrade gate. Earlier instrumented historical positive cases remain a separate record. The bounded observations are chart-time samples and do not verify continuous tick behavior, actual venue receipt or execution.

## Gate ledger

| Gate | Outcome |
| --- | --- |
| PR #2 standard and structural test suites | **PASS.** 127 standard and 21 structural tests at the exact PR head. |
| PR #3 candidate regression | **PASS.** 148 standard and 21 separate structural tests locally. Two added tests pin the display contract and reverse the final Pine source byte for byte to accepted v0.1.10. |
| Exact disposable compile and normal / constrained research readability | **PASS** for the two measured sizes and sampled states. |
| Existing layout modes and chart annotation consistency | **PASS**, sampled. Both left, Research only, Hidden and the default Corners exercised. All 39 displayed input labels and defaults match source. The disposable initial candidate's settings dialog matched the v0.1.10 default manifest and subsequent patches only changed table presentation. |
| Unsupported 15m overlay suppression | **PASS** on the exact v0.1.11 candidate. |
| Preserved named private release and rollback | **PASS.** Exact reopened v7 source and version history after cleanup, with only the accepted version restored on the saved layout. |
| Saved v7 bounded forming-to-close consistency and positive FVG reload | **PASS** at the documented PAXGUSDT cutoff. |
| Positive Fib, armed reference, contact/reaction or nominal geometry reload | **INSUFFICIENT.** No qualifying matching private reload in the bounded live observations. Historical intraday replay was blocked on Basic. |
| Continuous native intrabar and cross-device persistence | **NOT RUN.** |
| v0.1.11 named private persistence and post-integration native acceptance | **NOT RUN.** Candidate was tested disposable and both PRs remain draft. |
| Trading profitability | **NOT RUN.** This mission checked research software behavior. |

## Integration decision

Reviewed [PR #2](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/2) first at `9b765df5bb9ceebe77ce57b216281be6c6ba3282` against main `319459863fc138e8d347a1b00bc1de56fabb114c`. It adds the independent research engine, native acceptance evidence through v0.1.6 and tests. The original PDF and v0.1.3 baseline Pine are unchanged. The local ancestry-preserving merge result has the exact PR #2 tree `6146ab4972970edb4f90b2307c3ddefe257cc7a9`. Git's whitespace scan flags Markdown hard line breaks in the historical Phase 3.6 document. This is a formatting observation in the base PR.

Reviewed [PR #3](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/3) against that base. Its existing overlay history plus the dashboard increment leave the engine and prior fixtures intact. GitHub reported both drafts open and clean/mergeable. The repository metadata allows merge commits and reports push/admin for the connection, main reports unprotected, and the visible ruleset and review lists were empty. The detailed branch-protection endpoint returned HTTP 403, so detailed enforcement remains unverified. Mechanical mergeability and repository metadata do not remove the established draft integration decision.

Use an ancestry-preserving merge for PR #2 first, then verify actual main, retarget PR #3, check reachable pinned fixture commits and rerun regressions. Verify the resulting Pine build and display natively before accepting a new named private release. The pinned test fixtures use historical Git objects, so a new merge method would need a separate reproducibility check. Keep both draft and preserve the named version 7.0 while preparing that decision.
