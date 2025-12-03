from .const import CONF_LANGUAGE_CODE as CONF_LANGUAGE_CODE, DATA_MEM_STORAGE as DATA_MEM_STORAGE, DATA_SESSION as DATA_SESSION, DOMAIN as DOMAIN, SUPPORTED_LANGUAGE_CODES as SUPPORTED_LANGUAGE_CODES
from .helpers import GoogleAssistantSDKAudioView as GoogleAssistantSDKAudioView, InMemoryStorage as InMemoryStorage, async_send_text_commands as async_send_text_commands, best_matching_language_code as best_matching_language_code
from _typeshed import Incomplete
from gassist_text import TextAssistant
from homeassistant.components import conversation as conversation
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery, intent as intent
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.typing import ConfigType as ConfigType

SERVICE_SEND_TEXT_COMMAND: str
SERVICE_SEND_TEXT_COMMAND_FIELD_COMMAND: str
SERVICE_SEND_TEXT_COMMAND_FIELD_MEDIA_PLAYER: str
SERVICE_SEND_TEXT_COMMAND_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_setup_service(hass: HomeAssistant) -> None: ...

class GoogleAssistantConversationAgent(conversation.AbstractConversationAgent):
    hass: Incomplete
    entry: Incomplete
    assistant: TextAssistant | None
    session: OAuth2Session | None
    language: str | None
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    @property
    def supported_languages(self) -> list[str]: ...
    async def async_process(self, user_input: conversation.ConversationInput) -> conversation.ConversationResult: ...
