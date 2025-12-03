from .const import DOMAIN as DOMAIN
from .coordinator import RomyVacuumCoordinator as RomyVacuumCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class RomyEntity(CoordinatorEntity[RomyVacuumCoordinator]):
    _attr_has_entity_name: bool
    romy: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: RomyVacuumCoordinator) -> None: ...
