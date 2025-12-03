from .const import DOMAIN as DOMAIN
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class TrafikverketCameraEntity(CoordinatorEntity[TVDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, entry_id: str) -> None: ...

class TrafikverketCameraNonCameraEntity(TrafikverketCameraEntity):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, entry_id: str, description: EntityDescription) -> None: ...
    @callback
    def _update_attr(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
