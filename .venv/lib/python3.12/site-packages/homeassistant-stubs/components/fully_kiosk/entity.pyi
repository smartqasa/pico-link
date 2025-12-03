from .const import DOMAIN as DOMAIN
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components import mqtt as mqtt
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

def valid_global_mac_address(mac: str | None) -> bool: ...

class FullyKioskEntity(CoordinatorEntity[FullyKioskDataUpdateCoordinator], Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator) -> None: ...
    async def mqtt_subscribe(self, event: str | None, event_callback: CALLBACK_TYPE) -> CALLBACK_TYPE | None: ...
