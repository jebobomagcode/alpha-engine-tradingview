# Phase 2 frozen-prefix evidence set v1

**12 November 2026 · Asia/Manila**  
**Parent research checkpoint** [d16b65e96e82f849386e2685c99b2308bd5b9458](https://github.com/jebobomagcode/alpha-engine-tradingview/commit/d16b65e96e82f849386e2685c99b2308bd5b9458)  
**Purpose** Compare three descriptive reaction timing policies on fixed input. The source packets are qualitative. The numerical packets are constructed. This file contains the pre-adjudication inputs and protocol.  
**Methodology** [Reconciled specification](../methodology/08-cross-module-causal-reconciliation.md) · [Existing 23 RC paper cases](phase2-causal-reconciliation-paper-cases.md)

## A. Source observation packets

The [original Coach PDF](../../sources/coach%20trading%20lessons.pdf) matched the [manifest](../SOURCE_MANIFEST.md), SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. The cutoff for each source packet is the specified passage or static image as published in the PDF. Historical receipt and decision clocks are unavailable. Adjacent or subsequent displayed bars are not reconstructed into an earlier as-of prefix.

| Packet | Observations admitted to the packet | Missing evidence or scope |
| --- | --- | --- |
| S01 · [pp6, 10](../../sources/coach%20trading%20lessons.pdf#page=10) | Coach uses higher timeframe for trend and zone and offers 5m confirmation. Lesson 08 says to wait for the zone and confirm on the lower timeframe, with entry after confirmation closes. It gives engulfing, rejection with follow-through and strong body as alternatives. | Workflow text only. No timed OHLC, contemporaneous zone selection, or decision receipt. Exact touch-to-reaction order within a 5m candle is unspecified. |
| S02 · [p9, first image](../../sources/coach%20trading%20lessons.pdf#page=9) | The FXOpen Gold Spot/USD 1H screenshot labels a downtrend, LH/LL, resistance, support and a bearish engulfing annotation. Preserve the image’s attribution and timeframe. | No corresponding 5m prefix or verified receipt time for the highlighted formation. Chart annotations are displayed observations, with original annotation time unknown. |
| S03 · [pp12–13](../../sources/coach%20trading%20lessons.pdf#page=12) | The FOREX.com gold example depicts 1H and 5m. Coach describes sideways context, support around 4,670–4,680, resistance around 4,730–4,750, price near the middle around 4,710, and a conditional break-of-confirmation workflow. | A different scenario family from p10 directional continuation. Image panels do not establish synchronized finalized candles, contemporaneous zone availability, or a historical decision cutoff. |

## B. Numerical packet protocol

- **Coverage.** Twelve hypothetical 1H→5m episodes, P01–P12. Nine scheduled decision cutoffs per episode. These are fixtures in one fictional feed, with no instrument, venue or calendar claims. Times are offsets in seconds from 10:00:00 on a fictional clock. Cases exercise distinct failure modes, with some paired variations of earlier RC ideas.
- **Observation identity.** In each episode, records are namespaced by its ID. A declared common prior 1H candle and a selected 1H annotation are context inputs. Manual direction is stipulated for the timing comparison. Its annotation is not inferred from the single supplied bar. The selected annotation includes support [99,100], or the reflected resistance for P02. The 1H context record and the 5m predecessor have separate identities. The four 5m intervals are [-300,0), [0,300), [300,600), [600,900). Open and close offsets specify nominal bar boundaries.
- **Availability.** Include an observation only when its receipt offset is at or before the decision cutoff. Equal decision-time receipts are stipulated to be included by that decision batch. Each receipt explicitly records whether inclusion at a simultaneous bar open is demonstrated or unknown. Receipt by a decision batch does not prove inclusion at a separate opening event. The source packets lack this clock. Each listed OHLC is a final record for its version.
- **Frozen views.** A prefix ID is episode ID plus the decision offset. Its evidence is the shared metadata and only that episode’s records received by the cutoff, in availability order. Calendar boundaries tell the reviewer which bars should already have closed. Missing receipts appear as missing, without a disclosed future arrival time or future OHLC. At the decision cutoff, preceding versions remain visible. Later corrections enter as separate records and preserve prior decisions.
- **Common shape and gates.** Strict opposite-color real-body engulfing of the immediately preceding qualified 5m bar. For the short mirror in P02, reverse direction, reflect every price by 200 minus price, and exchange high and low. Require final evidence, qualified pre-known context and zone by touch-bar open, and inclusive final-bar geometric overlap. Check far-side closing invalidation strictly beyond the far edge. Continue tracking an episode through overlap. A wholly outside separator on the approach side, included by re-entry open, separates a new visit from the prior one. A material correction removing accepted contact sends the live setup to reassessment.
- **Common evaluation.** When a scheduled final bar is missing and needed to decide the current gate, record data insufficiency with the missing ID. Preserve prior eligible output as historical if applicable. No required trade-risk evidence is supplied, so a qualified reaction leads to RISK_INCOMPLETE for the fuller M05 gate. The same exclusive expiry at offset 930 applies to every episode and policy. 960 is an audit cutoff. Apply the terminal state once known. Delayed evidence cannot revive the attempt. Record first eligibility at the earliest scheduled decision that qualifies and report later state changes.
- **Policies.** Same = R2-B accepts a qualified same-bar or later-bar reaction. Later = R2-A requires reaction onset strictly later in nominal bar order than the accepted touch of its episode. Strict = Later plus evidence that final touch was included by the reaction bar’s open. “By the open” includes witnessed same-clock ties ordered before or at the opening boundary. A known late receipt fails that predicate. An unresolved tie leaves the predicate unknown. These policies share every other input, gate and horizon.
- **Metrics.** Compare qualification by the exclusive deadline, first eligible cutoff, paired delay where both qualify, and reasons for non-qualification. Measure detection delay as first eligible cutoff minus the reaction bar’s nominal close. Compare candidate stage rather than fills, risk completion or returns. Report source packets separately. Later and Strict losses relative to Same are missed *diagnostic* cases in this set, not estimated market false negatives.
- **Review order.** Freeze this file before recording outcomes. Present each cutoff through an evidence-only view filtering by the receipt field. A reviewer can take a new isolated copy of each view without the full fixture or prior labels. Include all eligible observations and any source-policy limits. Record the reviewer and exposure limits. A same-model design and adjudication pass does not establish reviewer independence.

## C. Frozen numerical payload

In each 5m bar row, the columns are open offset, close offset, O, H, L, C, receipt offset, and tie evidence. BEFORE_OPEN is witnessed inclusion by any coincident next open. UNKNOWN_OPEN is usable at the decision batch with earlier-at-open order unresolved. AFTER_OPEN marks a later arrival relative to that bar’s immediately following open. A context override replaces the default annotation receipt. Other observations list their own receipt and provenance. The optional tape is exhaustive for its constructed bar only and is supplementary under the fixed geometric-overlap comparison.

~~~json
{
  "version": "phase2-prefix-v1",
  "decision_cutoffs": [0, 300, 304, 600, 602, 604, 900, 930, 960],
  "expiry": 930,
  "context": {
    "bar": [-7200, -3600, 99, 107, 97, 104, -3598],
    "direction": "UP",
    "zone": [99, 100],
    "annotation_receipt": -20
  },
  "cases": {
    "P01": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,100.5,105,99.5,104,300,"BEFORE_OPEN"],
        [300,600,104,105,103,104,600,"BEFORE_OPEN"],
        [600,900,104,104.25,102.5,103,900,"BEFORE_OPEN"]
      ]
    },
    "P02": {
      "direction": "DOWN", "zone": [100,101], "context_ohlc": [101,103,93,96],
      "bars": [
        [-300,0,97,99.25,96,99,0,"BEFORE_OPEN"],
        [0,300,97,100.5,96,99,300,"BEFORE_OPEN"],
        [300,600,99.5,99.75,95,96,600,"BEFORE_OPEN"],
        [600,900,96,97,95,96,900,"BEFORE_OPEN"]
      ]
    },
    "P03": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,103,104,99.5,101,303,"AFTER_OPEN"],
        [300,600,100.5,105,100.25,104,600,"BEFORE_OPEN"],
        [600,900,104,105,103,104,900,"BEFORE_OPEN"]
      ]
    },
    "P04": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,103,104,99.5,101,300,"UNKNOWN_OPEN"],
        [300,600,100.5,105,100.25,104,600,"BEFORE_OPEN"],
        [600,900,104,105,103,104,900,"BEFORE_OPEN"]
      ]
    },
    "P05": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,103,104,99.5,101,603,"AFTER_OPEN"],
        [300,600,100.5,105,100.25,104,601,"AFTER_OPEN"],
        [600,900,104,105,103,104,900,"BEFORE_OPEN"]
      ]
    },
    "P06": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,103,104,99.5,101,300,"BEFORE_OPEN"],
        [300,600,102,103,100.5,101,600,"BEFORE_OPEN"],
        [600,900,100.5,104,99.25,103,900,"BEFORE_OPEN"]
      ]
    },
    "P07": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,101,103,98,98.5,300,"BEFORE_OPEN"],
        [300,600,98,104,97.5,102,600,"BEFORE_OPEN"],
        [600,900,102,104,101,103,900,"BEFORE_OPEN"]
      ]
    },
    "P08": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,103,104,99.5,101,300,"BEFORE_OPEN"],
        [300,600,100.5,105,100.25,104,931,"AFTER_OPEN"],
        [600,900,104,105,103,104,900,"BEFORE_OPEN"]
      ]
    },
    "P09": {
      "annotation_receipt": 120,
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,100.5,105,99.5,104,300,"BEFORE_OPEN"],
        [300,600,104,105,103,104,600,"BEFORE_OPEN"],
        [600,900,104,104.25,102.5,103,900,"BEFORE_OPEN"]
      ]
    },
    "P10": {
      "bars": [
        [-300,0,100.75,101.25,100.25,100.5,0,"BEFORE_OPEN"],
        [0,300,100.25,103,98,101,300,"BEFORE_OPEN"],
        [300,600,101,103,100.5,101,600,"BEFORE_OPEN"],
        [600,900,101,102,100.25,101,900,"BEFORE_OPEN"]
      ],
      "tape": {"receipt": 300, "bar_open": 0, "prices": [[0,100.25],[70,103],[140,98],[299,101]]}
    },
    "P11": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,100.5,105,99.5,104,300,"BEFORE_OPEN"],
        [300,600,103.5,104,99.75,102,600,"BEFORE_OPEN"],
        [600,900,101.5,105,100.5,104,900,"BEFORE_OPEN"]
      ]
    },
    "P12": {
      "bars": [
        [-300,0,103,104,100.75,101,0,"BEFORE_OPEN"],
        [0,300,100.5,105,99.5,104,300,"BEFORE_OPEN"],
        [300,600,104,105,103,104,600,"BEFORE_OPEN"],
        [600,900,104,104.25,102.5,103,900,"BEFORE_OPEN"]
      ],
      "revision": [0,300,100.5,105,100.25,104,602,"AFTER_OPEN"]
    }
  }
}
~~~

The payload contains 48 base 5m bars, one later final-bar version, 12 instances of a 1H context candle, 12 context/zone annotations, and one constructed four-observation tape. P02 has a reflected directional comparison. The shared schedule gives 108 numerical prefixes. The three source packets are separate because none includes the raw timed 1H/5m evidence required for historical adjudication.
