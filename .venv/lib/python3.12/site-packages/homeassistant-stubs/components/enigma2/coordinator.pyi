from .const import CONF_SOURCE_BOUQUET as CONF_SOURCE_BOUQUET, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity_component import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from openwebif.api import OpenWebIfDevice, OpenWebIfStatus

LOGGER: Incomplete

class Enigma2UpdateCoordinator(DataUpdateCoordinator[OpenWebIfStatus]):
    device: OpenWebIfDevice
    unique_id: str | None
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> OpenWebIfStatus: ...
