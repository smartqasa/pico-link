from .coordinator import CalendarUpdateCoordinator as CalendarUpdateCoordinator, DiskSpaceDataUpdateCoordinator as DiskSpaceDataUpdateCoordinator, HealthDataUpdateCoordinator as HealthDataUpdateCoordinator, MoviesDataUpdateCoordinator as MoviesDataUpdateCoordinator, QueueDataUpdateCoordinator as QueueDataUpdateCoordinator, RadarrDataUpdateCoordinator as RadarrDataUpdateCoordinator, StatusDataUpdateCoordinator as StatusDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete
type RadarrConfigEntry = ConfigEntry[RadarrData]

@dataclass(kw_only=True, slots=True)
class RadarrData:
    calendar: CalendarUpdateCoordinator
    disk_space: DiskSpaceDataUpdateCoordinator
    health: HealthDataUpdateCoordinator
    movie: MoviesDataUpdateCoordinator
    queue: QueueDataUpdateCoordinator
    status: StatusDataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: RadarrConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RadarrConfigEntry) -> bool: ...
