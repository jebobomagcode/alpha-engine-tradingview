# Agent operating instructions — Alpha Engine TradingView

Applies to any ChatGPT, coding agent, or collaborator working in this repository.

## Mandatory recovery order
1. Inspect the actual current default-branch HEAD and working tree; never assume a remembered SHA.
2. Read README.md, docs/RECOVERY.md, docs/STATE.md, docs/DECISIONS.md, docs/SOURCE_MANIFEST.md, docs/PCSS_PROTOCOL.md, and docs/LESSON_COVERAGE.md.
3. Confirm source availability and SHA-256 checksums before making source-specific fidelity claims.
4. Resume from the earliest incomplete, verified checkpoint. Never manufacture study progress, implementation, tests, GitHub writes, or user decisions.

## Hard boundaries
- Repository allowed for writes: **jebobomagcode/alpha-engine-tradingview ONLY**.
- This is a completely fresh and independent project. Do **not** modify, integrate, port, pull code or decisions from, or deploy unrelated/legacy projects. Similar names are not a license to cross boundaries.
- The **sole Coach Fredy-origin authority** is the user-supplied 35-page coach trading lessons.pdf. Never claim to have later Coach sources or private guidance.
- **Owner market scope (D-013): crypto only for future TradingView implementation, including XAUUSDT, XAUTUSDT, PAXGUSDT.** These are not interchangeable feeds/products. Read `docs/MARKET_SCOPE.md` before suggesting a symbol, data model or test. Cover all Coach lessons in original order, including Forex and PH stocks, without making these separate implementation targets.
- The user's complete PCSS document defines the teaching standard; docs/PCSS_PROTOCOL.md is the resumable operational summary.
- External books, market research, Pine docs, reasoning, and experimentation are allowed as *independent* additions, explicitly labeled. Do not silently promote supplements to Coach claims.
- Respect current scope: **All 35 source PDF pages are now studied and documented (2026-11-09). Conceptual methodological research and documentation are authorized; Pine coding, deployment, trading and backtesting are NOT authorized by the study direction alone.** See docs/SOURCE_STUDY_COMPLETION_AUDIT.md and docs/STATE.md; preserve finished lessons and only write to this repository.
- Phase 3 D-021 authorizes the single Lesson 08 chart-only diagnostic and bounded private chart acceptance. See [current state](docs/STATE.md) and the [implementation record](docs/implementation/phase3-lesson08-diagnostic.md) for the exact scope.
- This is a PUBLIC repository. The owner authorized publishing the **original Coach PDF** on 2026-11-09, and the original binary is now present at `sources/coach trading lessons.pdf`: verified Git blob SHA-1 `c99de01b9178e16e240f83f5c4594fa5683a1ba2`, matching local original, first uploaded in commit `02816ae53b6f2bea7a0b8427c12ff8324a24be98`. Use this exact repository copy when available; verify identity if a later revision appears. This narrowly scoped authorization does **not** extend to the personal PCSS source, private conversations, sensitive data, credentials, access tokens, or other third-party documents.

## Provenance labels
For every rule/design finding use at least one clear label:
- COACH_EXPLICIT: supported directly by original PDF (identify page and passage/figure).
- INTERPRETATION: inferred operationalization where original wording is incomplete.
- INDEPENDENT_EXTENSION: externally researched or new rule/method, not attributed to Coach.
- EXPERIMENTAL: hypothesized or prototype idea without adequate validation.
- VALIDATED: specific reproducible checks passed; state what they establish, not more.
- OPEN_UNRESOLVED: uncertainty remains; avoid presenting precision that the evidence does not support.

Retain the original baseline while exploring extensions; avoid conflating tested software behavior with verified financial performance.

## Continuous workflow when authorized
For each manageable lesson or independently testable increment:
1. Inspect and inventory every relevant source item, including figures and examples.
2. Teach meticulously in PCSS sequence; preserve original wording/intent and separate commentary.
3. Identify ambiguities and defects; challenge assumptions with Ponder-style reasoning and independent corroboration where useful.
4. Write a rule specification with explicit definitions, thresholds, bar-state semantics, timeframe context, edge cases, and uncertainty.
5. Only after implementation is authorized: implement incremental Pine logic; inspect for repaint, future leak, MTF security issues, alerts, limits, and chart usability.
6. Test source fidelity, computation, Pine compilation/chart output where access permits, behavior, and historical compatibility independently.
7. Commit and push the results **to this repository** after each meaningful, independently verifiable increment, including progress, evidence links, decisions, test outcomes, blockers, and next step. Verify push and remote HEAD. Do not claim a commit until readback proves it exists.
8. Update docs/STATE.md and docs/LESSON_COVERAGE.md. If interrupted, continue at earliest unfinished item rather than restarting.

## Guardrails
- User decides when to move from conceptual study to code/deployment and may revise architecture.
- No live trading, brokerage orders, promise of returns, or automated execution authorized by these docs.
- TradingView Strategy Tester results are not real executions. Require cost/slippage assumptions, no lookahead, walk-forward/out-of-sample checks, and stated limitations.
- The current approach is **indicator first, strategy later/optional**, with common methodology and source provenance. Revisit if hard evidence favors strategy-first.
- If an original file is missing, request/recover it rather than writing fabricated source-specific coverage.

When starting a new chat, prefer the exact prompt in docs/RECOVERY.md.
