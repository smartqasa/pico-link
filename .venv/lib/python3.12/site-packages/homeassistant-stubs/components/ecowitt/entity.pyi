from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioecowitt import EcoWittSensor as EcoWittSensor
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class EcowittEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    ecowitt: EcoWittSensor
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, sensor: EcoWittSensor) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
