# Phase 2 M02/M04/M05-R2 — Zone Contact, Candle Reaction and Entry-Timing Contract

**STATUS: RESEARCH COMPARISON, NOT CODE, NOT A STRATEGY OR ORDER POLICY.** 2026-11-11 Asia/Manila.
**Coach PDF:** p8 engulfing at support/resistance; p9 trend-zone-signal; p10 Lesson08 says wait for zone (otherwise **NO TRADE**) and then LTF confirmation, **entry after confirmation candle CLOSES**; p11 S/R needs confirmation; pp12–13 conditional range case says **“entry sa break ng confirmation”**. These are **distinct source contexts**. [M01-R1 reference timing](04-reference-arming-and-pivot-order.md), [previous M05 draft](02-topdown-entry-state-and-risk.md), [zone hypotheses](03-zones-sr-ob-fvg-fibonacci.md).
**All OHLC and state semantics below are independent technical candidates**, not additional words from Coach.

## 1. Five causal layers that must not be collapsed

1. **Context known:** prior completed HTF bars establish a directional/range scenario and its qualification time. LTF must not use future HTF bar values.
2. **Zone known:** geometric interval and source provenance exist *before* candidate contact. A zone invented later cannot justify an earlier touch.
3. **Physical contact?** OHLC overlap of a zone may be measured, but does not always identify exact tick-by-tick price path or executable fill. Record a \`GEOMETRIC_OVERLAP\` observation, not an “executed at zone”.
4. **Reaction closed:** one independently defined candle or a multi-candle follow-through becomes final/available. A developing pattern is PROVISIONAL.
5. **Entry proposal eligible:** only after necessary source gates and risk information. Eligibility is NOT an actual fill; a strategy would additionally specify order placement and realistic execution mechanics.

**Temporal convention R2-A (conservative research baseline):** A zone is eligible for touch on a lower-timeframe bar only if \`zone.known_at <= touch_bar.open_at\`. A completed touch bar supplies the earliest **confirmed contact evidence** at its \`available_at\`. A *different, later* final lower-timeframe candle must provide the confirmation. Bar order alone does not establish that the touch was observed before reaction onset. The [12 November reconciliation](08-cross-module-causal-reconciliation.md#5-bounded-lesson-08-profile-and-comparison) compares a later-bar version with both inputs known by decision and a strict version requiring touch known by reaction open. This deliberately errs toward delayed signals; it is **not** a Coach-specified mandatory additional candle.

**Alternative R2-B (same-closed-bar confirmation):** If the zone was known before the touch bar opened, allow the same **fully closed** LTF candle to count both geometric zone touch and a valid independently specified engulfing/rejection/strong candle at its close. The combined evidence is available no earlier than that close, and only after its required final inputs have arrived. No retrospective in-bar order/fill is inferred. R2-B is more responsive and may better match Coach's “one strong confirmation enough,” but it requires later check of how pattern and zone position are defined.

**Alternative R2-C (time-resolved sequence):** If genuinely available lower-resolution ordered observations (not just the OHLC summary) establish zone touch before a distinct subsequent reaction, apply those recorded timestamps. Coverage/costs may be limited; this cannot be claimed from a single ordinary OHLC bar.

**Working comparison:** R2-A versus R2-B for indicator-style analysis, with R2-C where verifiable. None is an approved strategy entry rule.

## 2. Event data contracts (research)

| Record | Required fields and semantics |
|---|---|
| \`context\` | instrument/product/feed, HTF, regime, source hypothesis and regime_known_at |
| \`zone\` | zone_id, kind, [low,high], unit, provenance, definition candles, known_at, active window and invalidation policy |
| \`touch\` | zone_id, LTF bar ID, overlap method, bar.open_at/close_at/available_at, flag \`GEOMETRIC_OVERLAP\` or \`NO_OVERLAP\` |
| \`reaction\` | side/pattern hypothesis, candle(s) IDs, finality, pattern known_at, same-bar/later-bar designation |
| \`eligibility\` | prior context/zone/reaction evidence references and causal checks, status/reasons, risk completeness and expiry |
| \`execution\` | **NOT SPECIFIED**, no actual order, fill timestamp, fee, stop/target collision or performance |

**Overlap test candidate**: for zone \([a,b]\) and completed candle \([L_t,H_t]\), geometric intersection when \(H_t\ge a\) and \(L_t\le b\). For a body-contact comparator use interval \([\min(O_t,C_t),\max(O_t,C_t)]\) instead. Exact equality is a boundary contact only if instrument tick and comparison policies permit it. Geometric overlap by OHLC does **not** certify every intermediate price actually traded in a discontinuous market or that an order at that price would fill.

**Source-pattern candidate definitions:** PDF p8 bullish big green engulfing red near support / bearish big red engulfing green near resistance, without unique body-vs-wick or min-size inequality. PDF p10 offers an **OR** of engulfing, long wick **plus follow-through**, or strong body. We must preserve that a “long wick + follow-through” case requires additional confirmation by its own source wording and is not interchangeable with a standalone wick in every setup. Any chosen ratio (e.g., wick/body > \(\kappa\)) is independent and must have edge cases for zero body/range, equality, bad OHLC and tick rounding. No thresholds are chosen here.

## 3. Zone invalidation and simultaneous contact: explicit alternate policies

For a support/demand interval \([a,b]\), a proposed (not source-certified) invalidation policy **I1** is a *fully completed closing break below \(a\)*; for resistance/supply a close above \(b\). Alternative **I2** invalidates on wick excursion beyond far boundary. Alternative **I3** requires subsequent acceptance and/or structural break before invalidation. These differ materially in crypto volatility.

**Conservative priority for an indicator research candidate:** if the same completed candle both overlaps the zone and **closes beyond the defined invalidation boundary** under I1, record \`TOUCHED_AND_INVALIDATED\` and **do not** promote the episode to WAIT_CONFIRMATION or a valid new entry. OHLC cannot establish which touch and rejection/stop event came first. If it merely wicks beyond but closes back within, I1 and I2 disagree; report the hypothesis rather than hide the difference.

Zone must be active when contact evidence arises. If the source says “last touch” or a zone has been revisited many times, treat each \`contact_episode_id\` separately with a later rearming/expiry policy **OPEN**. No perpetual re-emission on every bar inside a zone without an explicit design.

## 4. Two independent source branches for final trigger

**Lesson08-style trend-continuation branch:**
- Wait for eligible prior HTF trend, pre-known support/resistance zone, qualifying touch, and completed lower-timeframe candle reaction. Then output \`CANDIDATE_FOR_REVIEW\` only if risk proposal is also coherent.
- Under R2-A touch and confirmation are on **separate** completed bars. Under R2-B they may be the same completed bar. In either, **no candidate before confirmation close and availability**.
- “Entry after confirmation candle closes” is **source statement**; whether hypothetical fill happens at next bar open, limit/stop or later price is separate future strategy modeling, NOT an immediate fill at observed close.

**Lesson10-style conditional RANGE branch:** PDF p13 says “entry sa break ng confirmation” near the zone after a reversal candle, which is not equivalent to an explicitly after-close entry. Distinct independent alternatives:
- **RB1**: after a *completed* reversal candle is known, a later bar **wicks** beyond that candle's direction-specific reference extreme; a possible breakout trigger, NOT assumed filled order.
- **RB2**: after that candle, a later bar **closes** beyond its extreme; later/less noisy, still not an executed order.
- **RB3**: source-annotation/manual interpretation with specified confirmation candle and break point known-at.
Keep the trigger reference (e.g., bullish signal high or bearish signal low), the signal known-at time and subsequent break distinct. A signal candle cannot exceed its own final extreme. If a subsequent bar starts before the signal reference is available, a crossing observed before arming cannot qualify for a post-arming wick trigger. If only that subsequent bar’s final range is available, it does not establish whether the crossing occurred before or after arming.

A range long at support and a trend short against resistance on a different timeframe are not one global BUY/SELL truth: each scenario and opposing context must be reported with rationale and invalidation.

## 5. Temporal examples and same-bar caution

Illustrative UTC-neutral timestamps; all prices fictitious, not current crypto observations:

| Time | Observation | R2-A sequential | R2-B same-bar |
|---|---|---|---|
| 09:55 | 1H source support zone [98,100] and trend already known | Can begin eligible 5m touch search | Same |
| 10:00–10:05 | 5m candle low99 high103, bullish body-engulf, closes102 | CONTACT known at10:05, WAIT_CONFIRMATION | CONTACT+REACTION known at10:05, candidate only after risk check |
| 10:05–10:10 | 5m next candle closes with qualifying distinct confirmation | Candidate after10:10, if risk complete | Might already have candidate after10:05 |
| 10:10–10:15 | price below zone floor on close97 | Invalidate under I1; new entry disallowed | Same |
| 09:55–10:00 | zone becomes known at09:59 while 5m candle already forming | That 5m bar is NOT eligible for baseline contact; next opens10:00 | Same baseline availability guard |

**Critical caveat:** One completed 5m OHLC candle has high/low extremes but not necessarily their within-bar chronological ordering; an entry triggered *during* that candle cannot be reconstructed from that bar alone after looking at its final close. External TradingView documentation on historical strategy bar fills uses explicit emulator assumptions; those are simulation mechanics, not proof of actual fills.

## 6. Discriminating thought fixtures (MANUAL EXPECTATIONS ONLY, not code)

All times/levels fictitious; equal boundaries, invalidation and risk follow explicit candidate assumptions.

| ID | Constructed observation | R2-A conservative expected | R2-B difference |
|---|---|---|---|
| TIME-01 | Zone known before touch bar, no overlapping price | WAIT_ZONE | same |
| TIME-02 | Zone only first known at touch bar close | No eligible historical contact | same |
| TIME-03 | Zone known before bar; wick overlaps, body stays outside | Contact under wick geometry; none under body-only | same |
| TIME-04 | Touch bar is still developing | CONTACT_PENDING, not confirmed | same |
| TIME-05 | Touch bar closes and also body-engulfs at support | WAIT_CONFIRMATION for separate later bar | Candidate reaction at same close, risk pending |
| TIME-06 | Completed touch at t, subsequent confirmation candle developing | WAIT_CONFIRMATION | may use earlier same-bar only if qualifying |
| TIME-07 | Completed touch then later closed bullish reaction; risk complete | CANDIDATE_FOR_REVIEW after later close | same or earlier depending first candle |
| TIME-08 | Touch and close beyond demand-zone invalidation floor | TOUCHED_AND_INVALIDATED; no candidate | same under I1 |
| TIME-09 | Wick pierces floor but close inside support | I1 zone active, I2 invalidates | same policy contrast |
| TIME-10 | Previous touch without signal; 3 bars remain inside zone | Episode/rearm definition OPEN; no repetitive fresh signal inferred | same |
| TIME-11 | New 1H zone becomes final during already-open 5m bar | Eligible only for later bar starting after zone known under baseline | same |
| TIME-12 | Valid contact, 5m bullish engulf, stop unknown | RISK_INCOMPLETE, not placed trade | same |
| TIME-13 | Source range reversal candle closes at10:05, high105; next candle wicks106 closes104 | RB1 break observed after signal, RB2 no close break | same range branch |
| TIME-14 | Constructed RB1 case. Signal bar [10:00, 10:05) has final high 105, first available at 10:05:03. A separately timestamped observation at 10:05:01 in the subsequent bar reaches 106. No later eligible breach is supplied. | The observed excursion predates arming and cannot trigger RB1. With only the later bar’s final high 106 and no ordered evidence, classify the post-arming wick sequence as unknown. | Same range-branch boundary. |
| TIME-15 | 4H trend source still forming, 5m zone+signal final | CONTEXT_INSUFFICIENT for that HTF requirement | same |
| TIME-16 | Two equivalent overlapping S/R+FVG annotations generated from same bars | Two names not automatically two independent signals | same |
| TIME-17 | 5m bar gaps from above zone to below; high/low ranges straddle zone | Geometric overlap may be recorded, exact zone-price trade/fill UNKNOWN | same |
| TIME-18 | An active setup already has a valid contact. A required reaction bar is either final and flat at O=H=L=C=100, or final and malformed at (O,H,L,C)=(100,100,99,101). Assume no other reaction qualifies. | Flat: ZERO_RANGE for ratio-dependent geometry, WAIT_CONFIRMATION under this candidate. Malformed: DATA_INSUFFICIENT for the affected required reaction input. | Same input distinction. |

**12 November correction (E1, E5):** TIME-14 previously compared a candle’s intrabar price to its own final maximum. TIME-18 combined a strong green body with zero range and treated valid flat data as malformed. A valid bar has every constituent price at or below its final high, and zero range forces all four OHLC values equal. The corrected rows keep their IDs. [Original rows at the reviewed revision](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/bad2c01fe961f0f05de6e05555b914baf4062c5d/docs/methodology/05-zone-contact-reaction-timing.md).

**Review disposition:** 18 manually specified expected cases are design assertions, not executed TradingView tests, market statistics, or verified profitability.

## 7. Ponder comparison and next stage

**R2-A is stronger** for conservative causal sequencing and simplest event audit, but may reject source-consistent valid one-candle reactions; **R2-B is stronger** for responsiveness and plausible fidelity to “one strong confirmation enough,” but has more same-bar sequencing ambiguity; **R2-C supplies more ordering information** when reliable intrabar order exists, at higher data/complexity cost. No preference should be marketed as objectively “best” without validation.

**PROVISIONAL RESEARCH RECOMMENDATION:** carry R2-A as a strict falsifiable baseline and R2-B as an **end-of-bar** competitor for later runtime verification. Never interpret either as permission to backfill intrabar orders. Keep range “break of confirmation” RB1/RB2 separate. Final thresholds, contact episode reset and trade execution remain OPEN.

**NEXT:** refine candle-pattern alternatives and compare the most consequential R1/R2 discriminating cases with source teaching examples; draft a test protocol that separates manual logical adjudication, later synthetic runtime checks and later real market backtests (only after user authorizes implementation).
