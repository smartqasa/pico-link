from . import BrotherConfigEntry as BrotherConfigEntry, BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from brother import BrotherSensors as BrotherSensors
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

ATTR_COUNTER: str
ATTR_REMAINING_PAGES: str
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class BrotherSensorEntityDescription(SensorEntityDescription):
    value: Callable[[BrotherSensors], StateType | datetime]

SENSOR_TYPES: tuple[BrotherSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BrotherConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BrotherPrinterSensor(CoordinatorEntity[BrotherDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: BrotherSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BrotherDataUpdateCoordinator, description: BrotherSensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
