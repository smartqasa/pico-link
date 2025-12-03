from . import EcowittConfigEntry as EcowittConfigEntry
from .entity import EcowittEntity as EcowittEntity
from _typeshed import Incomplete
from aioecowitt import EcoWittSensor as EcoWittSensor
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM, US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM
from typing import Final

_METRIC: Final[Incomplete]
_IMPERIAL: Final[Incomplete]
ECOWITT_SENSORS_MAPPING: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: EcowittConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcowittSensorEntity(EcowittEntity, SensorEntity):
    entity_description: Incomplete
    def __init__(self, sensor: EcoWittSensor, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
