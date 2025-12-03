from . import BMWConfigEntry as BMWConfigEntry
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from .entity import BMWBaseEntity as BMWBaseEntity
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfLength as UnitOfLength, UnitOfPressure as UnitOfPressure, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True)
class BMWSensorEntityDescription(SensorEntityDescription):
    key_class: str | None = ...
    is_available: Callable[[MyBMWVehicle], bool] = ...

TIRES: Incomplete
SENSOR_TYPES: list[BMWSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: BMWConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWSensor(BMWBaseEntity, SensorEntity):
    entity_description: BMWSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
