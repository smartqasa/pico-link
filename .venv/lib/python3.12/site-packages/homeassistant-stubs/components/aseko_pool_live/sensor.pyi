from .coordinator import AsekoConfigEntry as AsekoConfigEntry
from .entity import AsekoEntity as AsekoEntity
from aioaseko import Unit as Unit
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class AsekoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Unit], StateType]

SENSORS: list[AsekoSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: AsekoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsekoSensorEntity(AsekoEntity, SensorEntity):
    entity_description: AsekoSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
