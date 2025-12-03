from .const import DOMAIN as DOMAIN
from .coordinator import AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AndroidIPCamBaseEntity(CoordinatorEntity[AndroidIPCamDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    cam: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AndroidIPCamDataUpdateCoordinator) -> None: ...
