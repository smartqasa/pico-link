from . import BraviaTVCoordinator as BraviaTVCoordinator
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class BraviaTVEntity(CoordinatorEntity[BraviaTVCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BraviaTVCoordinator, unique_id: str, model: str) -> None: ...
