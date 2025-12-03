from .coordinator import APCUPSdCoordinator as APCUPSdCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Final

type APCUPSdConfigEntry = ConfigEntry[APCUPSdCoordinator]
PLATFORMS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: APCUPSdConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: APCUPSdConfigEntry) -> bool: ...
