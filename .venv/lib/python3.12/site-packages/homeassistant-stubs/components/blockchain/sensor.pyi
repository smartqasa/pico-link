from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

_LOGGER: Incomplete
CONF_ADDRESSES: str
DEFAULT_NAME: str
SCAN_INTERVAL: Incomplete
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class BlockchainSensor(SensorEntity):
    _attr_attribution: str
    _attr_icon: str
    _attr_native_unit_of_measurement: str
    _attr_name: Incomplete
    addresses: Incomplete
    def __init__(self, name: str, addresses: list[str]) -> None: ...
    _attr_native_value: Incomplete
    def update(self) -> None: ...
