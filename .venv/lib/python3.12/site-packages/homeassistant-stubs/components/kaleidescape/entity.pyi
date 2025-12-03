from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from kaleidescape import Device as KaleidescapeDevice

_LOGGER: Incomplete

class KaleidescapeEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: KaleidescapeDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
