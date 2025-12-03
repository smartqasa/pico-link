from .const import DOMAIN as DOMAIN
from .coordinator import PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PrusaLinkEntity(CoordinatorEntity[PrusaLinkUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    def device_info(self) -> DeviceInfo: ...
