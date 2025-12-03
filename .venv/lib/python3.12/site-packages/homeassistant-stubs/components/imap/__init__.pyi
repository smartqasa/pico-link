from .const import CONF_ENABLE_PUSH as CONF_ENABLE_PUSH, DOMAIN as DOMAIN
from .coordinator import ImapDataUpdateCoordinator as ImapDataUpdateCoordinator, ImapMessage as ImapMessage, ImapPollingDataUpdateCoordinator as ImapPollingDataUpdateCoordinator, ImapPushDataUpdateCoordinator as ImapPushDataUpdateCoordinator, connect_to_server as connect_to_server
from .errors import InvalidAuth as InvalidAuth, InvalidFolder as InvalidFolder
from _typeshed import Incomplete
from aioimaplib import IMAP4_SSL as IMAP4_SSL, Response as Response
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[Platform]
CONF_ENTRY: str
CONF_SEEN: str
CONF_UID: str
CONF_TARGET_FOLDER: str
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
_SERVICE_UID_SCHEMA: Incomplete
SERVICE_SEEN_SCHEMA = _SERVICE_UID_SCHEMA
SERVICE_MOVE_SCHEMA: Incomplete
SERVICE_DELETE_SCHEMA = _SERVICE_UID_SCHEMA
SERVICE_FETCH_TEXT_SCHEMA = _SERVICE_UID_SCHEMA
type ImapConfigEntry = ConfigEntry[ImapDataUpdateCoordinator]

async def async_get_imap_client(hass: HomeAssistant, entry_id: str) -> IMAP4_SSL: ...
@callback
def raise_on_error(response: Response, translation_key: str) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ImapConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ImapConfigEntry) -> bool: ...
