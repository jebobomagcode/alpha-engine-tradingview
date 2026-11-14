# Alpha Engine TradingView v1.1 — How everything is intended to work

> **PROVISIONAL PRODUCT BLUEPRINT — 2026-11-14 (Asia/Manila). NOT FINALIZED, NOT AN IMPLEMENTATION CLAIM.** This document is the consolidated, user-facing end-to-end product description requested by the owner. It must undergo Work's independent design critique under **D-040** before final product requirements are frozen. The owner explicitly selected **D-038 Binance USDⓈ-M stablecoin-settled perpetuals only**, **LONG and SHORT**, and **D-039 4H / 1H / 15m / 5m** analysis. Most decision thresholds, interaction details and timeframe roles below are **engineering proposals**, not separate owner approvals or rules claimed verbatim from Coach Fredy.

Related source-of-truth: [Decision register](../DECISIONS.md), [current state](../STATE.md), [Work product-review brief](../implementation/v1-1-work-provisional-design-review-brief.md), [Binance contract qualification](../implementation/v1-1-binance-usds-m-perpetual-qualification.md), [four-timeframe timing contract](../implementation/v1-1-four-timeframe-mtf-contract.md), [Work parity reconciliation](../implementation/v1-1-work-parity-reconciliation.md), [accepted private v1 ledger](../implementation/phase3-8-v1-stabilization.md#integrated-private-v1-release--2026-11-13-pht).

## 1. Purpose and boundary of the product

The desired product is a **private TradingView research indicator** that runs on the user's selected, verified Binance USDⓈ-M USD-stablecoin perpetual chart. Its job is to interpret qualified price evidence, display the structure and locations that matter, investigate **both LONG and SHORT** candidate setups and explain clearly **why an observation qualifies, why it is only a watch item, why it becomes invalid, or why evidence is insufficient**.

**It is not a trading bot, guaranteed strategy, autonomous Binance executor, calibrated prediction engine, account-risk manager, or all-markets background scanner.** A script attached to one chart does not inherently monitor every contract. Expected profitability, win rate, execution fills, funding, fees and liquidation are **not proven** merely because the software compiles or generates reasonable chart drawings.

The methodology has two explicitly separate origins: **Coach Fredy's actual PDF → completed PCSS interpretations**, and **independently designed/tested AI research hypotheses** for things the PDF does not quantify. Do not silently attribute strict pivot windows, numeric EMA settings, candlestick formula conventions or novel scoring rules to the Coach.

## 2. Market eligibility — what can enter the engine?

**Only Binance USDⓈ-M linear perpetual contracts** denominated/quoted/settled in USD-pegged stablecoins, **initially USDT and USDC**, plus other actual USD-stablecoin contracts **only after their Binance product identity and mechanics are positively verified**. Examples of candidate families: BTCUSDT perpetual, ETHUSDT perpetual and eligible USDC perpetuals; a Binance gold-referencing USDⓈ-M perpetual may be eligible **by contract family** if independently qualified. Examples are **not a statement that each exact TradingView symbol is natively verified in the currently accepted v1**.

**Excluded:** Binance Spot (including PAXGUSDT Spot and tokenized-gold Spot), Binance COIN-M inverse/coin-settled perpetuals, dated/quarterly/delivery futures, options, non-Binance venues, and standalone forex/equity feeds.

**Proposed qualification sequence:**
1. Identify the exact TradingView feed and contract, not just a ticker name or suffix.
2. Match verified Binance USDⓈ-M contract metadata where available: perpetual type, exchange, quote, margin/settlement assets, current trading status and price/quantity precision. Pine may **not** expose all Binance metadata or permit arbitrary REST calls; a conservative supported-contract manifest or similar design requires Work's review.
3. Require standard trade-price OHLC candles of the same product and an eligible 5m host chart for the first implementation; do not substitute Spot, mark-price, index-price, COIN-M or other symbols.
4. Check positive, symbol-relative tick size; history completeness, warmup and 15m/1H/4H evidence readiness. Reject/withhold unsupported or unidentified cases with an honest status, not fictional numbers.
5. Track each eligibility/qualification outcome separately from runtime analysis and separately from tested/accepted native coverage.

**Design objective:** avoid a permanent arbitrary five-ticker whitelist *if technical safety can be maintained*. Dynamic compatibility is not the same as claiming every future Binance perpetual is automatically verified.

## 3. The user's normal workflow inside TradingView

**Step 1 — Open TradingView.** Choose a qualifying Binance USDⓈ-M perpetual chart. The *initial host-chart recommendation* is **standard 5-minute candles**; all four analysis timeframes should still be included via same-product time series.

**Step 2 — Attach the private Alpha Engine indicator.** It reads the active ticker, timeframe, chart type and price evidence. The indicator should show a clear qualification failure if the product or timeframe cannot be trusted; it should never silently analyze a wrong instrument.

**Step 3 — Interpret four timeframe layers** as described below. A context row or tooltip should show not just a direction but when its source data last closed and whether enough evidence exists. There is no mandatory all-four-bullish/all-four-bearish assumption.

**Step 4 — Inspect price locations and chart drawings.** Confirmed swing labels and structural events, current relevant support/resistance, candidate demand/supply, FVG/OB, Fibonacci levels and moving-average context appear only when the source event is actually confirmed and has not expired. UI clutter should be bounded.

**Step 5 — Read the workflow decision.** The engine tracks proposed candidate lifecycle states such as WATCH → CONTACT → REACTION OBSERVED → SETUP QUALIFIED, or WAIT / INSUFFICIENT / REASSESS / INVALIDATED / EXPIRED. These precise labels/transition tests remain **proposed**, not implemented complete state definitions.

**Step 6 — Consider conditional price geometry.** If qualified directional conditions and valid levels exist, the indicator can show nominal Entry (E), Stop (SL), Target (TP) and reward:risk (R). These are research reference prices, **not orders** and not a recommendation guaranteeing execution.

**Step 7 — On new closed evidence, reassess.** Replacements and invalidations must be visible. A past chart cannot retroactively act as though a swing, FVG or candle reaction was known before its confirming close.

GitHub and Python are **development and acceptance tools**. The user should not need to run Python or GitHub commands for routine chart reading.

## 4. Four-timeframe analysis — exact layers, proposed roles

| Timeframe | Recommended primary role | Evidence expected | State limitation |
| --- | --- | --- | --- |
| **4H** | Macro directional/structural regime | Confirmed trend, regime, important reference locations, timestamp | Forming 4H data must not become confirmed evidence |
| **1H** | Intermediate structure and context | Confirmed HH/HL/LH/LL, possible BOS/CHoCH, 1H context/levels, timestamp | Agreement with 4H is informative, not automatic permission |
| **15m** | Setup development and AOI | Candidate supply/demand, OB, FVG, fib/location, transitions, timestamp | A 15m area of interest is not a 5m trigger |
| **5m** | Local timing/confirmation | Prior-known reference, contact, confirmed directional reaction, invalidation and possible nominal geometry | Price touching a zone does not equal a trade signal |

A 5m decision at **10:05 UTC** cannot use unfinished **10:00–10:15** 15m information. Use the last eligible **confirmed** 15m close (10:00 UTC under the proposed alignment), independently confirmed 1H/4H values, and a completed 5m close. At a higher-timeframe boundary, test the exact known-at order; never infer that all four timeframes update at the same instant with the same evidence.

**Conflicts:** e.g., 4H bullish, 1H bearish, 15m mixed and 5m bullish must yield a truthful conflict/WAIT/INSUFFICIENT characterization according to explicit rules. **No majority-of-four LONG/SHORT voting and no synthetic probability.** A 5m chart can show four analytical layers; supporting a **15m host chart with all 5m events** is a separate potentially difficult lower-timeframe engineering requirement and is **not claimed yet**.

## 5. What modules perform internally?

**A — Product/data gate:** exact Binance perpetual identity, source type, standard candles, timeframe, positive tick and history/warmup; else explain insufficiency.

**B — Structure:** strict, confirmed swing pivots; HH/HL/LH/LL roles; eligible structural references and their creation/arming/consumption/replacement/retirement; continuation BOS vs possible CHoCH. Pivot *origin* and *known-at* must be distinct.

**C — Locations:** candidate support/resistance, supply/demand, order blocks, three-bar FVGs, retracement/Fibonacci locations. Zones may be OPEN, TESTED, INVALID, REPLACED or otherwise terminated only under defined, testable transitions. Existing v1 has bounded latest FVG/OB logic, not comprehensive zone history.

**D — Momentum and HTF context:** independently confirmed 4H/1H/15m evidence, selected EMA/RSI context if justified; distinguish structural direction from indicator momentum, and missing data from contradiction. Numeric EMA/RSI settings in v1 are AI research conventions, not universally established Coach requirements.

**E — LONG/SHORT setup engines:** independent, testable bullish demand/support and bearish supply/resistance workflows, including touch, reaction, invalidation, prior-armed reference gating, ambiguity and stale-state expiration. A direction label is not itself a setup. Explicit context conflicts must be explained rather than papered over.

**F — Geometry and output:** show E/SL/TP/R only if ordering and eligibility pass, plus supporting source cutoff, status/reason and optional chart guides. The model must not imply position size, realistic fill or actual P&L.

These are product-level modules; code interfaces, exact rule thresholds and final presentation require review.

## 6. Long and short — example journeys

### Hypothetical LONG

4H and 1H show a context that supports evaluating an upward setup; 15m has a qualified demand/support AOI; 5m approaches the zone. On first touch: **CONTACT**, not necessarily LONG. If a pre-armed reference and accepted closed-candle bullish reaction are present, and no invalidation exists, the engine may classify a **LONG setup candidate**, with nominal entry price, a protective stop **below entry**, and target **above entry**. If close invalidates the demand region, the setup must be retired/reassessed.

**Nominal long R** = (Target − Entry)/(Entry − Stop), only if Stop < Entry < Target.

### Hypothetical SHORT

4H/1H context supports evaluating a downward setup; 15m identifies a qualified supply/resistance AOI; 5m tests that region. A bearish closed-candle reaction may become a **SHORT setup candidate**, only if its independent structural/reference/context gates pass. A protective stop is **above entry**, target **below entry**, and invalidation on a wrong-side confirmed break must be tracked. SHORT is a new product requirement; merely reversing a green arrow from v1 would be insufficient.

**Nominal short R** = (Entry − Target)/(Stop − Entry), only if Target < Entry < Stop.

### Conflicting or missing evidence

If 4H and 1H disagree, if 15m has no confirmed zone, if 5m history has a gap, or if product identity is uncertain, the result should explain **WAIT / CONFLICT / INSUFFICIENT / REASSESS** rather than filling a trade direction by fiat. A valid *observation* and a qualified *setup* are distinct. No setup need exist on many bars.

All journeys are **illustrations**, not actual Binance signals or performance evidence.

## 7. Setup-state meanings (provisional taxonomy)

| State | Intended meaning | Misinterpretation to avoid |
| --- | --- | --- |
| **WATCH** | Relevant structural or location hypothesis exists | Not an entry |
| **CONTACT** | Completed price evidence intersects the AOI | Not a confirmed reaction |
| **REACTION OBSERVED** | Defined bearish/bullish response confirmed | Not automatically qualified for execution |
| **SETUP QUALIFIED** | All selected formal gates and valid price geometry pass | Not a promise of profit or fill |
| **WAIT** | Conditions incomplete, but observed feed may be otherwise valid | Not a fabricated trade |
| **INSUFFICIENT** | Required source, context, warmup, contract or validation unavailable | Not a directional conclusion |
| **REASSESS / INVALIDATED / EXPIRED** | Earlier reference/setup changed or ceased being eligible | Not a persistent live instruction |

The exact naming, precedence, temporal persistence and whether a single bar can move through multiple states require formal Work review. Historical labels and current actionable displays must be distinct.

## 8. What the user should see — chart plus dashboard

**Chart overlay:** swing roles and relevant BOS/possible CHoCH labels; bounded live important references; optional FVG/OB bands; optional Fib 50/61.8/70.5 and EMA context; contact/reaction markers; E/SL/TP guides **only** with valid geometry. Old labels and invalidated guides should not clutter or masquerade as current signals.

**Dashboard:** compact, readable and source-aware. Proposed fields:
- Exact product/venue/feed, price source, chart timeframe, last confirmed 5m cutoff, build/version and eligibility.
- **4H** regime/structure + latest confirmed source time + readiness.
- **1H** intermediate structure + latest confirmed source time + readiness.
- **15m** current candidate location/zone and lifecycle + latest confirmed source time + readiness.
- **5m** local structural/reaction status + exact decision time.
- Overall state (WATCH, WAIT, CONTACT, OBSERVED, QUALIFIED, REASSESS, INVALIDATED, INSUFFICIENT), **direction if qualified**, and a human-readable *reason*.
- Conditional nominal E/SL/TP/R; provenance or tooltip for known-at source, zone/reference ID and invalidation.

The interface must show what is **known**, not make a probability claim. Dense research detail can reside in a tooltip or optional expanded view; avoid obstructing price candles.

### Illustrative dashboard state (NOT LIVE DATA)

Product: verified BINANCE USDⓈ-M BTCUSDT perpetual | chart: standard 5m | price: trade candles  
4H: down (confirmed) | 1H: down (confirmed)  
15m: candidate supply AOI (qualified) | 5m: reaction not confirmed  
**Overall: WAIT — potential SHORT location, no qualified 5m bearish reaction.**  
Nominal E / SL / TP: — / — / —.

## 9. Data and causality contract

The intended research contract binds, for each product and timeframe: **exact feed ID, trade vs mark/index source, candle open and close, cutoff, known-at time, origin, armed/replaced/retired time, validated tick arithmetic, warmup, gap/adjacency status, evidence version and source hash when testable**.

Use completed 5m values and strictly previous-closed HTF values from 15m/1H/4H according to tested TradingView history-offset/request semantics. Validate rollover boundaries, missing bars and discrepancies. A historical pivot appearing at its origin on a chart does **not** mean it was known then. Nonstandard chart types or data gaps must trigger truthful qualification failures.

Python research replay is a **partial independent comparator**. The existing integrated replay has structural/zone/bullish-reaction state with an externally supplied 1H/4H bullish-context flag but **no full 15m ledger, Fib projection or nominal geometry**. The accepted v1 Pine runtime has 5m host + qualified prior 1H/4H context, but no complete four-layer or bidirectional implementation. Model-vs-model, model-vs-native and visual same-cutoff reload findings must be reported separately.

## 10. Futures-specific interpretation and risk limits

Perpetuals can be **long or short**, but that does not mean the indicator should place Binance orders. The entry/stop/target price distances and ratio **R** do not encode actual fill probability, fee rate, funding, position quantity, leverage, maintenance margin, liquidation price, slippage, borrow restrictions or actual P&L. Invalid geometry must be withheld. No guaranteed returns, live profit claims or automatically optimized confidence score.

Order execution, position sizing and account-risk calibration would require separately defined specifications, Binance contracts/API/account permissions and controlled acceptance. That is **not** within this indicator-first release. Even a complete LONG/SHORT indicator cannot claim a profitable method without external out-of-sample/backtest/forward evidence.

## 11. Notifications, ChatGPT and market-wide monitoring — separate future possibilities

The accepted v1 Pine source is an **indicator**, not a TradingView `strategy()` executable and not an alert engine; it has **no `alert()` or `alertcondition()` calls** at the verified build. The user's prior TradingView Basic-plan test rejected technical alert creation; account eligibility should be rechecked rather than assumed to have changed.

Possible later stages:
- Named setup/transition alert conditions in Pine and real TradingView account entitlement validation.
- A secure webhook/event data pipeline, if desired and supported, with delivery provenance, replay protection and failure monitoring.
- An optional ChatGPT analysis companion operating on supplied charts or structured evidence; **not** a claim that TradingView can push notifications straight into the existing normal ChatGPT thread.
- A separately architected multi-symbol scanner if monitoring *all* Binance contracts becomes a requirement. **One indicator on one chart ≠ automatic full-market scanning.**
- A formal backtest/strategy module only after objective rules and stronger causal parity are qualified; software acceptance is not a trading edge.

These features are **not** part of the already delivered private v1 and have not been approved as v1.1 core acceptance gates.

## 12. What is built today versus what is proposed?

| Area | Accepted private v1 version 8.0 | Desired v1.1 (provisional) |
| --- | --- | --- |
| Scope | Five exact Binance 5m identities, mostly Spot plus XAUUSDT.P | Binance USDⓈ-M stablecoin-settled **perpetuals only**; verified capability-based qualification |
| Direction | Experimental bullish support/reaction and nominal geometry; bearish structure context observed | **Both LONG and SHORT** qualified research |
| Timeframes | Standard 5m chart + prior confirmed 1H/4H context | **4H / 1H / 15m / 5m** layered analysis |
| Structure, zones, Fib and drawings | Bounded implemented visual research and references | Extended, coherent bidirectional and four-layer interpretation |
| Data parity | Partially modeled/tested; true full Pine/Python parity unresolved | Full frozen per-cutoff/known-at/invalidation audit with qualified perpetual data |
| Positive native saved-reload cases | Positive Fib/armed/contact/reaction/geometry **INSUFFICIENT** at sampled cutoffs | Targeted native evidence, absent-case validation and truthful statuses |
| Account execution | No | No |
| Automatic all-market scanner | No | No initially |
| Economic performance validation | No demonstrated edge | Not established by engineering release |

The accepted v1 release remains private TradingView named version **8.0**, build **AE-0.1.11-0f4b3df98b90**, source blob **6fe1f8718ba8b742be500262a1df84fbd933c871**; saved **version 7.0** remains rollback. GitHub main verified at handoff as **8e60a982385e46aa818acb49103f1dedbe856b77**. Integrated main standard CI **148/148** and separate local structural tests **21/21** passed for the then-tested scope; not evidence of proposed v1.1 functioning.

## 13. Engineering and release sequence for Work to evaluate

**E0 — Preserve v1 and review the specification.** Do not restart completed 35-page Coach source study, v1 overlays, accepted SHA-pinned fixture ancestry, postmerge acceptance or private release.

**E1 — Identity/adapter vertical slice.** Verify exact Binance USDⓈ-M perpetual product and chart, USDT/USDC data with different tick sizes, and rejection of Spot, COIN-M, dated futures, mismatched source, unsupported quote and nonstandard chart.

**E2 — Four-timeframe causal evidence.** Same-product 4H/1H/15m/5m, per-layer confirmed close/known-at, warmup and gap checks, boundary and prefix-invariance tests, MTF conflict behavior.

**E3 — Bidirectional setups and geometry.** Implement and independently test both LONG and SHORT structural references, location, contact, reactions, invalidation and nominal E/SL/TP/R. Verify meaningful WITHHOLD as well as positive examples.

**E4 — Frozen parity + native/persistence audit.** Reuse frozen Spot receipts *only as historical regression*, derive new validated perpetual windows for v1.1; test Fib/references/zones/geometry and same-cutoff reload when a positive state is available. If unavailable, say INSUFFICIENT; don't block independent frozen work.

**E5 — Private successor release gates.** Retain v1 148-standard + 21-separate structural regression baseline, add new cases, verify native Pine compile, exact source, product-negative cases, 4TF operation, LONG/SHORT states, dashboard usability, layout persistence, private save/readback and preserved v7/v8 rollback. No public publication, live order automation or overclaiming.

**Ordering, product identity implementation, exact rules, alert priority and the semantics of QUALIFIED are open for Work's review; D-040 explicitly asks for comparative alternatives rather than automatic acceptance of this sequence.**

## 14. What Work should evaluate before the owner freezes the specification

1. Are these exact market and four-timeframe requirements feasible in native TradingView Pine, especially contract-type verification and safe 5m/15m boundary behavior? Where must an external verified manifest substitute for missing metadata?
2. Is fixed 5m host with four layers the right first release or would a configurable host/LTF strategy be better? Which falsifiable test separates them?
3. Which Coach claims are truly source-supported and which are independent AI hypotheses requiring ablation? What do the current strict swing, OB, Fib and reaction rules miss?
4. What conditions truly qualify LONG vs SHORT? How do we prevent direction conflict, stale references and symmetric-looking but unequal error cases?
5. How should WAIT / CONTACT / OBSERVED / QUALIFIED / REASSESS / INVALIDATED / INSUFFICIENT be represented for end users, without falsely implying executable trades?
6. Which native/replay/persistence gaps most threaten correctness? Which are data-limited but not release-critical?
7. What are the minimum safe accepted v1.1 capabilities, optional later features, hard-failure gates and owner decisions still needed?

**Work requested output:** requirement-vs-proposal matrix, feasibility table, three high-risk assumptions with falsification tests, at least two architecture options and tradeoffs, concrete LONG/SHORT/conflict/no-data journeys, scoped milestones and a short list of real owner choices. This design is **provisional**, and no new implementation, PR merge or TradingView version promotion is authorized by this blueprint alone.
