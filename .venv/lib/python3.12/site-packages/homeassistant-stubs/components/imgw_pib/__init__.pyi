from .const import CONF_STATION_ID as CONF_STATION_ID
from .coordinator import ImgwPibDataUpdateCoordinator as ImgwPibDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
_LOGGER: Incomplete
type ImgwPibConfigEntry = ConfigEntry[ImgwPibData]

@dataclass
class ImgwPibData:
    coordinator: ImgwPibDataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ImgwPibConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ImgwPibConfigEntry) -> bool: ...
