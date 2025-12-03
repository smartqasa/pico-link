from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class AirVisualProEntity(CoordinatorEntity):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
