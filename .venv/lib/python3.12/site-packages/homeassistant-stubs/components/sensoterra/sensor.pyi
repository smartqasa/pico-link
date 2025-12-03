from . import SensoterraConfigEntry as SensoterraConfigEntry
from .const import CONFIGURATION_URL as CONFIGURATION_URL, DOMAIN as DOMAIN, SENSOR_EXPIRATION_DAYS as SENSOR_EXPIRATION_DAYS
from .coordinator import SensoterraCoordinator as SensoterraCoordinator
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from sensoterra.probe import Probe as Probe, Sensor as Sensor

class ProbeSensorType(StrEnum):
    MOISTURE = ...
    SI = ...
    TEMPERATURE = ...
    BATTERY = ...
    RSSI = ...

SENSORS: dict[ProbeSensorType, SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: SensoterraConfigEntry, async_add_devices: AddEntitiesCallback) -> None: ...

class SensoterraEntity(CoordinatorEntity[SensoterraCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _sensor_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    entity_description: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SensoterraCoordinator, probe: Probe, sensor: Sensor, entity_description: SensorEntityDescription) -> None: ...
    @property
    def sensor(self) -> Sensor | None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
