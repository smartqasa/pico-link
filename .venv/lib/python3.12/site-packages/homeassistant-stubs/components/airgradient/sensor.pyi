from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import PM_STANDARD as PM_STANDARD, PM_STANDARD_REVERSE as PM_STANDARD_REVERSE
from .coordinator import AirGradientCoordinator as AirGradientCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from airgradient import Config as Config
from airgradient.models import Measures as Measures
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class AirGradientMeasurementSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Measures], StateType]

@dataclass(frozen=True, kw_only=True)
class AirGradientConfigSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Config], StateType]

MEASUREMENT_SENSOR_TYPES: tuple[AirGradientMeasurementSensorEntityDescription, ...]
CONFIG_SENSOR_TYPES: tuple[AirGradientConfigSensorEntityDescription, ...]
CONFIG_LED_BAR_SENSOR_TYPES: tuple[AirGradientConfigSensorEntityDescription, ...]
CONFIG_DISPLAY_SENSOR_TYPES: tuple[AirGradientConfigSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirGradientSensor(AirGradientEntity, SensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator, description: SensorEntityDescription) -> None: ...

class AirGradientMeasurementSensor(AirGradientSensor):
    entity_description: AirGradientMeasurementSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

class AirGradientConfigSensor(AirGradientSensor):
    entity_description: AirGradientConfigSensorEntityDescription
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator, description: AirGradientConfigSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
