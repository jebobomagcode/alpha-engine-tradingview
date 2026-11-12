# Phase 3.2 — saved-script cleanup and persistence interruption handoff

**Date:** 2026-11-12, Asia/Manila  
**Repository:** `jebobomagcode/alpha-engine-tradingview` ONLY  
**Starting verified main:** `534aa6945095b090ee85d0051257f571a46f4141`  
**Accepted source:** [Pine v0.1.1](../../pine/lesson08-diagnostic.pine); build `L08-0.1.1-7fbb3eb381b6`  
**Prior native acceptance:** [Phase 3.1](phase3-lesson08-diagnostic.md#phase-31--v011-build-identity-and-lifecycle-12-november-2026)  
**Status:** IN PROGRESS. This entry records an interruption, not a successful private save.

## Owner authorization and scope

The owner explicitly authorized permanent deletion of **all previously saved Pine scripts owned by their TradingView account**, solely to make its Basic-plan saved-script slot available for the independent Alpha Engine TradingView diagnostic. This was an explicit narrow exception to the otherwise strict prior-project isolation rule. No earlier GitHub repository, source, website, or external asset may be accessed or modified. This permission was limited to the TradingView saved-script inventory and, if needed, obsolete diagnostic chart instances. It did not authorize public publication, buying a plan, trades, strategies, or expanding Pine behavior.

## Evidence handed off from interrupted Work session

The owner provided two screenshots of the Work conversation:

- Work reported an inventory of **one** pre-existing saved script and independently requested item-specific irreversible deletion confirmation.
- The owner replied **"i confirm"** to that item-specific deletion request.
- Work subsequently reported **"The confirmed script is gone, and the saved-script list stayed empty after a browser refresh."** It then stated its intention to save the exact v0.1.1 draft privately, reopen it, and verify saved bytes.
- Work stated that the v0.1.1 editor source matched GitHub byte-for-byte and that 21 local checks passed. These repeat the accepted Phase 3.1 source/test status; this handoff did not independently re-run those tests.
- The screenshots show that the Work usage limit interrupted continuation. They do **not** show a successful private save, saved-script reopen, durable chart restoration, or an updated GitHub commit.

These are **owner-supplied screenshots containing Work's reported observations**, not a fresh independent TradingView inventory read. Do not promote the deletion or the save to independently verified platform acceptance based on this handoff alone.

## Gate ledger at interruption

| Gate | Disposition | Basis |
| --- | --- | --- |
| Owner consent to delete the one identified old saved script | REPORTED CONFIRMED | Specific owner confirmation in screenshot, consistent with earlier broad authorization. |
| Removal of the old script | REPORTED COMPLETE, NOT INDEPENDENTLY RECHECKED HERE | Work's post-action screenshot text. |
| Empty saved-script inventory after refresh | REPORTED COMPLETE, NOT INDEPENDENTLY RECHECKED HERE | Work's post-refresh screenshot text. |
| Exact v0.1.1 repository source and release ID | PREVIOUSLY PASS (PHASE 3.1) | Pine source and 21 tests recorded in prior acceptance; no new source revision. |
| Private save of Alpha Engine v0.1.1 | NOT VERIFIED | No final successful-save observation supplied. |
| Saved source reopen and exact-byte readback | NOT RUN / NOT EVIDENCED | Work had announced it as its next action. |
| Saved instance chart reload and exact-build/input parity | NOT RUN / NOT EVIDENCED | Historical v0.1.0 draft restoration failure remains relevant. |
| Realtime closed-bar / live hour-rollover from v0.1.1 | PREVIOUSLY PASS (PHASE 3.1) | Keep previous scope, no new test attempted here. |

## Minimal next acceptance actions

1. Using a supported **interactive TradingView browser**, inspect **Open my script** again; independently confirm the previous inventory is empty. Do not re-open or explore deleted legacy content.
2. On standard `BINANCE:PAXGUSDT` Spot **5m**, load the exact [authorized Pine source](../../pine/lesson08-diagnostic.pine). Do not modify it to avoid chasing a moving build.
3. Confirm the editor bytes match the repository source SHA-256 **`1bb0613634f6cd941853552aaa5bab605b2296a541007ffb6c70f24f20b73c91`** and panel build ID **`L08-0.1.1-7fbb3eb381b6`**, separately.
4. Save it **privately** as the sole saved script; require an actual save-success result. If a platform confirmation is necessary, handle it through supported user interaction.
5. Reopen the script from **Open my script** and re-check complete saved-source bytes. Editor persistence alone is not proof of saved-source persistence.
6. Add/load the **saved** instance on the qualified chart, confirm build ID and all relevant setup inputs, record a closed-bar state, then refresh. Compare the same identifiable saved build after reload.
7. Record exact PASS/FAIL/INSUFFICIENT/NOT RUN for editor, saved source, compiled chart, browser reload, input identity and any genuine realtime observation. Preserve previous draft-restore failures.
8. Update [Phase 3 acceptance](phase3-lesson08-diagnostic.md), [STATE](../STATE.md), [DECISIONS](../DECISIONS.md) and [RECOVERY](../RECOVERY.md) **only after** actual new evidence; verify the GitHub commit/readback.

## Owner-assisted TradingView verification after Work interruption — 2026-11-12, approximately 16:12–16:29 PHT

The owner supplied further screenshots from their own authenticated TradingView browser. Unlike the earlier Work-only report, these show the current account UI, but they are **visual evidence**, not full-source byte attestations.

- **Saved-script presence:** In *Indicators → My scripts*, the single visible saved entry is named `Alpha Engine TradingView — Lesson 08 Diagnostic`. A subsequently opened named Pine Editor document showed the expected v0.1.1 indicator header, `SYMBOL = "BINANCE:PAXGUSDT"` and `BUILD_ID = "L08-0.1.1-7fbb3eb381b6"`. The previous screenshot with `Untitled script` was a separate default editor document and is not evidence that the saved source is a template. Full editor contents were **not** extracted or byte-compared during this user-assisted step.
- **Compiled chart and initial refresh:** The chart panel displayed the exact v0.1.1 build. One owner hard refresh restored the saved v0.1.1 build but also restored the **wrong** `PAXGUSDT.P` perpetual market, so the explicit `INSUFFICIENT · chart identity` guard was correctly shown. The chart's instrument restoration is a separate layout/state concern from the Pine source.
- **Qualified spot chart:** After selecting the non-`.P` Binance PAXG/USDT **Spot** 5m chart, the panel displayed `EXPIRED · exclusive cutoff`, geometric overlap with physical touch unknown, and the unchanged v0.1.1 build. That terminal result matches the old declared expiry in the saved chart inputs; it is not evidence of an indicator error.
- **Latest refresh report:** The owner then returned screenshots responding to the instructed layout-save and refresh test: the chart again displayed `PAX Gold / TetherUS · 5 · Binance` (Spot, no `.P`) with the same `L08-0.1.1-7fbb3eb381b6` build. The named saved script remained accessible in Pine Editor, and the beginning of its source still matched the expected release header, build constant and exact symbol. Screenshots do not independently establish that every source byte or all 16 original input values were preserved, nor that chart layout was durably saved.
- **Scope:** These are owner-supplied screenshots. No direct browser-control action, full script export, broker activity, market trade, or new Pine release was performed by this conversation.

| Phase 3.2 acceptance gate | Updated result | Bound of support |
| --- | --- | --- |
| Named private saved-script inventory entry | **PASS (visual inventory)** | Entry visible under My scripts; count/ownership of any hidden entries not independently inventoried here. |
| Saved Pine Editor script reopen | **PASS (visual)** | Named document and expected v0.1.1 source header visible. |
| Expected visible build marker after hard refresh | **PASS (visual)** | Exact build ID displayed on chart. |
| Correct Spot chart after user's subsequent refresh | **PASS (visual, reported refresh)** | Chart label PAX Gold / TetherUS, 5m, Binance, no perpetual marker. |
| Saved source full SHA-256 / byte equality | **NOT VERIFIED** | Requires complete saved-source copy/export rather than screenshots of the first lines. |
| All 16 saved setup inputs and full state parity | **NOT VERIFIED** | No paired full settings and exact state capture across refresh. |
| TradingView native venue receipt, physical touch, execution | **INSUFFICIENT** | The diagnostic remains geometric-only. |

**Next:** Have the owner export or copy the complete named saved-script text (as `.pine` or plain text) and compare its SHA-256 against the authoritative repository source hash `1bb0613634f6cd941853552aaa5bab605b2296a541007ffb6c70f24f20b73c91`. A copied source may contain platform line-ending changes; report and compare raw and LF-normalized bytes separately if needed. If exact source matches, record the saved-source gate PASS. Preserve the v0.1.0 draft-restore failure as historical; do not change Pine logic merely to improve a document-level acceptance gate.

## Uploaded complete Pine editor export — exact-source check, 2026-11-12

After the user reopened the named saved script in Pine Editor, they followed the requested complete-copy workflow and uploaded `alpha-engine-v0.1.1.pine.txt` to this conversation. The uploaded file was read byte-for-byte in the local analysis container and compared with the version-controlled v0.1.1 source.

| Measurement | Observed value |
| --- | --- |
| Original uploaded byte length | **11,351** |
| Original uploaded SHA-256 | `f38ac37c9b9f89400396c7d41155fa8cf38545af8878065740adbb05b04337e1` |
| Original line endings | **187 CRLF** terminators; no bare CR, no BOM |
| Canonical LF-normalized length | **11,164 bytes** |
| Canonical LF-normalized SHA-256 | `1bb0613634f6cd941853552aaa5bab605b2296a541007ffb6c70f24f20b73c91` |
| Canonical Git blob SHA-1 (with Git blob header) | `80cd5291507fcbb8c919ed02c0f56fb921299b98` |
| Current repository Pine blob | `80cd5291507fcbb8c919ed02c0f56fb921299b98` |
| Embedded release identifier | `L08-0.1.1-7fbb3eb381b6` |

**Result — PASS (saved editor export, canonical content equality):** The LF-normalized complete uploaded source matches both the accepted repository SHA-256 and the exact Git blob identity. The sole difference is Windows CRLF versus repository LF serialization. This resolves the previous full-source content-identity gap for the complete owner-exported editor text. The comparison is **not** an independent TradingView API fetch or cryptographic digest of TradingView's compiled artifact; provenance from the saved-script editor is based on the owner's immediately preceding screenshots and upload.

**Remaining checkpoint:** The user's screenshots visually support the correct compiled v0.1.1 build after reload on the qualified Spot 5m chart. A screenshot-level build marker and complete saved editor export are stronger than header inspection, but no paired before/after inspection of **all 16 setup input values** was supplied. Treat that exact-input parity as **NOT VERIFIED**. Native receipt sequence, physical touch, fills and financial performance remain outside scope.

This upload must **not** replace or modify the checked-in Pine source; its canonical content is already identical.

## Owner-assisted paired Inputs screenshots — 2026-11-12, 16:36 PHT

The owner supplied **two** TradingView screenshot captures of the `Alpha Engine | Lesson 08 Research v0.1.1` **Inputs** dialog, from approximately **16:36:19** and **16:36:51 PHT**, in response to the request for a before/after reload settings check. Both screenshots show the same values for **eight of the twelve Pine input declarations**, represented by **twelve visible UI controls** because four datetime inputs have two controls each:

| Visible Pine input | First screenshot | Second screenshot | Visual parity |
| --- | --- | --- | --- |
| Enable declared setup | Checked | Checked | MATCH |
| Setup version | 33 | 33 | MATCH |
| Bullish context reference · 1H close | 2026-11-12 14:00 | 2026-11-12 14:00 | MATCH |
| Context available at · declared | 2026-11-12 14:55 | 2026-11-12 14:55 | MATCH |
| Zone available at · declared | 2026-11-12 14:55 | 2026-11-12 14:55 | MATCH |
| Exclusive expiry | 2026-11-12 15:20 | 2026-11-12 15:20 | MATCH |
| Support floor | 3900 | 3900 | MATCH |
| Support ceiling | 4050 | 4050 | MATCH |

**Observation — PASS for visible-field equality.** Both screenshots show the named v0.1.1 indicator settings, qualified non-perpetual `PAXGUSDT` chart context and consistent values for the eight visible Pine inputs. The owner was following a requested reload check, but the screenshots **do not themselves prove the precise sequence of a browser refresh between captures**, and no separate browser reload event was observed by this chat. Other earlier screenshots established a same-build chart restoration after a reported hard refresh.

**Remaining exact-input gate — INSUFFICIENT for all-input parity:** Four Pine input declarations were below the visible scroll area in both screenshots: `Show nominal geometry`, `Entry reference`, `Stop reference` and `Target reference`. These must be checked after scrolling inside the Inputs dialog. The separately accepted Phase 3.1 manifest listed nominal geometry disabled and the three optional prices zero, but these current screenshots do not verify their persisted values. Do not describe the eight checked inputs as all sixteen UI controls or all twelve Pine inputs. Timezone interpretation is based on the earlier PHT input manifest; both screenshots display the same literal date/time.

A prior complete Pine Editor upload already established **full source equality** after CRLF→LF normalization. This update changes neither Pine code nor acceptance of live venue receipt, physical-touch or execution outcomes.

## Non-goals

No new Pine features or changed v0.1.1 algorithm. No strategy, alerts, backtesting, trading or publication. No cross-project access. The account's **one saved script** cap is not lifted by deleting older scripts; maintain this one saved slot for the current Alpha Engine diagnostic.

**Recovery point:** Complete named saved-script editor source identity is now PASS after CRLF→LF normalization, and the expected chart build survived hard refresh on the correct Spot instrument. The remaining optional exact acceptance item is a paired full 16-input settings readback; do not change/rebuild source merely for that. Do not repeat completed studies.
