# Current project state — canonical checkpoint

**Checkpoint date:** 2026-11-09 (Asia/Manila)
**Repository:** jebobomagcode/alpha-engine-tradingview
**Phase:** 1 — meticulous source-ordered PCSS study (Lessons 01–02 completed, Lesson 03 next)
**Authorized market implementation scope:** crypto ecosystem, explicitly XAUUSDT, XAUTUSDT and PAXGUSDT (D-013, [market scope](MARKET_SCOPE.md)).
**Scope authorized:** sequential PCSS source study, independent literature/research supplements, study/rule-design notes, and continuous verified GitHub documentation. User explicitly said "lets start!" on 2026-11-09.
**Scope NOT YET authorized:** code or deploy an indicator/strategy, connect brokerage automation, or place trades. The current checkpoint is Lesson 02 study; no Pine implementation has occurred.

## Confirmed starting state
- The repository was initialized with only a minimal README.
- GitHub visibility was verified **public**. Owner specifically authorized public upload of the Coach PDF; no authorization to publish the full personal PCSS.
- The 35-page Coach PDF and original PCSS Markdown existed in the initiating chat; their exact SHA-256 identities appear in docs/SOURCE_MANIFEST.md.
- The owner **authorized and manually completed public upload of the original Coach PDF on 2026-11-09**. The PDF is committed at `sources/coach trading lessons.pdf` in owner upload commit `02816ae53b6f2bea7a0b8427c12ff8324a24be98`. GitHub tree confirms blob SHA-1 `c99de01b9178e16e240f83f5c4594fa5683a1ba2` and 2,267,976 bytes, identical to the local original's Git hash. The SHA-256 on the original is in `docs/SOURCE_MANIFEST.md`.
- The user chose a new project fully independent of previous engines and repositories.
- The PDF is the only Coach-origin input; independent research, Ponder-style reasoning and substantial improvements are specifically required.
- Working architecture: indicator first, future strategy possible, shared methodology with provenance.
- **New owner direction D-013:** implementation targets crypto, including XAUUSDT, XAUTUSDT, PAXGUSDT; instrument product and exchange feed must be distinguished. Forex and PSE equity teaching remains in PCSS for fidelity, but neither is an independent implementation target. See `docs/MARKET_SCOPE.md`.
- No exact exchange-qualified TradingView chart symbols, spot-vs-derivatives selection for XAUTUSDT/PAXGUSDT, or backtest datasets have been approved/verified.
- Formal PCSS **Lessons 01 and 02** were taught and source-audited, with records in `docs/lessons/01-trading-101.md` and `docs/lessons/02-basic-candlestick-patterns.md`. Lesson 02 images and supplementary inverted-hammer comparison were individually accounted for; candidate formalization is in `docs/research/02-candlestick-rule-candidates.md`. **2 numbered lessons completed**, **0 Pine scripts written**, **0 backtests**, **0 deployments**.
- The full original Coach PDF page 1 was inspected visually and in extracted text. PCSS source file SHA-256 matched its manifest. No original page-1 chart figure, proof, or problem was present.

## Latest completed item and next step
- **Last item completed:** Lesson 02, *Basic Candlestick Pattern*, PDF pages 2–3, including all three taught patterns, six illustrated panels, the side-by-side Shooting Star vs Inverted Hammer figure, and Coach's comparison/confirmation mnemonic. Record: `docs/lessons/02-basic-candlestick-patterns.md`.
- **Next:** Lesson 03, *Trading Risk Reward*, PDF pages 4–5. Source-led risk/reward scenarios, exact calculation verification, win-rate break-even and compounding caveats. Do **not** pre-teach that material or skip source numerical cases.
- **Unresolved rule design:** numerical wick/body/doji thresholds, trend and zone recognition, real-time confirmation and cross-asset constraints. All remain proposals in `docs/research/02-candlestick-rule-candidates.md`.
- **Pacing:** Stop at this checkpoint; the user triggers the next lesson with "Next" or "Proceed".
- **Authorized:** continue source-led study and Ponder-style critical enhancements when instructed to advance; GitHub checkpoint after each meaningful lesson.
- **Not authorized:** Pine implementation, backtesting or deployment without later direction.

## GitHub continuity rule
Keep the methodology study and decision log synchronized after each verified increment. Obtain the actual latest commit from GitHub, do not assume this text contains a self-updating SHA. If a new chat begins, verify the PDF identity and resume at Lesson 03; don't restart completed Lessons 01–02.

## Unresolved decisions
- Final feature set and exact formal signal definitions.
- Exact crypto venues, chart symbol prefixes, trading products, session specifications, and initial test universe (including product variants for XAUTUSDT/PAXGUSDT).
- Which enhanced methods survive empirical scrutiny.
- Strategy delivery date and whether it is optional or essential.
- Actual source-file availability in any later chat.
- Actual Pine compilation and TradingView account constraints (not yet assessed for this new project).

## Explicit guardrails
No reliance on or modification of older projects; no unsupported success claims; study is authorized, but **coding remains on hold pending later owner direction**. Resume using docs/RECOVERY.md.
