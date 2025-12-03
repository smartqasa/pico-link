from .coordinator import ElgatoConfigEntry as ElgatoConfigEntry, ElgatoData as ElgatoData, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ElgatoSensorEntityDescription(SensorEntityDescription):
    has_fn: Callable[[ElgatoData], bool] = ...
    value_fn: Callable[[ElgatoData], float | int | None]

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElgatoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoSensorEntity(ElgatoEntity, SensorEntity):
    entity_description: ElgatoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
