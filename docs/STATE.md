# Current project state — canonical checkpoint

**Checkpoint date:** 2026-11-09 (Asia/Manila)
**Repository:** jebobomagcode/alpha-engine-tradingview
**Phase:** 1 — meticulous source-ordered PCSS study (Lessons 01–20 completed, Lesson 21 next)
**Authorized market implementation scope:** crypto ecosystem, explicitly XAUUSDT, XAUTUSDT and PAXGUSDT (D-013, [market scope](MARKET_SCOPE.md)).
**Scope authorized:** sequential PCSS source study, independent literature/research supplements, study/rule-design notes, and continuous verified GitHub documentation. User explicitly said "lets start!" on 2026-11-09.
**Scope NOT YET authorized:** code or deploy an indicator/strategy, connect brokerage automation, or place trades. The current checkpoint is Lesson 17 study; no Pine implementation has occurred.

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
- Formal PCSS **Lessons 01–03** have been taught and source-audited. Lesson 03 (pp. 4–5) includes every Coach scenario, verified arithmetic, exact zero-cost win-rate break-even correction, compounding-model distinction and 1:1 comparison; records: `docs/lessons/03-trading-risk-reward.md` and `docs/research/03-risk-reward-spec-candidates.md`. Lessons 01–02 were already completed and preserved. **20 numbered lessons completed**, **0 Pine scripts written**, **0 backtests**, **0 deployments**.
- **Lesson 04 complete:** original PDF p. 6 HTF/LTF workflow, exact HTF (1H/4H) and LTF (5m/15m) options, 5m example, trend/zone plus pullback/bounce/confirmation/entry/SL/TP all source-audited. Independent temporal-causality research: `docs/lessons/04-time-frame.md`, `docs/research/04-multi-timeframe-causality.md`. No source diagrams/exercises on this page.
- **Lesson 05 complete:** original PDF p. 7 leverage and margin examples, 17 source-inventory items, crypto-vs-Forex comparison, risk and margin distinctions audited. Both $100-based numerical examples verified; fixed margin vs fixed notional risk distinction emphasized. Independent liquidation/solvency research: `docs/lessons/05-leverage-margin.md`, `docs/research/05-margin-leverage-solvency-candidates.md`. No software or exchange-specific liquidation calculation implemented.
- **Lesson 06 complete:** original PDF p. 8 both engulfing descriptions and three illustration panels, with explicit body-vs-shadow/strong-vs-weak ambiguity, synthetic OHLC cases and independent Pine temporal-validity considerations. Source and research documents in `docs/lessons/06-engulfing-pattern.md`, `docs/research/06-engulfing-formalization.md`.
- **Lesson 07 complete:** original PDF p. 9 market structure and confluence including 3 original panels (gold spot / USD FXOpen 1H screenshot plus two structure schematics), uptrend HH/HL, downtrend LH/LL, sideways/higher-TF exception, three-factor validity and Coach's unverified “high probability” BUY/SELL claims. Files: `docs/lessons/07-market-structure-confluence.md` and `docs/research/07-market-structure-confluence-candidates.md`.
- **Lesson 08 complete:** original PDF p. 10 full gated Trading workflow, explicit NO TRADE if zone not touched, three *alternative* confirmation types including rejection plus follow-through, entry only after confirmation close, SL outside S/R and TP next level **or** 1:2/1:3 RR, and five-step recap. Audit `docs/lessons/08-trading-entry-workflow.md`; research `docs/research/08-entry-state-machine-candidates.md`. No charts/quantitative source examples on page.
- **Lesson 09 complete:** original PDF p. 11 Support & Resistance, single annotated chart with red resistance/green support bands and repeated tests; floor/ceiling descriptions, BUY/SELL location mnemonic, support/resistance role reversal and confirmation requirement. Source `docs/lessons/09-support-resistance.md`; independent research `docs/research/09-zone-role-reversal-candidates.md`. Break, zone-touch and flip-retention definitions explicitly unresolved.
- **Lesson 10 complete:** original PDF pp. 12–13 FOREX.com Gold Spot/USD 1H and 5m screenshots, support 4670–4680, resistance 4730–4750, sideways bias, 5m ~4710 in middle = not ideal. Conditional SELL 4730–4750 + reversal + break confirmation + stop 4755 + target support; BUY 4670–4680 + reversal + break confirmation + stop 4665 + target resistance. No reversal = no trade. Study `docs/lessons/10-marking-support-resistance.md`; research `docs/research/10-range-entries-and-confirmation-break.md`. Entry prices unknown; RR calculations in study are explicitly illustrative.
- The full original Coach PDF page 1 was inspected visually and in extracted text. PCSS source file SHA-256 matched its manifest. No original page-1 chart figure, proof, or problem was present.

## Latest completed item and next step
- **Last completed:** Lesson 20 CHoCH (Change of Character), original Coach PDF p25, containing four interpreted figure panels in three embedded graphic regions plus short Taglish prose. Full visual/source audit: docs/lessons/20-choch-change-of-character.md; independent causal-break research: docs/research/20-choch-confirmed-pivots-and-break-semantics.md.
- **COACH:** CHoCH means *possible* trend reversal or shift, not proved reversal. In established downtrend, breaking previous Lower High (LH) implies potential bullish CHoCH; in uptrend breaking previous Higher Low (HL) implies potential bearish CHoCH. Source F1 shows green bullish BOS, red bearish CHoCH, red bearish BOS then green bullish CHoCH. F2 shows LH/LL, bearish BOS, demand zone, CHOCH horizontal breakout and later advance; bottom F3 bearish and F4 bullish labeled zigzags. No original prices, historical trade fills, precise SL/TP or probability.
- **Material unknowns:** precise eligible “previous” swing, protected/internal/external hierarchy, wick vs close and tick buffer, pivot confirmation latency, follow-through/BOS necessity, timeframe precedence, event/candidate known-at timestamps and actual financial edge. Do not backplot an unconfirmed pivot as an available live signal.
- **Cross-lesson:** Earlier Lessons 07, 11, 12 establish structure and BOS/CHoCH distinction; p25 CHoCH is local to the timeframe and does not necessarily reverse a 4H trend. Source example chart resembles illustration earlier in Lesson12; repeated figure is not independent statistical evidence.
- **Next:** Lesson 21 — 4H/1H chart setup with BOS, CHoCH, RSI, EMA, FVG, OB; original PDF **pp26–28** according to coverage ledger, includes TON/USDT original charts. NOT YET STUDIED. Begin only on next owner instruction.
- **Scope:** PCSS source study, independent research and GitHub synchronization only. No Pine code, chart runtime, backtests, deployments, orders or other repository changes.

## GitHub continuity rule
Keep the methodology study and decision log synchronized after each verified increment. Obtain the actual latest commit from GitHub, do not assume this text contains a self-updating SHA. If a new chat begins, verify the PDF identity and resume at Lesson 21; don't restart completed Lessons 01–20.

## Unresolved decisions
- Final feature set and exact formal signal definitions.
- Exact crypto venues, chart symbol prefixes, trading products, session specifications, and initial test universe (including product variants for XAUTUSDT/PAXGUSDT).
- Which enhanced methods survive empirical scrutiny.
- Strategy delivery date and whether it is optional or essential.
- Actual source-file availability in any later chat.
- Actual Pine compilation and TradingView account constraints (not yet assessed for this new project).

## Explicit guardrails
No reliance on or modification of older projects; no unsupported success claims; study is authorized, but **coding remains on hold pending later owner direction**. Resume using docs/RECOVERY.md.
