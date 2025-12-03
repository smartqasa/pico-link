from . import ApSystemsData as ApSystemsData
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class ApSystemsEntity(Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, data: ApSystemsData) -> None: ...
