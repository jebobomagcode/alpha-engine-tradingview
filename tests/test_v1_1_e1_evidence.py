"""Read the E1 evidence and oracle fixtures without network access."""

from dataclasses import replace
from datetime import datetime
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
import unittest

from research.v1_1.evidence_contract import (
    INTERVAL_MS, Candle, Chart, Ledger, Market, Status, binance_trade_candle, qualify,
)


ROOT = Path(__file__).resolve().parents[1]
RECEIPTS = ROOT / "docs/research/evidence/v1-1-e1"
FIXTURE = ROOT / "tests/fixtures/v1_1/e1-cutoffs.json"
SOURCE = "BINANCE_FAPI_TRADE_KLINES"


class EvidenceContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(FIXTURE.read_text())
        cls.manifest = json.loads((RECEIPTS / "manifest.json").read_text())
        cls.exchange = json.loads((RECEIPTS / "exchange-info-excerpt.json").read_text())
        cls.receipt = json.loads((RECEIPTS / "trade-klines-receipt.json").read_text())
        cls.epoch = cls.fixture["epoch_ms"]
        cls.warmup = cls.fixture["warmup"]
        cls.markets = {}
        for raw in cls.exchange["symbols"]:
            row = cls.manifest["markets"][raw["symbol"]]
            tick, = [item["tickSize"] for item in raw["filters"]
                     if item["filterType"] == "PRICE_FILTER"]
            market = Market(cls.manifest["venue"], cls.manifest["segment"], raw["symbol"],
                            raw["contractType"], raw["status"], raw["baseAsset"],
                            raw["quoteAsset"], raw["marginAsset"], row["settlement"], tick,
                            row["tradingview_ticker"], cls.exchange["server_time_ms"],
                            Status(row["native_status"]))
            cls.markets[market.symbol] = market
        cls.series = cls.markets["BTCUSDT"].series_id
        cls.candles = []
        for interval, offsets in cls.fixture["close_offsets_ms"].items():
            for offset in offsets:
                close = cls.epoch + offset
                cls.candles.append(Candle(cls.series, SOURCE, interval, close - INTERVAL_MS[interval],
                                          close, **cls.fixture["candle_template_ticks"],
                                          final=True, revision=1, modeled_at_ms=close, receipt_id="synthetic-e1-v1"))

    def decide(self, offset, rows=None, *, clock="modeled", warmup=None):
        ledger = Ledger(self.series, SOURCE, self.candles if rows is None else rows)
        return ledger.decide(self.epoch + offset, clock=clock, warmup=warmup or self.warmup)

    def test_exchange_and_market_receipt_identity(self):
        for path, key in (("exchange-info-excerpt.json", "exchange_info_excerpt_sha256"),
                          ("trade-klines-receipt.json", "trade_klines_receipt_sha256"),
                          ("tradingview-chart-sample.json", "tradingview_chart_sample_sha256")):
            self.assertEqual(sha256((RECEIPTS / path).read_bytes()).hexdigest(), self.manifest[key])
        self.assertEqual(self.exchange["futures_type"], "U_MARGINED")
        self.assertEqual(self.exchange["endpoint"], "https://fapi.binance.com/fapi/v1/exchangeInfo")
        self.assertEqual(self.receipt["endpoint"], "https://fapi.binance.com/fapi/v1/klines")
        self.assertEqual(self.receipt["price_basis"], "TRADE")
        self.assertEqual({s: (m.quote, m.margin, m.settlement, m.tick) for s, m in self.markets.items()},
                         {"BTCUSDT": ("USDT", "USDT", "USDT", "0.10"),
                          "ETHUSDC": ("USDC", "USDC", "USDC", "0.01")})

    def test_admission_and_exclusion_matrix(self):
        captured_at = int(datetime.fromisoformat(self.exchange["retrieved_at_utc"]).timestamp() * 1000)
        for case in self.fixture["admission_cases"]:
            with self.subTest(case=case["id"]):
                market = self.markets[case["market"]]
                chart = Chart(market.tradingview_ticker, "TRADE", "5m", True, market.tick)
                market = replace(market, **case.get("market_changes", {}))
                chart = replace(chart, **case.get("chart_changes", {}))
                audit = captured_at if "audit_offset_ms" not in case else (
                    market.metadata_server_ms + case["audit_offset_ms"])
                admission = qualify(market, chart, audit_ms=audit, max_metadata_age_ms=172_800_000)
                for gate in ("product", "mapping", "native"):
                    result = getattr(admission, gate)
                    self.assertEqual([result.status, result.reason], case[gate])

    def test_simultaneous_rollover_and_first_eligible_cutoff(self):
        for case in self.fixture["schedule_expectations"]:
            with self.subTest(case=case):
                result = self.decide(case["host_open_offset_ms"])
                self.assertEqual(result.cutoff_ms, self.epoch + case["cutoff_offset_ms"])
                self.assertEqual(result.gate.status, case["status"])
                for interval, offset in case["closes_ms"].items():
                    candle = result.layers[interval].candle
                    self.assertEqual(candle.confirmed_ms, self.epoch + offset)
                    self.assertEqual(candle.origin_ms, candle.confirmed_ms - INTERVAL_MS[interval])
                    self.assertEqual(candle.modeled_at_ms, candle.confirmed_ms)
                    self.assertIsNone(candle.observed_at_ms)

    def test_missing_stale_delayed_malformed_and_warmup_oracle(self):
        for case in self.fixture["evidence_cases"]:
            with self.subTest(case=case["id"]):
                interval, op = case["interval"], case["op"]
                rows = list(self.candles)
                if op == "drop_interval":
                    rows = [row for row in rows if row.interval != interval]
                else:
                    at = self.epoch + case["close_offset_ms"]
                    row, = [row for row in rows if (row.interval, row.close_ms) == (interval, at)]
                    if op != "conflict":
                        rows.remove(row)
                    changes = {"delay": {"modeled_at_ms": self.epoch + case.get("value", 0)},
                               "conflict": {"close_tick": 100}, "wrong_source": {"source_id": "MARK"},
                               "unfinalized": {"final": False}}
                    if op != "drop":
                        rows.append(replace(row, **changes[op]))
                result = self.decide(case["host_open_offset_ms"], rows,
                                     warmup=self.warmup | {interval: case.get("warmup", 1)})
                self.assertEqual(result.gate.status, case["status"])
                layer = result.layers[interval]
                self.assertEqual(layer.gate.reason, case["reason"])
                latest = case["latest_visible_offset_ms"]
                self.assertEqual(layer.latest_visible_close_ms, None if latest is None else self.epoch + latest)

    def test_modeled_and_observed_clocks_never_substitute(self):
        self.assertEqual(self.decide(0, clock="observed").gate.status, Status.INSUFFICIENT)
        rows = [replace(row, observed_at_ms=row.close_ms) for row in self.candles]
        at_boundary = self.decide(0, rows, clock="observed")
        self.assertEqual(at_boundary.layers["5m"].gate.status, Status.PASS)
        self.assertTrue(all(at_boundary.layers[tf].gate.reason == "STALE_PREVIOUS_CANDLE"
                            for tf in ("15m", "1h", "4h")))
        self.assertEqual(self.decide(300_000, rows, clock="observed").gate.status, Status.PASS)
        late_host = [replace(row, observed_at_ms=row.close_ms + 1) if row.interval == "5m"
                     else row for row in rows]
        self.assertEqual(self.decide(300_000, late_host, clock="observed").layers["5m"].gate.status,
                         Status.INSUFFICIENT)

    def test_revisions_are_as_of_and_input_order_invariant(self):
        case = self.fixture["revision_case"]
        row, = [row for row in self.candles if (row.interval, row.close_ms) == (
            case["interval"], self.epoch + case["close_offset_ms"])]
        revised = replace(row, revision=2, close_tick=102,
                          modeled_at_ms=self.epoch + case["revised_modeled_offset_ms"])
        rows = [revised, *self.candles, row]
        prior = self.decide(case["prior_open_offset_ms"], rows)
        following = self.decide(case["next_open_offset_ms"], list(reversed(rows)))
        self.assertEqual(prior, self.decide(case["prior_open_offset_ms"]))
        self.assertEqual([x.layers[case["interval"]].candle.revision for x in (prior, following)],
                         case["expected_revisions"])
        self.assertEqual(self.decide(case["next_open_offset_ms"], rows), following)

    def test_future_append_cannot_change_a_closed_decision(self):
        for case in self.fixture["schedule_expectations"]:
            offset = case["host_open_offset_ms"]
            with self.subTest(offset=offset):
                cutoff = self.epoch + case["cutoff_offset_ms"]
                prefix = [row for row in self.candles if row.modeled_at_ms <= cutoff]
                self.assertEqual(self.decide(offset, prefix), self.decide(offset))
                for row in self.candles:
                    if row.interval != "5m" and row.close_ms == cutoff:
                        mutated = replace(row, close_tick=102)
                        modified = [mutated if original == row else original for original in self.candles]
                        self.assertEqual(self.decide(offset, modified), self.decide(offset))

    def test_refetches_preserve_deterministic_evidence_identity(self):
        original = self.decide(0).layers["15m"].candle
        duplicate = replace(original, receipt_id="z-refetch")
        self.assertEqual(self.decide(0, [duplicate, *self.candles]), self.decide(0))

    def test_strict_validation_and_history(self):
        prior = self.decide(0, warmup={tf: 2 for tf in INTERVAL_MS})
        self.assertEqual(prior.gate.status, Status.PASS)
        for tf, step in INTERVAL_MS.items():
            current = prior.layers[tf].candle
            self.assertEqual([c.close_ms for c in prior.layers[tf].history],
                             [current.close_ms - step, current.close_ms])
        host = prior.layers["5m"].candle
        for change in ({"high_tick": 1}, {"modeled_at_ms": host.close_ms - 1}, {"open_ms": 1},
                       {"observed_at_ms": host.close_ms - 1}, {"close_tick": True}):
            with self.subTest(change=change):
                rows = [replace(row, **change) if row == host else row for row in self.candles]
                self.assertEqual(self.decide(0, rows).layers["5m"].gate.reason, "INVALID_CANDLE")
        with self.assertRaises(ValueError):
            self.decide(1)
        with self.assertRaises(ValueError):
            self.decide(0, clock="exchange_guess")
        with self.assertRaises(ValueError):
            self.decide(0, warmup={"4h": 2})

    def test_actual_binance_coverage_and_native_interval_aggregation(self):
        grouped = {}
        start, end = self.receipt["start_ms"], self.receipt["end_exclusive_ms"]
        for capture in self.receipt["responses"]:
            request = capture["request"]
            symbol, tf = request["symbol"], request["interval"]
            key = (symbol, tf)
            self.assertNotIn(key, grouped)
            self.assertEqual((request["startTime"], request["endTime"]), (start, end - 1))
            raw = json.loads(capture["connector_response_text"])["result"]
            grouped[key] = [binance_trade_candle(self.markets[symbol], tf, row, final_by_ms=end,
                                                 receipt_id=self.manifest["trade_klines_receipt_sha256"])
                            for row in raw]
            self.assertTrue(all(row.observed_at_ms is None for row in grouped[key]))
            self.assertEqual([row.open_ms for row in grouped[key]], list(range(start, end, INTERVAL_MS[tf])))
            self.assertEqual(len(raw), request["limit"])
        self.assertEqual(set(grouped), {(s, tf) for s in self.markets for tf in INTERVAL_MS})
        self.assertEqual(sum(map(len, grouped.values())), 414)
        chart = json.loads((RECEIPTS / "tradingview-chart-sample.json").read_text())
        self.assertEqual((chart["chart_type"], chart["interval"]), ("Candles", "5m"))
        local_open = datetime.fromisoformat(chart["chart_time_local"])
        self.assertEqual(int(local_open.timestamp() * 1000), chart["open_ms"])
        self.assertEqual(set(chart["samples"]), set(self.markets))
        for symbol, market in self.markets.items():
            hosts = grouped[symbol, "5m"]
            sample = chart["samples"][symbol]
            self.assertEqual(sample["ticker"], market.tradingview_ticker)
            matched, = [row for row in hosts if row.open_ms == chart["open_ms"]]
            expected_ticks = (matched.open_tick, matched.high_tick, matched.low_tick, matched.close_tick)
            self.assertEqual(tuple(Decimal(p) / Decimal(market.tick) for p in sample["ohlc"]),
                             expected_ticks)
            all_rows = []
            for tf, step in INTERVAL_MS.items():
                bars = grouped[symbol, tf]
                all_rows.extend(bars)
                if tf == "5m":
                    continue
                for bar in bars:
                    index = (bar.open_ms - start) // INTERVAL_MS["5m"]
                    parts = hosts[index:index + step // INTERVAL_MS["5m"]]
                    self.assertEqual((bar.open_tick, bar.high_tick, bar.low_tick, bar.close_tick),
                                     (parts[0].open_tick, max(x.high_tick for x in parts),
                                      min(x.low_tick for x in parts), parts[-1].close_tick), (symbol, tf, bar.open_ms))
            ledger = Ledger(market.series_id, SOURCE, all_rows)
            for row in self.fixture["schedule_expectations"]:
                at = self.epoch + row["host_open_offset_ms"]
                decision = ledger.decide(at, clock="modeled", warmup=self.warmup)
                self.assertEqual(decision.gate.status, row["status"])
                self.assertEqual({tf: layer.candle.close_ms - self.epoch for tf, layer in decision.layers.items()},
                                 row["closes_ms"])

    def test_normalizer_rejects_off_grid_or_unclosed_input(self):
        cap = self.receipt["responses"][0]
        raw = json.loads(cap["connector_response_text"])["result"][0]
        market = self.markets["BTCUSDT"]
        with self.assertRaisesRegex(ValueError, "not yet final"):
            binance_trade_candle(market, "5m", raw, final_by_ms=raw[6], receipt_id="test")
        raw[1] = "71361.31"
        with self.assertRaisesRegex(ValueError, "off grid"):
            binance_trade_candle(market, "5m", raw, final_by_ms=raw[6] + 1, receipt_id="test")


if __name__ == "__main__":
    unittest.main()
