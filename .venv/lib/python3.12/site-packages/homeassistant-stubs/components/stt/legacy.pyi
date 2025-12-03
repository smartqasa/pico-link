import abc
from .const import AudioBitRates as AudioBitRates, AudioChannels as AudioChannels, AudioCodecs as AudioCodecs, AudioFormats as AudioFormats, AudioSampleRates as AudioSampleRates, DATA_PROVIDERS as DATA_PROVIDERS, DOMAIN as DOMAIN
from .models import SpeechMetadata as SpeechMetadata, SpeechResult as SpeechResult
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import AsyncIterable, Coroutine
from homeassistant.config import config_per_platform as config_per_platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.setup import SetupPhases as SetupPhases, async_prepare_setup_platform as async_prepare_setup_platform, async_start_setup as async_start_setup
from typing import Any

_LOGGER: Incomplete

@callback
def async_default_provider(hass: HomeAssistant) -> str | None: ...
@callback
def async_get_provider(hass: HomeAssistant, domain: str | None = None) -> Provider | None: ...
@callback
def async_setup_legacy(hass: HomeAssistant, config: ConfigType) -> list[Coroutine[Any, Any, None]]: ...

class Provider(ABC, metaclass=abc.ABCMeta):
    hass: HomeAssistant | None
    name: str | None
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
    @abstractmethod
    async def async_process_audio_stream(self, metadata: SpeechMetadata, stream: AsyncIterable[bytes]) -> SpeechResult: ...
    @callback
    def check_metadata(self, metadata: SpeechMetadata) -> bool: ...
