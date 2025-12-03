from .const import CONF_BASE_PATH as CONF_BASE_PATH, CONF_UPCOMING_DAYS as CONF_UPCOMING_DAYS, CONF_WANTED_MAX_ITEMS as CONF_WANTED_MAX_ITEMS, DEFAULT_UPCOMING_DAYS as DEFAULT_UPCOMING_DAYS, DEFAULT_WANTED_MAX_ITEMS as DEFAULT_WANTED_MAX_ITEMS, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import CalendarDataUpdateCoordinator as CalendarDataUpdateCoordinator, CommandsDataUpdateCoordinator as CommandsDataUpdateCoordinator, DiskSpaceDataUpdateCoordinator as DiskSpaceDataUpdateCoordinator, QueueDataUpdateCoordinator as QueueDataUpdateCoordinator, SeriesDataUpdateCoordinator as SeriesDataUpdateCoordinator, SonarrDataUpdateCoordinator as SonarrDataUpdateCoordinator, StatusDataUpdateCoordinator as StatusDataUpdateCoordinator, WantedDataUpdateCoordinator as WantedDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
