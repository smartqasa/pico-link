from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import RadarrDataUpdateCoordinator as RadarrDataUpdateCoordinator, StatusDataUpdateCoordinator as StatusDataUpdateCoordinator, T as T
from _typeshed import Incomplete
from homeassistant.const import ATTR_SW_VERSION as ATTR_SW_VERSION
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class RadarrEntity(CoordinatorEntity[RadarrDataUpdateCoordinator[T]]):
    _attr_has_entity_name: bool
    coordinator: RadarrDataUpdateCoordinator[T]
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RadarrDataUpdateCoordinator[T], description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
