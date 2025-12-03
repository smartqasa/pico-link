from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from lacrosse_view import Sensor

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class LaCrosseSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Sensor, str], float | int | str | None]

def get_value(sensor: Sensor, field: str) -> float | int | str | None: ...

PARALLEL_UPDATES: int
SENSOR_DESCRIPTIONS: Incomplete
UNIT_OF_MEASUREMENT_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaCrosseViewSensor(CoordinatorEntity[DataUpdateCoordinator[list[Sensor]]], SensorEntity):
    entity_description: LaCrosseSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    index: Incomplete
    def __init__(self, description: LaCrosseSensorEntityDescription, coordinator: DataUpdateCoordinator[list[Sensor]], sensor: Sensor, index: int) -> None: ...
    @property
    def native_value(self) -> int | float | str | None: ...
    @property
    def available(self) -> bool: ...
