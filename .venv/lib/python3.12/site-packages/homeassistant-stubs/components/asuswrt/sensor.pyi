from . import AsusWrtConfigEntry as AsusWrtConfigEntry
from .const import KEY_COORDINATOR as KEY_COORDINATOR, KEY_SENSORS as KEY_SENSORS, SENSORS_BYTES as SENSORS_BYTES, SENSORS_CONNECTED_DEVICE as SENSORS_CONNECTED_DEVICE, SENSORS_CPU as SENSORS_CPU, SENSORS_LOAD_AVG as SENSORS_LOAD_AVG, SENSORS_MEMORY as SENSORS_MEMORY, SENSORS_RATES as SENSORS_RATES, SENSORS_TEMPERATURES as SENSORS_TEMPERATURES, SENSORS_UPTIME as SENSORS_UPTIME
from .router import AsusWrtRouter as AsusWrtRouter
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util import slugify as slugify

@dataclass(frozen=True)
class AsusWrtSensorEntityDescription(SensorEntityDescription):
    factor: int | None = ...

UNIT_DEVICES: str
CPU_CORE_SENSORS: tuple[AsusWrtSensorEntityDescription, ...]
CONNECTION_SENSORS: tuple[AsusWrtSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AsusWrtConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsusWrtSensor(CoordinatorEntity, SensorEntity):
    entity_description: AsusWrtSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, router: AsusWrtRouter, description: AsusWrtSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | str | None: ...
