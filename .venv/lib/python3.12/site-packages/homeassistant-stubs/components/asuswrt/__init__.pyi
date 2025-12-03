from .router import AsusWrtRouter as AsusWrtRouter
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant

PLATFORMS: Incomplete
type AsusWrtConfigEntry = ConfigEntry[AsusWrtRouter]

async def async_setup_entry(hass: HomeAssistant, entry: AsusWrtConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AsusWrtConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: AsusWrtConfigEntry) -> None: ...
