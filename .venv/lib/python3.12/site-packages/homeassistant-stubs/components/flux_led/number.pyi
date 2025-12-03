import abc
from .const import DOMAIN as DOMAIN
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxEntity as FluxEntity
from .util import _effect_brightness as _effect_brightness
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Coroutine
from homeassistant import config_entries as config_entries
from homeassistant.components.light import EFFECT_RANDOM as EFFECT_RANDOM
from homeassistant.components.number import NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
DEBOUNCE_TIME: int

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxSpeedNumber(FluxEntity, CoordinatorEntity[FluxLedUpdateCoordinator], NumberEntity):
    _attr_native_min_value: int
    _attr_native_max_value: int
    _attr_native_step: int
    _attr_mode: Incomplete
    _attr_translation_key: str
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...

class FluxConfigNumber(FluxEntity, CoordinatorEntity[FluxLedUpdateCoordinator], NumberEntity, metaclass=abc.ABCMeta):
    _attr_entity_category: Incomplete
    _attr_native_min_value: int
    _attr_native_step: int
    _attr_mode: Incomplete
    _debouncer: Debouncer[Coroutine[Any, Any, None]] | None
    _pending_value: int | None
    def __init__(self, coordinator: FluxLedUpdateCoordinator, base_unique_id: str, key: str | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    @abstractmethod
    async def _async_set_native_value(self) -> None: ...
    def _pixels_and_segments_fit_in_music_mode(self) -> bool: ...

class FluxPixelsPerSegmentNumber(FluxConfigNumber):
    _attr_translation_key: str
    @property
    def native_max_value(self) -> int: ...
    @property
    def native_value(self) -> int: ...
    async def _async_set_native_value(self) -> None: ...

class FluxSegmentsNumber(FluxConfigNumber):
    _attr_translation_key: str
    @property
    def native_max_value(self) -> int: ...
    @property
    def native_value(self) -> int: ...
    async def _async_set_native_value(self) -> None: ...

class FluxMusicNumber(FluxConfigNumber, metaclass=abc.ABCMeta):
    @property
    def available(self) -> bool: ...

class FluxMusicPixelsPerSegmentNumber(FluxMusicNumber):
    _attr_translation_key: str
    @property
    def native_max_value(self) -> int: ...
    @property
    def native_value(self) -> int: ...
    async def _async_set_native_value(self) -> None: ...

class FluxMusicSegmentsNumber(FluxMusicNumber):
    _attr_translation_key: str
    @property
    def native_max_value(self) -> int: ...
    @property
    def native_value(self) -> int: ...
    async def _async_set_native_value(self) -> None: ...
