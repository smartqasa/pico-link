from .const import DOMAIN as DOMAIN
from .coordinator import WithingsDataUpdateCoordinator as WithingsDataUpdateCoordinator, WithingsDeviceDataUpdateCoordinator as WithingsDeviceDataUpdateCoordinator
from _typeshed import Incomplete
from aiowithings import Device as Device
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class WithingsEntity[_T: WithingsDataUpdateCoordinator[Any]](CoordinatorEntity[_T]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _T, key: str) -> None: ...

class WithingsDeviceEntity(WithingsEntity[WithingsDeviceDataUpdateCoordinator]):
    _attr_unique_id: Incomplete
    device_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: WithingsDeviceDataUpdateCoordinator, device_id: str, key: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device(self) -> Device: ...
