# Alpha Engine TradingView

**Independent, source-grounded, research-enhanced TradingView project.**

**Status (2026-11-09, Asia/Manila):** PCSS study authorized and **Lessons 01–16 (PDF pages 1–21) completed and source-audited**. Lesson 17 is next. **No formal Pine methodology implementation, backtests or deployments have started.**

## Start here — especially after losing a ChatGPT conversation

1. Read [docs/RECOVERY.md](docs/RECOVERY.md).
2. Read [docs/STATE.md](docs/STATE.md) for the latest verified checkpoint.
3. Read [docs/PROJECT_CHARTER.md](docs/PROJECT_CHARTER.md) and [docs/DECISIONS.md](docs/DECISIONS.md).
4. Read [docs/SOURCE_MANIFEST.md](docs/SOURCE_MANIFEST.md) and [docs/PCSS_PROTOCOL.md](docs/PCSS_PROTOCOL.md).
5. Check [docs/LESSON_COVERAGE.md](docs/LESSON_COVERAGE.md) before beginning or continuing any lesson.
6. Read [AGENTS.md](AGENTS.md) for operating instructions for a coding or AI assistant.
7. Read completed [Lesson 01](docs/lessons/01-trading-101.md), [Lesson 02](docs/lessons/02-basic-candlestick-patterns.md), [Lesson 03](docs/lessons/03-trading-risk-reward.md), and corresponding [candlestick](docs/research/02-candlestick-rule-candidates.md) / [risk-reward](docs/research/03-risk-reward-spec-candidates.md) research and [Lesson 04](docs/lessons/04-time-frame.md) plus its [MTF research](docs/research/04-multi-timeframe-causality.md) and [Lesson 05](docs/lessons/05-leverage-margin.md) with its [margin/solvency research](docs/research/05-margin-leverage-solvency-candidates.md) and [Lesson 06](docs/lessons/06-engulfing-pattern.md) with its [engulfing formalization research](docs/research/06-engulfing-formalization.md) and [Lesson 07](docs/lessons/07-market-structure-confluence.md) with its [market-structure research](docs/research/07-market-structure-confluence-candidates.md) and [Lesson 08](docs/lessons/08-trading-entry-workflow.md) with its [entry state-machine research](docs/research/08-entry-state-machine-candidates.md) and [Lesson 09](docs/lessons/09-support-resistance.md) with its [zone and role-flip research](docs/research/09-zone-role-reversal-candidates.md) and [Lesson 10](docs/lessons/10-marking-support-resistance.md) plus [range-entry research](docs/research/10-range-entries-and-confirmation-break.md) and [Lesson 11](docs/lessons/11-order-block-bos-choch.md) with its [OB/BOS/CHoCH research](docs/research/11-order-block-bos-choch-candidates.md) and [Lesson 12](docs/lessons/12-bos-break-of-structure.md) plus [BOS research](docs/research/12-bos-event-causality.md) and [Lesson 13](docs/lessons/13-manage-your-risk-sol.md) with its [countertrend and risk research](docs/research/13-countertrend-risk-mtf.md) and [Lesson 14](docs/lessons/14-fibonacci-retracement.md) with [Fibonacci candidate research](docs/research/14-fibonacci-candidate-specification.md) and [Lesson 15](docs/lessons/15-reliability-on-charting.md) with its [confluence and ablation research](docs/research/15-indicator-reliability-confluence-ablation.md) and [Lesson 16](docs/lessons/16-long-short-setup.md) with [continuation research](docs/research/16-long-short-continuation-state-candidates.md) before resuming at Lesson 17.

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
