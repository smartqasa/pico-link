from .const import ATTR_DIR_OF_TRAVEL as ATTR_DIR_OF_TRAVEL, ATTR_DIST_TO as ATTR_DIST_TO, ATTR_NEAREST as ATTR_NEAREST, ATTR_NEAREST_DIR_OF_TRAVEL as ATTR_NEAREST_DIR_OF_TRAVEL, ATTR_NEAREST_DIST_TO as ATTR_NEAREST_DIST_TO, DOMAIN as DOMAIN
from .coordinator import ProximityConfigEntry as ProximityConfigEntry, ProximityDataUpdateCoordinator as ProximityDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import NamedTuple

DIRECTIONS: Incomplete
SENSORS_PER_ENTITY: list[SensorEntityDescription]
SENSORS_PER_PROXIMITY: list[SensorEntityDescription]

class TrackedEntityDescriptor(NamedTuple):
    entity_id: str
    identifier: str
    name: str

def _device_info(coordinator: ProximityDataUpdateCoordinator) -> DeviceInfo: ...
async def async_setup_entry(hass: HomeAssistant, entry: ProximityConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProximitySensor(CoordinatorEntity[ProximityDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, description: SensorEntityDescription, coordinator: ProximityDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> str | float | None: ...

class ProximityTrackedEntitySensor(CoordinatorEntity[ProximityDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    tracked_entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, description: SensorEntityDescription, coordinator: ProximityDataUpdateCoordinator, tracked_entity_descriptor: TrackedEntityDescriptor) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def data(self) -> dict[str, str | int | None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> str | float | None: ...
