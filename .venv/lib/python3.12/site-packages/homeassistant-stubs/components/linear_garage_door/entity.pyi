from .const import DOMAIN as DOMAIN
from .coordinator import LinearDevice as LinearDevice, LinearUpdateCoordinator as LinearUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class LinearEntity(CoordinatorEntity[LinearUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _device_id: Incomplete
    _sub_device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LinearUpdateCoordinator, device_id: str, device_name: str, sub_device_id: str) -> None: ...
    @property
    def linear_device(self) -> LinearDevice: ...
    @property
    def sub_device(self) -> dict[str, str]: ...
