# Phase 3.6 — prospective S0 annotation pilot (preregistered protocol v1)

**Status: COLLECTION NOT STARTED.** Authorized by the owner after the Phase 3.6 review (2026-11-13, Asia/Manila). This is a **read-only research protocol**, not a selected BOS/CHoCH rule, live signal, accepted Pine feature, trading strategy or finding about analyst agreement. Complete original Coach source and Phase 3.6 methodology remain unchanged.

## Question and competing hypotheses

Can humans independently and consistently identify the **same structural anchor and role** on a frozen standard \`BINANCE:PAXGUSDT\` Spot 5m prefix *before seeing later bars*? An exact regime vote alone is **not** sufficient. Compare the source-faithful S0 manual reference to S1 strict 1/1, 2/2, 3/3 under identical observable prefixes, while keeping R1-A latest-close and R1-B reset/re-cross as **independent policy comparators**. S2 directional change and S3 rolling extremes remain nonselected challengers. Do **not** evaluate financial returns or optimize swing parameters.

The Coach PDF supplies qualitative HH/HL, LH/LL, BOS continuation and CHoCH possible-shift concepts. Swing scale, R1 arming, timestamps, annotation protocol and agreement metrics below are **INDEPENDENT EXPERIMENTAL RULES**, not Coach prescriptions.

## Preregistered sampling, not results

Qualified feed: \`BINANCE:PAXGUSDT\` **Spot**, standard candles, 5m, UTC data times and PHT display. Keep the private v0.1.3 saved script unchanged; M01 optional pivot display **OFF** while a reviewer labels an independent S0 anchor. Use a fixed approximately **10-hour preceding 5m window** (target: 120 already closed bars); if the view cannot show the planned complete prefix, mark the case insufficient rather than reconstruct it afterward.

Predeclare **12 slots** over four days, at **09:00, 15:00 and 21:00 PHT** on **November 14–17, 2026**. Each is the just-completed 5m cutoff. These are sampling slots, NOT forecasts, reminders, future tool executions, or claims that any screenshot will be collected. No opportunistic rescheduling after seeing price. If a slot is missed or the feed is wrong, log MISSED / INVALID; do not silently substitute another chart. All 12 slots remain in the denominator.

- At the scheduled cutoff, capture the chart **after that bar closes and before the next five-minute bar closes**; do not allow future completed candles into the prefix. Record the visible last closed UTC cutoff, capture time, feed identity, source mode, hash of the *exact* original capture, and the artifact's secure location separately.
- Each reviewer should inspect an identical screenshot with only the frozen prefix, without later price candles or another reviewer's labels. Turn OFF M01 and unrelated market-structure labels. Present the same scale instructions, standard candle type and qualified chart to both.
- Reviewers \`R1\` / \`R2\` independently submit one reference per case **or ABSTAIN**; abstention and ambiguity are valid data. Record regime, side, **exact origin**, **level as entered**, HH/HL/LH/LL role if legitimately supportable, declared scale, uncertainty/reason and annotation time. Do not infer that a role was actually known at the pivot's origin just because a screenshot displays it there.
- A truly live pilot requires **capture and annotations before the next scheduled 5m close**. If a second reviewer cannot do that, their later masked-prefix interpretation is \`FROZEN_PREFIX_PRACTICE\`, **not prospective realtime**. Separate the two groups in reporting; never silently combine them as one live cohort.
- Screenshots and reviewer source files may contain personal/account information. Keep their raw bytes in **owner-controlled private storage**. This repository is public: publish only this protocol, generic templates, validators, aggregate counts and explicitly approved anonymized evidence. A SHA-256 digest can identify a supplied file but does not establish when it was created.

The \`research/phase3_6/annotation_protocol.py\` validator checks syntax, a locked slot, self-reported chronological consistency, role/side/regime compatibility, future-hidden flag and screenshot-digest format. It **cannot** inspect the screenshot, authenticate its capture time, verify no future bars were actually visible, attest an exchange receipt, or prove reviewer independence. **GitHub commit timestamps can corroborate upload order** if raw evidence is securely submitted and committed before the next cutoff, but a later hash publication alone cannot substantiate prospective observation.

## Data record contract

Each record uses \`protocol = "P36-S0-PILOT-V1"\`, a slot \`case_id\` like \`P36-20261114-0900-PHT\`, a \`capture\` object and one \`annotation\` object.

- Capture fields: \`instrument = "BINANCE:PAXGUSDT"\`, \`market_type = "SPOT"\`, \`candle_kind = "STANDARD"\`, \`timeframe = "5m"\`, \`source_mode = "LIVE_CHART"\` or \`"FROZEN_PREFIX_PRACTICE"\`, \`target_cutoff_utc\`, \`last_visible_closed_utc\`, \`captured_at_utc\`, \`future_hidden = true\`, \`snapshot_sha256\` (64 hex).
- Annotation fields: \`reviewer_id = "R1"\` or \`"R2"\`, \`recorded_at_utc\`, \`blind_to_peer = true\`, \`selection = "ANCHOR"\` or \`"ABSTAIN"\`, \`regime\` (UP/DOWN/UNKNOWN/RANGE_CANDIDATE), \`swing_side\` (HIGH/LOW/null), \`pivot_origin_utc\` (null if abstaining), \`level_quote\` (a positive, explicitly entered decimal string, or null), \`role\` (HH/HL/LH/LL/null), \`scale = "5M_STRUCTURAL"\`, and a nonempty \`reason\`. For an uncertain anchor one may give a side but \`role = null\`; that must not become a BOS reference.

Each reviewer record is **immutable once submitted**; a correction creates a new revision linked to the original and published with its later time. The validator does not create revision identities automatically. Annotations after the cutoff are not automatically claims of a past as-of historical declaration. R1/R2 anonymization does not guarantee independence.

A deliberately incomplete illustrative skeleton (NOT evidence and not a valid submission):

\`\`\`json
{
  "protocol": "P36-S0-PILOT-V1",
  "case_id": "P36-20261114-0900-PHT",
  "capture": {
    "instrument": "BINANCE:PAXGUSDT", "market_type": "SPOT",
    "candle_kind": "STANDARD", "timeframe": "5m",
    "source_mode": "LIVE_CHART", "target_cutoff_utc": "2026-11-14T01:00:00Z",
    "last_visible_closed_utc": "2026-11-14T01:00:00Z",
    "captured_at_utc": null, "future_hidden": true,
    "snapshot_sha256": null
  },
  "annotation": {
    "reviewer_id": "R1", "recorded_at_utc": null, "blind_to_peer": true,
    "selection": "ABSTAIN", "regime": "UNKNOWN",
    "swing_side": null, "pivot_origin_utc": null,
    "level_quote": null, "role": null,
    "scale": "5M_STRUCTURAL", "reason": "Not yet assessed"
  }
}
\`\`\`

## Adjudication, analysis and stopping rules

Predeclare **exact anchor identity** as primary: same eligible pivot origin UTC, swing side, quote level and structural role at the same declared scale and as-of cutoff. Compare \`regime\` separately; agreement on only UP/DOWN does not count as exact anchor agreement. Record both reviewers' ABSTAIN separately from nonmatch. For levels, report any mismatch in quote units and ticks **only if contemporaneous venue tick metadata is available**. Do not silently snap a reviewer's submitted level to another price.

Calculate on matched valid pairs: exact-anchor agreement count / number of paired non-abstaining references; separately report role agreement, side agreement, regime agreement, coverage and abstention frequency (denominators explicit), plus disagreement reasons, 5m observed delay and policy-specific R1-A/R1-B eligibility if inputs are fully known. Also report counts across **all 12 scheduled slots** including MISSED, INVALID, single-reviewer only and practice. For pairs with at least one abstention, do not fabricate a matched reference. No return/win-rate/accuracy claim.

Practical pilot **process gate**, not a statistical power threshold: aim for at least **8 timely valid R1 live observations**, and **6 paired same-prefix R1/R2 annotations** (realtime or practice clearly separated). If unavailable, report partial coverage and the reason. A pilot this small cannot establish population-level reliability; **no automatic Pine or production policy selection follows a favorable agreement percentage**. Independent reviewer agreement is NOT RUN until at least two genuine independently submitted records exist.

**Stop/alter protocol before collecting more** if screenshots expose future bars, the visible cutoff cannot be verified, or the same reviewer sees the other's responses. Version the change; do not retrospectively reclassify old data. Once the predeclared slots have passed, report evidence, missingness, disagreement and whether a single manual-reference panel would materially reduce capture ambiguity. If reviewers disagree on anchor role/scale, favor clarifying the protocol or the manual baseline rather than promoting S1 as Coach-equivalent.

## Execution boundary and current ledger

| Gate | At protocol creation |
| --- | --- |
| Fixed sampling slots, evidence schema and abstention policy | PREREGISTERED, pending independent review |
| Research validator and controlled tests | Pending CI |
| Any of the 12 live chart captures | **NOT RUN** |
| Any prospective human/manual annotation | **NOT RUN** |
| Inter-reviewer agreement | **NOT RUN** |
| Real-world R1-A/R1-B policy comparison | **NOT RUN** |
| Pine native v0.1.4 or trading features | **NOT AUTHORIZED** |

Preserve draft [PR #2](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/2), accepted GitHub main \`319459863fc138e8d347a1b00bc1de56fabb114c\`, private Pine v0.1.3 build \`L08-0.1.3-3e3d909ba9f5\` and prior acceptance/rollback evidence. No automatic monitoring or background collection has been created.
