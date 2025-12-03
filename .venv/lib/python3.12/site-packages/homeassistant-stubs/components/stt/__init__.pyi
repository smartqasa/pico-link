import abc
from .const import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, DOMAIN as DOMAIN, SpeechResultState as SpeechResultState
from .legacy import Provider as Provider, async_get_provider as async_get_provider
from .models import SpeechMetadata as SpeechMetadata, SpeechResult as SpeechResult
from _typeshed import Incomplete
from abc import abstractmethod
from aiohttp import web
from collections.abc import AsyncIterable
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.restore_state import RestoreEntity
from typing import final

__all__ = ['async_get_provider', 'async_get_speech_to_text_engine', 'async_get_speech_to_text_entity', 'AudioBitRates', 'AudioChannels', 'AudioCodecs', 'AudioFormats', 'AudioSampleRates', 'DOMAIN', 'Provider', 'SpeechToTextEntity', 'SpeechMetadata', 'SpeechResult', 'SpeechResultState']

@callback
def async_get_speech_to_text_entity(hass: HomeAssistant, entity_id: str) -> SpeechToTextEntity | None: ...
@callback
def async_get_speech_to_text_engine(hass: HomeAssistant, engine_id: str) -> SpeechToTextEntity | Provider | None: ...

class SpeechToTextEntity(RestoreEntity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    __last_processed: str | None
    @property
    @final
    def state(self) -> str | None: ...
    @property
    @abstractmethod
    def supported_languages(self) -> list[str]: ...
    @property
    @abstractmethod
    def supported_formats(self) -> list[AudioFormats]: ...
    @property
    @abstractmethod
    def supported_codecs(self) -> list[AudioCodecs]: ...
    @property
    @abstractmethod
    def supported_bit_rates(self) -> list[AudioBitRates]: ...
    @property
    @abstractmethod
    def supported_sample_rates(self) -> list[AudioSampleRates]: ...
    @property
    @abstractmethod
    def supported_channels(self) -> list[AudioChannels]: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @final
    async def internal_async_process_audio_stream(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> SpeechResult: ...
    @abstractmethod
    async def async_process_audio_stream(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> SpeechResult: ...
    @callback
    def check_metadata(self, metadata: SpeechMetadata) -> bool: ...

class SpeechToTextView(HomeAssistantView):
    _legacy_provider_reported: bool
    requires_auth: bool
    url: str
    name: str
    providers: Incomplete
    def __init__(self, providers: dict[str, Provider]) -> None: ...
    async def post(self, request: web.Request, provider: str) -> web.Response: ...
    async def get(self, request: web.Request, provider: str) -> web.Response: ...
    def _get_provider(self, hass: HomeAssistant, provider: str) -> Provider: ...
    def _suggest_report_issue(self, hass: HomeAssistant, provider: str, provider_instance: object) -> str: ...
