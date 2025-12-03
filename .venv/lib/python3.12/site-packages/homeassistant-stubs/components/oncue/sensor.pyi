from .entity import OncueEntity as OncueEntity
from .types import OncueConfigEntry as OncueConfigEntry
from _typeshed import Incomplete
from aiooncue import OncueDevice as OncueDevice, OncueSensor as OncueSensor
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

SENSOR_TYPES: tuple[SensorEntityDescription, ...]
SENSOR_MAP: Incomplete
UNIT_MAPPINGS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OncueConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OncueSensorEntity(OncueEntity, SensorEntity):
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, OncueDevice]], device_id: str, device: OncueDevice, sensor: OncueSensor, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str: ...
