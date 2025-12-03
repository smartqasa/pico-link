from .const import DEFAULT_ACCESS as DEFAULT_ACCESS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector

type GoogleSheetsConfigEntry = ConfigEntry[OAuth2Session]
DATA: str
DATA_CONFIG_ENTRY: str
WORKSHEET: str
SERVICE_APPEND_SHEET: str
SHEET_SERVICE_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: GoogleSheetsConfigEntry) -> bool: ...
def async_entry_has_scopes(hass: HomeAssistant, entry: GoogleSheetsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoogleSheetsConfigEntry) -> bool: ...
async def async_setup_service(hass: HomeAssistant) -> None: ...
