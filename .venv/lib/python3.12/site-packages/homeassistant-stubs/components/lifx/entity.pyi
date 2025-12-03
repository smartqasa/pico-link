from .const import DOMAIN as DOMAIN
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class LIFXEntity(CoordinatorEntity[LIFXUpdateCoordinator]):
    _attr_has_entity_name: bool
    bulb: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator) -> None: ...
