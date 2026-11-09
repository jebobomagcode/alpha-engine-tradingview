# Alpha Engine TradingView

**Independent, source-grounded, research-enhanced TradingView project.**

**Status (2026-11-09, Asia/Manila):** Governance and recovery documentation established. **The PCSS lesson walkthrough, rule formalization, Pine Script implementation, backtests, and deployments have not started.** No indicator or strategy has yet been implemented.

## Start here — especially after losing a ChatGPT conversation

1. Read [docs/RECOVERY.md](docs/RECOVERY.md).
2. Read [docs/STATE.md](docs/STATE.md) for the latest verified checkpoint.
3. Read [docs/PROJECT_CHARTER.md](docs/PROJECT_CHARTER.md) and [docs/DECISIONS.md](docs/DECISIONS.md).
4. Read [docs/SOURCE_MANIFEST.md](docs/SOURCE_MANIFEST.md) and [docs/PCSS_PROTOCOL.md](docs/PCSS_PROTOCOL.md).
5. Check [docs/LESSON_COVERAGE.md](docs/LESSON_COVERAGE.md) before beginning or continuing any lesson.
6. Read [AGENTS.md](AGENTS.md) for operating instructions for a coding or AI assistant.

## Mission

Study the **one and only Coach Fredy source**, the user-supplied 35-page file named **coach trading lessons.pdf**, in complete source order using the user's Personal Comprehensive Study Standard (PCSS). Build independent knowledge and improvements where the source is incomplete. Eventually design and implement a well-tested TradingView research indicator, with the possibility of a separate strategy for objective backtesting.

**The PDF is the only Coach Fredy-authored source; it is not the only permissible knowledge source.** External technical references, original reasoning, quantitative research, and independently developed enhancements are welcome, but their origins must be distinguished from Coach Fredy's words.

**Project independence is mandatory:** do not read from, modify, merge, migrate, deploy, or otherwise operate on any earlier related projects as a shortcut. Treat this repository as a fresh start.

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
| [Source manifest](docs/SOURCE_MANIFEST.md) | Exact document identities, source hierarchy, public-repo precautions |
| [PCSS protocol](docs/PCSS_PROTOCOL.md) | Teaching, inventory, audit, checkpoint, and interpretation procedure |
| [Decisions](docs/DECISIONS.md) | Dated owner decisions and reconsideration triggers |
| [Research and validation](docs/RESEARCH_AND_VALIDATION.md) | Provenance, gaps, experimental rigor, engineering requirements |
| [Lesson coverage](docs/LESSON_COVERAGE.md) | 35-page source roadmap and completion ledger |
| [Roadmap](docs/ROADMAP.md) | Phases, gates, deliverables |
| [State](docs/STATE.md) | Truthful current checkpoint, open questions, next authorized action |
| [Recovery](docs/RECOVERY.md) | Copyable instructions to resume in a fresh ChatGPT conversation |

## Source distribution caution

This is a **public repository**. On 2026-11-09, the owner explicitly authorized the public upload of the original Coach PDF. **The binary file is not yet uploaded**: the initiating chat verified its bytes, but the available GitHub connector cannot transfer local binary attachments directly. The exact expected path is `sources/coach trading lessons.pdf`; the upload and byte-identity verification are tracked in [sources/README.md](sources/README.md). The personal PCSS file remains uncommitted; attach it in future chats as needed. Do not claim the Coach PDF is hosted until its Git blob matches the manifest.

**No trading advice or guaranteed return:** this is an analytical research and software engineering effort. Backtests, when eventually produced, are simulations with substantial limitations.
