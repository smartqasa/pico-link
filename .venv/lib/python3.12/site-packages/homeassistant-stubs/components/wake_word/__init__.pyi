import abc
from .const import DOMAIN as DOMAIN
from .models import DetectionResult as DetectionResult, WakeWord as WakeWord
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import AsyncIterable
from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.restore_state import RestoreEntity
from typing import final

__all__ = ['async_default_entity', 'async_get_wake_word_detection_entity', 'DetectionResult', 'DOMAIN', 'WakeWord', 'WakeWordDetectionEntity']

@callback
def async_default_entity(hass: HomeAssistant) -> str | None: ...
@callback
def async_get_wake_word_detection_entity(hass: HomeAssistant, entity_id: str) -> WakeWordDetectionEntity | None: ...

class WakeWordDetectionEntity(RestoreEntity, metaclass=abc.ABCMeta):
    _attr_entity_category: Incomplete
    _attr_should_poll: bool
    __last_detected: str | None
    @property
    @final
    def state(self) -> str | None: ...
    @abstractmethod
    async def get_supported_wake_words(self) -> list[WakeWord]: ...
    @abstractmethod
    async def _async_process_audio_stream(self, stream: AsyncIterable[tuple[bytes, int]], wake_word_id: str | None) -> DetectionResult | None: ...
    async def async_process_audio_stream(self, stream: AsyncIterable[tuple[bytes, int]], wake_word_id: str | None) -> DetectionResult | None: ...
    async def async_internal_added_to_hass(self) -> None: ...
