import voluptuous as vol
from .const import ATTR_BUTTON as ATTR_BUTTON, ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_PAYLOAD as ATTR_PAYLOAD, ATTR_SOUND_OUTPUT as ATTR_SOUND_OUTPUT, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, SERVICE_BUTTON as SERVICE_BUTTON, SERVICE_COMMAND as SERVICE_COMMAND, SERVICE_SELECT_SOUND_OUTPUT as SERVICE_SELECT_SOUND_OUTPUT, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from _typeshed import Incomplete
from aiowebostv import WebOsClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import NamedTuple

CONFIG_SCHEMA: Incomplete
CALL_SCHEMA: Incomplete

class ServiceMethodDetails(NamedTuple):
    method: str
    schema: vol.Schema

BUTTON_SCHEMA: Incomplete
COMMAND_SCHEMA: Incomplete
SOUND_OUTPUT_SCHEMA: Incomplete
SERVICE_TO_METHOD: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_control_connect(host: str, key: str | None) -> WebOsClient: ...
def update_client_key(hass: HomeAssistant, entry: ConfigEntry, client: WebOsClient) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
