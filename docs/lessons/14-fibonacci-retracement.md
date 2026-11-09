# PCSS Lesson 14 — Fibonacci Retracement (Original PDF page 19)

**Status:** COMPLETE as source-ordered study and independent arithmetic audit, 2026-11-09 Asia/Manila; NO Pine code, compilation, empirical backtest, deployment, orders or verified profitability. **Sole Coach-origin source:** [Original Coach PDF, page 19](../../sources/coach%20trading%20lessons.pdf). PDF SHA-256: 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730; private PCSS SHA-256: 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56. User's independent TradingView project is crypto-focused including separate XAUUSDT, XAUTUSDT, PAXGUSDT venue/product identities.

## Full source-order audit

Original page 19 inspected at rendered image resolution and checked against native PDF text. **One text-only page** with headings, red-circle bullets, ordered steps, and NO embedded chart, image, numeric worked trade, actual data table, formula, proof or exercise. Original heading spells “FIBONNACI”; normalized title here does not alter the meaning.

| ID | Source item, in original order | Audit |
| --- | --- | --- |
| 14-01 | Heading “14. FIBONNACI”; Fibonacci Retracement tool | Covered |
| 14-02 | Tool helps locate possible bounce/support/resistance after price pullback | Source qualitative claim; not guarantee |
| 14-03 | Coach-stated TradingView default levels: .236, .382, .5, .618, .786 | All five retained; actual chart settings customizable |
| 14-04 | Initial Golden Zone .5–.618, described as frequent reaction area | Unquantified |
| 14-05 | Uptrend: lowest swing low -> highest swing high -> await .5–.618 pullback | 3 steps retained |
| 14-06 | Downtrend: highest swing high -> lowest swing low -> await .5–.618 retracement | 3 steps retained |
| 14-07 | Initial entry .5–.618; stop BELOW/ABOVE .786 by long/short direction | Exact buffer/SL price unspecified |
| 14-08 | Four-item recap: Fib finds pullback entry; best zone .5–.618; follow trend; wait confirmation, not blind entry | All four kept |
| 14-09 | HTF 4H/Daily: identify trend, plot Fib, focus Golden Zone, wait | Full flow retained |
| 14-10 | Then LTF 5m/15m: engulfing, liquidity sweep, other confluence -> entry, SL, TP | Liquidity-sweep geometry/TP unspecified |
| 14-11 | Fibonacci settings note: default levels familiar as support/resistance by direction | Coach characterization |
| 14-12 | **Final instruction:** manually add custom .705 and find entries in **.618–.705** with confirmation | **Different** from initial Golden Zone; no explicit precedence |

## 1. Coach's tool and source explanation

**COACH EXPLICIT:** Fibonacci retracement aims to identify potential price-reaction locations after an impulse and correction. His stated original ratios are 0.236, 0.382, 0.5, 0.618 and 0.786, and he repeatedly calls 0.5–0.618 the Golden Zone. He encourages following the trend and confirmation rather than blind entry.

**Independent mathematical qualification:** 0.5 is the midpoint; it is not a successive-Fibonacci-number quotient. 0.705 is the explicitly added custom ratio, not compelled by the Fibonacci sequence. Describing a region as “golden” or well-known does not establish a quantitative success probability. TradingView's tool documentation confirms configurable ratios: https://www.tradingview.com/support/solutions/43000518158-fibonacci-retracement-drawing-tool/ .

## 2. Bullish and bearish plotting

**COACH EXPLICIT, uptrend:** from swing low to swing high, then wait for downward pullback to initial 0.5–0.618. **Downtrend:** from swing high to swing low, wait for upward pullback to 0.5–0.618.

**Independent arithmetic coordinate formalization:** Let confirmed swing low L < high H and retracement fraction r between 0 and 1.
- UP correcting down from H: P_up(r) = H − r(H−L).
- DOWN correcting up from L: P_down(r) = L + r(H−L).

These equations represent *economic price retracement fractions*. TradingView level labels can be reversed through its **Reverse** tool setting; verify displayed PRICE coordinates, not ratio labels alone.

### Independent hypothetical example, not Coach price data

Use low 100 USDT, high 120 USDT, range 20:

| r | Uptrend pullback price | Downtrend pullback price |
| --- | ---: | ---: |
| 0.236 | 115.28 | 104.72 |
| 0.382 | 112.36 | 107.64 |
| 0.500 | 110.00 | 110.00 |
| 0.618 | 107.64 | 112.36 |
| 0.705 | 105.90 | 114.10 |
| 0.786 | 104.28 | 115.72 |

**Initial GOLDEN band:** bullish [107.64, 110.00], bearish [110.00,112.36]. **Final customized deeper band:** bullish [105.90,107.64], bearish [112.36,114.10]. **Stop condition:** bullish price strictly below 104.28, bearish price strictly above 115.72; Coach supplies no fixed buffer, so those are inequalities and not complete executable stops. No target level or exact TP method given; actual RR is UNKNOWN.

## 3. Complete source top-down workflow, in order

Coach: choose HTF 4H/Daily; identify trend; draw Fib on relevant impulse; focus 0.5–0.618; wait for price to reach the zone; THEN move to LTF 5m/15m to seek engulfing, liquidity sweep or other past-lesson confluence; only then assess entry, SL and TP. In the final paragraph he says to add 0.705 manually and instead watch the interval 0.618–0.705 with the same confluence requirement.

**Connect to prior lessons:** Lesson 07 trends HH/HL vs LH/LL, Lesson 08 location-before-confirmation and NO TRADE, Lesson 10 no reversal -> no entry, Lesson 12 causal BOS/swing context. A Fib zone is a location filter, not an automatic order. Source does NOT formally define liquidity sweep geometry (relevant high/low, wick break versus closing recovery, maximum time separation).

## 4. Ponder — two source-based but different entry regions

Initial region [0.500,0.618] and final custom [0.618,0.705] share only boundary 0.618; they are NOT one identical interval. Source does not specify whether:
- A is standard and B is a deeper optional alternative;
- B supersedes A once 0.705 has been enabled;
- both are equally acceptable in a larger method.

**Decision at study stage:** preserve both with source provenance and mark selection OPEN_UNRESOLVED; do NOT silently merge to 0.5–0.705 or assert Coach always preferred the custom band.

## 5. Open mathematical and methodological issues

- Which confirmed HTF swing low/high should be used, how many bars establish it, and when becomes it knowable? No anchor selection algorithm in source.
- How long are anchors valid? Can the high/low update while price is approaching the zone? Dynamic hindsight drawing could create misleading historical entries.
- Wick touch, closing touch, body touch or tick/volatility tolerance? No rule.
- The stop must be beyond 0.786, but minimum tick/ATR buffer, order type, spread and slippage not defined.
- What TP? The page only says “SL and TP”; earlier source target options could be studied jointly but no specific Fibonacci target selected.
- What is a qualifying liquidity sweep or engulfing confirmation and which timing? Source incomplete.
- **TradingView math-mode distinction:** The Fib drawing supports Reverse and “Fib levels based on log scale.” On positive prices, a log-price retracement model would use P_up=H*(L/H)^r and P_down=L*(H/L)^r, which differs from arithmetic linear-price calculation; these formulas are independent math, not Coach source. Documentation: https://www.tradingview.com/support/solutions/43000518158-fibonacci-retracement-drawing-tool/ .
- Crypto venue/symbol precision: no transplant of anchor price levels between XAUUSDT gold derivatives and XAUTUSDT/PAXGUSDT token markets.
- The confluence of Fib/SR levels derived from the same swing may be statistically redundant, not independent evidence.

**Time integrity:** confirmed anchor must be known before a subsequent hypothetical entry is called valid. Official TradingView repainting documentation https://www.tradingview.com/pine-script-docs/concepts/repainting/ warns against backdating future-confirmed pivots and lookahead.

## 6. Source study conclusion

All 12 source inventory elements, both drawing directions, initial and custom bands, stop reference and original top-down flow audited. The source page has no embedded illustration, numerical trading example or exercise to omit. Independent six-level bull/bear arithmetic verified exactly. No actual signals, tests on candles, strategy backtests or code.

**Lesson 14 COMPLETE for PCSS teaching and research only. Next: Lesson 15 — Reliability on Charting (PDF p. 20), on owner direction.**
