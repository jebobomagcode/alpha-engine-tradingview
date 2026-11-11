# Phased roadmap — proposals, not completed work

| Phase | Target | Gate to advance |
| --- | --- | --- |
| 0. Governance and recovery | Define charter, source identities, decisions, workflow, repository checkpoint | Repo readback verifies docs; no formal study or code yet |
| 1. Complete PCSS source study | Detailed sequential coverage of all 21 lessons, 3 Q&As, and final notes, with figures/exercises and checkpoints | Verified source-coverage ledger, meaningful unresolved issues recorded |
| 2. Formal methodology | Explicit rules, mathematical definitions, baseline Coach interpretation, state transitions, timeframe policy | Source-to-spec traceability, competing interpretation review |
| 3. Enhanced research design | External evidence and testable improvements separated from the Coach baseline | Hypotheses and acceptance criteria established before performance optimization |
| 4. TradingView indicator | Pine script visualization, market state, confluence/WAIT diagnostics, optional alerts | Verified compilation, chart behavior, source fidelity, nonrepainting/MTF audit |
| 5. TradingView strategy | Separate strategy using the same well-specified rule concepts for orders and backtests | Technical execution and cost assumptions validated; out-of-sample tests |
| 6. Evaluation and iteration | Compare baseline and enhancements over market regimes and test cases | Evidence-bounded findings and clearly stated limitations |

The order is **conceptual**; detailed design questions may be explored while studying. **Phase 1 PCSS source study is COMPLETE across all 35 pages/26 units, documented in [source completion audit](SOURCE_STUDY_COMPLETION_AUDIT.md).** **Phase 2 research is IN PROGRESS:** 26-unit traceability, reconciliation, causal structure, entry/risk and zone alternatives, plus [R1 reference arming](methodology/04-reference-arming-and-pivot-order.md), [R2 zone-to-reaction timing](methodology/05-zone-contact-reaction-timing.md) and [November11 audit](audits/2026-11-11-causal-timing-reconciliation.md). M04 candle geometry has [R3](methodology/06-candle-pattern-and-confirmation-grammar.md) and M05 multi-timeframe conflict behavior has [R4](methodology/07-mtf-context-conflicts-and-causal-states.md), with [M07 validation protocol draft](research/phase2-mtf-validation-and-falsification-protocol.md). Parameters, profile selection, validation and execution remain OPEN. No coding authorization inferred. **Pine code, market backtests, deployment and trades are not authorized merely by the study request.** The project-specific implementation focus is **crypto including XAUUSDT, XAUTUSDT and PAXGUSDT** (see [MARKET_SCOPE.md](MARKET_SCOPE.md)); source study still covers Coach's Forex and Philippine stock sections without expanding the implementation scope.

## Recommended incremental delivery
- Each lesson: PCSS teaching + source inventory + interpretive uncertainties + checkpoint commit.
- Each rule specification: isolated artifact + source anchors + tests of definition and failure cases.
- Each implementation increment: Pine compile/behavior evidence where actually available; no invented acceptance reports.
- Regular state updates: docs/STATE.md, LESSON_COVERAGE.md, DECISIONS.md as needed.
- If interrupted: recover exact git HEAD and last status; do not restart completed or tested work.

## Major future decision points
- Should the indicator show a compact context dashboard, chart annotations, or both?
- Which interpretations of ambiguous patterns best preserve Coach intent and remain causal?
- Which enhancements provide measurable incremental value without overfitting?
- Should a shared Pine library be used? Only if practical constraints support it.
- Which exact crypto venues, market-product variants, sessions, bar granularities and risk models are suitable? Gold derivative XAUUSDT and tokenized gold XAUTUSDT/PAXGUSDT must be evaluated separately.
- When does it become worthwhile to build the strategy adapter?
