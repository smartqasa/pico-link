from .coordinator import SmDataUpdateCoordinator as SmDataUpdateCoordinator, SmFirmwareUpdateCoordinator as SmFirmwareUpdateCoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

@dataclass(kw_only=True)
class SmlightData:
    data: SmDataUpdateCoordinator
    firmware: SmFirmwareUpdateCoordinator
type SmConfigEntry = ConfigEntry[SmlightData]

async def async_setup_entry(hass: HomeAssistant, entry: SmConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SmConfigEntry) -> bool: ...
