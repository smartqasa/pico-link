from .const import CONF_SECRET as CONF_SECRET, DOMAIN as DOMAIN
from _typeshed import Incomplete
from airthings import AirthingsDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
PLATFORMS: list[Platform]
SCAN_INTERVAL: Incomplete
type AirthingsDataCoordinatorType = DataUpdateCoordinator[dict[str, AirthingsDevice]]
type AirthingsConfigEntry = ConfigEntry[AirthingsDataCoordinatorType]

async def async_setup_entry(hass: HomeAssistant, entry: AirthingsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirthingsConfigEntry) -> bool: ...
