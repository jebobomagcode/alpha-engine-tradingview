# Phase 3.5 — M01 data validation and evidence-status research candidate

**Date:** 2026-11-12 PHT · **Repository:** `jebobomagcode/alpha-engine-tradingview` only.  
**Starting accepted main:** `3458ff6854e9c349aef10a30e487a908a3648441`.  
**Candidate:** Pine v0.1.3, build `L08-0.1.3-3e3d909ba9f5`.  
**Scope:** Independent research-only M01 hardening; not Coach-specified pivot methodology, no trading signals.

## Purpose and changes

The Work resumption audit identified a demonstrable defect: the v0.1.2 strict pivot window checked bar availability and OHLC geometry but admitted nonpositive OHLC prices. This is inconsistent with the positive-price check used by the Lesson 08 Spot profile.

**Patch A — input validity:** All five (or more, if user changes L/R) bars forming an M01 candidate's complete confirmation window now require `low[offset] > 0`, in addition to the existing clock, OHLC availability, and geometry rules. All O/H/C prices are positive when positive low and the geometry inequalities hold. An invalid window cannot publish a new M01 pivot, regardless of the candidate's high/low relationship to adjacent bars. No modification to Lesson 08 eligibility.

**Patch B — evidence freshness as a separate reporting concern:** The M01 function additionally returns whether enough bars exist and whether the current completed window is valid. The chart stores one evidence label **only after a confirmed 5m close** and adds a new `M01 evidence` row:

- `Off · research` if pivot audit disabled.
- `INSUFFICIENT · chart identity` on wrong chart.
- `INSUFFICIENT · no closed 5m evaluation` until first eligible evaluation.
- `INSUFFICIENT · 5m history` if no complete L/R window exists.
- `INVALID · 5m OHLC/clock window` if the required window contains a bad price/clock/OHLC.
- `VALID · no new pivot` if current window is admissible but has no confirmed strict extremum.
- `VALID · new pivot` if the latest completed admissible window confirms an extremum.

Rows `M01 high` and `M01 low` intentionally **retain the last known historical pivot and its known-at timestamp** across later windows. That retained record is not proof of current evidence validity. The new row distinguishes the two meanings without erasing history. The evidence row cannot alter Lesson 08 decisions.

## Compatibility and evidence boundaries

- The original Coach methodology, all Lesson 08 original panel rows 0–12, risk display, 1H context, setup/contact IDs, R2-A/R2-B, expiry and REASSESS, and labeled effects remain unchanged.
- The M01 probe remains research-only, OFF by default, parameterized L/R; no BOS/CHoCH/alerts/strategy/forward performance claims.
- Earlier exact v0.1.2 Python tests and Phase 3.4 source isolation are pinned to the historical v0.1.2 commit, rather than weakening their acceptance requirements to refer to whichever version is current.
- New Phase 3.5 tests separately cover positive-price rejection, missing/invalid time/price evidence, valid-but-no-pivot, record retention after invalidity, exact source/build invariants, and all five frozen Binance PAXGUSDT positive-price pivot confirmations. This proves narrow Python-model and source invariants, **not native Pine compilation**.

## Validation gates

| Gate | Current |
| --- | --- |
| New v0.1.3 candidate committed to GitHub | PENDING |
| Historical 39 v0.1.2 checks | PENDING new CI |
| New independent M01 validity and freshness checks | PENDING new CI |
| Native TradingView compilation and panel evidence | NOT RUN |
| New build persistence in sole private saved script | NOT RUN — do not overwrite v0.1.2 prematurely |
| Realtime forming → close / receipt timing | NOT RUN |
| Trading performance or signal validation | OUT OF SCOPE |

**Deployment discipline:** v0.1.2 remains the single private saved TradingView script. Keep the v0.1.2 and v0.1.1 exact source history as rollback. Do not publish the Pine script publicly or change other projects.
