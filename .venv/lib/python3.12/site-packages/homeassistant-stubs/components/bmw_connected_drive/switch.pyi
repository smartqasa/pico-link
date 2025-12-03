from . import BMWConfigEntry as BMWConfigEntry
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from .entity import BMWBaseEntity as BMWBaseEntity
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class BMWSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[MyBMWVehicle], bool]
    remote_service_on: Callable[[MyBMWVehicle], Coroutine[Any, Any, Any]]
    remote_service_off: Callable[[MyBMWVehicle], Coroutine[Any, Any, Any]]
    is_available: Callable[[MyBMWVehicle], bool] = ...
    dynamic_options: Callable[[MyBMWVehicle], list[str]] | None = ...

CHARGING_STATE_ON: Incomplete
NUMBER_TYPES: list[BMWSwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: BMWConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWSwitch(BMWBaseEntity, SwitchEntity):
    entity_description: BMWSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
