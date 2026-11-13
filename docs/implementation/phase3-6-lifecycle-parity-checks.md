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

## Acceptance status

| Gate | Status |
| --- | --- |
| v0.1.4 prior private acceptance | PASS within prior recorded scope |
| New isolated lifecycle Python tests | CI PENDING |
| Same synthetic close sequence through actual Pine native executor | NOT RUN |
| Matched cutoff Pine/experimental Python lifecycle event parity | NOT RUN |
| Wider venues/timeframes/cache-bypass persistence | OPEN_UNRESOLVED |

The next native verification should compare the precise cutoff/source on BLOCK→GEOMETRIC TEST→INVALIDATED, GAP OPEN→GEOMETRIC TEST, REACTION WAIT→OBSERVED or REASSESS, and reference R1-A/R1-B retirement transitions. If the platform cannot inject controlled OHLC into a native Pine study, use witnessed chart evidence as a narrower acceptance and mark synthetic native equivalence NOT RUN. No human annotations or extra Coach sources are required.
