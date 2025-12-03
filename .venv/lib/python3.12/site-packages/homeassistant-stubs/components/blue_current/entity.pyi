import abc
from . import Connector as Connector
from .const import DOMAIN as DOMAIN, MODEL_TYPE as MODEL_TYPE
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity

class BlueCurrentEntity(Entity, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    connector: Incomplete
    signal: Incomplete
    has_value: bool
    def __init__(self, connector: Connector, signal: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
    @callback
    @abstractmethod
    def update_from_latest_data(self) -> None: ...

class ChargepointEntity(BlueCurrentEntity, metaclass=abc.ABCMeta):
    evse_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, connector: Connector, evse_id: str) -> None: ...
