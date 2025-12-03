from .const import CONF_LANGUAGE_CODE as CONF_LANGUAGE_CODE, DATA_MEM_STORAGE as DATA_MEM_STORAGE, DATA_SESSION as DATA_SESSION, DOMAIN as DOMAIN, SUPPORTED_LANGUAGE_CODES as SUPPORTED_LANGUAGE_CODES
from _typeshed import Incomplete
from aiohttp import web
from dataclasses import dataclass
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.media_player import ATTR_MEDIA_ANNOUNCE as ATTR_MEDIA_ANNOUNCE, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, MediaType as MediaType, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from homeassistant.helpers.event import async_call_later as async_call_later

_LOGGER: Incomplete
DEFAULT_LANGUAGE_CODES: Incomplete

@dataclass
class CommandResponse:
    text: str

async def async_send_text_commands(hass: HomeAssistant, commands: list[str], media_players: list[str] | None = None) -> list[CommandResponse]: ...
def default_language_code(hass: HomeAssistant) -> str: ...
def best_matching_language_code(hass: HomeAssistant, assist_language: str, agent_language: str | None = None) -> str: ...

class InMemoryStorage:
    hass: HomeAssistant
    mem: dict[str, bytes]
    def __init__(self, hass: HomeAssistant) -> None: ...
    def store_and_get_identifier(self, data: bytes) -> str: ...
    def retrieve(self, identifier: str) -> bytes | None: ...

class GoogleAssistantSDKAudioView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    mem_storage: InMemoryStorage
    def __init__(self, mem_storage: InMemoryStorage) -> None: ...
    async def get(self, request: web.Request, filename: str) -> web.Response: ...
