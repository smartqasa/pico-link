from .const import DOMAIN as DOMAIN
from .coordinator import TailwindDataUpdateCoordinator as TailwindDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class TailwindEntity(CoordinatorEntity[TailwindDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TailwindDataUpdateCoordinator, entity_description: EntityDescription) -> None: ...

class TailwindDoorEntity(CoordinatorEntity[TailwindDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    door_id: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TailwindDataUpdateCoordinator, door_id: str, entity_description: EntityDescription | None = None) -> None: ...
