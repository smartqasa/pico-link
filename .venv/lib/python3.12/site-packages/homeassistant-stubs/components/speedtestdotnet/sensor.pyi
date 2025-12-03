from . import SpeedTestConfigEntry as SpeedTestConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_BYTES_RECEIVED as ATTR_BYTES_RECEIVED, ATTR_BYTES_SENT as ATTR_BYTES_SENT, ATTR_SERVER_COUNTRY as ATTR_SERVER_COUNTRY, ATTR_SERVER_ID as ATTR_SERVER_ID, ATTR_SERVER_NAME as ATTR_SERVER_NAME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import SpeedTestDataCoordinator as SpeedTestDataCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfDataRate as UnitOfDataRate, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True)
class SpeedtestSensorEntityDescription(SensorEntityDescription):
    value: Callable = ...

SENSOR_TYPES: tuple[SpeedtestSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: SpeedTestConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SpeedtestSensor(CoordinatorEntity[SpeedTestDataCoordinator], SensorEntity):
    entity_description: SpeedtestSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _state: StateType
    _attrs: dict[str, Any]
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SpeedTestDataCoordinator, description: SpeedtestSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
