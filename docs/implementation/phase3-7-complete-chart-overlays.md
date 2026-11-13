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
