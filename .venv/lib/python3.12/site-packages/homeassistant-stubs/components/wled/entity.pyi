from .const import DOMAIN as DOMAIN
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class WLEDEntity(CoordinatorEntity[WLEDDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    def device_info(self) -> DeviceInfo: ...
