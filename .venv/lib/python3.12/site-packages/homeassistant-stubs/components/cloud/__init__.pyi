from . import account_link as account_link, backup as backup, http_api as http_api
from .client import CloudClient as CloudClient
from .const import CONF_ACCOUNTS_SERVER as CONF_ACCOUNTS_SERVER, CONF_ACCOUNT_LINK_SERVER as CONF_ACCOUNT_LINK_SERVER, CONF_ACME_SERVER as CONF_ACME_SERVER, CONF_ALEXA as CONF_ALEXA, CONF_ALEXA_SERVER as CONF_ALEXA_SERVER, CONF_ALIASES as CONF_ALIASES, CONF_CLOUDHOOK_SERVER as CONF_CLOUDHOOK_SERVER, CONF_COGNITO_CLIENT_ID as CONF_COGNITO_CLIENT_ID, CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_FILTER as CONF_FILTER, CONF_GOOGLE_ACTIONS as CONF_GOOGLE_ACTIONS, CONF_RELAYER_SERVER as CONF_RELAYER_SERVER, CONF_REMOTESTATE_SERVER as CONF_REMOTESTATE_SERVER, CONF_SERVICEHANDLERS_SERVER as CONF_SERVICEHANDLERS_SERVER, CONF_THINGTALK_SERVER as CONF_THINGTALK_SERVER, CONF_USER_POOL_ID as CONF_USER_POOL_ID, DATA_CLOUD as DATA_CLOUD, DATA_PLATFORMS_SETUP as DATA_PLATFORMS_SETUP, DOMAIN as DOMAIN, MODE_DEV as MODE_DEV, MODE_PROD as MODE_PROD
from .prefs import CloudPreferences as CloudPreferences
from .repairs import async_manage_legacy_subscription_issue as async_manage_legacy_subscription_issue
from .subscription import async_subscription_info as async_subscription_info
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from enum import Enum
from hass_nabucasa import Cloud
from homeassistant.components import alexa as alexa, google_assistant as google_assistant
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_SYSTEM as SOURCE_SYSTEM
from homeassistant.const import CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_REGION as CONF_REGION, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entityfilter as entityfilter
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.signal_type import SignalType as SignalType

DEFAULT_MODE = MODE_PROD
PLATFORMS: Incomplete
SERVICE_REMOTE_CONNECT: str
SERVICE_REMOTE_DISCONNECT: str
SIGNAL_CLOUD_CONNECTION_STATE: SignalType[CloudConnectionState]
STARTUP_REPAIR_DELAY: int
ALEXA_ENTITY_SCHEMA: Incomplete
GOOGLE_ENTITY_SCHEMA: Incomplete
ASSISTANT_SCHEMA: Incomplete
ALEXA_SCHEMA: Incomplete
GACTIONS_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

class CloudNotAvailable(HomeAssistantError): ...
class CloudNotConnected(CloudNotAvailable): ...

class CloudConnectionState(Enum):
    CLOUD_CONNECTED = 'cloud_connected'
    CLOUD_DISCONNECTED = 'cloud_disconnected'

@bind_hass
@callback
def async_is_logged_in(hass: HomeAssistant) -> bool: ...
@bind_hass
@callback
def async_is_connected(hass: HomeAssistant) -> bool: ...
@callback
def async_listen_connection_change(hass: HomeAssistant, target: Callable[[CloudConnectionState], Awaitable[None] | None]) -> Callable[[], None]: ...
@bind_hass
@callback
def async_active_subscription(hass: HomeAssistant) -> bool: ...
async def async_get_or_create_cloudhook(hass: HomeAssistant, webhook_id: str) -> str: ...
@bind_hass
async def async_create_cloudhook(hass: HomeAssistant, webhook_id: str) -> str: ...
@bind_hass
async def async_delete_cloudhook(hass: HomeAssistant, webhook_id: str) -> None: ...
@bind_hass
@callback
def async_remote_ui_url(hass: HomeAssistant) -> str: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _remote_handle_prefs_updated(cloud: Cloud[CloudClient]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
@callback
def _setup_services(hass: HomeAssistant, prefs: CloudPreferences) -> None: ...
