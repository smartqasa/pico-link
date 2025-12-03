from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from gotailwind import TailwindDeviceStatus
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type TailwindConfigEntry = ConfigEntry[TailwindDataUpdateCoordinator]
class TailwindDataUpdateCoordinator(DataUpdateCoordinator[TailwindDeviceStatus]):
    tailwind: Incomplete
    def __init__(self, hass: HomeAssistant, entry: TailwindConfigEntry) -> None: ...
    async def _async_update_data(self) -> TailwindDeviceStatus: ...
