# Work design-review brief — provisional v1.1 product direction

**Date:** 2026-11-14 Asia/Manila  
**Requested by owner:** Send Work the complete new direction and request a deliberate **Ponder-style product and methodology review** before freezing v1.1 requirements.  
**Status:** **DRAFT FOR WORK CRITICAL REVIEW — NOT FINAL PRODUCT DESIGN, NOT CODE AUTHORIZATION BY THIS BRIEF.**  
**Source of truth:** [PR #4](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/4), [DECISIONS](../DECISIONS.md), [STATE](../STATE.md), [RECOVERY](../RECOVERY.md). Recheck current repository refs before work.

## 1. What the owner has actually selected (current preferences, still open to deliberate revision)

These **explicit owner directions** supersede older proposals; their specific technical implementations are not final:

1. **Product:** Independent **Alpha Engine TradingView**, built on Coach Fredy's documented lessons + completed PCSS interpretation + separately attributed AI-designed research improvements; not a reactivation of an earlier Alpha Engine/Sites product.
2. **Market focus (D-038):** **Only Binance USDⓈ-M USD-stablecoin-quoted/settled PERPETUAL instruments** (USDT, USDC, any additional USD-stablecoin contract only after positive product verification). No Binance Spot, no COIN-M/inverse/coin-margined perps, no dated/delivery futures, no other exchange. The underlying can reference gold only when the actual Binance **contract product** meets these criteria; never substitute Spot XAU or a gold-backed token. Do not treat any USD-suffixed ticker or any `.P` suffix alone as sufficient evidence.
3. **Direction:** **Both LONG and SHORT** research workflows, rather than just the current experimental bullish support reaction.
4. **MTF analysis (D-039):** **4H, 1H, 15m and 5m** all required in the analytical framework.
5. **Interface:** Owner wants practical, readable on-chart TradingView research: structure, important locations/zones/Fib, reactions, invalidation, conditional nominal E/SL/TP/R, transparent dashboard explaining WAIT/INSUFFICIENT vs observed/qualified. These are the shared product vision, but exact labels, priorities, state-machine rules, chart settings and UI design are **provisional**.
6. **Principles:** Source-ground Coach claims vs independently invented improvements; reliable non-lookahead/cutoffs, transparent evidence, no manufactured trade, no proof of profitability from software tests. Indicator-first and private release remain the working path. ChatGPT companion, alert/webhook scanning and any execution/backtesting are **separate potential future capabilities**, not current completed integrations.

**Explicit owner qualifier:** “this is not yet final, we will also ask Work to [Ponder]”. Treat the above as the **current preferred scope to review**. Do **not** silently broaden or override choices. If Work sees material problems, present alternatives and tradeoffs for owner's decision, not a unilateral rewrite.

## 2. Proposed engineering interpretation — NOT confirmed owner choices

- 4H = broader market regime and qualified levels; 1H = intermediate structure; 15m = candidate setup/AOI and zone lifecycles; 5m = local closed-candle confirmation and nominal geometry.
- Initially host the indicator on **standard 5m** TradingView candles, requesting confirmed 15m/1H/4H values for the **same exact eligible Binance USDⓈ-M perpetual feed**.
- A chart on 15m is not initially the same use case as analyzing 5m *inside* a 15m host; naive lower-timeframe `request.security` selection does not reproduce full 5m event sequences.
- Require per-timeframe source identity, latest confirmed bar close, known-at timestamp, evidence readiness, gap/warmup, and explicit disagreement/unknown. **Do not require all four to agree by default or reduce them to an unjustified score/majority vote.**
- Model independent LONG/SHORT setup state machines: structural orientation, qualified support/demand or supply/resistance, reference arming and retirement, contact, reaction, valid E/SL/TP ordering, episode invalidation/expiration. The exact threshold definitions and possible mixed/countertrend cases need review and falsification.
- Use exact Binance contract verification and appropriately qualified TradingView chart metadata; Pine may not have adequate metadata to prove every derivative's margin/settlement/type independently. Consider whether a verified, versioned allowlist/manifest, user-supplied validated product ID, per-ticker adapter, or other conservative policy is actually implementable within Pine. **No broad unqualified symbol heuristics.**
- Product is an analytical indicator, not an order executor; R is **nominal price geometry**, not leverage-adjusted realized profit/risk. Dynamic eligibility is an objective, not current verified support for every listed perpetual.

## 3. Verified baseline and what has / has not been done

- **GitHub main** at time of handoff: `8e60a982385e46aa818acb49103f1dedbe856b77`, after ancestry-preserving PR #2 and #3 merges. 148/148 standard CI on integrated main (`3ec0fe7938fa4f74856ddf959601de49f212fe0a`), plus 21/21 separate local structure checks.
- **Private TradingView release accepted:** saved v1 script version **8.0**, build `AE-0.1.11-0f4b3df98b90`, Pine blob `6fe1f8718ba8b742be500262a1df84fbd933c871`, exact-source private save/readback and bounded native same-closed-cutoff reload; version **7.0** rollback retained. See [v1 release ledger](phase3-8-v1-stabilization.md#integrated-private-v1-release--2026-11-13-pht).
- **v1 actually supports** five exact chart identities (PAXGUSDT, XAUTUSDT, BTCUSDT, ETHUSDT Spot; XAUUSDT.P perpetual) **only on standard 5m**, experimental structural/zone/Fib/EMA/RSI drawings and 1H/4H confirmed context, plus PAXGUSDT Spot-only manual Lesson08 component. Current automated reaction/nominal geometry is **bullish-only**. It is **not** our D-038/D-039 finished product.
- **Key native gap:** matched-cutoff **positive** armed-reference/Fibonacci/contact/reaction/nominal geometry saved-script reload = **INSUFFICIENT**, not a release failure. Frozen/oracle tests support partial causal lifecycle reasoning, not full Pine runtime equivalence. Existing Python `research/phase3_6/integrated_replay.py` has 5m structure/zone/bullish reaction and accepts a single externally supplied bullish HTF flag; it neither independently produces full Fib/geometry nor has timestamped per-cutoff 15m/1H/4H input.
- **New v1.1 work to date is documentation-only:** draft PR #4 records D-038, D-039, a Binance eligibility/qualification plan, four-timeframe causal design, and Work parity reconciliation. **No new Pine logic, no new native qualification, no new saved TradingView release, no market-data acceptance implied**. PR #4 remains **draft**; do not merge or promote on this review alone.
- Work's previous suggestion to audit known-at and retired-state parity beginning on frozen PAXG Spot 5m is valuable as **read-only v1 historical regression**. It must not revive Spot as the primary v1.1 target. Prioritize verified Binance USDT/USDC perpetual samples for NEW v1.1 model and native testing.

## 4. What Work is being asked to Ponder independently

**Mission: critically review the product, evidence, methodology and feasibility, not just restate or automatically approve the draft.** In particular:

1. **Scope and viability:** Is Binance USDⓈ-M perpetual-only a coherent target and is “all eligible USDT/USDC and verified USD-stablecoin perpetuals” implementable safely in TradingView Pine? What proof of product identity is available in Pine; what must be maintained externally; what is unsupported? Distinguish contract `quoteAsset`, `marginAsset`, settlement, mark/index/trade price and known symbol metadata.
2. **Four-timeframe architecture:** Is 4H/1H/15m/5m hierarchy analytically justified? Should all four always be evaluated, and what occurs when they conflict? Compare at least two credible schemes: fixed roles with 5m host vs configurable host/trigger designs. Evaluate `request.security` confirmed HTF handling, exchange-time boundaries, historical gaps, data volume and resource limits.
3. **Methodology and source fidelity:** Audit Coach PDF → PCSS interpretation → deterministic source implementation → methodology qualification → tests. Identify where the present design extends Coach with independent heuristics (EMA20/50/200, RSI14, fixed swings, order-block convention, Wick rule, Fib geometry); specify which rules need empirically motivated ablation/falsification and which might be inappropriate for perpetual derivatives.
4. **Bidirectional LONG/SHORT:** Specify symmetric causal mechanics and intentionally asymmetric edge cases; investigate countertrend vs trend-following, BOS vs possible CHoCH, zone concurrency, ambiguity, staleness and no-trade states. Don't conflate informational observed event with qualified setup or trade trigger.
5. **Futures risk and operational meaning:** Determine how nominal E/SL/TP/R differs from leverage, margin, liquidation, funding, fees, slippage and quantity filters. What warnings/definitions must be displayed to avoid overclaiming?
6. **Parity and evidence:** Does the present Python replay actually compare what is known at each native Pine cutoff? Prioritize low-cost discriminating frozen perpetual windows, positive and *withheld* state cases, 15m boundary conditions, same-cutoff reload, negative venue/product gates and reproducible evidence. Specify when native vs model-only conclusions may be made.
7. **User experience:** Evaluate dashboard structure, overlay clutter, clear wording for WAIT / CONTACT / OBSERVED / QUALIFIED / REASSESS / INVALIDATED / INSUFFICIENT, input defaults and historical vs current indicators. User seeks a tool practical to use on TradingView, not an endless dashboard of jargon.
8. **Integration and staged roadmap:** Determine fastest safe increments without rewriting accepted v1 or colliding with work in other branches. Compare whether to stabilize parity first, implement the eligible perpetual adapter first, or deliver a vertical slice with contract eligibility + four MTFs + LONG/SHORT; recommend objective release gates. Alerts, automated scanner and ChatGPT integrations should be prioritized separately based on user entitlement and feasibility.

**Do not pretend the current accepted v1 is the finished v1.1 product or that a passing unit-test suite proves an edge.**

## 5. Required Work deliverable to owner

Return a **decision-oriented design review** containing:
- **A. Restated owner requirements** versus **provisional engineering interpretations**, with any ambiguity plainly identified.
- **B. Feasibility matrix:** requirement, what Pine/TradingView supports, what Binance verification may be needed, what remains unknown, proposed fallback.
- **C. Three highest-risk assumptions** and concrete tests capable of falsifying them.
- **D. At least two meaningful architecture options**, explicit tradeoffs, recommendation and what would trigger choosing the alternative.
- **E. Concrete end-to-end trading-chart user journey** for LONG, SHORT, conflicting/insufficient evidence and invalidation; distinguish actual state from future UX proposals.
- **F. Revised scoped milestones and test/acceptance gates**, separating software correctness, native runtime equivalence, source fidelity and **unproven** trading performance.
- **G. A short list of only the decisions genuinely needed from owner before requirements are frozen**; otherwise proceed with reasoned recommendations.

Do **not** merge draft PR #4, change main, alter the saved private TradingView version, publish a public indicator, wire live order execution, or start a wide engineering implementation merely because this design-review brief exists. Keep verified code/release baselines and frozen fixtures intact. Work may identify inaccuracies and propose doc corrections in a separate review artifact without turning a provisional hypothesis into an owner-approved fact.

## 6. Source links for Work

- [Current draft PR #4](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/4)
- [D-038 Binance USDⓈ-M qualification](v1-1-binance-usds-m-perpetual-qualification.md)
- [D-039 four-timeframe MTF](v1-1-four-timeframe-mtf-contract.md)
- [Work parity audit reconciliation](v1-1-work-parity-reconciliation.md)
- [Accepted private v1 release](phase3-8-v1-stabilization.md#integrated-private-v1-release--2026-11-13-pht)
- [Coach lesson coverage](../LESSON_COVERAGE.md)
- [Pine source](../../pine/alpha-engine-research.pine) and [integrated Python replay](../../research/phase3_6/integrated_replay.py)
