# Alpha Engine TradingView

**Independent, source-grounded, research-enhanced TradingView project.**

**Phase 1 and early Phase 2 record (2026-11-09, Asia/Manila):** Full original Coach PDF PCSS study COMPLETE (35 pages / 26 units). **Phase 2 formal methodology research IN PROGRESS.** New: [26-unit source traceability](docs/methodology/00-source-to-rule-traceability.md), [20 cross-lesson reconciliations](docs/METHODOLOGY_RECONCILIATION.md), [causal BOS/CHoCH foundation](docs/methodology/01-causal-market-structure.md), [entry/RSI/EMA/risk research](docs/methodology/02-topdown-entry-state-and-risk.md), [zone-generation alternatives](docs/methodology/03-zones-sr-ob-fvg-fibonacci.md). No Pine code, market backtests or deployments.


**Current Phase 3.4 checkpoint (2026-11-12):** [Pine v0.1.2](pine/lesson08-diagnostic.pine), build `L08-0.1.2-3b9eb3065294`, remains the sole owner-saved private indicator. [Work resumption and acceptance audit](docs/audits/2026-11-12-work-resumption-phase3-4.md): **39/39** local checks and [pinned GitHub CI](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43195302296) passed. Native same-cutoff M01 OFF/ON comparisons matched for the disabled setup and for two enabled historical reconstructions with contact, retained R2 records, and EXPIRED or REASSESS. Transition-cutoff and live/reload toggle parity remain open. Five recorded pivots matched fresh Binance Spot candles. The audit identifies one M01 input-validation discrepancy for owner review. [Canonical state](docs/STATE.md).

**Phase 3.1 checkpoint (2026-11-12)** — [Lesson 08 chart diagnostic v0.1.1](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/74e7814e308a40f769d9b57607ebde145f492b8d/pine/lesson08-diagnostic.pine), build `L08-0.1.1-7fbb3eb381b6`, adds verifiable build identity and separates current state from recorded reaction history. Scope is Binance Spot PAXGUSDT standard 5m. [Implementation and acceptance record](docs/implementation/phase3-lesson08-diagnostic.md) · [Canonical state](docs/STATE.md).

**Prior Phase 2 checkpoint (2026-11-12):** [M07 validation design](docs/research/phase2-mtf-validation-and-falsification-protocol.md#i-bounded-m07-profile) selects Binance Spot PAXGUSDT for a bounded Lesson 08 1H→5m comparison. The [frozen market receipt](docs/research/phase2-m07-frozen-market-evidence.md) and acceptance plan support owner review of a future chart-only prototype. See [canonical state](docs/STATE.md) for the scope and remaining TradingView checks.

**Prior Phase 2 checkpoint (2026-11-12):** [M06 risk and execution uncertainty](docs/methodology/09-m06-risk-and-execution-uncertainty.md) covers the Coach source, as-of risk inputs, [Binance public product metadata](docs/research/phase2-m06-binance-public-metadata.md) and [25 paper cases](docs/research/phase2-m06-paper-cases.md). The [state history](docs/STATE.md) records that owner-review checkpoint.

**Prior Phase 2 checkpoint (2026-11-12):** [Frozen-prefix timing assessment](docs/research/phase2-frozen-prefix-timing-assessment.md) compares three reaction policies on [12 constructed episodes and 3 qualitative source packets](docs/research/phase2-frozen-prefix-evidence-v1.md). [STATE](docs/STATE.md) records the provisional recommendation and the M06 owner-review point.

**Prior Phase 2 checkpoint (2026-11-12):** [Cross-module causal reconciliation](docs/methodology/08-cross-module-causal-reconciliation.md) and [23 manually adjudicated paper cases](docs/research/phase2-causal-reconciliation-paper-cases.md) address E1–E10. The bounded Lesson 08 comparison uses 1H context, 5m confirmation and a pre-known S/R zone. [STATE](docs/STATE.md) records the owner-review checkpoint and remaining decisions.

**Prior Phase 2 research (2026-11-11):** [M05 multi-timeframe states and conflict logic](docs/methodology/07-mtf-context-conflicts-and-causal-states.md) and [source-to-model falsification protocol](docs/research/phase2-mtf-validation-and-falsification-protocol.md). Treat 4H structure, 1H location, 15m reaction, and entry eligibility as separate evidence, with source style branches and known-at timing. M05 adds 30 designed cases: **140 paper-case rows total, none run as code or real crypto backtests**. That checkpoint identified M03 and M06 as later dependencies. The current next-step proposal is in STATE. No Pine code or deployments.

**Earlier Phase 2 research (2026-11-11):** [R1 causal structural reference arming and pivot ambiguity](docs/methodology/04-reference-arming-and-pivot-order.md), [R2 zone contact and candle timing](docs/methodology/05-zone-contact-reaction-timing.md), [Ponder correction audit](docs/audits/2026-11-11-causal-timing-reconciliation.md). 54 additional designed cases; 110 paper fixtures total, none executed. New [M04 candle-pattern and confirmation grammar](docs/methodology/06-candle-pattern-and-confirmation-grammar.md) distinguishes body engulf, full-range engulf, wick rejection plus follow-through, strong-body candidates and source context. **Corrected:** strict fractal high cannot be confirmed if a required right-hand bar has a higher close. Next M04 candle geometry and M05 cross-TF events; still no Pine code or market backtests.

**Latest targeted pre-implementation check (2026-11-10):** [Ponder/Jarvis audit and prioritized corrections](docs/audits/2026-11-10-phase2-preimplementation-audit.md). Important refinements: illustrated source p14 OB candle and 1→3 gap, reference arming when BOS/CHoCH pivots are late-confirmed, and Lesson08 closed-candle entry vs Lesson10 break-of-confirmation entry. **No code or market backtests performed.**

## Start here — especially after losing a ChatGPT conversation

1. Read [docs/RECOVERY.md](docs/RECOVERY.md).
2. Read [docs/STATE.md](docs/STATE.md) for the latest verified checkpoint.
3. Read [docs/PROJECT_CHARTER.md](docs/PROJECT_CHARTER.md) and [docs/DECISIONS.md](docs/DECISIONS.md).
4. Read [docs/SOURCE_MANIFEST.md](docs/SOURCE_MANIFEST.md) and [docs/PCSS_PROTOCOL.md](docs/PCSS_PROTOCOL.md).
5. Check [docs/LESSON_COVERAGE.md](docs/LESSON_COVERAGE.md) before beginning or continuing any lesson.
6. Read [AGENTS.md](AGENTS.md) for operating instructions for a coding or AI assistant.
7. Read completed [Lesson 01](docs/lessons/01-trading-101.md), [Lesson 02](docs/lessons/02-basic-candlestick-patterns.md), [Lesson 03](docs/lessons/03-trading-risk-reward.md), and corresponding [candlestick](docs/research/02-candlestick-rule-candidates.md) / [risk-reward](docs/research/03-risk-reward-spec-candidates.md) research and [Lesson 04](docs/lessons/04-time-frame.md) plus its [MTF research](docs/research/04-multi-timeframe-causality.md) and [Lesson 05](docs/lessons/05-leverage-margin.md) with its [margin/solvency research](docs/research/05-margin-leverage-solvency-candidates.md) and [Lesson 06](docs/lessons/06-engulfing-pattern.md) with its [engulfing formalization research](docs/research/06-engulfing-formalization.md) and [Lesson 07](docs/lessons/07-market-structure-confluence.md) with its [market-structure research](docs/research/07-market-structure-confluence-candidates.md) and [Lesson 08](docs/lessons/08-trading-entry-workflow.md) with its [entry state-machine research](docs/research/08-entry-state-machine-candidates.md) and [Lesson 09](docs/lessons/09-support-resistance.md) with its [zone and role-flip research](docs/research/09-zone-role-reversal-candidates.md) and [Lesson 10](docs/lessons/10-marking-support-resistance.md) plus [range-entry research](docs/research/10-range-entries-and-confirmation-break.md) and [Lesson 11](docs/lessons/11-order-block-bos-choch.md) with its [OB/BOS/CHoCH research](docs/research/11-order-block-bos-choch-candidates.md) and [Lesson 12](docs/lessons/12-bos-break-of-structure.md) plus [BOS research](docs/research/12-bos-event-causality.md) and [Lesson 13](docs/lessons/13-manage-your-risk-sol.md) with its [countertrend and risk research](docs/research/13-countertrend-risk-mtf.md) and [Lesson 14](docs/lessons/14-fibonacci-retracement.md) with [Fibonacci candidate research](docs/research/14-fibonacci-candidate-specification.md) and [Lesson 15](docs/lessons/15-reliability-on-charting.md) with its [confluence and ablation research](docs/research/15-indicator-reliability-confluence-ablation.md) and [Lesson 16](docs/lessons/16-long-short-setup.md) with [continuation research](docs/research/16-long-short-continuation-state-candidates.md) and [Lesson 17](docs/lessons/17-rsi-relative-strength-index.md) with its [RSI candidate research](docs/research/17-rsi-state-momentum-candidates.md) and [Lesson 18](docs/lessons/18-ema-exponential-moving-average.md) with its [EMA slope and range research](docs/research/18-ema-slope-redundancy-range-candidates.md) and [Lesson 19](docs/lessons/19-rsi-ema-topdown-analysis.md) with its [time-causal research](docs/research/19-topdown-timecausal-confluence-research.md) and [Lesson 20](docs/lessons/20-choch-change-of-character.md) with its [CHoCH swing and break research](docs/research/20-choch-confirmed-pivots-and-break-semantics.md) and [Lesson 21](docs/lessons/21-tonusdt-topdown-setup.md) with its [case-provenance research](docs/research/21-tonusdt-topdown-case-provenance-and-risk.md) and [Q&A Activity No. 1](docs/lessons/qa-01-btc-htf-bias-and-confirmation.md) with its [BTC multi-timeframe research](docs/research/qa-01-btc-mtf-continuation-retest-and-bearish-evidence.md) and [Q&A Activity No. 2](docs/lessons/qa-02-fartcoin-scalp-pullback.md) with [FARTCOIN RSI-band/risk research](docs/research/qa-02-fartcoin-scalp-entry-risk-and-rsi-band.md) and [Q&A Activity No. 3](docs/lessons/qa-03-btc-consolidation-retest-and-breakout.md) with [conditional BTC short/long research](docs/research/qa-03-btc-conditional-retest-breakout-risk.md) and [N-01 Location and Time PCSS](docs/lessons/note-01-location-time-and-economic-calendar.md) plus [independent crypto DST/news research](docs/research/note-01-crypto-sessions-dst-and-event-risk.md) and [N-02 final BPI source study](docs/lessons/note-02-bpi-bsp-stock-charting.md) with [N-02 research](docs/research/note-02-bpi-mtf-reversal-and-crypto-transfer.md) and [full-source audit](docs/SOURCE_STUDY_COMPLETION_AUDIT.md). Resume methodology specification research without restarting completed source units.

## Mission

Study the **one and only Coach Fredy source**, the user-supplied 35-page file named **coach trading lessons.pdf**, in complete source order using the user's Personal Comprehensive Study Standard (PCSS). Build independent knowledge and improvements where the source is incomplete. Eventually design and implement a well-tested TradingView research indicator, with the possibility of a separate strategy for objective backtesting.

**The PDF is the only Coach Fredy-authored source; it is not the only permissible knowledge source.** External technical references, original reasoning, quantitative research, and independently developed enhancements are welcome, but their origins must be distinguished from Coach Fredy's words.

**Project independence is mandatory:** do not read from, modify, merge, migrate, deploy, or otherwise operate on any earlier related projects as a shortcut. Treat this repository as a fresh start.

## Authorized market focus

**Crypto markets exclusively for the eventual TradingView implementation**, including **XAUUSDT**, **XAUTUSDT**, and **PAXGUSDT**. The gold-reference derivative and tokenized-gold pairs are distinct product types and require separate feed/product verification. Original PCSS lessons remain complete, including Coach's Forex and Philippine stock discussions, but those are *not* separate implementation target markets. See [market scope](docs/MARKET_SCOPE.md) (owner decision D-013).

## Architectural direction

- **Indicator first; strategy-ready design.** This is the current accepted, revisitable direction, not permission to begin coding.
- Document an original Coach-method baseline separately from interpretations and enhancements.
- Source-first PCSS learning, gap analysis, rigorous rules, continuous Ponder-style scrutiny, then tested implementation.
- Preserve caution/WAIT/NO TRADE states; no promise of profitability.
- Make GitHub the canonical record, updating it after meaningful, independently verifiable increments.

## Documents

| Document | Purpose |
| --- | --- |
| [Project charter](docs/PROJECT_CHARTER.md) | Goal, boundaries, principles, success criteria |
| [Authorized market scope](docs/MARKET_SCOPE.md) | Crypto focus, XAUUSDT/XAUTUSDT/PAXGUSDT differences and unresolved feed choices |
| [Source manifest](docs/SOURCE_MANIFEST.md) | Exact document identities, source hierarchy, public-repo precautions |
| [PCSS protocol](docs/PCSS_PROTOCOL.md) | Teaching, inventory, audit, checkpoint, and interpretation procedure |
| [Decisions](docs/DECISIONS.md) | Dated owner decisions and reconsideration triggers |
| [Research and validation](docs/RESEARCH_AND_VALIDATION.md) | Provenance, gaps, experimental rigor, engineering requirements |
| [Lesson coverage](docs/LESSON_COVERAGE.md) | 35-page source roadmap and completion ledger |
| [Roadmap](docs/ROADMAP.md) | Phases, gates, deliverables |
| [State](docs/STATE.md) | Truthful current checkpoint, open questions, next authorized action |
| [Recovery](docs/RECOVERY.md) | Copyable instructions to resume in a fresh ChatGPT conversation |

## Source distribution caution

This repository is **public**. The owner authorized uploading the original Coach PDF, and its exact binary is now **committed and Git-blob verified** at [sources/coach trading lessons.pdf](sources/coach%20trading%20lessons.pdf) (owner upload commit [02816ae](https://github.com/jebobomagcode/alpha-engine-tradingview/commit/02816ae53b6f2bea7a0b8427c12ff8324a24be98)). Its source identity and integrity checks are documented in [docs/SOURCE_MANIFEST.md](docs/SOURCE_MANIFEST.md). The full personal PCSS file remains uncommitted; attach it in future chats as needed.

**No trading advice or guaranteed return:** this is an analytical research and software engineering effort. Backtests, when eventually produced, are simulations with substantial limitations.
