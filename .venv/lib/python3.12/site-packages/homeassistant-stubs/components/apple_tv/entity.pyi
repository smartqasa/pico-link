from . import AppleTVManager as AppleTVManager
from .const import DOMAIN as DOMAIN, SIGNAL_CONNECTED as SIGNAL_CONNECTED, SIGNAL_DISCONNECTED as SIGNAL_DISCONNECTED
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from pyatv.interface import AppleTV as AppleTVInterface

class AppleTVEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    atv: AppleTVInterface | None
    manager: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, identifier: str, manager: AppleTVManager) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_device_connected(self, atv: AppleTVInterface) -> None: ...
    def async_device_disconnected(self) -> None: ...
