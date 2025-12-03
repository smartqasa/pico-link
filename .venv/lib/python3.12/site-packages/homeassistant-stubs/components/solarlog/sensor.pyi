from . import SolarlogConfigEntry as SolarlogConfigEntry
from .entity import SolarLogCoordinatorEntity as SolarLogCoordinatorEntity, SolarLogInverterEntity as SolarLogInverterEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from solarlog_cli.solarlog_models import InverterData as InverterData, SolarlogData as SolarlogData

@dataclass(frozen=True, kw_only=True)
class SolarLogCoordinatorSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SolarlogData], StateType | datetime | None]

@dataclass(frozen=True, kw_only=True)
class SolarLogInverterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[InverterData], float | None]

SOLARLOG_SENSOR_TYPES: tuple[SolarLogCoordinatorSensorEntityDescription, ...]
INVERTER_SENSOR_TYPES: tuple[SolarLogInverterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarlogConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SolarLogCoordinatorSensor(SolarLogCoordinatorEntity, SensorEntity):
    entity_description: SolarLogCoordinatorSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

class SolarLogInverterSensor(SolarLogInverterEntity, SensorEntity):
    entity_description: SolarLogInverterSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
