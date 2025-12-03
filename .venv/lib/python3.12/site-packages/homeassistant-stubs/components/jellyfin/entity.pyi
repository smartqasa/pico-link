from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class JellyfinEntity(CoordinatorEntity[JellyfinDataUpdateCoordinator]):
    _attr_has_entity_name: bool

class JellyfinServerEntity(JellyfinEntity):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: JellyfinDataUpdateCoordinator) -> None: ...

class JellyfinClientEntity(JellyfinEntity):
    session_id: Incomplete
    device_id: str
    device_name: str
    client_name: str
    app_version: str
    capabilities: dict[str, Any]
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    def __init__(self, coordinator: JellyfinDataUpdateCoordinator, session_id: str) -> None: ...
    @property
    def session_data(self) -> dict[str, Any]: ...
    @property
    def available(self) -> bool: ...
