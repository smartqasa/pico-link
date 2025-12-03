from .const import DOMAIN as DOMAIN
from .coordinator import LidarrDataUpdateCoordinator as LidarrDataUpdateCoordinator, T as T
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class LidarrEntity(CoordinatorEntity[LidarrDataUpdateCoordinator[T]]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LidarrDataUpdateCoordinator[T], description: EntityDescription) -> None: ...
