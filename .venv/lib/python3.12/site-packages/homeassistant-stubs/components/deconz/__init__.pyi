from .config_flow import get_master_hub as get_master_hub
from .const import CONF_MASTER_GATEWAY as CONF_MASTER_GATEWAY, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .deconz_event import async_setup_events as async_setup_events, async_unload_events as async_unload_events
from .errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .hub import DeconzHub as DeconzHub, get_deconz_api as get_deconz_api
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_update_master_hub(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
