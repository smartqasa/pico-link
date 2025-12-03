from . import LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class LektricoEntity(CoordinatorEntity[LektricoDeviceDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LektricoDeviceDataUpdateCoordinator, device_name: str) -> None: ...
