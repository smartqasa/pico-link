from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, TTN_API_HOST as TTN_API_HOST
from .coordinator import TTNCoordinator as TTNCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
