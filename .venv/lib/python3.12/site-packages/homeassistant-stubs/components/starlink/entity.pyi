from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class StarlinkEntity(CoordinatorEntity[StarlinkUpdateCoordinator], Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: StarlinkUpdateCoordinator, description: EntityDescription) -> None: ...
