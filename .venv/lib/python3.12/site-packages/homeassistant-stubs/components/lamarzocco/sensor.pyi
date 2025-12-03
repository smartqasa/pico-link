from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccScaleEntity as LaMarzoccScaleEntity, LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylamarzocco.devices.machine import LaMarzoccoMachine as LaMarzoccoMachine

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSensorEntityDescription(LaMarzoccoEntityDescription, SensorEntityDescription):
    value_fn: Callable[[LaMarzoccoMachine], float | int]

ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]
STATISTIC_ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]
SCALE_ENTITIES: tuple[LaMarzoccoSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoSensorEntity(LaMarzoccoEntity, SensorEntity):
    entity_description: LaMarzoccoSensorEntityDescription
    @property
    def native_value(self) -> int | float: ...

class LaMarzoccoScaleSensorEntity(LaMarzoccoSensorEntity, LaMarzoccScaleEntity):
    entity_description: LaMarzoccoSensorEntityDescription
