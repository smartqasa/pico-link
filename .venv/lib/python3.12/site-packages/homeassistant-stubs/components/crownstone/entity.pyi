from .const import CROWNSTONE_INCLUDE_TYPES as CROWNSTONE_INCLUDE_TYPES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from crownstone_cloud.cloud_models.crownstones import Crownstone as Crownstone
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class CrownstoneEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    device: Incomplete
    def __init__(self, device: Crownstone) -> None: ...
    @property
    def cloud_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
