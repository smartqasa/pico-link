from typing import TypedDict

class KrakenResponseEntry(TypedDict):
    ask: tuple[float, float, float]
    bid: tuple[float, float, float]
    last_trade_closed: tuple[float, float]
    volume: tuple[float, float]
    volume_weighted_average: tuple[float, float]
    number_of_trades: tuple[int, int]
    low: tuple[float, float]
    high: tuple[float, float]
    opening_price: float
type KrakenResponse = dict[str, KrakenResponseEntry]

DEFAULT_SCAN_INTERVAL: int
DEFAULT_TRACKED_ASSET_PAIR: str
DISPATCH_CONFIG_UPDATED: str
CONF_TRACKED_ASSET_PAIRS: str
DOMAIN: str
