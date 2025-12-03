from . import FileSizeConfigEntry as FileSizeConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import FileSizeCoordinator as FileSizeCoordinator
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: FileSizeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FilesizeEntity(CoordinatorEntity[FileSizeCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, description: SensorEntityDescription, entry_id: str, coordinator: FileSizeCoordinator) -> None: ...
    @property
    def native_value(self) -> float | int | datetime: ...
