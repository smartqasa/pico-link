from .const import DOMAIN as DOMAIN
from .coordinator import SpotifyCoordinator as SpotifyCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SpotifyEntity(CoordinatorEntity[SpotifyCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SpotifyCoordinator) -> None: ...
