from .coordinator import GlancesDataUpdateCoordinator as GlancesDataUpdateCoordinator
from _typeshed import Incomplete
from glances_api import Glances
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from typing import Any

PLATFORMS: Incomplete
_LOGGER: Incomplete
type GlancesConfigEntry = ConfigEntry[GlancesDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, config_entry: GlancesConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GlancesConfigEntry) -> bool: ...
async def get_api(hass: HomeAssistant, entry_data: dict[str, Any]) -> Glances: ...

class ServerVersionMismatch(HomeAssistantError): ...
