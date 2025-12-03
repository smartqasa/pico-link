from .const import CONF_SERVICE_ACCOUNT_INFO as CONF_SERVICE_ACCOUNT_INFO, CONF_STT_MODEL as CONF_STT_MODEL, DEFAULT_STT_MODEL as DEFAULT_STT_MODEL, DOMAIN as DOMAIN, STT_LANGUAGES as STT_LANGUAGES
from _typeshed import Incomplete
from collections.abc import AsyncIterable
from google.cloud import speech_v1
from homeassistant.components.stt import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, SpeechMetadata as SpeechMetadata, SpeechResult as SpeechResult, SpeechResultState as SpeechResultState, SpeechToTextEntity as SpeechToTextEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GoogleCloudSpeechToTextEntity(SpeechToTextEntity):
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _entry: Incomplete
    _client: Incomplete
    _model: Incomplete
    def __init__(self, entry: ConfigEntry, client: speech_v1.SpeechAsyncClient) -> None: ...
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_formats(self) -> list[AudioFormats]: ...
    @property
    def supported_codecs(self) -> list[AudioCodecs]: ...
    @property
    def supported_bit_rates(self) -> list[AudioBitRates]: ...
    @property
    def supported_sample_rates(self) -> list[AudioSampleRates]: ...
    @property
    def supported_channels(self) -> list[AudioChannels]: ...
    async def async_process_audio_stream(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> SpeechResult: ...
