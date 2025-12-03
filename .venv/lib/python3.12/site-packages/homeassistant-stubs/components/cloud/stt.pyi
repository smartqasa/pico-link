from .assist_pipeline import async_migrate_cloud_pipeline_engine as async_migrate_cloud_pipeline_engine
from .client import CloudClient as CloudClient
from .const import DATA_CLOUD as DATA_CLOUD, DATA_PLATFORMS_SETUP as DATA_PLATFORMS_SETUP, STT_ENTITY_UNIQUE_ID as STT_ENTITY_UNIQUE_ID
from _typeshed import Incomplete
from collections.abc import AsyncIterable
from hass_nabucasa import Cloud as Cloud
from homeassistant.components.stt import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, SpeechMetadata as SpeechMetadata, SpeechResult as SpeechResult, SpeechResultState as SpeechResultState, SpeechToTextEntity as SpeechToTextEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.setup import async_when_setup as async_when_setup

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CloudProviderEntity(SpeechToTextEntity):
    _attr_name: str
    _attr_unique_id = STT_ENTITY_UNIQUE_ID
    cloud: Incomplete
    def __init__(self, cloud: Cloud[CloudClient]) -> None: ...
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
    async def async_added_to_hass(self) -> None: ...
    async def async_process_audio_stream(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> SpeechResult: ...
