from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytautulli import PyTautulliApiUser as PyTautulliApiUser

class TautulliEntity(CoordinatorEntity[TautulliDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    user: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TautulliDataUpdateCoordinator, description: EntityDescription, user: PyTautulliApiUser | None = None) -> None: ...
