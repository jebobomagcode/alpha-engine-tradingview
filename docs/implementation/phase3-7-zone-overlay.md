# Order-block and three-bar FVG chart overlay

**2026-11-13 PHT · v0.1.8 visualization candidate.** The [v0.1.7 structural overlay](phase3-7-structure-overlay.md) remains the foundation. This is an independent experimental display of the existing [block and gap research states](ai-only-integrated-candidate.md). Geometric tests describe OHLC overlap. The drawing layer does not infer execution or profitability.

| Source identity | Value |
| --- | --- |
| Starting draft PR #3 head | `71f48925063b65ca4043a8fe8ee2575480a0d324` |
| Zone source | `10b3e965afb3cda33d8e327a4c941be6352bccd2` |
| Final candidate source | `14b57b6148a6c39d215ca309354544a59c6a5e74` |
| Build | `AE-0.1.8-6927cc23e060` |
| Pine blob / SHA-256 | `05c1e2453e36ac1b54ee2bc6a2c109e8200d4538` / `fd58a52d11637884171b47fbb7df1094c5cc3cfcf0d633b9a587b16f2bb0b30a` |

## Display contract

- Independent default-on controls expose the most recent order-block/supply-demand zone and the most recent three-bar FVG candidate. Each family reads its own engine known-at timestamp, side, price bounds and state after the confirmed 5m evaluation. The structure drawings, dashboard and research calculations match the v0.1.7 source after normalizing the title, build and drawing budgets.
- The box begins at the source known-at cutoff using Pine's time coordinates. Its rightward extension represents the latest candidate. OPEN and GEOMETRIC TEST remain extended. GEOMETRIC TEST mutes the fill and border. An INVALIDATED block becomes neutral and its right edge stops at the invalidating close. FVG continues to use the engine's OPEN / GEOMETRIC TEST lifecycle.
- The badge anchors at the close that established the displayed state. A short tooltip gives the originating knowledge time, bounds and state-change time. Text extends left of the anchor so it fits near the chart edge. The existing upper-right panel can still overlap recent drawings at some zooms.
- Replacement deletes the old box and badge before creating the current pair. The engine's final state wins if a close tests or invalidates an old zone and creates a replacement. A cleared engine snapshot deletes its objects. This is a latest-zone view. Replaced drawings leave the chart, and the color over a retained box reflects its current state.
- The layer adds at most two boxes and two badges. Including the accepted manual zone and existing markers, the indicator reserves three boxes, 37 labels and two lines. The accepted research engine's chart, enablement and finality gates also gate these drawings.

[TradingView Pine box coordinates and lifecycle](https://www.tradingview.com/pine-script-docs/visuals/lines-and-boxes/)

## Verification

| Gate | Result |
| --- | --- |
| Standard and separate structural suites | **PASS.** 137 local standard checks, including six added tests, and 21 separate structural tests. The new tests pin exact core preservation, state and timestamp bindings, draw gating and object lifecycle, modeled block/FVG transitions, replacement, continuity reset and frozen-prefix invariance under both R1 policies. The final candidate [CI run](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43374194745) is associated with the final source commit. |
| Exact native source and rendering | **PASS.** Copied back the complete unsaved Pine Editor buffer and matched the final GitHub SHA-256. TradingView compiled the exact candidate and displayed the build on standard Binance PAXGUSDT and BTCUSDT Spot 5m. At 05:45 UTC, PAXGUSDT matched the accepted dashboard with a new Supply OPEN block at 3905.97–3909.38 and Bull GEOMETRIC TEST FVG at 3905.26–3905.38. At 11:10 UTC PAXGUSDT showed the retained block and a replacement Bear OPEN FVG at 3881.67–3882.34. At 11:05 UTC BTCUSDT showed Demand INVALIDATED at 75310.00–75378.00 and Bull GEOMETRIC TEST FVG at 69286.24–69313.87. |
| Native object coordinates, replacement and invalidation | **PASS, instrumented historical scan.** Ran the exact drawing logic with a temporary read-only Pine audit appended. For each evaluated close it checked drawing presence, left time, prices, current state, badge bounds and invalidated right edge against the native engine. Candidate draw functions were unchanged. Both markets returned zero violations. The measured peak was two boxes with the manual setup disabled. |
| Visibility and unsupported interval | **PASS.** Native PAXGUSDT showed FVG alone and block alone when the other control was disabled. Both were visible when restored. At 15m the exact candidate withheld drawings and the audit counted zero evaluations or objects. |
| Non-repainting scope | **PASS** for closed-bar-only source isolation, frozen-prefix invariance, and native historical knowledge-time and state checks. Native candidate displayed the same retained states as the baseline during the forming PAXGUSDT bar. Continuous tick-by-tick and same-cutoff candidate reload parity were **NOT RUN**. |
| Accepted private release isolation | **PASS.** The temporary chart instance resurfaced after a browser pause and reload. Removed the candidate and audit instances, reopened named version 6, and copied back its exact v0.1.6 SHA-256 `9376df68e43cb76d260ab109ca69b1b2813366a75072856b506ae2397f76fcec`. The original standard PAXGUSDT Spot 5m layout reloaded with v0.1.6 alone after restoring all 24 accepted controls. No named Pine version was saved in this increment. |

### Native historical audit counts

R1-A, swing window 2, both zone switches on. Observed 2026-11-13 at the 11:10 UTC cutoff, 19:10 PHT. Each replacement count requires a prior and current known-at value and a changed timestamp. Test and invalidation counts track entry into the corresponding engine state. Audit violations compare the candidate's actual drawing objects with its native engine outputs.

| Binance Spot 5m | Closed bars | Violations | Peak boxes | OB / FVG replacements | OB / FVG tests | OB invalidations |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| PAXGUSDT | 5,314 | 0 | 2 | 14 / 1,920 | 12 / 1,018 | 12 |
| BTCUSDT | 5,318 | 0 | 2 | 15 / 1,538 | 12 / 865 | 12 |

The initial native build exposed right-edge badge clipping. The final candidate fixes the badge orientation while retaining the exact knowledge and state anchors. Draft PR #3 stays stacked on draft PR #2. Private promotion remains **NOT RUN**. Next visualization work covers Fibonacci retracements, EMA overlays, contact/reaction/invalidation markers and nominal risk geometry.
