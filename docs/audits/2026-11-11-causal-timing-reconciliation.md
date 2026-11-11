# Phase 2 Ponder Research Checkpoint — Causal Eligibility and Reaction Timing

**Date:** 2026-11-11 Asia/Manila.
**Status:** source-based reasoning and paper specification completed for this increment; **Phase 2 remains OPEN; no Pine or market backtest**.
**Repository:** independent \`jebobomagcode/alpha-engine-tradingview\` only.
**Sources:** original Coach PDF SHA-256 \`481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730\`, [source-study coverage](../SOURCE_STUDY_COMPLETION_AUDIT.md), [2026-11-10 audit](2026-11-10-phase2-preimplementation-audit.md). Re-read PDF native text pp8–15,19,25; figures for p14/p15 were inspected at prior audit and not newly claimed here.

## Scope and provenance

- **COACH_EXPLICIT:** p9 trend+zone+signal; p10 HTF bias, NO TRADE if price does not reach zone, completed lower-TF confirmation for the Lesson08 workflow; p13 separately says \`entry sa break ng confirmation\` for the conditional range example; p14–16 BOS = continuation after identifying previous HH/LL; p25 CHoCH = **possible** reversal via prior LH/HL.
- **INDEPENDENT math/engineering:** fractal pivots, multi-stage pivot/context timing, reference arming and consumption, simultaneous outside candle policy, closed-bar geometric zone overlap, same-touch-bar versus later-bar reaction policies, invalidation precedence, proposed status labels.
- **OUT OF SCOPE:** code, TradingView alert acceptance, exchange OHLC retrieval, historical outcome statistics, order fills, strategy emulator settings, trading or other repositories.

## Finding CR-01 — a flawed prior illustration corrected

The 2026-11-10 document's **AUD-C01** describes a high pivot106 becoming confirmed even though a required subsequent right candle closed107. Under the exact **strict local fractal pivot high** defined in M01-P1, this is **impossible**, since that later bar has high at least107 and violates the condition that candidate high106 strictly exceeds every required right-hand high. It must be **PIVOT_REJECTED**, NOT an eligible-but-prebreached pivot.

The genuine issue is **late reference eligibility**: a valid pivot may be confirmed before a price crossing, but regime/context may be known only afterward, or a manual input may be imported later. This still forbids retroactive BOS/CHoCH. Corrected [R1 specification](../methodology/04-reference-arming-and-pivot-order.md), cases ARM-01 (invalid pivot) and ARM-02 (valid pivot, later regime eligibility). The historical audit document remains intact with explicit supersession rather than silent erasure.

## Finding CR-02 — alternatives and provisional audit baseline

**R1-A reference arming:** frozen pivot ID and known-at times, prior regime eligibility, no pre-armed crossing, exact-once consumption, unavailable/ambiguous pivot -> INSUFFICIENT. **R1-B:** optional future reset and re-cross policy after prebreach; may recycle stale levels. **R1-C:** manual known-at source comparison. **Outside-bar ambiguity:** avoid inventing sequence of local high and low within one OHLC candle.

**R2-A zone/reaction:** for a pre-known eligible zone, first final touch bar establishes confirmed *geometric* contact at its availability time; distinct subsequent completed reaction required. **R2-B:** a source-compatible comparator permits the same final bar to evidence both contact and reaction if zone was pre-known before bar start. Neither provides a retroactive intrabar fill. **R2-C:** truly time-resolved lower-resolution observations can adjudicate when available.

**Range branch:** p13 break-of-confirmation ambiguity preserved as **RB1** later-bar wick breach versus **RB2** later-bar closing break, *after* the confirming pattern is known. Do not misquote either as Coach's exact unique entry order.

## Finding CR-03 — what a bar's range can and cannot establish

Even when \`high >= zone.low\` and \`low <= zone.high\`, that is **geometric overlap**. It may not establish ordered contact, a fill at a particular price, or within-bar sequence of rejection, invalidation and stop. Competing invalidation semantics (close beyond zone, wick beyond zone, later acceptance) are separate model choices. When a single final bar touches and closes beyond a provisional invalidation boundary, the conservative candidate rejects the new entry as TOUCHED_AND_INVALIDATED. This is an independent safety policy, not an original Coach numeric rule.

## Reviewed case inventory and verification limit

- [R1](../methodology/04-reference-arming-and-pivot-order.md): **16** constructed discriminating cases, ARM-01..ARM-16.
- [R2](../methodology/05-zone-contact-reaction-timing.md): **18** constructed cases, TIME-01..TIME-18.
- Existing [M01 foundation](../methodology/01-causal-market-structure.md): 16 original paper fixtures. Entry/risk and zone research: 20 each.
- **Total in currently documented specifications: 90 paper/constructed scenario rows** (16+20+20+16+18); this counts distinct documented rows, **NOT 90 executed assertions or market tests**.
- **Observed checks in this turn:** local original PDF checksum; GitHub current branch/readback and source texts; algebraic contradiction in former AUD-C01; logical derivation of proposed event-time constraints; paper inspection and fixture inventory. No independent external human expert, synthetic code runner or runtime TradingView check.

## Ponder choice and tradeoffs

| Criterion | Conservative baseline | Responsive comparator | Reversal condition |
|---|---|---|---|
| Structural event | R1-A no prebreach/retrospective event | R1-B later reset/re-cross | If R1-A loses too many clearly documented valid cases or has excessive delay, retain R1-B for testing |
| Outside candle | quarantine ambiguous high+low in one OHLC bar | separate high/low channels awaiting later sequence | Genuine intrabar observations resolve order |
| Zone reaction | R2-A next fully completed reaction | R2-B same completed touch+reaction | If source-congruent historical examples strongly need same-bar confirmation, prefer testing R2-B |
| Range trigger | preserve RB1/RB2 separately | evidence-backed manual annotation | Later source-grounded or user-authorized order policy sets exact event |

**Research recommendation, not Owner-approved implementation parameters:** R1-A and R2-A as **conservative comparison baselines**, against R1-B/R2-B and manual/source annotations. They deliberately favor auditability over responsiveness. This may harm practical signal timeliness and must be tested rather than asserted superior.

## Remaining dependency gates, next authorized Phase 2 work

1. M04 candle geometry: body engulf, wick rejection + follow-through, strong-body alternative, gap/doji/zero-range cases, explicit source-to-hypothesis provenance.
2. M05 conflict resolution and cross-TF known-at state transitions; avoid exposing a BUY/SELL in a context that was unavailable at decision time.
3. Later synthetic executable tests and historical venue-specific crypto studies require **separate implementation authorization**. No numerical win-rate, guarantee, trade advice, or automatic strategy behavior is established.

**Final status:** This research increment is **documented**, original PDF unchanged, current Phase2 still OPEN, code and deployment unchanged.
