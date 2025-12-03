import abc
from .const import ATTR_CACHE as ATTR_CACHE, ATTR_LANGUAGE as ATTR_LANGUAGE, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_OPTIONS as ATTR_OPTIONS, CONF_CACHE as CONF_CACHE, CONF_CACHE_DIR as CONF_CACHE_DIR, CONF_FIELDS as CONF_FIELDS, CONF_TIME_MEMORY as CONF_TIME_MEMORY, DATA_TTS_MANAGER as DATA_TTS_MANAGER, DEFAULT_CACHE as DEFAULT_CACHE, DEFAULT_CACHE_DIR as DEFAULT_CACHE_DIR, DEFAULT_TIME_MEMORY as DEFAULT_TIME_MEMORY, DOMAIN as DOMAIN, TtsAudioType as TtsAudioType
from .media_source import generate_media_source_id as generate_media_source_id
from .models import Voice as Voice
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Coroutine, Mapping
from homeassistant.components.media_player import ATTR_MEDIA_ANNOUNCE as ATTR_MEDIA_ANNOUNCE, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, MediaType as MediaType, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA
from homeassistant.config import config_per_platform as config_per_platform
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.setup import SetupPhases as SetupPhases, async_prepare_setup_platform as async_prepare_setup_platform, async_start_setup as async_start_setup
from homeassistant.util.yaml import load_yaml_dict as load_yaml_dict
from typing import Any

_LOGGER: Incomplete
CONF_SERVICE_NAME: str

def _deprecated_platform(value: str) -> str: ...

PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SERVICE_SAY: str
SCHEMA_SERVICE_SAY: Incomplete

async def async_setup_legacy(hass: HomeAssistant, config: ConfigType) -> list[Coroutine[Any, Any, None]]: ...

class Provider(metaclass=abc.ABCMeta):
    hass: HomeAssistant | None
    name: str | None
    @property
    def default_language(self) -> str | None: ...
    @property
    @abstractmethod
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_options(self) -> list[str] | None: ...
    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice] | None: ...
    @property
    def default_options(self) -> Mapping[str, Any] | None: ...
    def get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
