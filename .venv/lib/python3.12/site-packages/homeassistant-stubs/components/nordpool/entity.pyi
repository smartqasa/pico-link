from .const import DOMAIN as DOMAIN
from .coordinator import NordPoolDataUpdateCoordinator as NordPoolDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class NordpoolBaseEntity(CoordinatorEntity[NordPoolDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    area: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: NordPoolDataUpdateCoordinator, entity_description: EntityDescription, area: str) -> None: ...
