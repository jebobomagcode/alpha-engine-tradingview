# New ChatGPT conversation recovery — START HERE

This file is intended to prevent loss of decisions, source identity, and checked progress when a ChatGPT conversation ends or usage limits intervene.

## Copy/paste into a NEW ChatGPT conversation

> Continue my completely independent **Alpha Engine TradingView** project at https://github.com/jebobomagcode/alpha-engine-tradingview. Use GitHub as the authoritative project state. Before doing anything, inspect the actual current default-branch HEAD and read README.md, AGENTS.md, docs/STATE.md, docs/DECISIONS.md, docs/SOURCE_MANIFEST.md, docs/PCSS_PROTOCOL.md, docs/LESSON_COVERAGE.md and docs/ROADMAP.md. This project is independent from every previous Coach/Alpha Engine repository; do not access, reuse or modify any of them. Coach Fredy's sole source is the 35-page **coach trading lessons.pdf**. My PCSS file is **Personal_Comprehensive_Study_Standard_Revised_2026-10-17.md**. Use exact SHA-256 identifiers in SOURCE_MANIFEST.md. Study in original order without skipping figures/examples, apply continuous Ponder-style rigorous critique, and use independent research and mathematical reasoning to bridge gaps and substantially improve the methodology. Explicitly distinguish Coach source, interpretation, independent enhancement, and tested findings. Our working direction is an indicator first with a separately testable strategy later. Continuously update and verify this GitHub repository after meaningful increments. First tell me what is actually complete, what is not, and the next incomplete item (Lessons 01–06 complete, Lesson 07 next as of 2026-11-09); never invent past work. Respect the authorization and current scope in STATE.md. **Owner market decision D-013: this system targets CRYPTO (not standalone Forex or Philippine equities), explicitly including XAUUSDT, XAUTUSDT and PAXGUSDT; these have distinct product/feed mechanics. Read `docs/MARKET_SCOPE.md` and preserve original full Coach lesson coverage.** The original `sources/coach trading lessons.pdf` **is already uploaded and verified** (Git blob SHA-1 `c99de01b9178e16e240f83f5c4594fa5683a1ba2`; owner upload commit `02816ae53b6f2bea7a0b8427c12ff8324a24be98`). Obtain the original from that GitHub path, checking its identity if the repository changes. The full PCSS Markdown is not in this public repo, so ask me to reattach that file when needed. Do not invent any unavailable material.

## Recovery procedure for an assistant
1. Fetch repository metadata and current default-branch HEAD. Confirm exact repository name and visibility. Check for newer commits and that this guide has not been superseded.
2. Read AGENTS.md and the linked documents. Prefer verified repo history to incomplete memory or claims from a prior chat.
3. Check STATE.md for authorization and stage, LESSON_COVERAGE.md for the earliest unfinished item, DECISIONS.md for the latest owner direction.
4. Confirm attached source files exist; compare exact SHA-256 digests. A source-only summary in GitHub is NOT equivalent to having the original 35-page illustrated PDF.
5. State precisely which GitHub files and source versions were actually accessed, and whether study/implementation/testing occurred.
6. Follow only the user's presently authorized scope. Maintain GitHub as durable, readable checkpoint after every meaningful increment.

## What GitHub does and does not contain at this checkpoint
- **Contains:** complete operational project charter, dated decisions, the source identities/checksums, PCSS workflow summary, source-order page map, design/validation principles, roadmap and checkpoint.
- **Contains the original Coach PDF:** `sources/coach trading lessons.pdf`, uploaded by the owner in commit `02816ae53b6f2bea7a0b8427c12ff8324a24be98` and exact-byte matched against the original by Git blob hash `c99de01b9178e16e240f83f5c4594fa5683a1ba2`. The original SHA-256 is in `docs/SOURCE_MANIFEST.md`.
- **Contains completed study:** [Lesson 01](lessons/01-trading-101.md), [Lesson 02](lessons/02-basic-candlestick-patterns.md), [Lesson 03 risk-reward source study and arithmetic audit](lessons/03-trading-risk-reward.md); [Lesson 02 rule candidates](research/02-candlestick-rule-candidates.md) and [Lesson 03 risk/math design hypotheses](research/03-risk-reward-spec-candidates.md). The next lesson is Lesson 07, *Market Structure and Confluence*, PDF page 9. Completed [Lesson 06](lessons/06-engulfing-pattern.md) and its [research analysis](research/06-engulfing-formalization.md) are in GitHub. Completed [Lesson 04](lessons/04-time-frame.md) and [MTF causality research](research/04-multi-timeframe-causality.md), plus completed [Lesson 05](lessons/05-leverage-margin.md) and [margin/solvency research](research/05-margin-leverage-solvency-candidates.md), are in GitHub.
- **Does not yet contain:** the complete personal PCSS Markdown, any Pine code, validated signals, backtests or deployment. **They have not been silently performed.**
- **First source check:** inspect the original PDF at `sources/coach trading lessons.pdf`, verify Git blob SHA-1 `c99de01b9178e16e240f83f5c4594fa5683a1ba2` (and SHA-256 if the raw binary can be downloaded). If missing or different, retrieve the original; never assume a substituted PDF is equivalent.
- **Re-attach the complete personal PCSS** when needed for full-fidelity study. Do not claim any summary fully replaces the personal PCSS original.

## Safe continuation rules
- Work **only** in jebobomagcode/alpha-engine-tradingview.
- No publishing third-party full text or user-private contents in this public repo.
- Keep original Coach baseline and improvements distinct.
- Scope D-013: crypto only for implementation, explicitly including XAUUSDT, XAUTUSDT and PAXGUSDT; never treat derivative gold exposure and backed gold tokens as the same instrument or use one venue's feed for another silently. Full PCSS retains all original lessons.
- Ponder-style scrutiny is mandatory even if a specialized plugin is unavailable: articulate alternatives, counterexamples, competing assumptions and a falsifiable test.
- Verify remote push/readback after every real update; append actual commit SHA in a conversational handoff.
- Never equate strategy backtest profit to a demonstrated real-world edge.
