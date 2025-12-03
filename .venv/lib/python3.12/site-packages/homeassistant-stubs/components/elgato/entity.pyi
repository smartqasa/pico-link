from .const import DOMAIN as DOMAIN
from .coordinator import ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, CONF_MAC as CONF_MAC
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ElgatoEntity(CoordinatorEntity[ElgatoDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator) -> None: ...
