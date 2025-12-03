from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkData as StarlinkData
from .entity import StarlinkEntity as StarlinkEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfDataRate as UnitOfDataRate, UnitOfEnergy as UnitOfEnergy, UnitOfInformation as UnitOfInformation, UnitOfPower as UnitOfPower, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import now as now

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class StarlinkSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[StarlinkData], datetime | StateType]

class StarlinkSensorEntity(StarlinkEntity, SensorEntity):
    entity_description: StarlinkSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

SENSORS: tuple[StarlinkSensorEntityDescription, ...]
