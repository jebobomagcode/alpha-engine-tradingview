# Main-workspace response to Work v1.1 design review — provisional

**2026-11-14 Asia/Manila · Status: technical assessment and recommendations for owner consideration, NOT owner signoff or implementation authorization.**

**Work source:** [Work's 2026-11-14 full design review](v1-1-product-design-review.md), pinned review commit `ceb062cca28cb5a5dcfde29e7c8d11a68fe582a5`, plus the owner's uploaded local review and summary.  
**Existing source-of-truth:** [D-038–D-040](../DECISIONS.md), [provisional how-it-works blueprint](../product/v1-1-provisional-how-everything-works.md), [4TF MTF contract](v1-1-four-timeframe-mtf-contract.md).  
**Scope:** read/review/document only. No Pine changes, new exchange receipts, native tests, PR merge, private save or execution.

## Main conclusion

**Support Work's bounded, chart-first v1.1 architecture as the first *release increment*, but do not silently reduce the owner's full product destination.** The intended market is still **all positively qualified Binance USDⓈ-M USD-stablecoin-settled perpetual contracts** and four analysis periods **4H/1H/15m/5m**, with both LONG/SHORT. A short initial **verified USDT+USDC coverage set** is a rational staged release qualification plan, **not** permanent whitelist or exclusion of eligible additional symbols. Clarify this distinction in any eventual specification freeze.

Work's proposal for a single standard **5m host** with same-contract confirmed 15m/1H/4H packets is the lowest-risk first native implementation: it avoids unqualified 5m intrabar reconstruction on higher hosts. Native host flexibility is a later product option, not a newly owner-disallowed feature.

Maintain the existing named private TradingView **v8.0** build `AE-0.1.11-0f4b3df98b90`, rollback **v7.0**, GitHub `main` at `8e60a982385e46aa818acb49103f1dedbe856b77` at this review, and the separate v1 148/148 standard and 21/21 structural baselines. Work's PR #4 is documentation-only and draft.

## What this review supports, with precise limits

### 1) Product identity and feed correctness

Agree with a **versioned, evidence-bound product/feed manifest**, with separate raw Binance contract enum and normalized family, quote/margin/settlement evidence, exact TradingView *trade-price* feed, tick grid, metadata date, and native-test status. Positive admission must be narrower than simple `BINANCE:`, `.P`, `USDT` suffix or matched `syminfo.mintick`. Work correctly flags a frozen `TRADIFI_PERPETUAL` XAU record; a literal raw-`PERPETUAL` guard would create a false exclusion. **Qualification must retain room for verified Binance product variants without assuming universal current support**.

Caveat: A bundled Pine manifest is only as current as the script build. If an instrument is newly listed, delisted, renamed or repriced, the system needs a documented update mechanism and stale-metadata status. Do not imply the indicator can automatically discover and authenticate the live Binance derivatives universe entirely inside Pine. Record *in-scope*, *mapped*, *native-tested* and *ready at decision cutoff* separately.

### 2) Four clocks and no-lookahead causality

Agree with Work's **opening snapshot / closing transition** as the conservative first policy. For `[10:10,10:15)` 5m input, a 15m zone that only becomes known at **10:15** cannot retrospectively have governed contact during the same 5m interval; the new packet can affect a subsequent decision (e.g. **10:20** if included in the next interval opening snapshot). This policy must be verified on actual Pine behavior and identical per-timeframe input records; it is **not a claim of authenticated arrival timing**.

Important distinction: a packet may be mathematically completed at a shared timestamp without having been observed/delivered in a reproducible order. Keep `known-at (modeled)` and `actually received-at (observed)` distinct. When no receipt exists, label availability as model/chart-clock evidence only. Require pre/post 15m/1H/4H and simultaneous boundaries, stale held packets, warmup/gaps and future-prefix invariance. A verified 5m decision must never use 15m/1H/4H from a different symbol or mark/index series.

### 3) Narrow continuation profile, but preserve Coach cases

Agree with **one LONG and one SHORT continuation profile** for an initial testable slice: 4H regime, 1H structure, 15m preknown S/R AOI, 5m closed contact/reaction, independently testable invalidation, and separate geometry. Preserve a countertrend reaction as an observation when it fails continuation alignment. That is a **scoped v1.1 first-release profile**, not a claim that the Coach material has only continuation trades.

Work's source review identifies **range**, **break-of-confirmation-candle**, **reversal** and **alternative Q&A3 breakout/rejection** examples. Keep these **named future research profiles with source traceability**. A rigid, universal requirement for all four directional votes or an automatically hard 1H veto would exceed the Coach's conditional source examples and should be an empirical comparator. A 5m pullback opposite to the 4H direction may be a normal continuation retracement, not a global structural conflict.

Caveat: one 15m zone per side is a *presentation/episode policy*, not proof that other simultaneous valid zones do not exist. If zones overlap, define deterministic ranking, pinned episode identity, tie-breaks and replacement/retirement. Reject any version that changes an earlier zone selection based on a future bar. OB/FVG/Fib should remain visible as context while the S/R baseline is being qualified; expanding hard gates requires evidence.

### 4) Coach attribution corrections

I independently checked the local 35-page Coach PDF text and visually inspected its p14 order-block figure. The PDF **explicitly names RSI length 14, common EMA 20/50/200 and the separate 0.50–0.618 and 0.618–0.705 Fibonacci bands**. Therefore our earlier blueprint's blanket classification of **those numerical settings themselves** as independently invented AI defaults needs correction. The exact use as a mandatory EMA stack, 1H+4H veto, numerical zone rule or Fib anchor selection **remains independent formalization**. The p14 figure depicts swing-adjacent OB candles and a 1→3 gap; it **does not prescribe a universal opposite-color OB rule**, so the existing opposite-body detector must remain labeled experimental.

Protect this distinction in the canonical blueprint after owner review; source names of conventional parameters do **not** prove predictive usefulness in Binance perpetuals. Similarly, correlated BOS, OB, FVG and EMA responses should not be multiplied into an unsupported “confidence score”.

### 5) Setup qualification must be separate from price geometry

**Strongly support** Work's third recommendation. Track **product/data readiness**, **per-side episode**, **observation/reaction**, **formal setup qualification**, **blocker/invalidation**, **geometry availability**, and **history** separately.

An observed valid directional continuation can remain visible as a `SETUP QUALIFIED / GEOMETRY UNAVAILABLE — no eligible prior target` when its *setup rules* pass but a valid E/SL/TP cannot be computed. Do **not** label such a setup `TRADE READY`; no automatic executable trade instruction is implied even with geometry. Invalidated or consumed targets and same-bar wrong-side closes clear current geometry; earlier dated events persist. Nominal R derives strictly from displayed tick-normalized positive signed distances, not from hypothetical fees or slippage.

**Terminology issue for final spec:** Do not allow one generic `QUALIFIED` headline to blur a price-pattern observation, methodology qualification, geometry validity and trade execution. Propose `SETUP QUALIFIED` + a separately explicit `GEOMETRY VALID/UNAVAILABLE` badge or text.

### 6) Native acceptance and provider caveats

Accept Work's four independent release claims: (i) **correct product gate**, (ii) **causal frozen decisions on pinned inputs**, (iii) **native Pine behavior on actual named Binance perpetuals**, (iv) **named-script persistence**. These do not constitute source-faithful implementation of every Coach lesson and do not establish profitable trading performance.

Require **at least one native USDT and one native USDC qualified perpetual with different tick sizes**, positive LONG and SHORT cases where feasible, and adversarial negative feeds. For the desired first release with both directions and both quote families, Work reasonably treats absent positive native functionality on a required direction or quote family as a release blocker. A rare **positive same-cutoff reload** not observed in a bounded session stays `INSUFFICIENT` with a coverage limit, not a false PASS or automatic blanket FAIL. Disclose any retained uncertainty.

Do not make automatic TradingView alerts, scanning all Binance contracts, ChatGPT conversation push, live orders, leverage risk or profitability part of this indicator-first acceptance. They can be separately researched later, especially because the user's earlier TradingView Basic alert gate failed. Keep these product aspirations visible but not silently authorized.

## Three owner's open decisions — independent recommendations ONLY

| Choice Work asked the owner to settle | Recommended provisional answer | Boundary and tradeoff |
| --- | --- | --- |
| **1. Initial coverage and viewing** | **YES:** begin with a *small, positively verified* USDT + USDC perpetual subset on standard **5m host**; expand by documented qualification toward the owner's broader eligible-contract vision. XAUUSDT is **not mandatory at first private successor** unless the owner makes it a day-one requirement. | Highest chance of credible native evidence and preserved 4TF causality; not automatic coverage of all Binance perpetuals. If gold is an essential user workflow, move verified XAU into the initial acceptance matrix. |
| **2. Initial setup profile** | **YES:** bidirectional **continuation** first; expose range/reversal/breakout and countertrend **observations** without mislabeling them as continuation-qualified setups. Develop later named profiles after source-specific rules and timing checks. | Prevents first release from becoming untestably broad. Does not mean Coach's non-continuation lessons are abandoned. |
| **3. Qualified setup without geometry** | **YES:** preserve **SETUP QUALIFIED** if all setup gates pass; display **GEOMETRY UNAVAILABLE** when no valid stop/target exists. Do not present it as an executable trade. | Prevents deletion of real observed evidence. Differentiates event logic from price-risk model completeness. |

**These are the main workspace's recommendations, not owner approvals.** Do not record any of the three as closed in `DECISIONS.md` without explicit owner selection. The user previously said the product design is not yet final.

## Material additional checks before freezing the specification

1. **Release boundary versus aspirational coverage:** write explicit acceptance table for initial two contracts (USDT, USDC), positive/negative direction and 4TF readiness while naming the later expansion mechanism. Avoid claiming all contract families already accepted.
2. **Definition of SETUP QUALIFIED:** can a setup be 'qualified' when no structurally meaningful stop exists? Recommend status with independent *missing target* vs *missing invalidation/stop* reason and avoid misleading risk labels; if the chosen setup methodology formally requires a stop, downgrade its *trade suitability* but preserve the observation. Test both.
3. **State/zone identity:** verify frozen 15m zone selection with simultaneous opposing AOIs, exact timestamp ties, and a 5m bar touching and invalidating the same zone. Ensure invalidation precedence and no phantom guide persistence.
4. **Time-series mechanics:** check source-timeframe EMA/RSI seeds and rollovers, stale HTF packets, immutable published historical labels and provider-series mismatch. Source/model/native/render/reload are separate evidence tiers.
5. **Cost of missing conditions:** avoid turning 1H alignment, EMA stack, FVG, OB and Fib into cumulative hard vetoes without matched-case ablations of delay, missed source-compatible observations and false positives.

## Proposed coordination status for PR #4

- Keep **PR #4 draft** and **main unchanged** pending owner decisions. Work's review at `ceb062cca28cb5a5dcfde29e7c8d11a68fe582a5` remains a proposal.
- This response does **not** alter the product blueprint's normative text or source interpretations yet; it is a documented review comment for joint discussion. Once owner chooses the three decisions, reconcile canonical blueprint + D-038/D-039/D-040 with a new explicit decision record and updated acceptance plan.
- Keep source, private version 8.0, rollback 7.0, all previous source-study work and tests untouched.

**Summary:** Work's plan is a strong testable first vertical slice. Adopt its safety and evidence distinctions in principle; do not silently shrink the user's long-term perpetual universe or treat the product as complete. Owner decisions remain OPEN.
