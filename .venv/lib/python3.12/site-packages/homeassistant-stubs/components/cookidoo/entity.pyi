from .const import DOMAIN as DOMAIN
from .coordinator import CookidooDataUpdateCoordinator as CookidooDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class CookidooBaseEntity(CoordinatorEntity[CookidooDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    device_info: Incomplete
    def __init__(self, coordinator: CookidooDataUpdateCoordinator) -> None: ...
