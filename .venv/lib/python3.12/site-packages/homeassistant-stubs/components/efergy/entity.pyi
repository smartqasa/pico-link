from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from pyefergy import Efergy as Efergy

class EfergyEntity(Entity):
    _attr_attribution: str
    api: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: Efergy, server_unique_id: str) -> None: ...
