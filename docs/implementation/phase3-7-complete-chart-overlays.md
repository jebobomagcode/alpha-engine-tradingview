# Fibonacci, EMA and observation chart overlays

**2026-11-13 PHT · v0.1.10 visualization candidate.** The [structure](phase3-7-structure-overlay.md) and [zone](phase3-7-zone-overlay.md) layers remain available. This increment adds independent experimental chart displays for engine observations. Contact uses OHLC overlap. Reaction is a closed research classification. Nominal geometry expresses price distances and does not measure execution, returns, or profitability.

| Source identity | Value |
| --- | --- |
| Starting draft PR #3 head | `7c9f2c1ab08f6af40af0ffc4808c4f927eb480ed` |
| Fibonacci / EMA source | `579ed3ec997c3f9a7807f076ade4daf1e3351149`, build `AE-0.1.9-98ca36885208` |
| Observation / geometry source | `5302858e3e478c8e029479c2d10a798b60f50c55` |
| Final source | `a3f78d498b34b697257d00f030dacafafcdbfdce`, build `AE-0.1.10-148c152b12d2` |
| Final Pine blob / SHA-256 | `2632dc57ce6a53fe9e963dc830c15e567b6bbcd9` / `4c01ea5b52cf7aeaa81b698b0286d0764ea7e113b569e8eb8489321dfd8ef21b` |

## Display contract

| Layer | Source, timing and visibility |
| --- | --- |
| Fibonacci 50 / 61.8 / 70.5 | Default ON. One current three-line set reads the same numeric levels used in the dashboard. The set starts at the confirmed cutoff that first exposes the eligible pivot pair and direction. A changed pair or direction replaces the coordinates at the new cutoff. Loss of eligibility deletes the set. Current values are also named in the Data Window. |
| EMA 20 / 50 / 200 | Independently configurable and default OFF. Use the existing 5m momentum series at confirmed closes, after the same 200-bar readiness gate as the dashboard. The plot leaves a gap across insufficient bars. The forming bar adds no EMA sample. |
| Contact, reaction and support invalidation | Three switches default ON. Contact marks the first accepted geometric overlap in an episode. Reaction uses the engine's closed reaction flag. A same-close contact and reaction can share one label. Support close-through or reference consumption marks the first terminal close and the tooltip states which occurred. Ordinary departure keeps its existing lifecycle semantics. |
| Nominal entry / stop / target / R | Default OFF. Uses the exact numeric snapshot behind the integrated dashboard's nominal row, after its existing directional and positive-distance guards. Three short lines and one badge start at the qualifying close. The next close without a qualifying geometry clears all four objects. The badge tooltip names the three levels and nominal R. |
| Dashboard and density | Corners preserves the prior layout. Both left places the manual panel at middle-left and keeps research at bottom-left. Research only and Hidden clear the applicable table cells. Existing per-family density also caps the new observation history. The first implementation placed the manual panel at top-left, where it overlapped the native chart header. Native testing prompted the middle-left correction. |

The engine's original analytical behavior is covered by byte-exact source isolation after reversing the added numeric/display bindings, title and object-budget metadata. Fib draws at most three lines and nominal geometry at most three. With two armed-reference lines, three boxes, up to 16 labels in each of the three rolling histories, three original manual markers, two zone badges and one nominal badge, the script declares eight lines, three boxes and 54 labels.

- [TradingView Pine lines and boxes](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/)
- [TradingView Pine plots](https://www.tradingview.com/pine-script-docs/visuals/plots/)

## Acceptance

| Gate | Result |
| --- | --- |
| Regression and source isolation | **PASS.** 146 standard checks locally and in [final source CI](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43428979711). The 21 separate structural research checks passed locally. Four new guide checks and five observation checks cover formula and gate bindings, prior-source reconstruction, causal anchors, retirement, geometry clearing and object limits. |
| Exact native compile | **PASS** for both bounded increments. The complete untitled editor copy-back matched each committed SHA-256 before native compilation. The guide increment rendered on Binance PAXGUSDT and BTCUSDT Spot 5m. The corrected exact observation build also ran on both feeds and showed its build in the dashboard. |
| Fib and EMA native history | **PASS, instrumented.** On 10,672 closed bars, the temporary audit found zero Fib placement, level or retirement violations and a peak of five lines, including existing references. It counted eligible EMA closes. The exact three EMA plots also visibly rendered on both feeds with the three controls enabled. |
| Contact, reaction and nominal native history | **PASS, instrumented.** The audit used the unchanged drawing logic with nominal geometry enabled. It compared marker cutoff, line timestamps and prices, and stale-geometry clearing to the native engine. The default market samples had no positive reaction or geometry events. The existing PAXGUSDT wick comparator supplied three of each, including a 2026-11-09 13:50 UTC sample with E 4109.07, SL 4107.77, TP 4118.41 and 7.18R. |
| Dashboard, density and unsupported chart | **PASS, sampled.** The exact final build moved the manual table away from the upper-right candles and native header in Both left. Research only preserved the research table, Hidden removed both tables while keeping drawings, and a history cap of two reduced structural marker density. Standard Binance PAXGUSDT 15m withheld research overlays. |
| Same-cutoff dashboard consistency | **PASS, sampled.** Candidate and restored private baseline matched at 12:55 UTC on PAXGUSDT. Both displayed the 10:35 CHoCH candidate at 3887.63, possible shift, 1H/4H down, RSI 34.6, Bear OPEN gap 3879.28–3880.81 and Supply OPEN 3905.97–3909.38. |
| Accepted private release isolation | **PASS.** Removed the temporary candidate and probes. The existing named v0.1.6 script still reported version 6 and exact source SHA-256 `9376df68e43cb76d260ab109ca69b1b2813366a75072856b506ae2397f76fcec`. Verified the accepted 24 control values and restored the PAXGUSDT Spot 5m layout. Reload showed v0.1.6 alone. No new named version was saved. |
| Successor private persistence and continuous intrabar observation | **NOT RUN.** The candidate was tested as an untitled instance. Source guards and historical scans cover closed-cutoff behavior. Native tick-by-tick and same-cutoff successor private reload remain separate gates. |

### Native historical audit counts

All reported cutoffs below use 2026-11-13 UTC. The temporary Pine probes only measured the drawings and their input states. Market history lengths and warmup depend on the loaded chart data.

| Guide audit at 12:50 UTC | Closed bars | Fib-qualified bars | Starts or replacements | Retirements | EMA-eligible closes | Violations / peak lines |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| PAXGUSDT Spot 5m | 5,334 | 513 | 153 | 153 | 4,458 | 0 / 5 |
| BTCUSDT Spot 5m | 5,338 | 591 | 159 | 159 | 5,139 | 0 / 5 |

| Observation audit at 12:55 UTC | Closed bars | First contacts | Closed reactions | Invalidations | Nominal geometry | Violations | Peak lines / labels |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| PAXGUSDT Spot 5m, default reaction | 5,335 | 7 | 0 | 36 | 0 | 0 | 5 / 26 |
| BTCUSDT Spot 5m, default reaction | 5,339 | 0 | 0 | 31 | 0 | 0 | 5 / 26 |
| PAXGUSDT Spot 5m, wick comparator | 5,335 | 7 | 3 | 36 | 3 | 0 | 8 / 27 |

The PAXGUSDT default reaction audit had five peak lines and 26 labels. The wick case reused that same chart history with the existing alternative enabled. It is a separate policy run and should not be added to the distinct-market bar total.

The stacked [draft PR #3](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/3) remains based on [draft PR #2](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/2). Next release work is the exact successor's named private save, saved-editor readback, original and added input manifest, layout save, same-cutoff reload and rollback verification.

## Named private release acceptance — 2026-11-13 PHT

The existing named script, Alpha Engine TradingView — Lesson 08 Diagnostic, compiled and saved as private version **7.0** at 21:15 PHT. The editor copy-back was exact before Update on chart. The same action compiled the chart instance and created the saved version. The chart layout was saved through its own control and subsequently reported All changes saved. The same named version was opened through Open my script before and after the chart reload. The entire editor was copied back for each comparison, normalizing CRLF to LF and ensuring a terminal LF. Both comparisons matched the GitHub bytes, SHA-256 and Git blob.

| Release evidence | Value |
| --- | --- |
| Candidate checkpoint | `d354c4df69f80f10eee200d6f87eb25b84df7dcf` |
| Candidate source and build | `a3f78d498b34b697257d00f030dacafafcdbfdce` · `AE-0.1.10-148c152b12d2` |
| Normalized source SHA-256 | `4c01ea5b52cf7aeaa81b698b0286d0764ea7e113b569e8eb8489321dfd8ef21b` |
| Pine Git blob | `2632dc57ce6a53fe9e963dc830c15e567b6bbcd9` |
| Rollback | Private version 6, `AE-0.1.6-00d26a21011a`, SHA-256 `9376df68e43cb76d260ab109ca69b1b2813366a75072856b506ae2397f76fcec`, blob `12504758e6b4febedc07b4ce3aea760faf6923bb` |
| Candidate checkpoint CI | [Run 43429895366](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43429895366), job 131900481259, 146 tests passed. The separate 21 structural checks were carried forward from the earlier local run. |

### Controls and reload comparisons

Thirty-five source input declarations produced 39 displayed controls. The four date/time inputs each produced a date field and a time field.

| Group | Default values confirmed before and after the final reload |
| --- | --- |
| Manual setup (12) | Setup OFF, revision 1, four dates 1970-01-01 with four 08:00 PHT times (UTC epoch zero), support floor and ceiling 0 |
| Manual nominal geometry (4) | OFF, entry/stop/target 0 |
| M01 audit (3) | OFF, left and right widths 2 / 2 |
| Integrated research (5) | ON, strict swing width 2, R1-A, tolerance 1 tick, bullish rejection alternative OFF |
| Chart structure (4) | Swing labels, armed S/R and BOS/possible CHoCH ON, history per label type 8 |
| Chart zones (2) | OB/supply-demand and three-bar FVG ON |
| Chart guides (4) | Fib 50 / 61.8 / 70.5 ON, EMA 20/50/200 OFF |
| Chart observations (4) | Contact, closed reaction and support invalidation ON, integrated nominal geometry OFF |
| Dashboard (1) | Corners |

An additional save/reload enabled all three EMAs and the integrated nominal geometry switch. All 39 values restored in that configuration. The EMAs rendered at 3880.19, 3883.41 and 3892.83 at the same cutoff. Nominal geometry remained absent because the engine withheld qualification. The tested values were then returned to defaults, saved and reloaded again.

| Closed cutoff (UTC) | Capture times before / after reload (UTC) | Stable evidence on PAXGUSDT Spot, standard 5m |
| --- | --- | --- |
| 2026-11-13 13:15 | 13:19:48 / 13:19:56 | Both panels reported the same build. Manual setup insufficient because undeclared. Possible shift, CHoCH candidate at 10:35 @ 3887.63, 1H/4H down, RSI 40.0, reaction WAIT on bullish HTF alignment, Bear FVG OPEN 3876.39–3877.67, Supply OB OPEN 3905.97–3909.38. Swing/BOS/CHoCH labels, both zone drawings, the historical support-invalidation marker and three enabled EMA plots restored. |
| 2026-11-13 13:20 | 13:23:55 / 13:24:05 | Same build, manual reason, structural event, HTF alignment and reaction reason. RSI 33.5, Bear FVG OPEN 3876.15–3876.35 and Supply OB OPEN 3905.97–3909.38. Swing/BOS/CHoCH labels, zones and the historical invalidation marker restored. The three EMA plots were hidden at defaults. Confirmed HTF clocks were 13:00 (1H) and 12:00 (4H). |

Both pairs had no armed reference, active Fib, current reaction or nominal geometry. TradingView's forming prices and automatic scale varied across samples. The chart clock, dashboard state and confirmed event placements were compared at the same closed cutoff. BTCUSDT, ETHUSDT and XAUTUSDT Spot were also sampled at their 13:20 UTC close for an active Fib set. None qualified. This supplements the earlier instrumented positive history and does not extend the coverage of the matched private reloads.

| Gate | Result |
| --- | --- |
| Rollback identity and retention | **PASS.** Named v6 editor bytes matched GitHub before replacement, and version history listed v6 after v7 was saved. |
| Executed rollback after successful release | **NOT RUN.** The verified v6 history entry is the recovery path. |
| Exact candidate and native compilation | **PASS.** Editor equality before compilation and exact build in the running panels. |
| Named script save and full source readback | **PASS.** Same script at v7.0, with exact source before and after the browser reload. |
| Separate layout save and supported identity | **PASS.** Saved standard Binance PAXGUSDT Spot 5m layout restored v7.0. |
| Full control and default restoration | **PASS.** Original 24 and added 15 controls matched, including two saved configurations. |
| Same-cutoff dashboard, structure, OB/FVG, EMA and historical invalidation parity | **PASS** for the two observed pairs and the visible states listed above. |
| Positive armed reference, Fib, contact/reaction and nominal geometry at matched private reload cutoffs | **INSUFFICIENT.** No qualifying positive state for these layers in the paired samples. Historical positive evidence is separate. |
| Unsupported chart suppression | **PASS.** PAXGUSDT 15m standard candles and PAXGUSDT 5m Heikin Ashi both withheld research drawings and showed the standard 5m requirement. Restored standard 5m afterward. |
| Continuous native intrabar acceptance | **NOT RUN.** Two live same-cutoff snapshots are point observations. |
| Cross-device persistence | **NOT RUN.** Verified in one authenticated browser. |
| Chart readability at the sampled viewport | **FAIL** for unobstructed lower-left panel text. In the saved chart, candles could obscure research text, and the TradingView watermark overlapped the last row. The underlying state remained readable in an unobstructed sample. |

The Basic account showed a two-connection warning during layout save. Using TradingView's Restore connection control cleared the interruption. The layout acknowledgement, subsequent reloads and v7 source readback then passed. Native evidence was recorded without publishing private screenshots or account details.

### Bounded v1 readiness and integration

Private v0.1.10 is usable for the accepted research scope. The sampled chart presents coherent closed structure, zones, unsupported-state explanations and indicator identity. The actionable v1 usability issue is lower-left research table legibility. Evaluate TradingView's visual order and panel placement on a disposable instance first. TradingView documents that declaration-level visual settings apply when an instance is added, so a source edit to `behind_chart` alone cannot demonstrate a fix in an existing saved instance. Prefer the smallest correction that preserves candle and annotation readability, then verify at the normal and constrained viewport sizes. [TradingView visual order](https://www.tradingview.com/pine-script-docs/visuals/overview/#behind_chart).

Prioritize a same-build positive Fib or observation reload and a bounded live forming-to-close/reload sample before broadening runtime claims. Preserve current evidence distinctions for strict sequence, model-derived contact and nominal geometry.

Keep PR #3 based on PR #2 and keep both drafts for the integration decision. At inspection, main was `319459863fc138e8d347a1b00bc1de56fabb114c` and PR #2 was `9b765df5bb9ceebe77ce57b216281be6c6ba3282`. Both were reported clean and mergeable. Review and accept PR #2 against main first, then retarget or refresh PR #3 against the integrated base and check fresh CI. Preserve the pinned ancestors used by the regression suite. The guide, observation, zone, structure and native lifecycle checks load specific historical blobs via `git show`, and CI uses full checkout history. A squash or rebase that drops those objects from the fetched ancestry can break the suite even when the Pine bytes match. Use an ancestry-preserving integration or explicitly qualify a new reproducible fixture scheme before changing merge methods.
