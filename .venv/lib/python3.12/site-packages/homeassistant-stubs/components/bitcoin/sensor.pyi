from _typeshed import Incomplete
from blockchain import exchangerates, statistics
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_CURRENCY as CONF_CURRENCY, CONF_DISPLAY_OPTIONS as CONF_DISPLAY_OPTIONS, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
DEFAULT_CURRENCY: str
SCAN_INTERVAL: Incomplete
SENSOR_TYPES: tuple[SensorEntityDescription, ...]
OPTION_KEYS: Incomplete
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class BitcoinSensor(SensorEntity):
    _attr_attribution: str
    _attr_icon: str
    entity_description: Incomplete
    data: Incomplete
    _currency: Incomplete
    def __init__(self, data: BitcoinData, currency: str, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def update(self) -> None: ...

class BitcoinData:
    stats: statistics.Stats
    ticker: dict[str, exchangerates.Currency]
    def update(self) -> None: ...
