from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER
from .coordinator import SmBaseDataUpdateCoordinator as SmBaseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class SmEntity(CoordinatorEntity[SmBaseDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SmBaseDataUpdateCoordinator) -> None: ...
