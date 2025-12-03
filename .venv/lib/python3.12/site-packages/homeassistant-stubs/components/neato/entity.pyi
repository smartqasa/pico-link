from .const import NEATO_DOMAIN as NEATO_DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from pybotvac import Robot as Robot

class NeatoEntity(Entity):
    _attr_has_entity_name: bool
    robot: Incomplete
    _attr_device_info: DeviceInfo
    def __init__(self, robot: Robot) -> None: ...
