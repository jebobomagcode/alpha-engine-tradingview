# Cross-module causal reconciliation and Lesson 08 research profile

**12 November 2026 · Asia/Manila**  
**Status** Phase 2 conceptual research. The factual corrections and causal invariants are established at specification level. The compared policies are independent research choices.  
**Lineage** [Independent review, E1–E10](../audits/2026-11-12-independent-repository-and-methodology-review.md) · [Written corrections commit](https://github.com/jebobomagcode/alpha-engine-tradingview/commit/9ad7a0dda3ad5e2148cffd737674377e7df6473c) · [Paper cases and adjudication](../research/phase2-causal-reconciliation-paper-cases.md)

## 1. Source-to-rule traceability

The [35-page Coach PDF](../../sources/coach%20trading%20lessons.pdf) is the sole Coach authority. The attached PDF matched the committed blob and the manifest SHA-256. The completed 26-unit study and the historical audit remain the references for earlier work. [Manifest](../SOURCE_MANIFEST.md) · [Coverage](../LESSON_COVERAGE.md)

| Reference | Coach source and scope | Independent operational choice |
| --- | --- | --- |
| S1 · higher/lower roles | **COACH_EXPLICIT, pp6, 9–10.** Higher timeframe supplies trend and location. Lower timeframe supplies the setup and confirmation. The 1H or 4H to 5m workflow appears in p6. | One 1H→5m profile. Manual 1H bias and one fixed pre-known S/R interval isolate timing from detector selection. |
| S2 · location first | **COACH_EXPLICIT, p10.** Mark S/R and bias. Wait for the relevant zone. If price fails to reach it, no trade under this workflow. | Require a pre-known active zone and valid final 5m geometric overlap for this paper comparison. |
| S3 · confirmation alternatives | **COACH_EXPLICIT, pp8–10.** Engulfing is preferred in p10, with long-wick rejection plus follow-through and a strong body also given. Entry follows the relevant confirmation candle’s close. | Compare same-close and two later-bar policies. Exact inequalities and first-touch-candle eligibility remain unspecified by the PDF. |
| S4 · range | **COACH_EXPLICIT, pp12–13.** Sideways gold case with reversal patterns at boundaries and a break of confirmation. | Keep distinct RB1 wick and RB2 closing-break candidates. Each requires a later eligible observation and its own timing evidence. |
| S5 · structure | **COACH_EXPLICIT, pp14–16, 25.** Establish trend/structure before BOS. BOS is continuation and CHoCH signals a possible shift. | Pivot methods, arming, buffers, ties and regime handover remain independent choices. |
| S6 · other profiles | **COACH_EXPLICIT, pp18, 21, 24, 31.** SOL countertrend scalp, HTF-aligned continuation and 30m OB→5m scalp are different examples. | Preserve their distinct roles. The p10 profile uses RSI/EMA as optional context and introduces no mandatory RSI/EMA threshold. |
| S7 · Q&A3 | **COACH_EXPLICIT, p32.** Coach accepts the higher-timeframe bearish assessment and sees 15m consolidation. He discusses a conditional 15m short near 79,850 on rejection wick, bearish engulfing or failed breakout above about 79.8k. The conditional long has **BOS on 15m or BOS on 1H, or a 1H close above the stated 79,850–80k area**. | Keep all three long predicates and their timeframe-specific prerequisites. Track separate short and long scenarios. Threshold selection within or above the approximate area, expiry, and priority remain research choices. |

The p32 student’s 79,419 entry, 79,918 stop and 78,423 target belong to the student proposal. Coach’s conditional short has a stop around 80,250 and a target around 79k or lower with trailing language. He provides no corresponding exact long stop, target or realized fill. The original Bitstamp BTCUSD charts are 4H, 1H and 15m. They support the stated context, while synchronization and event ordering remain unverified. A 15m rejection may precede a 1H breakout in the same observation window. The later observation does not alter the earlier decision. [Original p32](../../sources/coach%20trading%20lessons.pdf#page=32) · [Q&A3 study](../lessons/qa-03-btc-consolidation-retest-and-breakout.md) · [Q&A3 research](../research/qa-03-btc-conditional-retest-breakout-risk.md)

## 2. Common causal contract

**INDEPENDENT_EXTENSION.** Use a qualified instrument/product, bar definition and source version. A known ordering means the earlier item precedes or is included at the relevant boundary. A shared timestamp by itself gives no tie order. A trusted capture ordinal or declared model boundary can supply it. If a required order is unsupported, preserve it as unknown. Record clock source, resolution and bar/session alignment.

| Field | Meaning | Ordering requirement |
| --- | --- | --- |
| **Origin** | Bar interval, swing bar, zone source interval, or observed tick instant. Final OHLC leaves the exact occurrence of its extremes unknown. | Origin may precede all later fields. Use actual observation granularity. |
| **Availability** | First observed inclusion of the input version on the selected evidence clock. | A final bar cannot be available before its close. Exchange close and receiver arrival are distinct. |
| **Confirmation** | Earliest boundary at which the predicate is established under the rule with its required final evidence. | It cannot precede the latest availability of its prerequisites. A strict pivot needs valid center, left and right bars, including a delayed left bar. |
| **Arming** | Boundary at which a frozen reference becomes eligible for its structural role and regime. | Requires confirmation, role/regime availability and declared freshness or prebreach checks. |
| **Decision** | Actual evaluation boundary and frozen evidence version set producing an as-of status. | Every required input belongs to its observable prefix and satisfies any earlier cutoff specific to its stage. |
| **Display** | First publication and a separate chart coordinate such as an earlier pivot origin. | Actionable publication follows decision. An origin marker drawn retrospectively carries the later confirmation time. |

For any decision at \(d\), every used input must be in its observable prefix. For a premise required at earlier boundary \(b\), it must also be known at \(b\). A 1H update received after a 5m bar opens may contribute to a new decision under a declared decision-time policy. It cannot establish the earlier opening premise. A replay may use a declared chart-bar observation clock. Native receipt time remains unknown when the replay does not carry it. An annotation created today takes today’s availability even if its origin is historical.

**Frozen output invariant.** Two evidence streams with the same observable prefix, versions and policy at a cutoff give the same as-of output. Later arrivals or later source revisions can cause new decisions or reassessment. Preserve the earlier decision and the version set that produced it. Do not treat an older close as the adjacent predecessor when the expected intervening bar is missing or invalid.

**E2 disposition.** A pivot belonging to bar 10 may first qualify after confirmation at bar 12. Showing its origin after bar 12 is compatible with an archived bar-10 decision in which it was unavailable. Eligibility, decision publication and rendering are separate checks. [Structure](01-causal-market-structure.md) · [Candles](06-candle-pattern-and-confirmation-grammar.md) · [M07](../research/phase2-mtf-validation-and-falsification-protocol.md)

## 3. Structural arming alternatives

**INDEPENDENT_EXTENSION.** Freeze the qualified pivot, role, timeframe, threshold and policy version in each comparison. For a high, the break side is a final close strictly above the threshold. For a low, it is strictly below. Equality is on the non-break side for this comparison. An eligible crossing uses adjacent qualified final closes, with the earlier on the non-break side and the later on the break side. For the strict open-boundary arming comparator in the paper cases, the reference must be armed at the crossing bar’s opening boundary. The resulting label describes a close-to-close crossing rather than an intrabar path or fill.

| Policy | Arming and suppression | Evidence and tradeoff |
| --- | --- | --- |
| **R1-A · latest close** | If the immediately preceding eligible final close at arming is beyond the threshold, block this reference. A missing predecessor makes the at-arming check unknown. Otherwise a later fresh eligible crossing can qualify. | Simple and responsive after a return before arming. A prior excursion that reverted before arming does not veto it. |
| **R1-B · reset then re-cross** | If beyond at arming, require a distinct later final close on the non-break side. The reset must be known at the crossing bar’s open. Then require a fresh crossing. | Recovers references excluded by A. May recycle stale references without an expiry or replacement rule. A consumed reference stays consumed. |
| **History comparator** | In the paper cases, check final closes whose nominal closing boundaries lie after pivot confirmation and up to arming, with inclusion at the boundary demonstrated. Block after any beyond-threshold close in that declared interval. A missing or not-yet-received expected bar makes the history gate unknown. | Catches reverted excursions. Requires history coverage and a justified window start. The stated window is a case convention. |
| **R1-C · manual reference** | Supply an identified level, role, timeframe and witnessed known-at boundary, then apply a declared gate above. | Useful source-facing control. Historical screenshot annotations alone cannot establish when the reference was knowable. |

A past beyond-threshold close and the at-arming price state are distinct. Track references as armed, blocked, reset pending, consumed or retired, with an evidence reason when eligibility is unknown. A new eligible pivot or role may merit a new reference ID. A relabeling, replay, or refreshed classification must not re-emit the same underlying crossing. A newly assigned structural role cannot make a pre-arm movement actionable. An outside candle can support unordered high and low observations. If their order is required and unavailable, withhold the derived ordered structure. A 5m possible CHoCH does not reclassify 1H structure by itself. [R1](04-reference-arming-and-pivot-order.md) · [Cases RC-03–07 and RC-20](../research/phase2-causal-reconciliation-paper-cases.md)

## 4. Stable setup and contact lifecycle

**INDEPENDENT_EXTENSION.** A setup is a scoped hypothesis with an immutable identity from qualified instrument/source, profile version, side, anchor context reference/version, and creation discriminator. Assign it once when the branch has enough identified context to be tracked. A zone may be absent before selection. Freeze the chosen interval and its version when selected for a live attempt. Replacing a material anchor or a frozen zone retires the old attempt and may create a separately identified successor. Re-reading evidence does not create a new setup.

A contact episode is a child of a setup and selected zone version. Its ID derives from the first accepted touch observation. Continuing overlap is the same visit. A new episode needs a declared reset and a later qualified re-entry while the setup remains viable. Under the paper convention, a distinct completed bar wholly outside on the approach side and known by the next re-entry bar’s open can reset the episode. A delayed, missing or invalid bar cannot prove that reset. The separator makes a future re-entry eligible for a new episode. It does not by itself erase the completed visit or disqualify a reaction on the departing bar. A reaction links to its contact episode, onset, qualifying final bar(s), policy, and decision boundary. Contact and reaction IDs do not change the setup identity.

| State or observation | Criteria |
| --- | --- |
| **DATA_INSUFFICIENT / CONTEXT_INSUFFICIENT / ZONE_INSUFFICIENT** | An input required by this branch is invalid or unknown. Record the missing dependency. A known mismatch is a false predicate. An optional unknown remains descriptive. |
| **WAIT_ZONE** | A live setup has compatible context and a pre-known eligible zone, with no eligible contact on the qualified prefix. |
| **CONTACT_PENDING** | Provisional evidence suggests touch. The final qualified contact is still unobserved. |
| **WAIT_CONFIRMATION** | A contact is confirmed and no qualifying completed reaction is available. Missing required reaction data gives insufficiency. A valid flat bar can leave a ratio-dependent reaction waiting with ZERO_RANGE. |
| **WAIT_BREAK** | A source-specific profile such as p13 can require a further break. Evaluate against the frozen trigger reference and the declared observation policy. |
| **Reaction qualified, risk incomplete** | The reaction is ready for a separate risk review. Existing M05 RISK_INCOMPLETE applies when its required risk evidence is absent. CANDIDATE_FOR_REVIEW requires the full M05 gates. |
| **REASSESS** | Newly available evidence challenges the active premise. Suspend current candidacy, then record resolution or a separate successor. The earlier decision retains its as-of evidence. |
| **INVALIDATED / EXPIRED / SUPERSEDED** | A known disqualifying event, a reached declared lifetime boundary, or replacement ends the attempt. Delayed evidence cannot reactivate a terminal attempt. If chronology is uncertain, preserve terminal reasons with the observed ordering limits. |

**E9 geometry.** A straddling high/low range can overlap a zone without proving a trade inside it. An opening gap from a wholly above bar to a wholly below bar can have no overlap in either bar. Where approach side is required, use qualified prior observations under a declared comparator. With levels 100, 100.75 and 101.50, a neighbor tolerance of 1 connects all three under single-link clustering, while zone diameter is 1.50. A moving EMA evaluated with a bar’s own close is a descriptive end-of-bar location. A pre-known zone requires an earlier frozen level. These alternatives stay outside the fixed-zone profile. [Zone alternatives](03-zones-sr-ob-fvg-fibonacci.md)

**E10 conflict and precedence.** Evaluate required predicates as true, false or unknown per branch, alongside provisional evidence and lifecycle. A recorded terminal disposition precludes new eligibility for that attempt. For live setups, expose the first unmet required gate and retain the other known reasons. A newly known invalidation can coexist with unknown trigger evidence. Distinguish disagreement among timeframe observations, opposing conditional watches, and two opposite candidates currently eligible at the same defined gate and cutoff. Only the third is an eligibility conflict at that gate. Preserve each branch’s lifetime, scope and evidence. [MTF statuses](07-mtf-context-conflicts-and-causal-states.md) · [Cases RC-14–19](../research/phase2-causal-reconciliation-paper-cases.md)

## 5. Bounded Lesson 08 profile and comparison

Use one fictional qualified market and standard 1H/5m OHLC. A witnessed, finalized 1H UP annotation with fixed pre-known support defines the long side. The short side mirrors it with DOWN and resistance. Context and zone must be included by the touch-bar opening boundary. A newly available 1H assessment can disconfirm the thesis by decision but cannot establish the past opening premise. For timing comparisons only, use strict real-body engulfing on opposite-color bars as an independent paper predicate. The source’s other confirmation alternatives remain available.

A final eligible 5m bar geometrically overlaps a closed zone if its high reaches the zone’s lower bound and its low reaches the upper bound. The episode starts when that final evidence is accepted. For the paper invalidation comparator, a close strictly beyond the far boundary ends the attempt. If the touch bar closes below the support floor, record both observations and block promotion. The profile stops its assessment at reaction and risk completeness.

| Policy | Information required | Earliest qualification and missed cases |
| --- | --- | --- |
| **R2-B · same closed bar allowed** | Pre-known zone and context. One final bar may supply geometric touch and the directional reaction. Every dependency must be available by decision. Later bars may qualify under the bar-order criterion. | Earliest decision after both facts and their dependencies are available. Can capture an isolated touch-and-engulf. A single bar cannot establish the precise internal order. |
| **R2-A · later bar by bar order** | The reaction-onset bar is strictly later than the touch bar in the 5m sequence. Both inputs must be available by decision. Reaction may start or arrive before the touch is observed, provided the attempt is still active at evaluation. | Earliest nominal completion is one 5m bar later on adjacent regular bars. Receipt and evaluation can add delay. Misses same-bar-only reactions. |
| **R2-A · later bar with touch known at open** | In addition to later bar order, final touch must be included by reaction onset on the declared evidence clock. A tie needs ordering evidence. | Can admit the adjacent bar if touch is already included by its open. Late receipt can delay qualification further or miss the only qualifying reaction. |
| **R2-C · ordered observations** | Qualified intrabar observations may show zone encounter and reaction onset in order. The p10 confirmation still requires its declared close. | Resolves some paths left ambiguous by OHLC, at greater data and rule cost. Outside the bounded profile. |

For a single-candle pattern, reaction onset is the directional candle’s opening boundary. Prior geometry bars are dependencies, rather than onset. For long-wick rejection plus follow-through, onset is the rejection bar and completion is the required later follow-through close. A rejection on the touch bar plus later follow-through can qualify under B. The later completion alone cannot satisfy a later-onset rule.

**E7 comparison result.** The [paired paper cases](../research/phase2-causal-reconciliation-paper-cases.md) establish one- and two-bar differences under specified arrivals, a same-close-only observation, and an out-of-order delivery where bar-order qualification must wait for both inputs. The observed-sequence policy is a useful conservative control. Same-close is the strongest challenger given the source’s single-confirmation language. These cases show possible delay and missed scenarios, with no estimated real-market frequency or superiority.

## 6. Findings, unresolved decisions and readiness

| Finding | Disposition |
| --- | --- |
| E1, E5 | **VALIDATED, logic.** Corrected impossible TIME-14 and TIME-18 premises and distinguished flat from malformed data. |
| E2 | **VALIDATED, logic.** Decision and publication obey their cutoffs. Earlier rendering coordinates remain possible. |
| E3 | **INDEPENDENT_EXTENSION.** Split current price state from pre-arm breach history. Compared R1 policies on the same paths. |
| E4 | **COACH_EXPLICIT.** Restored all three p32 breakout alternatives. Priority, threshold geometry and shared lifetime are open. |
| E6 | **VALIDATED, geometry.** Directional rejection requires the corresponding wick. Maximum wick fraction is direction-neutral. |
| E7 | **INDEPENDENT_EXTENSION.** Separated later bar order, observed touch before onset, and same-close qualification. |
| E8–E10 | **INDEPENDENT_EXTENSION.** Defined stable setup identity, episode and zone alternatives, and branch-scoped eligibility. Production selection is open. |

| Decision | Open issue | Most useful discriminating check |
| --- | --- | --- |
| D-C01 | Clock observability and timestamp ties. | Compare native receipt and chart-bar boundaries in delayed, equal-time and out-of-order cases if later authorized. RC-02, 10–11, 21. |
| D-C02 | Latest close, reset, history window and completeness. | Compare returned breach, persistent breach, reset and a missing pre-arm bar against the same frozen reference. RC-03–06. |
| D-C03 | Pivot degree, same-side replacement, outside bar and regime handover. | Blind annotate identical prefixes and compare reference identity without imposing an intrabar order. RC-07, 20. |
| D-C04 | R2 onset and qualification policy. | Compare same-only, adjacent late touch, out-of-order and follow-through cases. Measure first eligibility, delay and misses. RC-08–13. |
| D-C05 | Zone generation, approach, overlap, invalidation and re-entry. | Compare straddle versus observed encounter, zone-spanning gap, joint touch/invalidation and separated re-entry. Test cluster diameter versus linkage. RC-14–16, 19. |
| D-C06 | Lifetime, re-evaluation, revisions and branch conflict. | Compare delayed evidence around expiry, material anchor replacement, opposite watch and concurrently eligible cases. RC-17–18, 22–23. |
| D-C07 | Numeric patterns, instrument/product and runtime mapping. | Use paired frozen prefixes on both sides, then test qualified clock, tick and equality behavior under separately authorized runtime checks. |
| D-C08 | Q&A3 approximate threshold and structural breakout model. | Isolate the three breakout predicates, then measure how independently declared thresholds or BOS definitions change classification. RC-17. |

**Defined enough to carry into later design:** timestamp roles, admissibility, append-only decisions, directional wick primitives, source branch alternatives and stable identity. The compared policies have determinate outputs on the declared paper cases. **Open before implementation behavior can be selected:** market/feed, real clock observability, detector thresholds, profile defaults, reset/freshness, and treatment of incomplete or simultaneous evidence. This mission establishes conceptual and manual verification.

**Next proposed step, subject to owner review:** independently adjudicate frozen 1H/5m prefixes with both same-close and strict observed-sequence comparators. Record coverage, delay and open-tie evidence. Use that comparison to settle the initial policy and clock assumptions before specifying M06.
