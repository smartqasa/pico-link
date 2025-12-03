from .const import DOMAIN as DOMAIN
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

MANUFACTURER: str
MODEL: str
MODEL2: str

class DiffuserEntity(CoordinatorEntity[RitualsDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: RitualsDataUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
