from . import TechnoVEConfigEntry as TechnoVEConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from .entity import TechnoVEEntity as TechnoVEEntity
from .helpers import technove_exception_handler as technove_exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from technove import TechnoVE as TechnoVE
from typing import Any

@dataclass(frozen=True, kw_only=True)
class TechnoVENumberDescription(NumberEntityDescription):
    native_max_value_fn: Callable[[TechnoVE], float]
    native_value_fn: Callable[[TechnoVE], float]
    set_value_fn: Callable[[TechnoVEDataUpdateCoordinator, float], Coroutine[Any, Any, None]]

async def _set_max_current(coordinator: TechnoVEDataUpdateCoordinator, value: float) -> None: ...

NUMBERS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TechnoVEConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TechnoVENumberEntity(TechnoVEEntity, NumberEntity):
    entity_description: TechnoVENumberDescription
    def __init__(self, coordinator: TechnoVEDataUpdateCoordinator, description: TechnoVENumberDescription) -> None: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_value(self) -> float: ...
    @technove_exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
