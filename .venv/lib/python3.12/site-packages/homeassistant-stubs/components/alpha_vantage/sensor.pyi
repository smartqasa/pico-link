from _typeshed import Incomplete
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_CURRENCY as CONF_CURRENCY, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
ATTR_CLOSE: str
ATTR_HIGH: str
ATTR_LOW: str
ATTRIBUTION: str
CONF_FOREIGN_EXCHANGE: str
CONF_FROM: str
CONF_SYMBOL: str
CONF_SYMBOLS: str
CONF_TO: str
ICONS: Incomplete
SCAN_INTERVAL: Incomplete
SYMBOL_SCHEMA: Incomplete
CURRENCY_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AlphaVantageSensor(SensorEntity):
    _attr_attribution = ATTRIBUTION
    _symbol: Incomplete
    _attr_name: Incomplete
    _timeseries: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_icon: Incomplete
    def __init__(self, timeseries: TimeSeries, symbol: dict[str, str]) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def update(self) -> None: ...

class AlphaVantageForeignExchange(SensorEntity):
    _attr_attribution = ATTRIBUTION
    _foreign_exchange: Incomplete
    _from_currency: Incomplete
    _to_currency: Incomplete
    _attr_name: Incomplete
    _attr_icon: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, foreign_exchange: ForeignExchange, config: dict[str, str]) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def update(self) -> None: ...
