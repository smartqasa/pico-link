from .const import CONF_HOSTNAME as CONF_HOSTNAME, CONF_IPV4 as CONF_IPV4, CONF_IPV6 as CONF_IPV6, CONF_PORT_IPV6 as CONF_PORT_IPV6, CONF_RESOLVER as CONF_RESOLVER, CONF_RESOLVER_IPV6 as CONF_RESOLVER_IPV6, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

DEFAULT_RETRIES: int
MAX_RESULTS: int
_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

def sort_ips(ips: list, querytype: str) -> list: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WanIpSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _unrecorded_attributes: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    hostname: Incomplete
    resolver: Incomplete
    querytype: Incomplete
    _retries: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, hostname: str, resolver: str, ipv6: bool, port: int) -> None: ...
    _attr_native_value: Incomplete
    _attr_available: bool
    async def async_update(self) -> None: ...
