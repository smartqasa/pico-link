from .api import IottyProxy as IottyProxy
from .const import DOMAIN as DOMAIN
from .coordinator import IottyDataUpdateCoordinator as IottyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from iottycloud.lightswitch import Device as Device

_LOGGER: Incomplete

class IottyEntity(CoordinatorEntity[IottyDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _iotty_device_name: str
    _iotty_cloud: IottyProxy
    _iotty_device: Device
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: IottyDataUpdateCoordinator, iotty_cloud: IottyProxy, iotty_device: Device) -> None: ...
