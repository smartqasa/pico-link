from .const import DOMAIN as DOMAIN
from .coordinator import EvilGeniusUpdateCoordinator as EvilGeniusUpdateCoordinator
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class EvilGeniusEntity(CoordinatorEntity[EvilGeniusUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    def device_info(self) -> DeviceInfo: ...
