from . import BMWConfigEntry as BMWConfigEntry
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from .entity import BMWBaseEntity as BMWBaseEntity
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class BMWNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[MyBMWVehicle], float | int | None]
    remote_service: Callable[[MyBMWVehicle, float | int], Coroutine[Any, Any, Any]]
    is_available: Callable[[MyBMWVehicle], bool] = ...
    dynamic_options: Callable[[MyBMWVehicle], list[str]] | None = ...

NUMBER_TYPES: list[BMWNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: BMWConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWNumber(BMWBaseEntity, NumberEntity):
    entity_description: BMWNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
