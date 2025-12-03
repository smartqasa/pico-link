from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import FastdotcomDataUpdateCoordinator as FastdotcomDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.start import async_at_started as async_at_started

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
