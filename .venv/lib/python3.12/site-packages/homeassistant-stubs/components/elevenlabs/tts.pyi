from . import ElevenLabsConfigEntry as ElevenLabsConfigEntry
from .const import CONF_OPTIMIZE_LATENCY as CONF_OPTIMIZE_LATENCY, CONF_SIMILARITY as CONF_SIMILARITY, CONF_STABILITY as CONF_STABILITY, CONF_STYLE as CONF_STYLE, CONF_USE_SPEAKER_BOOST as CONF_USE_SPEAKER_BOOST, CONF_VOICE as CONF_VOICE, DEFAULT_OPTIMIZE_LATENCY as DEFAULT_OPTIMIZE_LATENCY, DEFAULT_SIMILARITY as DEFAULT_SIMILARITY, DEFAULT_STABILITY as DEFAULT_STABILITY, DEFAULT_STYLE as DEFAULT_STYLE, DEFAULT_USE_SPEAKER_BOOST as DEFAULT_USE_SPEAKER_BOOST, DOMAIN as DOMAIN
from _typeshed import Incomplete
from elevenlabs import AsyncElevenLabs as AsyncElevenLabs
from elevenlabs.types import Model as Model, Voice as ElevenLabsVoice, VoiceSettings
from homeassistant.components.tts import ATTR_VOICE as ATTR_VOICE, TextToSpeechEntity as TextToSpeechEntity, TtsAudioType as TtsAudioType, Voice as Voice
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from types import MappingProxyType
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

def to_voice_settings(options: MappingProxyType[str, Any]) -> VoiceSettings: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ElevenLabsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElevenLabsTTSEntity(TextToSpeechEntity):
    _attr_supported_options: Incomplete
    _attr_entity_category: Incomplete
    _client: Incomplete
    _model: Incomplete
    _default_voice_id: Incomplete
    _voices: Incomplete
    _voice_settings: Incomplete
    _latency: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_supported_languages: Incomplete
    _attr_default_language: Incomplete
    def __init__(self, client: AsyncElevenLabs, model: Model, voices: list[ElevenLabsVoice], default_voice_id: str, entry_id: str, title: str, voice_settings: VoiceSettings, latency: int = 0) -> None: ...
    def async_get_supported_voices(self, language: str) -> list[Voice]: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
