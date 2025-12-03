from . import AutomowerConfigEntry as AutomowerConfigEntry, remove_work_area_entities as remove_work_area_entities
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerControlEntity as AutomowerControlEntity, WorkAreaControlEntity as WorkAreaControlEntity, _work_area_translation_key as _work_area_translation_key, handle_sending_exception as handle_sending_exception
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes, WorkArea as WorkArea
from aioautomower.session import AutomowerSession as AutomowerSession
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@callback
def _async_get_cutting_height(data: MowerAttributes) -> int: ...
async def async_set_work_area_cutting_height(coordinator: AutomowerDataUpdateCoordinator, mower_id: str, cheight: float, work_area_id: int) -> None: ...
async def async_set_cutting_height(session: AutomowerSession, mower_id: str, cheight: float) -> None: ...

@dataclass(frozen=True, kw_only=True)
class AutomowerNumberEntityDescription(NumberEntityDescription):
    exists_fn: Callable[[MowerAttributes], bool] = ...
    value_fn: Callable[[MowerAttributes], int]
    set_value_fn: Callable[[AutomowerSession, str, float], Awaitable[Any]]

MOWER_NUMBER_TYPES: tuple[AutomowerNumberEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class WorkAreaNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[WorkArea], int]
    translation_key_fn: Callable[[int, str], str]
    set_value_fn: Callable[[AutomowerDataUpdateCoordinator, str, float, int], Awaitable[Any]]

WORK_AREA_NUMBER_TYPES: tuple[WorkAreaNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerNumberEntity(AutomowerControlEntity, NumberEntity):
    entity_description: AutomowerNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: AutomowerNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...

class WorkAreaNumberEntity(WorkAreaControlEntity, NumberEntity):
    entity_description: WorkAreaNumberEntityDescription
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: WorkAreaNumberEntityDescription, work_area_id: int) -> None: ...
    @property
    def translation_key(self) -> str: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
