# Causal chart structure overlay

**2026-11-13 PHT · v0.1.7 visualization candidate.** This is the first increment after [private v0.1.6 acceptance](phase3-6-v016-market-qualification.md#named-private-release-acceptance--2026-11-13-pht). It is an independent experimental display of the existing closed-bar calculations. The Coach and PCSS provenance of those calculations remains in the [integrated methodology record](ai-only-integrated-candidate.md).

| Identity | Value |
| --- | --- |
| Accepted private release | v0.1.6 version 6, `AE-0.1.6-00d26a21011a` |
| Visualization source | `5fcd4caf099f57340aa3fc4e6aa972428f358a3c` |
| Candidate build | `AE-0.1.7-9e93706426d6` |
| Candidate Git blob | `505811f7b8719548294d8797a8b86d2ddd11867d` |
| Candidate SHA-256 | `bb9c39801c0729279ddf06ed45c6b9bb85470beeb74983e6e1ff12471f17caa1` |

## Drawing semantics

| Layer | Timing and state |
| --- | --- |
| HH, HL, LH and LL | First classified observation of each new origin per side, from the same references the dashboard receives. Place the label at the observing 5m close and offset it above or below that candle. Tooltip shows observation time, original pivot open and level. Historical role labels record what the engine classified at that close, including classifications whose reference never became armed. Subsequent changes at the same origin remain visible through the current dashboard and active level. |
| Support and resistance | At most one line per side, only while the dashboard reference is ARMED. The horizontal line starts at its arming cutoff. A consumed, prebreached, retired, reset-pending or unavailable reference removes its line. A newer armed reference reuses the existing line where possible. |
| BOS and possible CHoCH | Use the existing event and mark only the cutoff on which it is recorded. The question mark and tooltip identify an experimental candidate. Tooltips give the closed cutoff, crossed level, and reference policy. |

The accepted research logic and dashboard source are byte-identical after reversing only the indicator title, build ID and drawing budget declaration. The overlay does not write research state or request market data. It uses the same qualified chart, integrated enablement and closed-bar gates.

Four settings control the overlay. Three independent switches default ON. History defaults to eight swing labels and eight event labels, with a range of two to 16 per family. Old labels are deleted before a replacement is created. The Pine declaration reserves 35 labels in total, including three for the original Lesson 08 module, and at most two lines. Swing labels remain informational in insufficient current states. Live reference lines follow the current research state and disappear when it provides no armed reference.

- [TradingView Pine lines and boxes](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/)
- [TradingView Pine text and shapes](https://www.tradingview.com/pine-script-docs/visuals/text-and-shapes/)

## Verification

| Gate | Result |
| --- | --- |
| Regression and frozen research model | **PASS.** 131 standard local tests and 21 separate structural tests. The four added checks cover byte-exact core isolation, causal label anchors and deduplication, object limits and retirement gates, and both R1 policy models on the frozen PAXGUSDT tape. The first run failed because the new fixture used three incorrect model attribute names. The fixture was corrected and the full suite passed. Pine source was unchanged by that correction. |
| Exact native compile | **PASS.** Complete unsaved editor copy-back matched candidate SHA-256. Native chart reported build `AE-0.1.7-9e93706426d6`. |
| PAXGUSDT Spot 5m render and baseline parity | **PASS.** HH, HL, LH, LL, BOS? and CHoCH? visible, with two active lines matching LH 3915.53 and LL 3900.98. At 05:25 UTC the candidate and v0.1.6 had matching structure, event, references, HTF, momentum, reaction, gap, Fib and block outputs. |
| Visibility and density | **PASS.** With the three switches OFF the drawings cleared after redraw and the dashboard stayed active. At a cap of two, the chart showed two swing labels, two candidate markers and both active lines. |
| Second native feed and absent references | **PASS.** Binance BTCUSDT Spot 5m rendered two swing labels and two possible CHoCH events at the reduced cap. The 05:25 UTC dashboard had no active references and neither line was drawn. This sampled observation establishes state correspondence. A live reference retirement was **NOT RUN**. |
| Unsupported chart | **PASS.** Binance PAXGUSDT at 15m displayed INSUFFICIENT and no structure drawings. |
| Release isolation | **PASS.** v0.1.7 ran in an untitled buffer. The temporary chart instance was removed. Reopened the existing named private version 6 and verified exact v0.1.6 source after the test. The original standard PAXGUSDT Spot 5m layout reloaded with v0.1.6 alone. |
| Expanded graphics and private v0.1.7 persistence | **NOT RUN.** The first increment covers structure only. Zone and gap boxes, Fib and optional EMA overlays, contact/reaction/invalidation markers and nominal geometry are subsequent increments. |

Next, draw the existing order-block/supply-demand and three-bar gap states with left edges at their known-at cutoffs and explicit tested/invalidated behavior. Keep the accepted release and this tested structure layer as separate checkpoints.
