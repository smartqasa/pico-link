from .controller import EcovacsController as EcovacsController
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from sucks import VacBot as VacBot

PLATFORMS: Incomplete
type EcovacsConfigEntry = ConfigEntry[EcovacsController]

async def async_setup_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EcovacsConfigEntry) -> bool: ...
