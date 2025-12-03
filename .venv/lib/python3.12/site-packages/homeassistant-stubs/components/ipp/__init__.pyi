from .const import CONF_BASE_PATH as CONF_BASE_PATH
from .coordinator import IPPDataUpdateCoordinator as IPPDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete
type IPPConfigEntry = ConfigEntry[IPPDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: IPPConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
