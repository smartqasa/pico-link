from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .coordinator import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ValloxEntity(CoordinatorEntity[ValloxDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _device_uuid: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator) -> None: ...
