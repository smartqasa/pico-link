from .const import DOMAIN as DOMAIN
from .subscriber import Subscriber as Subscriber
from _typeshed import Incomplete
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

_LOGGER: Incomplete

class DevoloDeviceEntity(Entity):
    _attr_has_entity_name: bool
    _device_instance: Incomplete
    _homecontrol: Incomplete
    _attr_available: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    subscriber: Subscriber | None
    sync_callback: Incomplete
    _value: float
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _sync(self, message: tuple) -> None: ...
    def _generic_message(self, message: tuple) -> None: ...
