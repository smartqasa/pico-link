from .const import DOMAIN as DOMAIN
from .coordinator import MyUplinkDataCoordinator as MyUplinkDataCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class MyUplinkEntity(CoordinatorEntity[MyUplinkDataCoordinator]):
    _attr_has_entity_name: bool
    device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, device_id: str, unique_id_suffix: str) -> None: ...

class MyUplinkSystemEntity(MyUplinkEntity):
    system_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MyUplinkDataCoordinator, system_id: str, device_id: str, unique_id_suffix: str) -> None: ...
