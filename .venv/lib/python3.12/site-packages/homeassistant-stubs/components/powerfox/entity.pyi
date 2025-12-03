from .const import DOMAIN as DOMAIN
from .coordinator import PowerfoxDataUpdateCoordinator as PowerfoxDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from powerfox import Device as Device

class PowerfoxEntity(CoordinatorEntity[PowerfoxDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PowerfoxDataUpdateCoordinator, device: Device) -> None: ...
