from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters.Types import Nullable as Nullable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify

AIR_QUALITY_MAP: Incomplete
CONTAMINATION_STATE_MAP: Incomplete
OPERATIONAL_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True)
class MatterSensorEntityDescription(SensorEntityDescription, MatterEntityDescription): ...

class MatterSensor(MatterEntity, SensorEntity):
    entity_description: MatterSensorEntityDescription
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterOperationalStateSensor(MatterSensor):
    states_map: dict[int, str]
    _attr_options: Incomplete
    _attr_native_value: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
