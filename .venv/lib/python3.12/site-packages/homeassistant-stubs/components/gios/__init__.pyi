from .const import CONF_STATION_ID as CONF_STATION_ID, DOMAIN as DOMAIN
from .coordinator import GiosDataUpdateCoordinator as GiosDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete
type GiosConfigEntry = ConfigEntry[GiosData]

@dataclass
class GiosData:
    coordinator: GiosDataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: GiosConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GiosConfigEntry) -> bool: ...
