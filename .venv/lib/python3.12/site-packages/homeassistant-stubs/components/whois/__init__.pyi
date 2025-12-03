from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS, SCAN_INTERVAL as SCAN_INTERVAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from whois import Domain as Domain

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
