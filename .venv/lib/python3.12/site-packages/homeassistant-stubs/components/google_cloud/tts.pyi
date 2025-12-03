import voluptuous as vol
from .const import CONF_ENCODING as CONF_ENCODING, CONF_GAIN as CONF_GAIN, CONF_GENDER as CONF_GENDER, CONF_KEY_FILE as CONF_KEY_FILE, CONF_PITCH as CONF_PITCH, CONF_PROFILES as CONF_PROFILES, CONF_SERVICE_ACCOUNT_INFO as CONF_SERVICE_ACCOUNT_INFO, CONF_SPEED as CONF_SPEED, CONF_TEXT_TYPE as CONF_TEXT_TYPE, CONF_VOICE as CONF_VOICE, DEFAULT_GAIN as DEFAULT_GAIN, DEFAULT_LANG as DEFAULT_LANG, DEFAULT_PITCH as DEFAULT_PITCH, DEFAULT_SPEED as DEFAULT_SPEED, DOMAIN as DOMAIN
from .helpers import async_tts_voices as async_tts_voices, tts_options_schema as tts_options_schema, tts_platform_schema as tts_platform_schema
from _typeshed import Incomplete
from google.cloud import texttospeech
from homeassistant.components.tts import CONF_LANG as CONF_LANG, Provider as Provider, TextToSpeechEntity as TextToSpeechEntity, TtsAudioType as TtsAudioType, Voice as Voice
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_get_engine(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> Provider | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BaseGoogleCloudProvider:
    _client: Incomplete
    _voices: Incomplete
    _language: Incomplete
    _options_schema: Incomplete
    def __init__(self, client: texttospeech.TextToSpeechAsyncClient, voices: dict[str, list[str]], language: str, options_schema: vol.Schema) -> None: ...
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def default_language(self) -> str: ...
    @property
    def supported_options(self) -> list[str]: ...
    @property
    def default_options(self) -> dict[str, Any]: ...
    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice] | None: ...
    async def _async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...

class GoogleCloudTTSEntity(BaseGoogleCloudProvider, TextToSpeechEntity):
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _entry: Incomplete
    def __init__(self, entry: ConfigEntry, client: texttospeech.TextToSpeechAsyncClient, voices: dict[str, list[str]], language: str, options_schema: vol.Schema) -> None: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...

class GoogleCloudTTSProvider(BaseGoogleCloudProvider, Provider):
    name: str
    def __init__(self, client: texttospeech.TextToSpeechAsyncClient, voices: dict[str, list[str]], language: str, options_schema: vol.Schema) -> None: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
