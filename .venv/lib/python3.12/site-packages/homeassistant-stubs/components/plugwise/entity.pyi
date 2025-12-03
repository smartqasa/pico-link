from .const import DOMAIN as DOMAIN
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import ATTR_NAME as ATTR_NAME, ATTR_VIA_DEVICE as ATTR_VIA_DEVICE, CONF_HOST as CONF_HOST
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, CONNECTION_ZIGBEE as CONNECTION_ZIGBEE, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from plugwise.constants import GwEntityData as GwEntityData

class PlugwiseEntity(CoordinatorEntity[PlugwiseDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _dev_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device(self) -> GwEntityData: ...
