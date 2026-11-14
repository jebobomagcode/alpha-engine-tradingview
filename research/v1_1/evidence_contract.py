"""D-041 E1: exact trade-feed admission and as-of candle evidence.

This layer emits evidence, leaving continuation and geometry to later modules.
"""

from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from enum import StrEnum
from fractions import Fraction


INTERVAL_MS = {"5m": 300_000, "15m": 900_000, "1h": 3_600_000, "4h": 14_400_000}
HOST_MS = INTERVAL_MS["5m"]


class Status(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    INSUFFICIENT = "INSUFFICIENT"
    NOT_RUN = "NOT RUN"


@dataclass(frozen=True)
class Gate:
    status: Status
    reason: str


@dataclass(frozen=True)
class Market:
    venue: str
    segment: str
    symbol: str
    raw_contract_type: str
    trading_status: str
    base: str
    quote: str
    margin: str
    settlement: str
    tick: str
    tradingview_ticker: str
    # The pinned metadata record is reviewed at a separately supplied audit time.
    metadata_server_ms: int
    native_status: Status = Status.NOT_RUN

    @property
    def series_id(self):
        return f"{self.venue}:{self.segment}:{self.symbol}:TRADE"


@dataclass(frozen=True)
class Chart:
    ticker: str
    price_basis: str
    interval: str
    standard_ohlc: bool
    tick: str | None


@dataclass(frozen=True)
class Qualification:
    product: Gate
    mapping: Gate
    native: Gate


def _tick(value):
    try:
        number = Decimal(value) if isinstance(value, str) else None
    except (InvalidOperation, TypeError, ValueError):
        return None
    return number if number is not None and number.is_finite() and number > 0 else None


def qualify(market, chart, *, audit_ms, max_metadata_age_ms):
    """Evaluate a pinned product and exact manifest/chart mapping independently.

    PASS mapping checks the supplied chart fields, not native runtime behavior.
    """
    if type(audit_ms) is not int or type(max_metadata_age_ms) is not int or max_metadata_age_ms < 0:
        raise ValueError("invalid metadata audit clock")
    tick = _tick(market.tick)
    if (market.venue, market.segment, market.raw_contract_type) != ("BINANCE", "USDⓈ-M", "PERPETUAL"):
        product = Gate(Status.FAIL, "OUT_OF_E1_PRODUCT_SCOPE")
    elif market.trading_status != "TRADING":
        product = Gate(Status.FAIL, "CONTRACT_NOT_TRADING")
    elif not all((market.symbol, market.base, market.quote, market.margin, market.settlement)) or tick is None:
        product = Gate(Status.INSUFFICIENT, "PRODUCT_FIELDS_UNVERIFIED")
    elif market.quote not in {"USDT", "USDC"} or market.quote != market.margin or market.quote != market.settlement:
        product = Gate(Status.FAIL, "OUT_OF_E1_UNIT_SCOPE")
    elif type(market.metadata_server_ms) is not int or not 0 <= audit_ms - market.metadata_server_ms <= max_metadata_age_ms:
        product = Gate(Status.INSUFFICIENT, "METADATA_OUTSIDE_AUDIT_WINDOW")
    else:
        product = Gate(Status.PASS, "VERIFIED_PRODUCT_FIELDS")

    chart_tick = _tick(chart.tick)
    if not market.tradingview_ticker:
        mapping = Gate(Status.INSUFFICIENT, "NO_VERIFIED_CHART_MAPPING")
    elif chart.ticker != market.tradingview_ticker or not chart.ticker.startswith("BINANCE:"):
        mapping = Gate(Status.FAIL, "TICKER_MISMATCH")
    elif chart.price_basis != "TRADE" or chart.interval != "5m" or chart.standard_ohlc is not True:
        mapping = Gate(Status.FAIL, "UNSUPPORTED_CHART")
    elif tick is None or chart_tick is None:
        mapping = Gate(Status.INSUFFICIENT, "TICK_UNVERIFIED")
    elif chart_tick != tick:
        mapping = Gate(Status.FAIL, "TICK_MISMATCH")
    else:
        mapping = Gate(Status.PASS, "EXACT_MAPPING_FIELDS")

    if product.status != Status.PASS or mapping.status != Status.PASS:
        native = Gate(Status.NOT_RUN, "ADMISSION_PREREQUISITES_UNMET")
    else:
        native = Gate(Status(market.native_status), "NATIVE_GATE_" + Status(market.native_status).name)
    return Qualification(product, mapping, native)


@dataclass(frozen=True)
class Candle:
    series_id: str
    source_id: str
    interval: str
    open_ms: int
    close_ms: int  # Exclusive close boundary.
    open_tick: int
    high_tick: int
    low_tick: int
    close_tick: int
    final: bool
    revision: int
    modeled_at_ms: int
    observed_at_ms: int | None = None
    receipt_id: str = ""

    @property
    def origin_ms(self):
        return self.open_ms

    @property
    def confirmed_ms(self):
        return self.close_ms

    def available(self, clock):
        return self.modeled_at_ms if clock == "modeled" else self.observed_at_ms

    def valid(self):
        step = INTERVAL_MS[self.interval]
        prices = (self.open_tick, self.high_tick, self.low_tick, self.close_tick)
        return (
            type(self.open_ms) is int and self.open_ms >= 0 and self.open_ms % step == 0
            and type(self.close_ms) is int and self.close_ms - self.open_ms == step and self.final is True
            and type(self.revision) is int and self.revision > 0
            and isinstance(self.receipt_id, str) and bool(self.receipt_id)
            and type(self.modeled_at_ms) is int and self.modeled_at_ms >= self.close_ms
            and (self.observed_at_ms is None
                 or type(self.observed_at_ms) is int and self.observed_at_ms >= self.close_ms)
            and all(type(price) is int and price > 0 for price in prices)
            and self.low_tick <= min(self.open_tick, self.close_tick)
            and max(self.open_tick, self.close_tick) <= self.high_tick
        )


def binance_trade_candle(market, interval, row, *, final_by_ms, receipt_id):
    """Normalize a pinned /fapi/v1/klines row with an explicit finality bound.

    The caller binds the response's requested symbol and endpoint to this market.
    An exclusive interval boundary supplies modeled availability only.
    """
    tick = _tick(market.tick)
    if (interval not in INTERVAL_MS or tick is None or type(final_by_ms) is not int
            or not isinstance(row, (list, tuple)) or len(row) != 12
            or type(row[0]) is not int or type(row[6]) is not int
            or not isinstance(receipt_id, str) or not receipt_id):
        raise ValueError("invalid Binance kline envelope")
    prices = [_tick(p) for p in row[1:5]]
    if any(price is None for price in prices):
        raise ValueError("invalid Binance OHLC price")
    ratios = [Fraction(price) / Fraction(tick) for price in prices]
    if any(ratio.denominator != 1 for ratio in ratios):
        raise ValueError("Binance OHLC is off grid")
    close_ms = row[6] + 1
    candle = Candle(market.series_id, "BINANCE_FAPI_TRADE_KLINES", interval,
                    row[0], close_ms, *(ratio.numerator for ratio in ratios),
                    close_ms <= final_by_ms, 1, close_ms, receipt_id=receipt_id)
    if not candle.valid():
        raise ValueError("malformed or not yet final Binance kline")
    return candle


@dataclass(frozen=True)
class Layer:
    gate: Gate
    expected_close_ms: int
    latest_visible_close_ms: int | None
    candle: Candle | None = None
    history: tuple[Candle, ...] = ()  # Oldest to newest, only when the layer passes.


@dataclass(frozen=True)
class Decision:
    open_ms: int
    cutoff_ms: int
    clock: str
    layers: dict[str, Layer]
    gate: Gate


class Ledger:
    """Index immutable evidence by source interval and close, including revisions."""

    def __init__(self, series_id, source_id, candles):
        self.series_id = series_id
        self.source_id = source_id
        self._rows = {interval: defaultdict(list) for interval in INTERVAL_MS}
        for candle in candles:
            if candle.interval not in INTERVAL_MS or type(candle.close_ms) is not int:
                raise ValueError("unindexable evidence row")
            self._rows[candle.interval][candle.close_ms].append(candle)
        self._closes = {interval: sorted(rows) for interval, rows in self._rows.items()}

    def _visible(self, interval, close_ms, asof_ms, clock, before_open):
        rows = self._rows[interval].get(close_ms, ())
        return [row for row in rows if _visible_at(row, asof_ms, clock, before_open)]

    def _resolve(self, rows):
        if any((row.series_id, row.source_id) != (self.series_id, self.source_id) for row in rows):
            return Gate(Status.FAIL, "FEED_MISMATCH"), None
        if any(type(row.revision) is not int or row.revision < 1 for row in rows):
            return Gate(Status.FAIL, "INVALID_REVISION"), None
        if any(not isinstance(row.receipt_id, str) or not row.receipt_id for row in rows):
            return Gate(Status.FAIL, "MISSING_RECEIPT_ID"), None
        version = max(row.revision for row in rows)
        latest = {row for row in rows if row.revision == version}
        # Provenance can differ when identical evidence is fetched more than once.
        payloads = {(row.open_ms, row.open_tick, row.high_tick, row.low_tick,
                     row.close_tick, row.final, row.modeled_at_ms, row.observed_at_ms) for row in latest}
        if len(payloads) != 1:
            return Gate(Status.FAIL, "CONTRADICTORY_REVISION"), None
        row = min(latest, key=lambda r: r.receipt_id)
        if row.final is False:
            return Gate(Status.INSUFFICIENT, "UNFINALIZED_CANDLE"), None
        if not row.valid():
            return Gate(Status.FAIL, "INVALID_CANDLE"), None
        return Gate(Status.PASS, "CONFIRMED_CANDLE"), row

    def layer(self, interval, close_ms, asof_ms, clock, *, before_open, warmup):
        step = INTERVAL_MS[interval]
        rows = self._visible(interval, close_ms, asof_ms, clock, before_open)
        if not rows:
            older = next((t for t in reversed(self._closes[interval]) if t < close_ms
                          and self._visible(interval, t, asof_ms, clock, before_open)), None)
            reason = "MISSING_EXPECTED_CANDLE" if older is None else "STALE_PREVIOUS_CANDLE"
            return Layer(Gate(Status.INSUFFICIENT, reason), close_ms, older)
        gate, candle = self._resolve(rows)
        history = []
        if gate.status == Status.PASS:
            history.append(candle)
            for i in range(1, warmup):
                prior = self._visible(interval, close_ms - i * step, asof_ms, clock, before_open)
                if not prior:
                    return Layer(Gate(Status.INSUFFICIENT, "WARMUP_GAP"), close_ms, close_ms, candle)
                prior_gate, prior_candle = self._resolve(prior)
                if prior_gate.status != Status.PASS:
                    return Layer(Gate(prior_gate.status, "WARMUP_" + prior_gate.reason),
                                 close_ms, close_ms, candle)
                history.append(prior_candle)
        return Layer(gate, close_ms, close_ms, candle, tuple(reversed(history)))

    def decide(self, open_ms, *, clock, warmup):
        """Select exactly the expected HTF closes at open and host close at cutoff."""
        if clock not in {"modeled", "observed"}:
            raise ValueError("unknown evidence clock")
        if type(open_ms) is not int or open_ms < 0 or open_ms % HOST_MS:
            raise ValueError("host open must be on the UTC 5m grid")
        if warmup.keys() != INTERVAL_MS.keys() or any(type(n) is not int or n < 1 for n in warmup.values()):
            raise ValueError("warmup must specify four positive candle counts")
        cutoff_ms = open_ms + HOST_MS
        layers = {}
        for interval, step in INTERVAL_MS.items():
            if interval == "5m":
                layers[interval] = self.layer(interval, cutoff_ms, cutoff_ms, clock,
                                              before_open=False, warmup=warmup[interval])
            else:
                layers[interval] = self.layer(interval, open_ms // step * step, open_ms, clock,
                                              before_open=True, warmup=warmup[interval])
        if any(layer.gate.status == Status.FAIL for layer in layers.values()):
            gate = Gate(Status.FAIL, "CONTRADICTORY_OR_INVALID_EVIDENCE")
        elif any(layer.gate.status == Status.INSUFFICIENT for layer in layers.values()):
            gate = Gate(Status.INSUFFICIENT, "REQUIRED_LAYER_NOT_READY")
        else:
            gate = Gate(Status.PASS, "FOUR_CONFIRMED_LAYERS")
        return Decision(open_ms, cutoff_ms, clock, layers, gate)


def _visible_at(row, asof_ms, clock, before_open):
    available = row.available(clock)
    # A malformed modeled clock can be diagnosed once the interval is closed.
    if type(available) is not int:
        return clock == "modeled" and row.close_ms <= asof_ms
    if row.close_ms > asof_ms:
        return False
    if clock == "observed" and before_open:
        # Equality alone supplies no order relative to the opening snapshot.
        return available < asof_ms
    return available <= asof_ms
