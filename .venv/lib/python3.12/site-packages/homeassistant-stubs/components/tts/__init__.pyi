import asyncio
from .const import DEFAULT_CACHE_DIR as DEFAULT_CACHE_DIR, TtsAudioType as TtsAudioType
from .legacy import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, Provider as Provider
from .media_source import generate_media_source_id as generate_media_source_id
from .models import Voice as Voice
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Mapping
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.helpers.typing import ConfigType
from propcache import cached_property
from typing import Any, TypedDict, final

__all__ = ['async_default_engine', 'async_get_media_source_audio', 'async_support_options', 'ATTR_AUDIO_OUTPUT', 'ATTR_PREFERRED_FORMAT', 'ATTR_PREFERRED_SAMPLE_RATE', 'ATTR_PREFERRED_SAMPLE_CHANNELS', 'ATTR_PREFERRED_SAMPLE_BYTES', 'CONF_LANG', 'DEFAULT_CACHE_DIR', 'generate_media_source_id', 'PLATFORM_SCHEMA_BASE', 'PLATFORM_SCHEMA', 'SampleFormat', 'Provider', 'TtsAudioType', 'Voice']

ATTR_AUDIO_OUTPUT: str
ATTR_PREFERRED_FORMAT: str
ATTR_PREFERRED_SAMPLE_RATE: str
ATTR_PREFERRED_SAMPLE_CHANNELS: str
ATTR_PREFERRED_SAMPLE_BYTES: str
CONF_LANG: str

class TTSCache(TypedDict):
    filename: str
    voice: bytes
    pending: asyncio.Task | None

@callback
def async_default_engine(hass: HomeAssistant) -> str | None: ...
async def async_support_options(hass: HomeAssistant, engine: str, language: str | None = None, options: dict | None = None) -> bool: ...
async def async_get_media_source_audio(hass: HomeAssistant, media_source_id: str) -> tuple[str, bytes]: ...

class TextToSpeechEntity(RestoreEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _attr_should_poll: bool
    __last_tts_loaded: str | None
    _attr_default_language: str
    _attr_default_options: Mapping[str, Any] | None
    _attr_supported_languages: list[str]
    _attr_supported_options: list[str] | None
    @property
    @final
    def state(self) -> str | None: ...
    @cached_property
    def supported_languages(self) -> list[str]: ...
    @cached_property
    def default_language(self) -> str: ...
    @cached_property
    def supported_options(self) -> list[str] | None: ...
    @cached_property
    def default_options(self) -> Mapping[str, Any] | None: ...
    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice] | None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_speak(self, media_player_entity_id: list[str], message: str, cache: bool, language: str | None = None, options: dict | None = None) -> None: ...
    @final
    async def internal_async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
    def get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...

class SpeechManager:
    hass: Incomplete
    providers: dict[str, Provider]
    use_cache: Incomplete
    cache_dir: Incomplete
    time_memory: Incomplete
    file_cache: dict[str, str]
    mem_cache: dict[str, TTSCache]
    filename_to_token: dict[str, str]
    token_to_filename: dict[str, str]
    def __init__(self, hass: HomeAssistant, use_cache: bool, cache_dir: str, time_memory: int) -> None: ...
    def _init_cache(self) -> dict[str, str]: ...
    async def async_init_cache(self) -> None: ...
    async def async_clear_cache(self) -> None: ...
    @callback
    def async_register_legacy_engine(self, engine: str, provider: Provider, config: ConfigType) -> None: ...
    @callback
    def process_options(self, engine_instance: TextToSpeechEntity | Provider, language: str | None, options: dict | None) -> tuple[str, dict[str, Any]]: ...
    async def async_get_url_path(self, engine: str, message: str, cache: bool | None = None, language: str | None = None, options: dict | None = None) -> str: ...
    async def async_get_tts_audio(self, engine: str, message: str, cache: bool | None = None, language: str | None = None, options: dict | None = None) -> tuple[str, bytes]: ...
    @callback
    def _generate_cache_key(self, message: str, language: str, options: dict | None, engine: str) -> str: ...
    async def _async_get_tts_audio(self, engine_instance: TextToSpeechEntity | Provider, cache_key: str, message: str, cache: bool, language: str, options: dict[str, Any]) -> str: ...
    async def _async_save_tts_audio(self, cache_key: str, filename: str, data: bytes) -> None: ...
    async def _async_file_to_mem(self, cache_key: str) -> None: ...
    @callback
    def _async_store_to_memcache(self, cache_key: str, filename: str, data: bytes) -> None: ...
    async def async_read_tts(self, token: str) -> tuple[str | None, bytes]: ...
    @staticmethod
    def write_tags(filename: str, data: bytes, engine_name: str, message: str, language: str, options: dict | None) -> bytes: ...

class TextToSpeechUrlView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    tts: Incomplete
    def __init__(self, tts: SpeechManager) -> None: ...
    async def post(self, request: web.Request) -> web.Response: ...

class TextToSpeechView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    tts: Incomplete
    def __init__(self, tts: SpeechManager) -> None: ...
    async def get(self, request: web.Request, filename: str) -> web.Response: ...

# Names in __all__ with no definition:
#   SampleFormat
