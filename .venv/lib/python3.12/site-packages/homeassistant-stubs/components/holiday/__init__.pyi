from .const import CONF_CATEGORIES as CONF_CATEGORIES, CONF_PROVINCE as CONF_PROVINCE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.setup import SetupPhases as SetupPhases, async_pause_setup as async_pause_setup

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
