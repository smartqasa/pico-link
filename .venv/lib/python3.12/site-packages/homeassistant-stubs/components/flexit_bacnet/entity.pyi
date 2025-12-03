from .const import DOMAIN as DOMAIN
from .coordinator import FlexitCoordinator as FlexitCoordinator
from _typeshed import Incomplete
from flexit_bacnet import FlexitBACnet as FlexitBACnet
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class FlexitEntity(CoordinatorEntity[FlexitCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FlexitCoordinator) -> None: ...
    @property
    def device(self) -> FlexitBACnet: ...
