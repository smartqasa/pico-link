from . import WLEDConfigEntry as WLEDConfigEntry
from .const import ATTR_INTENSITY as ATTR_INTENSITY, ATTR_SPEED as ATTR_SPEED
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from .helpers import wled_exception_handler as wled_exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from wled import Segment as Segment

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class WLEDNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[Segment], int | None]

NUMBERS: Incomplete

class WLEDNumber(WLEDEntity, NumberEntity):
    entity_description: WLEDNumberEntityDescription
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _segment: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int, description: WLEDNumberEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> float | None: ...
    @wled_exception_handler
    async def async_set_native_value(self, value: float) -> None: ...

@callback
def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
