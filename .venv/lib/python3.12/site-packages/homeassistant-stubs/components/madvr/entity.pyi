from .const import DOMAIN as DOMAIN
from .coordinator import MadVRCoordinator as MadVRCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class MadVREntity(CoordinatorEntity[MadVRCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: MadVRCoordinator) -> None: ...
