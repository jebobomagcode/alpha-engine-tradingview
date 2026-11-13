# Phase 3.6 next gate — v0.1.4 zone/reaction lifecycle controlled oracle

**Research only.** This increment does not change Pine, accepted TradingView private version 4, or GitHub `main`. The v0.1.4 native acceptance in [the previous release record](ai-only-integrated-candidate.md) remains valid **for its tested scope**. This note adds an independently testable *Python specification projection* for adversarial lifecycle cases; it does NOT execute Pine and does NOT claim Pine↔Python parity yet.

## Frozen contract, modeled 5m bars

- A candidate block or 3-bar gap is first usable on the **next** bar after it is known. A block's wrong-side close invalidates before same-bar overlap. Invalidated block status persists; a later fresh block requires a new identity. Geometric wick overlap is not physical contact, an order fill, or market performance.
- A gap is OPEN until a later geometric overlap makes it GEOMETRIC TEST. No separate permanent gap invalidation exists in this bounded v0.1.4 implementation; do not describe the gap model as a complete mitigation lifecycle.
- An eligible previous-open HL support can record a same-bar final engulf or optional wick rejection; a close through support invalidates before reaction; departure after prior touch ends the episode. A new **qualified anchor identity** resets a terminal episode; the same anchor does not automatically reset.
- Incomplete bars and discontinuous windows withhold decisions; no later bar rewrites an earlier observation. Time is modeled integer-minute chart clock, not authentic venue receipt order. RSI/EMA and HTF source qualification still use the existing acceptance scope.
- The separate `replay_structure` research model remains the structural candidate comparator, but it does not model order-block/gap/engulf state. These tests fill that coverage gap without asserting independent human review.

## Adversarial cases

Eleven explicitly constructed, hand-adjudicated Python tests are in `tests/test_phase3_6_lifecycle_parity_oracle.py`; the pure research model is `research/phase3_6/lifecycle_parity_oracle.py`. They cover creation-time non-use, bull/bear block invalidation, persistent invalidation, gap geometry-only state, nonfinal/adjacency withholding, first-contact engulf, support invalidation precedence, departure terminal state, new-anchor reset, HTF-context unknown, and epoch gap reset. They intentionally do **not** claim a native Pine runtime execution.

**Important open ambiguity:** a prior reference of the same underlying origin may later regain ARMED status under an R1-B reset/re-cross policy. Reusing the identical episode identity means the previously ended reaction remains ended. Whether a new reset epoch should create a distinct reaction episode needs an explicitly versioned decision and native adversarial evidence; do not silently make historical events reusable.

## Integrated multi-module modeled replay — 2026-11-13 PHT

**PASS:** Nine new integrated replay unit tests; [GitHub Actions run 43341833165](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43341833165) **104/104** standard tests (95 prior + nine integrated). These checks use [research/phase3_6/integrated_replay.py](../../research/phase3_6/integrated_replay.py) and [tests/test_phase3_6_integrated_replay.py](../../tests/test_phase3_6_integrated_replay.py).

- Frozen 288-bar PAXGUSDT Spot 5m source is evaluated under S1 strict widths 1/2/3, R1-A/R1-B, and several genuinely truncated prefix cutoffs. Result snapshots—including latest gap, block, candidate event and support episode—were invariant to future candles in the checked comparisons.
- Distinguish older-gap `OPEN → GEOMETRIC TEST` from the case where the same candle also creates a newer gap; latest-only Pine policy overwrites the displayed gap with new `OPEN`. The first draft test incorrectly assumed both could be reported simultaneously; it was corrected and the replacement policy pinned as a separate test. Earlier failed run [43341495424](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43341495424) is preserved for traceability.
- An incomplete/missing adjacent bar clears the latest zone and reaction episode research states. Synthetic model epochs and explicitly supplied HTF booleans are not proof of actual 1H/4H feed confirmation. Unknown HTF context remains INSUFFICIENT, never inferred. Numeric values such as `1` or `0` cannot silently stand for verified context.
- **NOT RUN:** executing these candles in Pine, an independent venue-timed HTF receipt, same-cutoff native Pine/reference-model parity, cross-market stress testing, or full multi-zone lifecycle. Do not mark private TradingView v0.1.4 native acceptance as newly expanded; the previous approved scope remains unchanged.

## Source-projected transition differential and invalid evidence fix

[Source-projected Python mirror](../../research/phase3_6/pine_lifecycle_projection.py) and [test harness](../../tests/test_phase3_6_pine_lifecycle_projection.py) were introduced on the same draft branch **without modifying Pine**. [GitHub Actions 43343804439](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43343804439) **112/112 PASS**, 104 previously passed + two closed-interval oracle reset cases + six mirror checks. The 288 generated BLOCK/GAP combinations and 1,536 episode combinations match the separate reference model for the declared state inputs. Source substring guards check that the frozen v0.1.4 Pine transitions still contain the modeled branch order.

**Verified research defect and correction:** the earlier Python `advance_episode` returned the existing episode unchanged when a modeled close was invalid. The frozen Pine evaluation clears episodes on `contiguous=false`, including a malformed finalized close. The research oracle now clears instead; an unconfirmed forming candle in realtime is not claimed to have executed any close transition.

**Source-helper risk, reachability OPEN:** The v0.1.4 Pine helper stores a single most recent terminal origin per side. The mirror's isolated constructed case shows an older origin can be marked ARMED if it is presented again after the latest terminal origin changes. This is **not evidence that actual Pine S1 pivot progression can produce the problematic recurrence**, and is not an observed live-chart fault. Check adversarial source-consistent structural progression and consider full immutable anchor-key terminal history for an unsaved future candidate. Do not change the saved v0.1.4 acceptance without full validation.

A draft differential test incorrectly asserted 3,072 combinations; the actual Cartesian grid enumerated 1,536. The corrected count passed; the prior failure is preserved in [Actions run 43343716407](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43343716407).

**Evidence classification:** source-projected Python consistency PASS only; true runtime Pine/Python parity **NOT RUN**. Human annotation and new Coach consultation are not required; no trading outcome or venue receipt authentication is implied.

## Acceptance status

| Gate | Status |
| --- | --- |
| v0.1.4 prior private acceptance | PASS within prior recorded scope |
| New isolated lifecycle Python tests | **PASS:** 11/11 new cases; [GitHub Actions 43333980361](https://github.com/jebobomagcode/alpha-engine-tradingview/actions/runs/43333980361) **95/95** standard checks overall |
| Same synthetic close sequence through actual Pine native executor | NOT RUN |
| Matched cutoff Pine/experimental Python lifecycle event parity | NOT RUN; integrated Python prefix checks and source-projected Python differential PASS only |
| Wider venues/timeframes/cache-bypass persistence | OPEN_UNRESOLVED |

The next native verification should compare the precise cutoff/source on BLOCK→GEOMETRIC TEST→INVALIDATED, GAP OPEN→GEOMETRIC TEST, REACTION WAIT→OBSERVED or REASSESS, and reference R1-A/R1-B retirement transitions. If the platform cannot inject controlled OHLC into a native Pine study, use witnessed chart evidence as a narrower acceptance and mark synthetic native equivalence NOT RUN. No human annotations or extra Coach sources are required.
