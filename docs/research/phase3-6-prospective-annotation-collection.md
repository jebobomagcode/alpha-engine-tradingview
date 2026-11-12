# Phase 3.6 — S0 pilot collection checklist and preflight ledger (historical, superseded)

**HISTORICAL — CANCELLED BEFORE COLLECTION by owner D-032 on 2026-11-13 PHT.** This proposal and its validator are retained only as prior research. Its 12 planned future slots were cancelled, NOT missed or completed; 0 captures, 0 reviewer records, no human agreement. Do not solicit any reviewer or owner action. Current path: [AI-only engineering](../implementation/ai-only-accelerated-completion-plan.md). The text below is superseded historical documentation, not an active task.



**Checkpoint:** 2026-11-13 PHT. **INDEPENDENT_EXTENSION:** operator checklist for the [preregistered v1 protocol](phase3-6-prospective-annotation-pilot.md). The sampling grid, evidence schema and policy comparators are unchanged.

## Capture and submit within each five-minute window

1. Before the slot, open [TradingView BINANCE:PAXGUSDT](https://www.tradingview.com/chart/?symbol=BINANCE%3APAXGUSDT&interval=5). Check Binance **Spot**, **5m**, standard **Candles**, and a PHT display (UTC+8). Use a view with no M01 or other structural labels. Leave the private saved indicator alone. Frame approximately 10 hours of history, targeting 120 closed bars.
2. Just after the scheduled close, locate the last completed candle using the chart's time axis or crosshair. For **09:00 PHT**, that candle opened at **08:55 PHT** and closed at **09:00 PHT**. The **09:00-open** candle is already forming. Take a local region screenshot whose last visible candle is the completed one. Keep the symbol, interval, time scale, and enough price scale to identify the reference. Exclude the forming candle, changing quotes and account information from what reviewers see. If the full planned prefix or cutoff cannot be checked, record the limitation.
3. Save the capture bytes privately, record actual capture time to the second in UTC, and compute SHA-256 over the exact file both reviewers will see. Use the same unchanged prefix for both. If using a separate sanitized reviewer image, keep the original private and document the relationship and both digests. Never make a public chart-image link for private evidence.
4. Work from the frozen capture. Independently submit **one ANCHOR or ABSTAIN** before the next 5m close. Use the card below. Record actual submission time and keep the original annotation immutable. If a private service provides a timestamped receipt tied to the exact record, retain it alongside the record. Prepare the form and the private channel before the slot.
5. If a willing second human is available, send them only the frozen prefix and the same instructions. Keep both answers hidden from each other until submission. Record independent reviewer participation only when it happened. A later blinded interpretation belongs in `FROZEN_PREFIX_PRACTICE`. A live R1 and a later practice R2 are separate records and cannot produce a same-cohort pair. Reviewer IDs R1/R2 are separate from arming policies R1-A/R1-B.

For the first slot, use `P36-20261114-0900-PHT` and cutoff `2026-11-14T01:00:00Z`. Capture and submit before **09:05 PHT** (`01:05:00Z`, exclusive). If the window is missed, retain the scheduled ID and record MISSED. If the wrong feed, cutoff or unblinded view was used, record INVALID with reason. Do not backfill a prospective annotation.

### Private reviewer card

Record these fields using the exact [v1 JSON schema](phase3-6-prospective-annotation-pilot.md#data-record-contract). Keep the private file location and any submission receipt separately from the validator JSON.

| Capture record | Reviewer record |
| --- | --- |
| Case ID, source mode, qualified feed, target cutoff UTC, visible last close UTC, actual capture UTC, future hidden, and exact snapshot SHA-256 | R1 or R2, recorded UTC, peer-blind status, ANCHOR or ABSTAIN, regime, and a brief reason including uncertainty |
| Exact frozen screenshot with enough visible context to check the cutoff | For ANCHOR, HIGH/LOW, exact UTC **opening time** of selected origin bar, exact displayed quote string, role HH/HL/LH/LL or null, and scale `5M_STRUCTURAL`. For ABSTAIN, leave side/origin/level/role null. If exact origin or level cannot be read, use ABSTAIN and say why. |

The validator's `REPORTED_LIVE_TIMELINESS_NOT_AUTHENTICATED` means the supplied times pass chronology checks. A service's receipt tied to the annotation and screenshot digest can independently corroborate submission by its server time. That does not establish the exact screen capture time, absence of later information, or genuine reviewer independence by itself. Save receipt evidence when available and distinguish it from local file metadata and declared timestamps.

## Pending slots

All rows were future at this checkpoint. Capture windows include the listed cutoff and exclude the deadline. Pending rows are neither missed observations nor successful observations.

| Case ID | Cutoff PHT | Cutoff UTC | Deadline PHT | Live status |
| --- | --- | --- | --- | --- |
| P36-20261114-0900-PHT | Nov 14 09:00 | Nov 14 01:00 | 09:05 | PENDING |
| P36-20261114-1500-PHT | Nov 14 15:00 | Nov 14 07:00 | 15:05 | PENDING |
| P36-20261114-2100-PHT | Nov 14 21:00 | Nov 14 13:00 | 21:05 | PENDING |
| P36-20261115-0900-PHT | Nov 15 09:00 | Nov 15 01:00 | 09:05 | PENDING |
| P36-20261115-1500-PHT | Nov 15 15:00 | Nov 15 07:00 | 15:05 | PENDING |
| P36-20261115-2100-PHT | Nov 15 21:00 | Nov 15 13:00 | 21:05 | PENDING |
| P36-20261116-0900-PHT | Nov 16 09:00 | Nov 16 01:00 | 09:05 | PENDING |
| P36-20261116-1500-PHT | Nov 16 15:00 | Nov 16 07:00 | 15:05 | PENDING |
| P36-20261116-2100-PHT | Nov 16 21:00 | Nov 16 13:00 | 21:05 | PENDING |
| P36-20261117-0900-PHT | Nov 17 09:00 | Nov 17 01:00 | 09:05 | PENDING |
| P36-20261117-1500-PHT | Nov 17 15:00 | Nov 17 07:00 | 15:05 | PENDING |
| P36-20261117-2100-PHT | Nov 17 21:00 | Nov 17 13:00 | 21:05 | PENDING |

## Adjudication after submission

- **Reviewer agreement:** validate each actual record and compare only identical snapshot bytes, distinct genuine independent reviewers and the same evidence mode. Keep abstentions, role-null anchors, exact origin/side/role/level matches and regime-only matches separate. Two controlled preflight probes confirmed that the current `compare_pair` can report an exact schema match when both roles are null, and treats different quote strings as different even when decimal padding is the only difference. Keep the raw results, exclude role-null records from the *eligible* exact-reference numerator and denominator, and report decimal-equivalent formatting separately. Do not silently change the submitted price or the validator.
- **S0 versus S1:** when exact closed OHLC for the same feed and cutoff is available, freeze that tape and apply strict 1/1, 2/2 and 3/3 under the ordered baseline in the [structural-reference contract](phase3-6-structural-reference-contract.md). Compare origin, side, level, role and regime separately. Report pending right bars, ties, dual extrema, missing tape, or no eligible role. Preserve the cutoff result before reporting any later confirmation delay. An unreadable price or missing OHLC is INSUFFICIENT for exact comparison.
- **R1-A versus R1-B:** use the same eligible S0 anchor, declared availability and qualified predecessor closes. Do not backdate a declaration made between two boundaries. Under the modeled chart clock, first consider it at the next admissible opening boundary, using the adjacent final close available there. If real receipt order is absent, report only modeled eligibility. Freeze the same follow-up evidence bounds for both policies before reviewing the following price path. If it does not establish a reset or re-cross, report unresolved or no observed event through the common bound, as appropriate. Do not score returns.

## Preflight gate ledger

| Gate | 2026-11-13 PHT outcome |
| --- | --- |
| Protocol, dates and validator | **PASS.** Compared all 12 UTC cutoffs to the validator, reran only its 12 targeted checks, and read back the existing 67-test CI result. Prior 55 accepted and 21 structural research tests preserved. |
| Qualified chart availability | **PASS for preflight.** TradingView showed `BINANCE:PAXGUSDT`, 5 minutes, Candles, and UTC+8. This was outside the scheduled windows and no screenshot was collected. |
| Prospective evidence | **NOT RUN.** 0/12 captured, 0 missed, 0 invalid, 12 pending at this checkpoint. |
| Reviewer records and independent agreement | **NOT RUN.** 0 R1, 0 R2, 0 practice, 0 valid pairs, and no receipt evidence. Agreement has no denominator. |
| S0/S1 and R1-A/R1-B comparisons on observed pilot evidence | **NOT RUN.** No actual paired prefix, exact price tape or qualifying annotation for these comparisons. |
| v0.1.4 read-only diagnostic | **INSUFFICIENT.** Revisit if observed capture failures show that a panel would improve cutoff, origin or reference recording. Reviewer disagreement about structural role would instead motivate clearer manual criteria. |

No reminders or background collection are configured. Preserve the source protocol and keep public updates limited to safe status, aggregate outcomes and approved anonymized evidence.
