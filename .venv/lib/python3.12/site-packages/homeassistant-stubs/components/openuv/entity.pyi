from .const import DOMAIN as DOMAIN
from .coordinator import OpenUvCoordinator as OpenUvCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class OpenUvEntity(CoordinatorEntity):
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenUvCoordinator, description: EntityDescription) -> None: ...
