from .const import CONF_SOURCE_ID as CONF_SOURCE_ID, LOGGER as LOGGER
from .dms import get_domain_data as get_domain_data
from .util import generate_source_id as generate_source_id
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
