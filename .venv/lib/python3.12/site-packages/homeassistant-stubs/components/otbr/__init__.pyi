from . import websocket_api as websocket_api
from .const import DOMAIN as DOMAIN
from .util import GetBorderAgentIdNotSupported as GetBorderAgentIdNotSupported, OTBRData as OTBRData, update_issues as update_issues, update_unique_id as update_unique_id
from _typeshed import Incomplete
from homeassistant.components.thread import async_add_dataset as async_add_dataset
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
type OTBRConfigEntry = ConfigEntry[OTBRData]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: OTBRConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OTBRConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: OTBRConfigEntry) -> None: ...
