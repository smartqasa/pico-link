from .const import DATA_CONNECTIONS as DATA_CONNECTIONS, SIGNAL_WEBSOCKET_CONNECTED as SIGNAL_WEBSOCKET_CONNECTED, SIGNAL_WEBSOCKET_DISCONNECTED as SIGNAL_WEBSOCKET_DISCONNECTED
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class APICount(SensorEntity):
    _attr_name: str
    _attr_native_unit_of_measurement: str
    _attr_native_value: int
    def __init__(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _update_count(self) -> None: ...
