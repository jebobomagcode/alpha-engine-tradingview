"""Verify the bounded exchange receipt and candidate feed bindings."""

from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import unittest

from research.phase3_6.integrated_replay import replay_integrated
from research.phase3_6.reference_model import Bar


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "pine/alpha-engine-research.pine"
RECEIPT = ROOT / "docs/research/evidence/binance-market-qualification-v016.json"
SPOT = {"PAXGUSDT": "PAXG", "XAUTUSDT": "XAUT", "BTCUSDT": "BTC", "ETHUSDT": "ETH"}
PERIOD = {"5m": 300_000, "1h": 3_600_000, "4h": 14_400_000}


class MarketQualification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evidence = json.loads(RECEIPT.read_text())
        cls.markets = cls.evidence["markets"]
        cls.source = SOURCE.read_text()

    def test_receipt_identity_and_window(self):
        self.assertEqual(hashlib.sha256(RECEIPT.read_bytes()).hexdigest(),
                         "e7215e4cc7c74b947d58a6b3980e95b795a8bc6369e5aad194e8fa6bd57f479e")
        self.assertEqual((self.evidence["start_ms"], self.evidence["end_exclusive_ms"]),
                         (1794441600000, 1794456000000))

    def test_exact_listing_units_and_tick(self):
        self.assertEqual(set(self.markets), {*SPOT, "XAUUSDT"})
        for name, market in self.markets.items():
            with self.subTest(symbol=name):
                self.assertEqual(market["status"], "TRADING")
                self.assertEqual((market["quote"], Decimal(market["tick"])), ("USDT", Decimal(".01")))
                self.assertEqual(market["base"], SPOT.get(name, "XAU"))
                if name in SPOT:
                    self.assertEqual((market["product"], market["endpoint"], market["margin"]),
                                     ("SPOT", "/api/v3/klines", None))
                    self.assertEqual((market["base_precision"], market["quote_precision"]), (8, 8))
                else:
                    self.assertEqual((market["product"], market["endpoint"], market["margin"]),
                                     ("TRADIFI_PERPETUAL", "/fapi/v1/klines", "USDT"))
                    self.assertEqual(market["price_precision"], 2)

    def test_closed_candles_are_contiguous_valid_and_on_grid(self):
        for symbol, market in self.markets.items():
            tick = Decimal(market["tick"])
            self.assertEqual(set(market["bars"]), set(PERIOD))
            for interval, step in PERIOD.items():
                with self.subTest(symbol=symbol, interval=interval):
                    bars = market["bars"][interval]
                    opens = range(self.evidence["start_ms"], self.evidence["end_exclusive_ms"], step)
                    self.assertEqual([bar[0] for bar in bars], list(opens))
                    for opened, o, h, lo, c, closed in bars:
                        o, h, lo, c = map(Decimal, (o, h, lo, c))
                        self.assertTrue(0 < lo <= min(o, c) <= max(o, c) <= h)
                        self.assertTrue(all(price % tick == 0 for price in (o, h, lo, c)))
                        self.assertEqual(closed, opened + step - 1)

    def test_all_higher_timeframe_ohlc_matches_5m_aggregation(self):
        for symbol, market in self.markets.items():
            for interval in ("1h", "4h"):
                step = PERIOD[interval]
                for opened, o, h, lo, c, _ in market["bars"][interval]:
                    with self.subTest(symbol=symbol, interval=interval, opened=opened):
                        group = [row for row in market["bars"]["5m"] if opened <= row[0] < opened + step]
                        self.assertEqual(len(group), step // PERIOD["5m"])
                        expected = (Decimal(group[0][1]), max(Decimal(row[2]) for row in group),
                                    min(Decimal(row[3]) for row in group), Decimal(group[-1][4]))
                        self.assertEqual(tuple(map(Decimal, (o, h, lo, c))), expected)

    def test_market_replays_are_prefix_invariant_and_lack_confirmed_context(self):
        for symbol, market in self.markets.items():
            tick = Decimal(market["tick"])
            bars = tuple(Bar(row[0] // 60_000, *(int(Decimal(p) / tick) for p in row[1:5]))
                         for row in market["bars"]["5m"])
            for policy in ("A", "B"):
                with self.subTest(symbol=symbol, policy=policy):
                    full = replay_integrated(bars, as_of=bars[-1].cutoff, policy=policy)
                    self.assertEqual(len(full), 48)
                    self.assertTrue(all(frame.reaction_status == "INSUFFICIENT · closed data"
                                        for frame in full))
                    for size in (12, 24, 36):
                        prefix = replay_integrated(bars[:size], as_of=bars[size - 1].cutoff, policy=policy)
                        self.assertEqual(prefix, full[:size])

    def test_pine_bindings_and_fail_closed_gates(self):
        source = self.source
        candidates = re.findall(r'^    "(BINANCE:[A-Z.]+)" => syminfo.basecurrency == "([A-Z]+)" \? "([^"]+)"', source, re.M)
        expected = [(f"BINANCE:{symbol}", base, "Spot") for symbol, base in SPOT.items()]
        self.assertCountEqual(candidates, expected)
        self.assertIn(
            '"BINANCE:XAUUSDT.P" => syminfo.basecurrency == "" or syminfo.basecurrency == "XAU"'
            ' ? "USDT-margined gold perpetual" : ""', source,
        )
        ids = re.findall(r'^    "([^"]+)" =>', source.split("switch syminfo.tickerid", 1)[1], re.M)
        self.assertCountEqual(ids, [ticker for ticker, _, _ in expected] + ["BINANCE:XAUUSDT.P"])
        self.assertIn('syminfo.currency == "USDT" and syminfo.mintick == 0.01', source)
        self.assertIn("timeframe.isminutes and timeframe.multiplier == 5 and chart.is_standard", source)
        self.assertIn('not chart.is_standard or not timeframe.isminutes or timeframe.multiplier != 5 ? "INSUFFICIENT · use standard 5m candles"', source)
        self.assertIn('"Market / evidence", ticker.standard(syminfo.tickerid)', source)
        for line in source.splitlines():
            if "request.security(syminfo.tickerid," in line:
                self.assertNotIn("ticker.standard(", line)
        self.assertIn("closed == boundary and opened == boundary - period and opened - first == 49 * period", source)
        self.assertIn("highTicks >= floorTicks and lowTicks <= ceilingTicks", source)
        self.assertIn("closeTicks < floorTicks", source)
        self.assertIn("if barstate.islast and syminfo.tickerid == SYMBOL", source)
