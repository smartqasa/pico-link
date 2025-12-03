from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, METOFFICE_COORDINATES as METOFFICE_COORDINATES, METOFFICE_DAILY_COORDINATOR as METOFFICE_DAILY_COORDINATOR, METOFFICE_HOURLY_COORDINATOR as METOFFICE_HOURLY_COORDINATOR, METOFFICE_NAME as METOFFICE_NAME, MODE_3HOURLY as MODE_3HOURLY, MODE_DAILY as MODE_DAILY
from .data import MetOfficeData as MetOfficeData
from .helpers import fetch_data as fetch_data, fetch_site as fetch_site
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import TimestampDataUpdateCoordinator as TimestampDataUpdateCoordinator

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def get_device_info(coordinates: str, name: str) -> DeviceInfo: ...
