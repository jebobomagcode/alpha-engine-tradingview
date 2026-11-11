# Phase 2 frozen-prefix timing policy assessment

**12 November 2026 · Asia/Manila**  
**Scope** Lesson 08 directional continuation, 1H context, 5m reaction, one pre-known fixed S/R interval.  
**Provenance** [Frozen evidence and protocol v1](phase2-frozen-prefix-evidence-v1.md) · [Pre-adjudication commit 5c3eeb1](https://github.com/jebobomagcode/alpha-engine-tradingview/commit/5c3eeb13b4f4b9cd4a0539b50cc8059f1ece52b5) · [Cross-module reconciliation](../methodology/08-cross-module-causal-reconciliation.md)

## 1. Exact evidence coverage and method

- **Source.** Three static source packets cover pages 6, 9, 10, 12 and 13 of the verified Coach PDF. S02 uses the first image on p9, and S03 uses the combined 1H/5m image on p12 plus the adjacent text. The original PDF blob and SHA-256 match the manifest. The packets contain zero historical decision prefixes with timed final OHLC and observed availability. S01 supports workflow only. S02 lacks 5m evidence. S03 is a sideways range example with its own break-of-confirmation condition. None contributes to the numerical comparison. [Coach PDF](../../sources/coach%20trading%20lessons.pdf)
- **Constructed.** Twelve episodes, P01–P12. Each has nine scheduled cutoffs, for **108 frozen numerical prefixes** and **324 policy verdicts**. Inputs contain 48 base 5m bars, one separate corrected version, 12 instances of a 1H context candle, 12 stipulated context/zone annotations, and four ordered observations in one constructed bar. P02 is the reflected short. The 23 prior RC rows remain conceptual background and are outside these counts.
- **Exposure and independence.** The evidence payload and common rubric were committed and read back before recording outcomes. Each cutoff view included only receipts by that cutoff. I recorded judgments in chronological rounds, then reconciled the comparison matrix. The same model authored the fixtures and adjudicated them, so author foreknowledge was possible. There was no genuinely independent blind reviewer. This is an auditable single-model manual pass with future observations withheld from each displayed view. Its evidence level is logical and conceptual.
- **Controlled comparison.** Same OHLC, versions, direction, S/R, body-engulf definition, reset, close invalidation and exclusive expiry at +930 s for all three policies. The same clock and scheduled cutoffs apply to all. Eligibility means first qualified descriptive reaction, with M05 risk incomplete. No fills, orders, market predictions or P&L are evaluated.

## 2. First eligibility and disagreements

Same is R2-B, Later is R2-A by nominal bar order, and Strict is Later plus evidence that final touch was included by reaction open. Times are seconds from 10:00:00. A dash means the policy produced no eligible decision during the common horizon. The delay column measures from the nominal close of the qualifying reaction to the first scheduled eligibility decision.

| Episode | Same | Later | Strict | Detection delay and decisive difference |
| --- | ---: | ---: | ---: | --- |
| P01 | 300 | — | — | 0 s for Same. First touch and strict body engulf occupy one final bar. No later qualifying pattern occurs. |
| P02 | 600 | 600 | 600 | 0 s for all. Reflected short with final touch included at the adjacent reaction’s opening boundary. |
| P03 | 600 | 600 | — | 0 s for Same/Later. The touch arrives at +303, three seconds after the adjacent reaction opens. Strict’s premise is known false. |
| P04 | 600 | 600 | — | 0 s for Same/Later. Touch is visible at the +300 decision. Its order relative to the same-stamped open is unknown, so Strict cannot adjudicate that premise. |
| P05 | 604 | 604 | — | 4 s from nominal reaction close, 1 s from last required receipt. Reaction arrives at +601 and its touch/predecessor at +603. The +602 prefix cannot qualify. Strict’s open-time premise is known false. |
| P06 | 900 | — | — | 0 s for Same. The +600 separator creates a new visit on re-entry. The new contact and engulf share the same bar. Later/Strict cannot borrow the older episode’s touch. |
| P07 | — | — | — | Final touch geometry and closing invalidation coincide at +300. An otherwise engulfing next bar cannot revive the attempt. |
| P08 | — | — | — | The adjacent reaction is absent at the required cutoff and arrives at +931, after the +930 expiry. No retrospective qualification. |
| P09 | — | — | — | Context/zone first supplied at +120, after the only overlap bar opened. It cannot establish an earlier opening premise. Subsequent bars do not touch. |
| P10 | 300 | — | — | 0 s for Same under the declared geometric predicate. The complete constructed tape has no print inside [99,100], despite high/low overlap and an engulfing body. |
| P11 | 300 | 900 | 900 | 0 s from each policy’s own reaction close. The first eligible decision differs by 600 s because the later policies need a second shape. Continuing overlap keeps the same contact episode. |
| P12 | 300 | — | — | 0 s for the issued Same decision. A correction received at +602 removes the original overlap and causes current reassessment. The archived +300 decision remains reconstructible from v1. |

### Counts and delay

| Measure | Same | Later | Strict |
| --- | ---: | ---: | ---: |
| At least one eligible decision before expiry | 9/12 | 5/12 | 2/12 |
| Active qualified reaction at +900 | 8/12 | 5/12 | 2/12 |
| Eligible under Same but missed by deadline | — | 4 | 7 |
| Among first eligible decisions, delay from qualifying bar close | Eight at 0 s, one at 4 s | Four at 0 s, one at 4 s | Two at 0 s |

Seven episodes disagree on whether eligibility occurs by expiry. P11 adds a first-decision timing disagreement, for **eight** episodes with either kind of difference. On the five jointly qualifying Same/Later episodes, the paired Later-minus-Same delays are 0, 0, 0, 0 and 600 s. On the two jointly qualifying Same/Strict episodes, the delays are 0 and 600 s. These paired delays measure the policy’s decision time on the same episode. They are distinct from processing delay after whichever reaction bar the policy accepts.

With a common contact episode, fixed shared gates and no policy-specific side effects, Strict’s candidate set is contained in Later’s, which is contained in Same’s. Wider diagnostic coverage follows from that definition. The cases were deliberately constructed to expose differences, so the counts give neither population rates nor evidence of predictive quality. P10 and P12 illustrate why the additional raw coverage needs evidence labels and version-aware current status.

## 3. As-of status ledger

Each cell gives **Same / Later / Strict**, in that order. The cutoff is in seconds. Z = WAIT_ZONE, C = CONTEXT_INSUFFICIENT, U = required finalized data missing, W = WAIT_CONFIRMATION, L = wait with the required touch-at-open condition known false for the available reaction, T = timing evidence insufficient for that reaction because the tie is unknown, Q = reaction qualified with RISK_INCOMPLETE, X = INVALIDATED, R = REASSESS, E = EXPIRED. L and T are reasons in this assessment, rather than new implementation statuses. The first Q remains in the archived record through later transitions.

| Episode | 0 | 300 | 304 | 600 | 602 | 604 | 900 | 930 | 960 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | ZZZ | QWW | QWW | QWW | QWW | QWW | QWW | EEE | EEE |
| P02 | ZZZ | WWW | WWW | QQQ | QQQ | QQQ | QQQ | EEE | EEE |
| P03 | ZZZ | UUU | WWW | QQL | QQL | QQL | QQL | EEE | EEE |
| P04 | ZZZ | WWW | WWW | QQT | QQT | QQT | QQT | EEE | EEE |
| P05 | ZZZ | UUU | UUU | UUU | UUU | QQL | QQL | EEE | EEE |
| P06 | ZZZ | WWW | WWW | WWW | WWW | WWW | QWW | EEE | EEE |
| P07 | ZZZ | XXX | XXX | XXX | XXX | XXX | XXX | XXX | XXX |
| P08 | ZZZ | WWW | WWW | UUU | UUU | UUU | UUU | EEE | EEE |
| P09 | CCC | ZZZ | ZZZ | ZZZ | ZZZ | ZZZ | ZZZ | EEE | EEE |
| P10 | ZZZ | QWW | QWW | QWW | QWW | QWW | QWW | EEE | EEE |
| P11 | ZZZ | QWW | QWW | QWW | QWW | QWW | QQQ | EEE | EEE |
| P12 | ZZZ | QWW | QWW | QWW | RRR | RRR | RRR | EEE | EEE |

**Missing evidence ledger.** P09 has no 1H direction/zone annotation at offset 0. P03 lacks L1 at +300. P05 lacks L1 at +300 and +304, L1 and L2 at +600, and L1 alone at +602. P08 lacks L2 at +600, +602, +604, +900 and expiry. At +960 that record is available for audit. P04 lacks proof of ordering at the adjacent open throughout. All source packets lack comparable native timing. All constructed episodes lack risk-completion inputs.

## 4. Remaining dependencies and discriminating checks

| Decision | What this study establishes | Open choice and most useful check |
| --- | --- | --- |
| **D-C01 · timestamps** | Nominal bar ordering can be distinguished from receipt ordering. P03 and P04 have the same nominal sequence as a known-on-time case but different eligibility evidence. P05 demonstrates that as-of qualification can be valid even with out-of-order receipts, once both records are included. | Verify which boundary is actually observable on the intended data path. Capture one qualified feed with finality, nominal close, independently logged receipt or explicit bar-clock semantics, opening-event ordering, and actual evaluation cutoff. Compare the same captured sequence to a historical reconstruction. If exact order is unobserved, keep it unknown. |
| **D-C02 · reference arming** | The bounded p10 profile accepts a stipulated 1H context and has no BOS trigger dependency. In prior RC-03, 107 then 105 before arming high 106 distinguishes the history block from latest-close, despite the same at-arming state. RC-04 distinguishes reset from permanent block, and RC-06 shows that a gap can defeat a complete-history test while a separately qualified adjacent crossing remains evaluable. | Keep arming outside the first p10 reaction comparison. If a later profile requires BOS/CHoCH, freeze reference and role and compare returned breach, persistent breach, valid reset and missing-history pairs against contemporaneous structural annotations. Latest-close is the simpler arming control. History interval and re-use remain open. |
| **D-C04 · timing** | P01 and P06 show source-compatible candidate geometries that Later and Strict exclude. P03 and P05 show source-compatible later-bar geometries that Strict excludes due to evidence arrival. P04 is indeterminate for Strict. P11 shows the delay when both approaches eventually qualify. | Compare the same live-captured or appropriately labeled evidence prefixes using blinded annotation of source compatibility and scope. Include same-bar and later-only cases. Measure paired delay, missed source-compatible reactions, and extra reactions adjudicated as inadmissible or uncertain. |
| **D-C05 · contact and reset** | P10 proves bar overlap can coexist with a fully observed sequence containing no zone price. P06 demonstrates that an already known separator can change which visit the reaction belongs to. Under a counterfactual continuous-visit rule, the +900 shape could borrow the +300 touch. The fixed comparison excludes that borrowing. | Evaluate two independent annotations on a common set of visit sequences, including missing or late separator and apparent gap-through. With qualified fine-resolution observations where available, compare geometric overlap with actual observed zone prints. Freeze one reset policy for a comparison, then vary it separately. |
| **D-C06 · lifecycle** | P07 preserves known invalidation despite later reversal. P08 shows expiry depends on availability at a permitted decision. P12 separates the current corrected view from the earlier as-issued decision. | Replay captured versions and material context updates on the same setup ID. Confirm no duplicate first eligibility, no terminal resurrection, and an auditable correction trail. Determine actual expiry and treatment of unresolved active reassessment from that evidence. The +930 deadline is a fixture convention. |

## 5. Challenge checks and source limits

**Clock leakage.** P09 would incorrectly qualify Same at +300 if the +120 context/zone receipt were treated as knowledge at time 0. P05 would qualify too early if sorted solely by bar sequence and treated as available at nominal close. P08 would qualify if the late bar were inserted retroactively at +600. P12 would lose its original eligibility if the final stored version were substituted into earlier prefixes. The recorded outcomes preserve the original boundaries.

**Geometry and sequencing.** P10’s bar (100.25,103,98,101) spans the zone. Its four stipulated prices all lie outside [99,100]. Same accepts the geometric pattern under the fixed rule, while the full constructed tape defeats any claim of an actual zone print. A coarse later-bar requirement can avoid that specific extra label but does not itself prove physical contact. Preserve both facts when available. For P06, the separator’s final low 100.5 is above support and was included before re-entry, so the prior visit cannot satisfy the later condition for a different visit.

**Source fidelity.** Lesson 08 orders location, confirmation and closed-candle entry, and permits one strong confirmation. A completed same-bar geometric touch and engulf can fit a descriptive reading of that workflow, but the text does not establish that Coach would accept every such candle or require a same-bar policy. The alternative that contact must be observed before searching for a reaction is plausible. Strict implements a specific observed-before-open requirement that the PDF does not quantify. The constructed cases demonstrate exclusions without establishing a compensating empirical benefit. They also omit the other p10 pattern types, market regimes, and live data quality. [Original Lesson 08, p10](../../sources/coach%20trading%20lessons.pdf#page=10)

**Verification boundary.** Input identities, valid OHLC ordering, the partial-order examples, row counts, and first-eligibility arithmetic were checked. Historical rendering, live receipt capture, reliability, and predictive benefit remain unverified. The source samples cannot settle the default policy.

## 6. Provisional recommendation and M06 handoff

**Provisional research policy.** Use R2-B for the first eventual *descriptive* 1H→5m indicator profile. Allow either a same-closed-bar reaction or a later reaction within its qualified contact episode. Label the observation as geometric overlap when that is the evidence, disclose ambiguous order or an observed contradiction, and retain the separate M05 risk gate. Require context and zone known by touch-bar open and final inputs by decision. Use the common lifecycle and retain source and version provenance. This is a recommendation for a research comparison, with production choices open.

**Simpler comparator and strongest alternative.** Use R2-A by later bar order as the simpler sequential comparison. It needs a distinct reaction candle and complete evidence by decision, without asserting a native reception order. It is preferable if blinded adjudication shows that same-bar cases regularly violate the intended confirmation order or create unacceptable geometric-only candidates. Use Strict as an additional diagnostic only where the clock can show touch before onset. Promote Strict over ordinary Later only if measured disambiguation justifies its extra exclusions and delay.

**Reversal criterion.** Freeze a single qualified 1H/5m evidence set with both same-bar and later-bar opportunities, including negatives, gaps, tied boundaries, delayed receipts and zone-reset cases. Give separate reviewers only receipt-bounded snapshots and the source workflow, withholding policy outcomes and future observations. Require separate labels for geometric overlap, verified physical touch where observable, source compatibility, and indeterminate order. Compare disagreements, coverage and paired delay. Prefer Later if qualified blind labels demonstrate a material inadmissible same-bar burden with acceptable coverage loss. Consider Strict only with usable native ordering and evidence that it removes wrong-order classifications beyond what Later removes. Define acceptable tradeoffs before reviewing the labels. No market-performance claim follows from this descriptive test.

**Before M06.** Confirm the provisional research choice and the handoff contract with the owner. The contract should carry setup ID, instrument/feed, zone and evidence version, contact episode and evidence type, reaction onset/close/availability, decision cutoff, timing policy, current terminal/reassessment state and reason. The risk layer should receive a currently qualified reaction with explicit risk inputs or unknowns. A historical qualification, pending/insufficient setup, expired attempt, or geometric-only observation without its evidence label cannot be promoted silently. Keep expiry, reset, arming and real clock assumptions explicit or conditional.

**Recommendation for beginning M06.** After owner review, begin M06 as a bounded risk-interface specification conditional on the provisional reaction input. This study provides enough evidence to define that interface. Selection of production timing, market-specific numerical parameters, execution assumptions and runtime validation remain separate decisions. The next empirical requirement for selecting an indicator policy is the paired receipt-bounded annotation test above.
