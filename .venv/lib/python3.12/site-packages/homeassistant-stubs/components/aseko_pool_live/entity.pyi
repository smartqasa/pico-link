from .const import DOMAIN as DOMAIN
from .coordinator import AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from _typeshed import Incomplete
from aioaseko import Unit as Unit
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AsekoEntity(CoordinatorEntity[AsekoDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _unit: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unit: Unit, coordinator: AsekoDataUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def unit(self) -> Unit: ...
    @property
    def available(self) -> bool: ...
