from . import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class RokuEntity(CoordinatorEntity[RokuDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: RokuDataUpdateCoordinator, description: EntityDescription | None = None) -> None: ...
