from homeassistant.components.hassio import get_os_info as get_os_info
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.hassio import is_hassio as is_hassio

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
