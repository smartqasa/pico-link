from . import BMWConfigEntry as BMWConfigEntry
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from .entity import BMWBaseEntity as BMWBaseEntity
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class BMWSelectEntityDescription(SelectEntityDescription):
    current_option: Callable[[MyBMWVehicle], str]
    remote_service: Callable[[MyBMWVehicle, str], Coroutine[Any, Any, Any]]
    is_available: Callable[[MyBMWVehicle], bool] = ...
    dynamic_options: Callable[[MyBMWVehicle], list[str]] | None = ...

SELECT_TYPES: tuple[BMWSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: BMWConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWSelect(BMWBaseEntity, SelectEntity):
    entity_description: BMWSelectEntityDescription
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWSelectEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
