from .base import FritzBoxPhonebook as FritzBoxPhonebook
from .const import CONF_PHONEBOOK as CONF_PHONEBOOK, CONF_PREFIXES as CONF_PREFIXES, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
type FritzBoxCallMonitorConfigEntry = ConfigEntry[FritzBoxPhonebook]

async def async_setup_entry(hass: HomeAssistant, config_entry: FritzBoxCallMonitorConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: FritzBoxCallMonitorConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: FritzBoxCallMonitorConfigEntry) -> None: ...
