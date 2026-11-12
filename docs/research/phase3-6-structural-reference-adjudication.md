# Phase 3.6 — Falsification results and implementation decision

**Classification:** READY FOR BOUNDED IMPLEMENTATION PROPOSAL. The proposal is for a manual-reference evidence panel. Automated swing significance, regime assignment and BOS/CHoCH remain open. The [original paper plan](../implementation/phase3-6-m01-structural-reference-readiness.md) is preserved. This adjudication qualifies its assumptions via the [source and event contract](phase3-6-structural-reference-contract.md).

## Evidence and execution

Rendered and inspected original PDF pp. 6, 9–10, 14–16, 25. Used complete constructed OHLC and modeled delivery times for the pivot and arming cases. Role/regime inputs explicitly supplied to the R1 model isolate arming from regime selection. Some ordering fixtures supply frozen swing records directly. They do not assert a generated market history. No Coach screenshot candles, prospective annotations, physical trades or native receipt times were reconstructed.

The [fixture file](../../research/phase3_6/test_reference_model.py) pins hand-calculated outputs independently of the [Python model](../../research/phase3_6/reference_model.py). An independent review here means challenging the prior proposal. One model authored the fixture expectations and code, with no second human or blind reviewer. Inputs are closed 5m integer-tick bars for one declared market and scale, with nominal time in minutes UTC or minutes from a fictional start. Ordered batches are explicitly provided by fixtures. The harness is intentionally limited to one reference stream at a time. Multi-reference arbitration, raw source revisions and provisional leg replacement after a reference is frozen are specified constraints for later work, outside these executed checks.

Run from repository root with Python 3.10+:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s research/phase3_6 -p 'test_*.py' -v
```

**VALIDATED within this finite suite:** 21/21 Python tests passed. F01–F14 each have one named check, six counterexamples are F15–F20, and one additional check compares S0/S1 under several windows. Subtests are included in those 21. The prior 55/55 native-independent v0.1.3 checks were read back from GitHub Actions job `131296530681` on [run 43251028044](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43251028044). They were not rerun. The new suite did not execute the existing Pine or perform a market backtest.

## Original cases re-adjudicated

| Case | Correction or clarified input | Pinned outcome |
| --- | --- | --- |
| F01 | Original exact OHLC and 10:25 cutoff retained. The center H112 and L95 strictly exceed the two-side extrema. | Pending before 10:25, both observations at 10:25 for one origin, no ordering or structural regime. |
| F02 | Equal 10:05 high 112 invalidates the high side only. Mirrored a low tie. | Low-only at original high tie, high-only at mirrored low tie. |
| F03 | Omitted 10:15 and supplied an actual 10:25 replacement bar. Also checked invalid, nonfinal and duplicate evidence. | Gap or invalid window is INSUFFICIENT. No “next two available rows” substitution. |
| F04 | Qualified pair without a second high or low. | UNKNOWN regime and no assigned structural role. |
| F05 | Full pivot and post-confirmation OHLC below. Explicit final 10:10 close remains 107. UP role is externally available only at 10:10. | A prebreached, B reset pending, history veto policy blocks. Only B emits on the tested later re-cross. |
| F06 | Same pivot and 10:05 excursion. 10:10 close is 105 and the 10:10–15 bar is eligible but closes at 105. | A/B arm at the 10:10 boundary and first emit at 10:20. Complete-history veto detects 10:05 and suppresses. No backdating under any policy. |
| F07 | Added anchored role alias and a later reset/re-cross. The new role does not change the semantic anchor. | One event under the original stream, none under the alias when consumption is supplied. |
| F08 | H108/C105 versus H108/C107, same known predecessor below 106 and identical valid O/L. | First is wick-only. Second records a closed cross and wick test. No fill evidence. |
| F09 | Compare the identical crossing candle with regime available at its open boundary or only at its close. | First can qualify. Second cannot qualify that bar and reports prebreach for A. B first qualifies only after distinct return and re-cross. |
| F10 | Down/LH and mirrored up/HL possible shifts. Mirror also checks downward continuation in established DOWN. | Both CHoCH candidates enter POSSIBLE_SHIFT. No reverse-regime or trade assertion. |
| F11 | Later 1H contradiction represented as external retirement after a previously frozen 5m decision. | Earlier decision is unchanged, future structural evaluation stops. This fixture does not test native HTF mapping or Lesson 08 reassessment. |
| F12 | Change venue, product, price basis or TF, or move a manual declaration's known-at after the claimed cutoff. | Provenance mismatch is INSUFFICIENT. Late declaration is WAIT at the earlier cutoff. |
| F13 | Structural event coexists with missing pre-known zone/contact, or with no closed reaction after contact. | Lesson 08 remains WAIT_ZONE or WAIT_REACTION. This is an independent interface contract, not execution of Lesson 08 source. |
| F14 | Constructed ordered prefix L90/H105/L95/H111, then H104 with no intervening admitted low. Also checked a low-side mirror. | Quarantine leaves UNKNOWN. More-extreme compression retains H111 and UP. Using the latest H104 would make the signs mixed and erase that regime even though both observations are locally valid. |

### F05/F06 common OHLC and policy difference

| Opens UTC | O | H | L | C at next boundary |
| --- | ---: | ---: | ---: | ---: |
| 09:35 | 101 | 103 | 100 | 102 |
| 09:40 | 102 | 104 | 101 | 103 |
| 09:45 | 103 | 106 | 102 | 104 |
| 09:50 | 104 | 105 | 101 | 103 |
| 09:55 | 103 | 105 | 102 | 104 |
| 10:00 | 104 | 108 | 103 | 107 |
| 10:05 F05 | 107 | 108 | 105 | 107 |
| 10:05 F06 | 107 | 108 | 104 | 105 |
| 10:10 | 106 | 107 | 104 | 105 |
| 10:15 | 105 | 109 | 104 | 108 |

At 10:00, the high at 09:45 is strictly greater than the two left and two right highs (103, 104, 105, 105). The first C107 is at 10:05 after that window. The same externally supplied UP/HH premise is available at 10:10 for all arming comparators. It is a synthetic dependency and does not follow from one confirmed high. R1-C can supply that declaration without changing the results of A, B or history veto. Native ordering at the shared opening/closing wall-clock remains unverified.

| Case | R1-A latest close | R1-B reset and re-cross | Complete-history veto |
| --- | --- | --- | --- |
| F05, still beyond at 10:10 | Block this anchor | Reset at 10:15, first eligible cross observed at 10:20 | Block |
| F06, already returned by 10:10 | Arm at 10:10, first eligible cross observed at 10:20 | Same as A | Block on earlier 10:05 close |
| F18, pre-arm 10:05 evidence missing, independently valid anchor/role and 10:10 predecessor | Arm at 10:10, first eligible cross at 10:20 | Same arming under its latest-close requirement | INSUFFICIENT |

On F06 the history veto rejects a source-compatible continuation observation without a demonstrated advantage. The price did make a fresh cross after a distinct return, and the Coach PDF prescribes no complete-history veto. Source compatibility in this example is conditional on the analyst's choice of reference. F05 makes the complementary case for testing B: a clean later reset can matter, but reuse of the old unconsumed level could be stale. No case resolves which behavior improves structure identification out of sample.

### Added counterexamples

| Case | Pinned result and reason |
| --- | --- |
| F15 late left-window evidence | Window ends 10:00 but the 09:35 bar becomes available only at 10:03. Pivot confirmed then, not at 10:00. No 10:05 break classification from late arming. |
| F16 equality and buffer | With L106, closes 106, 107, 108. First event on 107 with buffer 0, on 108 with buffer 1. Low threshold must remain positive. |
| F17 batch, late origin, gap | Same received batch with distinct known origins can be sorted when evidence is complete. An older-origin record delivered after release of a later origin cannot splice backward. Clean post-gap candidates start a new segment. |
| F18 missing and late evidence | Distinguish a missing older pre-arm close for history veto from a missing immediate predecessor for any fresh cross. Delayed data does not revise an earlier frame. |
| F19 two wicks | H108/L94 around references 106 and 101, C104. Both wick tests are geometrically possible, with no closed crossing or deducible order. |
| F20 invalid original counterexample form | Replacing the last required right bar with H108/C107 eliminates the candidate high 106. This reproduces the earlier AUD-C01 mathematical rejection, not the late-arming case. |

## Same-prefix model challenge

An artificial 5m tape uses O=C, H=C+1 and L=C−1 with the exact closes `104, 103, 100, 103, 110, 107, 105, 108, 107, 106, 107, 112, 109, 108, 109`, beginning at minute 0. At minute 65, the declared coarse S0 annotation selects L99@10, H111@20, L104@30, H113@55. It is a controlled comparison annotation with modeled availability, inspired by the qualitative source zigzags. It is neither a blinded verdict nor a Coach screenshot digitization.

| Candidate | Result on the common tape |
| --- | --- |
| S0 | UP at minute 65 by the declared manual scale and role. |
| S1 1/1 | UP at 65. Agreement on regime does not by itself imply agreement on protected reference. |
| S1 2/2 | UNKNOWN at 65: local H109@35 and L105@45 enter the sequence, while H113@55 still needs its second right bar. UP at 70, with L105 instead of manual L104 as the latest low. |
| S1 3/3 | UNKNOWN even at 75: wider windows discard these lows and the first low lacks its required left history. Changing left/right counts changed both delay and which points were accepted. |
| S2, hand calculation | Seed an upswing after close100 at minute 15. A three-tick reversal confirms peak close110 at minute 30 and peak close112 at minute 65, whereas five ticks confirms the first at 35 and leaves the second pending at 65. This close model supplies turning candidates with different prices and clocks from H/L observations. |
| S3, hand calculation | With N=3, close110 at minute 25 breaks prior highs max104 while no four-swing regime is established. The rolling rule measures local breakout only. |

The S1 result falsifies the inference that successful strict-fractal detection is sufficient to recover the analyst's scale or protected reference. A narrower window can seem better on delay while selecting a different structure. The wider window also illustrates left-history truncation, which a fair future calibration must separate from true scale disagreement. This tape proves possible disagreement and parameter sensitivity. It supplies no comparative accuracy rate.

Another ordering hazard arises if a previous H105 is treated as structurally eligible only when a new H110 later confirms. An intervening C108 on or before the H110 origin is already beyond 105. The later HH label cannot qualify that earlier crossing, even though the static price plot looks like a clean BOS. The same risk applies when a manual input is adjusted after looking at the whole chart or when a chart refresh changes the data start or revised bars.

## Bounded follow-up proposal

**Recommended baseline.** Collect prospective, versioned S0 declarations of one reference and its prior regime, use the frozen R1-A closed-cross policy for the first evidence comparison, retain R1-B as the principal stale-anchor/recovery comparator and complete-history veto as a coverage-sensitive check. Use S1 quarantine for deterministic comparison, compression as a challenge, S2 as an amplitude challenger, and S3 as a negative control. No window, buffer, expiry, replacement, protected-swing rule or automated regime algorithm is selected for production.

**Smallest separate native proposal.** If authorized later, put one optional read-only row behind a research toggle on the qualified standard 5m chart. Accept one manual reference with exact source identity, tick price, origin, role, prior regime, revision and modeled as-of time. Read only the adjacent final bars and display observation provenance, arming status and first eligible closed-cross cutoff. Keep one bounded reference and one decision marker placed at the decision cutoff. Never draw a break at the pivot origin. Clearly mark retrospective reconstruction, UNKNOWN for receipt-order-dependent evidence and a wick-only diagnostic if included. Keep build identity, Lesson 08 calculations and current M01 probe isolated. Leave auto-swing detection, autonomous BOS/CHoCH labeling, HTF adoption, alerts and entry logic outside this proposal.

**Native acceptance before a compatibility claim.** Verify exact build and input manifests on `BINANCE:PAXGUSDT` Spot standard 5m. Pin origin, manual known-at, bar intervals and source version, then exercise same-boundary arming, forming-to-final behavior, late declaration, missing predecessor, equality, wick-only, one-time consumption, and the distinct F05/F06 outcomes in an independent oracle. Compare all existing Lesson 08 and M01 outputs at identical cutoffs with the diagnostic OFF/ON. Capture one genuine live closed decision under the exact candidate and inputs, then compare reload and saved-source restoration separately. A modeled historical reconstruction and a native observation have separate evidence records. [TradingView bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/) · [TradingView repainting, dataset changes and drawing in the past](https://www.tradingview.com/pine-script-docs/concepts/repainting/)

**Strongest objection.** A new chart row could lend visual authority to a manually chosen level without resolving source-consistent swing significance. A timestamped external S0 annotation log is cheaper to start and can validate reviewer agreement before any Pine changes. If reviewers cannot independently agree on scale and protected role using frozen prefixes, or the one-row diagnostic does not improve capture fidelity, keep the annotation log and defer automated structure. If the reviewers agree but S1 misses eligible references or fires materially later, test S2 at predeclared reversal distances and compare coverage/delay without selecting on returns.

| Gate | Outcome |
| --- | --- |
| Coach conceptual traceability and original figure review | PASS within cited pages |
| F01–F20 and constructed S0/S1 finite deterministic results | PASS, 21/21 Python checks |
| Source-faithful automated swing/role selection, scale and production R1 choice | INSUFFICIENT |
| Independent prospective analyst annotations and empirically discriminating coverage | NOT RUN |
| Phase 3.6 native Pine, realtime receipt, multi-reference and chart persistence | NOT RUN |
| Trading performance | NOT RUN, outside this research |
