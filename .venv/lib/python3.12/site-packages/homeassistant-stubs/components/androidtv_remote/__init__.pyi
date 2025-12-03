from .helpers import create_api as create_api, get_enable_ime as get_enable_ime
from _typeshed import Incomplete
from androidtvremote2 import AndroidTVRemote
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
PLATFORMS: list[Platform]
AndroidTVRemoteConfigEntry = ConfigEntry[AndroidTVRemote]

async def async_setup_entry(hass: HomeAssistant, entry: AndroidTVRemoteConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
