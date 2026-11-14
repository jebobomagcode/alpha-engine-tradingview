# v1.1 coordination handoff — Work parity proposal reconciled with D-038

**Date:** 2026-11-14 Asia/Manila  
**Status:** OWNER-SUPPLIED WORK ADVICE REVIEWED; ENGINEERING PLAN, **NOT** TEST EXECUTION OR NATIVE ACCEPTANCE  
**Primary scope:** [D-038](../DECISIONS.md), [active Binance USDⓈ-M perp qualification](v1-1-binance-usds-m-perpetual-qualification.md)  
**Current draft:** [PR #4](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/4), documents only.  
**Coordination:** Treat GitHub as the cross-conversation handoff. Do not restart completed v1 studies, prior audits or merges; don't overwrite work performed on another branch without checking current refs.

## Current verified immutable baseline

- `main` HEAD at handoff: `8e60a982385e46aa818acb49103f1dedbe856b77`; bounded v1 owner-private TradingView version **8.0**, build `AE-0.1.11-0f4b3df98b90`, Pine Git blob `6fe1f8718ba8b742be500262a1df84fbd933c871`; saved version 7.0 remains rollback.
- Main integrated PR #2 and #3, 148/148 standard postmerge CI at `3ec0fe7938fa4f74856ddf959601de49f212fe0a` plus 21/21 separate local structural checks. Later `main` checkpoint was docs-only.
- Last native accepted reload on **PAXGUSDT Spot 5m** verified structure/zone/FVG state but **no positive current Fibonacci, armed reference, contact/reaction or nominal E/SL/TP state**. These positive-state reloads remain **INSUFFICIENT**, not FAIL. Continuous intrabar and cross-device NOT RUN. The accepted bounded release is not invalidated.
- Owner's **new target** (D-038): **Binance USDⓈ-M stablecoin-settled PERPETUAL swaps ONLY** (USDT/USDC and any positively verified other USD-stablecoin contracts), with both LONG and SHORT informational research. No Binance Spot, COIN-M inverse/coin-settled, dated futures, other exchanges or public release. Gold-referencing Binance USDⓈ-M perpetual can qualify by exact contract metadata.
- Work's prior statement “no open PRs” was accurate only before PR #4; **PR #4 now exists**, draft. Verify GitHub again before reporting freshness.

## Assessment of Work's proposed next step

Work proposed a focused v1.1 Pine↔Python parity audit of *what became known, when and when it ceased to be valid*, beginning from PAXGUSDT **Spot** frozen/live 5m, comparing armed-reference/Fib creation, persistence, replacement and retirement, then reaction/geometry and positive same-cutoff saved reload.

**Accept the causal audit objective, but adapt the sequencing to D-038:**

1. **R00 — read-only legacy regression preflight:** Use the already frozen v1 Spot receipts and historical SHA-pinned fixtures to inventory what is currently modeled and to protect the accepted lifecycle behavior. **Do not treat Spot as a new v1.1 runtime target, spend time seeking a new Spot positive-state native event as a blocking gate, or manufacture full Pine parity from source-text checks.** Spot fixtures remain useful as v1 regression truth for the historical build.
2. **R01 — contract/product adapter and stablecoin perpetual baseline (current top feature priority):** Verify exact Binance USDⓈ-M `PERPETUAL` contract and TradingView feed identity; reject Spot, COIN-M, delivery contracts and unknown feeds. Require positive actual USDT and USDC cases; permit XAUUSDT.P only if its product metadata qualifies. Handle variable ticks, source series identity, quote/margin/settlement. Never simply lift chart gates.
3. **R02 — targeted causal parity on eligible perpetual tapes:** Create or qualify frozen *perpetual* windows for the same source product, test structural reference creation/arming/replacement/retirement, BOS/possible CHoCH, FVG/OB open/geometric-test/invalidated states, and Fib birth/replacement/retirement. Report cutoff, available-at, source candle IDs, prices in actual ticks, chart/evidence status and reason for withholding. Compare deterministic models; native Pine comparisons separately where observable.
4. **R03 — complete directional and HTF model:** The existing `research/phase3_6/integrated_replay.py` accepts a **single** `confirmed_bullish_context: bool | None` for the replay, not a cutoff-indexed authenticated HTF series; do not invent 1H/4H context from a short 5m tape. Add a per-cutoff confirmed 1H/4H context evidence contract with known-at times and missing-data states. Add independent Fib and nominal E/SL/TP projections; `IntegratedFrame` currently contains structural, reference-ID, event, gap/block and reaction fields **but not Fib or geometry**. Then qualify both LONG and SHORT resistance/supply vs support/demand state machines with asymmetric edge conditions tested.
5. **R04 — positive-state persistence audit:** If a suitably qualified *perpetual* native positive state occurs, compare exact named-script version, same closed cutoff before/after reload, full input manifest, drawing price/timing, and absent-state clearing. A bounded window with no positive state remains **INSUFFICIENT**; continue independent deterministic frozen-window research and do not falsely claim a pass. Basic-plan intraday replay remains previously reported blocked, not assumed newly available.
6. **R05 — successor release:** Confirm newly added and retained tests, 148 legacy standard + 21 separate structural baseline, native Pine exact-source compile and negative product/timeframe gates, causality, risk geometry visibility and rollback. Do not change private v8 or publish until separately verified and accepted under existing change controls.

## Parity audit matrix and falsification gates

| Evidence field | Minimum requirement |
| --- | --- |
| Product | Exact `BINANCE:` TradingView ticker, Binance USDⓈ-M `PERPETUAL` `exchangeInfo` identity, quote/margin/settlement, bar-price source (last trade vs mark/index) |
| History | Source digest, timezone (UTC for source; PHT for reports), source bar open/close, 5m sequence and gaps |
| Context | Separate confirmed 1H and 4H evidence time, *known-at* cutoff, warmup readiness and no lookahead |
| Reference | Side/direction, pivot origin, confirmation/armed time, price ticks, predecessor ID, replaced/retired reason |
| Overlay | Fib source anchor IDs and level rounding; FVG/OB creation/test/invalidations; absent/withheld drawings |
| Reaction | LONG and SHORT support/resistance contact, reaction, consumed/expired/invalidation rules, optional wick policy |
| Nominal geometry | Direction, E, SL, TP, R algebra, tick normalization; **not actual P&L, liquidation, fees or fills** |
| Parity | Same chart product and same closed cutoff; compare model-vs-model separately from model-vs-native; record mismatches rather than averaging them away |
| Persistence | Named version and script source digest, saved input manifest, positive-state before/after at exact closed cutoff, last-forming price separately |
| Status | PASS / FAIL / INSUFFICIENT / NOT RUN; never upgrade an unseen positive native state from source-only tests |

### Existing resources, limits, and non-duplication

- [Private v1 release ledger](phase3-8-v1-stabilization.md#integrated-private-v1-release--2026-11-13-pht)
- [Integrated replay](../../research/phase3_6/integrated_replay.py): causal structure, latest zone and bullish support/reaction comparator only; does not execute Pine, authenticate TradingView candles, output Fib or geometry, or supply a per-bar HTF receipt. Use it as a **partial foundation**, not proof of complete parity.
- [Integrated tests](../../tests/test_phase3_6_integrated_replay.py), [Fib drawing checks](../../tests/test_phase3_7_chart_guides.py) and [reaction/geometry checks](../../tests/test_phase3_7_chart_observations.py): valuable prior evidence; source-fragment tests are not a Pine runtime executor.
- Existing frozen PAXGUSDT Spot 5m receipt in `docs/research/evidence/m07-paxgusdt-spot-v1/klines-5m.json` is **historical v1 regression only** under D-038. Do not purge it.
- Work's original recommendation to start with armed references and Fibonacci is useful for **research coverage**, but any NEW native product qualification should favor target-market Binance stablecoin perpetuals over Spot.
- Owner's Coach PDF → PCSS interpretation → deterministic implementation → methodology qualification → tests/historical compatibility remains the source-lineage policy, without repeating already completed 35-page studies.

## Resume instructions for normal ChatGPT and Work

Verify `main`, PR #4 and any new engineering PRs before acting. Read current [STATE](../STATE.md), [D-038](../DECISIONS.md) and this handoff. Keep PR #4 documentation-only and draft unless independently ready; implement R01+ on a separate development branch after coordinating to prevent collisions. Preserve stable source hashes, test ancestry and owner-private v8; do not resume PAXGUSDT Spot as primary supported v1.1 market. Mark any external or native observations actually run with precise evidence. No scheduled automatic/background work is implied by this handoff.
