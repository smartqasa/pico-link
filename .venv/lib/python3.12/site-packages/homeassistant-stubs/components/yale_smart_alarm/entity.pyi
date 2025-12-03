from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODEL as MODEL
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from yalesmartalarmclient import YaleLock as YaleLock

class YaleEntity(CoordinatorEntity[YaleDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: str
    _attr_device_info: DeviceInfo
    def __init__(self, coordinator: YaleDataUpdateCoordinator, data: dict) -> None: ...

class YaleLockEntity(CoordinatorEntity[YaleDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: str
    _attr_device_info: Incomplete
    lock_data: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, lock: YaleLock) -> None: ...

class YaleAlarmEntity(CoordinatorEntity[YaleDataUpdateCoordinator], Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator) -> None: ...
