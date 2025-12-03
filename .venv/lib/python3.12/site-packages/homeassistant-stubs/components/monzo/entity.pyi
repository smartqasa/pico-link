from .const import DOMAIN as DOMAIN
from .coordinator import MonzoCoordinator as MonzoCoordinator, MonzoData as MonzoData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class MonzoBaseEntity(CoordinatorEntity[MonzoCoordinator]):
    _attr_attribution: str
    _attr_has_entity_name: bool
    index: Incomplete
    _data_accessor: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: MonzoCoordinator, index: int, device_model: str, data_accessor: Callable[[MonzoData], list[dict[str, Any]]]) -> None: ...
    @property
    def data(self) -> dict[str, Any]: ...
