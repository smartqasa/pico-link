from .hub import PulseHub as PulseHub
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

CONF_HUBS: str
PLATFORMS: Incomplete
type AcmedaConfigEntry = ConfigEntry[PulseHub]

async def async_setup_entry(hass: HomeAssistant, config_entry: AcmedaConfigEntry) -> bool: ...
async def _migrate_unique_ids(hass: HomeAssistant, entry: AcmedaConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: AcmedaConfigEntry) -> bool: ...
