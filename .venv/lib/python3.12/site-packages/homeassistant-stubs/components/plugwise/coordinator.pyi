from .const import DEFAULT_PORT as DEFAULT_PORT, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, GATEWAY_ID as GATEWAY_ID, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from plugwise import PlugwiseData

class PlugwiseDataUpdateCoordinator(DataUpdateCoordinator[PlugwiseData]):
    _connected: bool
    config_entry: ConfigEntry
    api: Incomplete
    _current_devices: set[str]
    new_devices: set[str]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _connect(self) -> None: ...
    async def _async_update_data(self) -> PlugwiseData: ...
    def _async_add_remove_devices(self, data: PlugwiseData, entry: ConfigEntry) -> None: ...
    def _async_remove_devices(self, data: PlugwiseData, entry: ConfigEntry) -> None: ...
