from .const import DATA_COMPONENT as DATA_COMPONENT, DATA_TTS_MANAGER as DATA_TTS_MANAGER, DOMAIN as DOMAIN
from .helper import get_engine_instance as get_engine_instance
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import TypedDict

URL_QUERY_TTS_OPTIONS: str

async def async_get_media_source(hass: HomeAssistant) -> TTSMediaSource: ...
@callback
def generate_media_source_id(hass: HomeAssistant, message: str, engine: str | None = None, language: str | None = None, options: dict | None = None, cache: bool | None = None) -> str: ...

class MediaSourceOptions(TypedDict):
    engine: str
    message: str
    language: str | None
    options: dict | None
    cache: bool | None

@callback
def media_source_id_to_kwargs(media_source_id: str) -> MediaSourceOptions: ...

class TTSMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    @callback
    def _engine_item(self, engine: str, params: str | None = None) -> BrowseMediaSource: ...
