from . import NanoleafCoordinator as NanoleafCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class NanoleafEntity(CoordinatorEntity[NanoleafCoordinator]):
    _attr_has_entity_name: bool
    _nanoleaf: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: NanoleafCoordinator) -> None: ...
