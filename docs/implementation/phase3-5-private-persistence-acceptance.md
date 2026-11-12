# Phase 3.5 private TradingView persistence evidence

**Observed** 2026-11-12, Asia/Manila. **Scope** the existing named private script and its existing chart layout. Draft PR #1 remains subject to owner evidence review.

## Authorization and source provenance

The owner explicitly approved both preserving the observed native v0.1.2 ending as the rollback and replacing the existing named private **Alpha Engine TradingView — Lesson 08 Diagnostic** after exact v0.1.3 editor copy-back.

- **Baseline v0.1.2:** chart build `L08-0.1.2-3b9eb3065294`, named library version 2.0. The preflight captured all 19 displayed input values, layout identity and the qualified standard `BINANCE:PAXGUSDT` Spot 5m chart. The raw native copy-back matched the prior accepted owner export, SHA-256 `549b6af465c03ac53ed04d0d98e331025a91fd4154b6104abb2e7af7524849fc`, including after a separate read-only baseline reload. The observed native ending and all 19 inputs are in the owner-private backup. [Earlier v0.1.2 source evidence](phase3-3-m01-pivot-probe.md#phase-33--complete-v012-owner-exported-pine-source-comparison-2026-11-12)
- **Preflight discrepancy:** after CRLF-to-LF conversion, the v0.1.2 native copy is the canonical source with one terminal LF absent. Strict equality after CRLF conversion alone failed. The private backup preserves the observed native bytes. The canonical Git rollback remains at `3458ff6854e9c349aef10a30e487a908a3648441`, blob `dd1691072e3f81d18217c50efa87c4d6fa6b43e3`. The v0.1.1 rollback remains at `74e7814e308a40f769d9b57607ebde145f492b8d`. The approved ending exception applies to the old private rollback.
- **Verified candidate:** PR head `681f4e4eafc61376d4939c03d76a5414940e6fc0`, Pine blob `218e54cf573d6dfcc7b3306d22a0a34f966db160`, SHA-256 `8d168c72506b8bc6b4f1595598d8743070675509e79dcee6574dddacc586fe4a`, build `L08-0.1.3-3e3d909ba9f5`. Full editor copy-back before save and after chart reload matched after CRLF-to-LF conversion only, with the terminal LF present. The personal script library reported the same named entry as version **3.0**, updated at 23:22 PHT.

## Native observations

The private script save and the separate chart layout save were both performed. Before touching settings after the first browser tab reload, the existing layout displayed v0.1.3, standard candles, `BINANCE:PAXGUSDT` Spot 5m and the original disabled setup. The 15:20 UTC closed-bar panel matched before and after reload, including all three M01 rows off and the 15:00 UTC 1H reference. All 19 original controls matched in the reopened Inputs dialog.

For revision 31, only the M01 checkbox changed between the 23:26:42 and 23:27:11 PHT captures. Both panels showed the 15:25 UTC cutoff, build v0.1.3, the 15:00 UTC 1H reference at 3870.73, `REASSESS · episode ended`, contact at Nov 11 14:50 UTC and both R2 records at 15:00 UTC. Setup identity, nominal risk, strict receipt uncertainty and geometric-touch evidence matched. The OFF panel showed all three M01 rows off. The ON panel showed high 3907.72 known 14:35, low 3883.33 known 14:25 and `VALID · no new pivot`. Lesson 08 events in this fixture are retrospective reconstructions.

The non-default revision-31 ON layout was saved for a second persistence check. At 23:29:30 PHT, the live panel still showed the 15:25 UTC cutoff. The live panel advanced to 15:30 UTC by 23:30:04 PHT. After a normal browser tab reload, the restored chart at 23:30:13 PHT showed that same 15:30 cutoff, build, Lesson 08 fields, M01 evidence status and retained high/low. All 19 non-default input controls matched, including four dates and four times, support bounds, configured setup, and M01 ON at 2/2. This observes a live 5m close and then closed-state reconstruction across reload. There was no new M01 pivot at that close. It does not establish exchange receipt order or actual physical touch.

The owner’s original input manifest was subsequently restored, separately saved to the layout, and read back. The final private chart uses v0.1.3 with setup disabled, nominal geometry disabled and M01 OFF. The revision-31 fixture was temporary.

### Owner-assisted cache-bypassing refresh

After the original input manifest was restored and saved at 23:31:38 PHT, the owner completed Chrome Ctrl+Shift+R on the existing chart. The native undo marker present before the handoff was absent afterward. At 23:34:26 PHT the saved layout had restored without any indicator or setting changes. The chart showed the same 15:30 UTC cutoff, the v0.1.3 build, the qualified Spot 5m chart and the original disabled-setup panel with all three M01 rows off. All 19 original controls matched when reopened. The named editor copy matched canonical v0.1.3 after CRLF-to-LF conversion only, retained the terminal LF and matched the raw copy from the prior normal reload.

## Gate ledger

| Gate | Outcome | Evidence |
| --- | --- | --- |
| Exact native v0.1.2 backup and original layout/controls | **PASS** | Prior accepted raw digest matched, with baseline build and all 19 inputs captured. |
| Preflight CRLF-only v0.1.2 comparison to canonical Git | **FAIL** | One terminal LF absent in the native copy. The owner accepted the exact observed raw backup as the rollback. |
| v0.1.3 source SHA-256, blob and build | **PASS** | Recomputed against Git and matched complete staged editor copy-back before Save Script. |
| Save into the existing private named entry | **PASS** | One matching entry, native version 3.0. |
| Separate chart layout save | **PASS** | Layout reported all changes saved. |
| Ordinary browser reload, restored build and qualified chart | **PASS** | Restored before settings or editor were opened. |
| Reopened saved editor exact source | **PASS** | CRLF-to-LF normalization only, terminal LF retained. |
| All 19 inputs on reload | **PASS** | Matched both the original manifest and a separate non-default revision-31 manifest. |
| Matched-cutoff M01 OFF/ON and original Lesson 08 fields | **PASS** | Same 15:25 UTC cutoff and identical other inputs. Revision-31 setup and R2 history reconstructed. |
| Sampled realtime closed state across ordinary reload | **PASS** | Same 15:30 UTC cutoff and panel after a genuine observed live cutoff advance. |
| Explicit cache-bypassing hard refresh | **PASS, owner-assisted** | The owner completed Ctrl+Shift+R. The native undo marker cleared and the same 15:30 UTC panel, saved build, 19 controls and exact named source were verified after restoration. Earlier connected-browser shortcut attempts did not navigate. |
| Venue receipt and physical touch | **INSUFFICIENT** | Chart confirmation and modeled geometric overlap are distinct from venue receipt and verified touch. |

There was no observed v0.1.3 source or layout restoration mismatch requiring rollback. See the [rollback procedure](phase3-5-test-hardening-and-persistence.md#final-owner-assisted-persistence-procedure) for later failures. The test and Pine files retain the exact verified identities from [CI run 43243497408](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43243497408). This checkpoint changes documentation only. The 55 tests were not rerun.
