from .hub import DeconzHub as DeconzHub
from .util import serial_from_unique_id as serial_from_unique_id
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_ZIGBEE as CONNECTION_ZIGBEE, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from pydeconz.models.group import Group as PydeconzGroup
from pydeconz.models.light import LightBase as PydeconzLightBase
from pydeconz.models.scene import Scene as PydeconzScene
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase

type _DeviceType = PydeconzGroup | PydeconzLightBase | PydeconzSensorBase | PydeconzScene
class DeconzBase[_DeviceT: _DeviceType]:
    unique_id_suffix: str | None
    _device: _DeviceT
    hub: Incomplete
    def __init__(self, device: _DeviceT, hub: DeconzHub) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def serial(self) -> str | None: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...

class DeconzDevice[_DeviceT: _DeviceType](DeconzBase[_DeviceT], Entity):
    _attr_should_poll: bool
    _name_suffix: str | None
    _update_key: str | None
    _update_keys: set[str] | None
    TYPE: str
    _attr_name: Incomplete
    def __init__(self, device: _DeviceT, hub: DeconzHub) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def async_update_connection_state(self) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...
    @property
    def available(self) -> bool: ...

class DeconzSceneMixin(DeconzDevice[PydeconzScene]):
    _attr_has_entity_name: bool
    group: Incomplete
    _attr_name: Incomplete
    _group_identifier: Incomplete
    def __init__(self, device: PydeconzScene, hub: DeconzHub) -> None: ...
    def get_device_identifier(self) -> str: ...
    def get_parent_identifier(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
