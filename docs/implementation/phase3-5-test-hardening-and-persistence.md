# Phase 3.5 test hardening and owner-assisted persistence gate

**Recorded** 2026-11-12 (Asia/Manila) · **Repository** `jebobomagcode/alpha-engine-tradingview`

**Disposition: Ready for owner-assisted persistence acceptance.** Draft PR #1 contains the tested candidate. The private saved script remains v0.1.2. Candidate saved-source readback and matched reload are **NOT RUN**.

## Checkpoints and scope

| Item | Verified identity |
| --- | --- |
| Accepted GitHub `main` | `3458ff6854e9c349aef10a30e487a908a3648441` |
| Draft PR #1 | `feat/phase3-5-m01-validity-freshness-20261112`, reviewed starting head `51cf1a9fc94de1bb0f5693b6913b68102afe207a` |
| Test hardening commit | `227ef8d7f79198b54cb67661f2aa3cf8238ad666`, new `tests/test_phase3_5_m01_source.py` |
| Candidate Pine | v0.1.3, build `L08-0.1.3-3e3d909ba9f5`, Git blob `218e54cf573d6dfcc7b3306d22a0a34f966db160`, SHA-256 `8d168c72506b8bc6b4f1595598d8743070675509e79dcee6574dddacc586fe4a` |
| Private rollback baseline | v0.1.2, build `L08-0.1.2-3b9eb3065294`, Git blob `dd1691072e3f81d18217c50efa87c4d6fa6b43e3`, SHA-256 `a6e624777d792ec528389746da86d54bacc58f412d7ab8040c84fde325b78dd2` |
| Earlier rollback | v0.1.1 at `74e7814e308a40f769d9b57607ebde145f492b8d`, Git blob `80cd5291507fcbb8c919ed02c0f56fb921299b98` |

[Draft PR #1](https://github.com/jebobomagcode/alpha-engine-tradingview/pull/1) · [Independent audit at 016b2e5](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/016b2e5ccc8c28185557eabe85dd10dfa35be736/docs/audits/2026-11-12-phase3-5-independent-review.md)

## Actual test and mutation results

**55/55 PASS** locally on the intended source after isolated mutation trials. All 50 preexisting checks are intact. The 21 Lesson 08 checks read current source, the 13 Phase 3.3 and five Phase 3.4 checks use historical source pins, and the original 11 Phase 3.5 checks retain the independent Python model and source assertions. Five added checks exercise source-derived M01 functions and adapter behavior or inspect the table structure. [Test source](../../tests/test_phase3_5_m01_source.py)

The new adapter translates the checked-in `strictPivots` function, its actual call and tuple bindings, the guarded record updates, and the `M01 evidence` display expression. Explicit expected statuses and event tuples are authored from the fixtures. This lets a behaviorally defective Pine expression fail even when its expected text is still present.

| Mutation applied separately | Intended check failed |
| --- | --- |
| Replace `and low[offset] > 0` with `and (true or low[offset] > 0)` | Complete-window guard admitted zero and negative lows at all five positions. Positive controls continued to pass. |
| Exchange `VALID · new pivot` and `VALID · no new pivot` | The valid/no-event, high-only, low-only and dual-event expectations failed. The truth table also covers insufficient history, invalid evidence, OFF, wrong chart and precedence. |
| Set table height to 15 and retain row index 15 | The referenced indexes differed from the declared row range. The structural check also requires unique coverage, M01 rows and unchanged index pass-through to the cells. |

Ten additional isolated mutations were rejected: a center-only price guard, high-only event status, duplicate row, a removed M01 low row with compacted indexes, an added out-of-range row with a dynamic label, a shifted cell row, an ignored clock gap, a cleared retained high on invalidity, a forming-bar commit, and a high timestamp written to the low record. These bring the total to **13 rejected mutants**.

Mutation runs used a disposable detached worktree and a fresh Python process for each variant. Each changed Pine file had its test-only build digest recomputed by masking the build literal with `__BUILD__` and hashing the source. Every run executed 55 tests and reached its named semantic or structural failure with zero test errors. The source was restored between trials. For reproduction, apply the edits in the table one at a time in a disposable checkout, recalculate the digest, then run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Verified the actual Actions logs for the test commit. The push job ran on `227ef8d7f79198b54cb67661f2aa3cf8238ad666`. The PR job checked out GitHub's synthetic merge of that head into accepted main. Both ran **55 tests** with all five new checks passing. [Push run 43242802360](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43242802360) · [PR run 43242812102](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43242812102)

## Sequential recovery

The constructed OHLC stream omits the bar opening at minute 25. It contains 16 distinct closes per setting. The test feeds each prefix first as a forming bar and then as a confirmed close. Times are elapsed synthetic minutes and prices are fixture values.

| Cutoff (minutes) | 2 left / 2 right | 1 left / 2 right | Observed retained records |
| --- | --- | --- | --- |
| 5, 10, 15 | Insufficient | Insufficient | None |
| 20 | Insufficient | Valid, no event | None |
| 25 | Valid, dual event | Valid, dual event | High 110 and low 95. Both origin 10, known 25. |
| 30 | No bar | No bar | No evaluation |
| 35, 40, 45 | Invalid | Invalid | Both original records retained |
| 50 | Invalid | Valid, no event | Both original records retained |
| 55, 60, 65 | Valid, no event | Valid, no event | Both original records retained |
| 70 | Valid, new high | Valid, new high | High 120, origin 55, known 70. Original low retained. |
| 75, 80 | Valid, no event | Valid, no event | Both records retained |
| 85 | Valid, new low | Valid, new low | Low 100, origin 70, known 85. High 120 retained. |

Expected and observed statuses, event flags and stored price/origin/known triples matched at every close. Forming samples preserved the prior status and both records. The proof covers these fixture states and exact source fragments. It does not prove Pine's full runtime, sub-tick rounding, feed behavior, or reload persistence. The stored timestamps identify modeled candle opens and closes. Exchange receipt and physical touch remain unobserved.

## Source, methodology and prior native evidence

The test and documentation changes leave the exact candidate Pine bytes and build applicable to all earlier checks. Original Lesson 08 decisions, R2-B/R2-A, risk and receipt-uncertainty semantics retain the audited source identity. The original Coach PDF, all 26 PCSS units, CI workflow and rollback sources remain intact. The strict pivot continues to be an **INDEPENDENT_EXTENSION / EXPERIMENTAL** rule. [Lesson 08 source study](../lessons/08-trading-entry-workflow.md) · [Independent audit, methodology section](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/016b2e5ccc8c28185557eabe85dd10dfa35be736/docs/audits/2026-11-12-phase3-5-independent-review.md#e-lesson-08-compatibility-and-provenance)

Prior **PASS** evidence remains applicable to the exact v0.1.3 build: complete source copy-back in the temporary editor draft, native compile, standard `BINANCE:PAXGUSDT` Spot 5m chart, M01 OFF and valid statuses, one observed 14:25 UTC live close and bounded revision-31 Lesson 08 ON/OFF parity. Native malformed-window, short-history, unsupported-chart and hourly-rollover tests remain **NOT RUN**. Saved-source equality, full input persistence and same-build matched reload remain **NOT RUN**. [Independent audit, native verification](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/016b2e5ccc8c28185557eabe85dd10dfa35be736/docs/audits/2026-11-12-phase3-5-independent-review.md#f-native-tradingview-verification)

## Final owner-assisted persistence procedure

**The next owner action** is to explicitly authorize or perform the update of the existing named private `Alpha Engine TradingView — Lesson 08 Diagnostic` with the exact candidate after steps 1–2. The save occurs only at step 3. Use the private Pine **Save Script** operation. TradingView distinguishes a temporary draft created with **Add to chart** from **Save Script** in the personal script library. Chart layout saves separately restore the chart and its indicators/settings. [TradingView draft and script save](https://www.tradingview.com/support/solutions/43000711497-how-to-create-a-new-script/) · [TradingView layouts](https://www.tradingview.com/support/solutions/43000746975-tradingview-layouts-a-quick-guide/)

1. **Capture and back up.** In one chart tab, record the named private script, v0.1.2 build, chart layout, `BINANCE:PAXGUSDT` Spot identity, standard candles, 5m interval, chart timezone, last closed UTC cutoff, panel and all inputs. Reopen the named v0.1.2 script and keep a local full source copy plus the pinned rollback blob. Normalize CRLF to LF only and verify the full v0.1.2 SHA-256 above. Capture all 15 declarations, presented as 19 controls because each of the four datetimes has a date and a time field.
2. **Verify candidate bytes and manifest.** Use the exact PR Pine blob and expected build above. Paste the full source into the existing named script editor and copy it back before saving. Compare normalized bytes and SHA-256. Keep all final manifest values explicit, including the eight setup controls by declaration, four nominal-risk declarations and M01 enable/left/right. If using the pinned revision-31 reconstruction, record it as reconstructed history and restore the owner's original setup after the check. Use the candidate's intended M01 setting for the layout to be tested.
3. **Owner saves privately.** Use **Save Script** on the existing named script. After the chart displays the exact candidate build, confirm the intended values in Inputs and save the current chart layout separately. Capture the entire input manifest and panel after both saves. If the platform asks for a separate slot or the save is blocked, stop and record the exact prompt.
4. **Reload and verify restoration before touching the chart.** Hard-refresh the same chart and read the auto-restored symbol, product, candle type, interval, build, Inputs and panel before manually changing or re-adding anything. Then open the named saved script from the personal script library and copy all editor text back. Match its SHA-256 after CRLF-to-LF normalization. Verify all 19 controls against the recorded manifest using the same timezone or equivalent UTC values. An editor tab left open from the draft is insufficient evidence.
5. **Compare observable behavior.** Capture matching cutoff pairs with only the M01 toggle changed. OFF should show all three M01 rows off. ON should show the last evaluated closed-window status and retained pivots. Compare original Lesson 08 fields, setup/contact IDs, confirmed 1H reference, reason code, R2-B/R2-A history and nominal geometry. At revision 31 the earlier native checks showed `REASSESS`, geometric contact on Nov 11 14:50 UTC and both R2 records at 15:00 UTC. Use the same closed 5m cutoff for live before/after panel comparisons. If the cutoff rolls, repeat the pair or mark state parity **NOT RUN**. Report a historical reconstruction separately from a realtime-to-reload observation. If available, record a live confirmed transition before refresh and verify that same build, inputs and closed cutoff afterwards. An unobserved malformed, invalid or warm-up state remains **NOT RUN** natively.
6. **Handle failure and restore the original settings.** A source mismatch before save stops the operation. After a save or restore mismatch, record which step failed, capture the observed build/fields, and have the owner restore the verified v0.1.2 source into the same named script if a rollback is needed. Restore the input/layout snapshot, reload, and reverify source hash, build and inputs. If the platform blocks rollback, record the blocker without deleting a saved script. After a successful test, restore the owner's chosen input manifest, save that layout and confirm the resulting state.

**Record separate verdicts** for private save, exact saved-source readback, restored build, complete input parity, same-cutoff M01/lesson output parity, and realtime-to-reload parity. Attach timestamps and observed comparisons. Stop for owner review before promoting the draft PR.

For a reproducible enabled-setup comparison, revision 31 uses `configured=true`, revision 31, UTC anchor **2026-11-11 14:00**, context-known and zone-known **14:50**, expiry **15:15**, floor **4000** and ceiling **4008**. Nominal geometry is off and all three numeric risk inputs are zero. M01 uses 2 left and 2 right, with only the enable flag changing between the paired captures. The four Asia/Manila input times on November 11 are **22:00 / 22:50 / 22:50 / 23:15**. This manifest is a test fixture, separate from the owner's original chart settings.

## Review of remaining limitations

The checks are intentionally coupled to the small Pine fragment actually used. Unsupported syntax or a structural refactor requires reviewing the adapter. Independent expectations and known bad mutations give the checks a falsification target without a second implementation of the whole indicator. The visible status still reports the last evaluated close rather than feed freshness. Native observation and saved-instance recovery have their own evidence gates.
