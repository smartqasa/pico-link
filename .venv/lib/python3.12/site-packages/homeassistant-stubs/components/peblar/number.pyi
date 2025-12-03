from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarData as PeblarData, PeblarDataUpdateCoordinator as PeblarDataUpdateCoordinator, PeblarRuntimeData as PeblarRuntimeData
from .entity import PeblarEntity as PeblarEntity
from .helpers import peblar_exception_handler as peblar_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from peblar import PeblarApi as PeblarApi
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarNumberEntityDescription(NumberEntityDescription):
    native_max_value_fn: Callable[[PeblarRuntimeData], int]
    set_value_fn: Callable[[PeblarApi, float], Awaitable[Any]]
    value_fn: Callable[[PeblarData], int | None]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PeblarNumberEntity(PeblarEntity[PeblarDataUpdateCoordinator], NumberEntity):
    entity_description: PeblarNumberEntityDescription
    _attr_native_max_value: Incomplete
    def __init__(self, entry: PeblarConfigEntry, coordinator: PeblarDataUpdateCoordinator, description: PeblarNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
    @peblar_exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
