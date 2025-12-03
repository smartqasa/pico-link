from . import BMWConfigEntry as BMWConfigEntry
from .const import UNIT_MAP as UNIT_MAP
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from .entity import BMWBaseEntity as BMWBaseEntity
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from bimmer_connected.vehicle.reports import ConditionBasedService as ConditionBasedService
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_system import UnitSystem as UnitSystem
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete
ALLOWED_CONDITION_BASED_SERVICE_KEYS: Incomplete
LOGGED_CONDITION_BASED_SERVICE_WARNINGS: set[str]
ALLOWED_CHECK_CONTROL_MESSAGE_KEYS: Incomplete
LOGGED_CHECK_CONTROL_MESSAGE_WARNINGS: set[str]

def _condition_based_services(vehicle: MyBMWVehicle, unit_system: UnitSystem) -> dict[str, Any]: ...
def _check_control_messages(vehicle: MyBMWVehicle) -> dict[str, Any]: ...
def _format_cbs_report(report: ConditionBasedService, unit_system: UnitSystem) -> dict[str, Any]: ...

@dataclass(frozen=True, kw_only=True)
class BMWBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[MyBMWVehicle], bool]
    attr_fn: Callable[[MyBMWVehicle, UnitSystem], dict[str, Any]] | None = ...
    is_available: Callable[[MyBMWVehicle], bool] = ...

SENSOR_TYPES: tuple[BMWBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: BMWConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWBinarySensor(BMWBaseEntity, BinarySensorEntity):
    entity_description: BMWBinarySensorEntityDescription
    _unit_system: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWBinarySensorEntityDescription, unit_system: UnitSystem) -> None: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
