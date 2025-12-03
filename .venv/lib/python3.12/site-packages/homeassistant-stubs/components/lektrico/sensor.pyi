from . import LektricoConfigEntry as LektricoConfigEntry, LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from .entity import LektricoEntity as LektricoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_TYPE as CONF_TYPE, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import IntegrationError as IntegrationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LektricoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType]

LIMIT_REASON_OPTIONS: Incomplete
SENSORS_FOR_CHARGERS: tuple[LektricoSensorEntityDescription, ...]
SENSORS_FOR_LB_DEVICES: tuple[LektricoSensorEntityDescription, ...]
SENSORS_FOR_1_PHASE: tuple[LektricoSensorEntityDescription, ...]
SENSORS_FOR_3_PHASE: tuple[LektricoSensorEntityDescription, ...]
SENSORS_FOR_LB_1_PHASE: tuple[LektricoSensorEntityDescription, ...]
SENSORS_FOR_LB_3_PHASE: tuple[LektricoSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LektricoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LektricoSensor(LektricoEntity, SensorEntity):
    entity_description: LektricoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, description: LektricoSensorEntityDescription, coordinator: LektricoDeviceDataUpdateCoordinator, device_name: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...
