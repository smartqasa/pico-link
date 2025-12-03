import abc
from .const import CONF_URL_ENERGY as CONF_URL_ENERGY, CONF_URL_WEATHER as CONF_URL_WEATHER, DATA_DEVICE_IDS as DATA_DEVICE_IDS, DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DOMAIN as DOMAIN, SIGNAL_NAME as SIGNAL_NAME
from .data_handler import NetatmoDataHandler as NetatmoDataHandler, NetatmoDevice as NetatmoDevice, NetatmoRoom as NetatmoRoom, PUBLIC as PUBLIC
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from pyatmo import DeviceType, Home as Home, Module as Module, Room as Room
from pyatmo.modules.base_class import NetatmoBase as NetatmoBase
from typing import Any

class NetatmoBaseEntity(Entity):
    _attr_attribution = DEFAULT_ATTRIBUTION
    _attr_has_entity_name: bool
    data_handler: Incomplete
    _publishers: list[dict[str, Any]]
    _attr_extra_state_attributes: Incomplete
    def __init__(self, data_handler: NetatmoDataHandler) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoDeviceEntity(NetatmoBaseEntity, metaclass=abc.ABCMeta):
    device: Incomplete
    def __init__(self, data_handler: NetatmoDataHandler, device: NetatmoBase) -> None: ...
    @property
    @abstractmethod
    def device_type(self) -> DeviceType: ...
    @property
    def device_description(self) -> tuple[str, str]: ...
    @property
    def home(self) -> Home: ...

class NetatmoRoomEntity(NetatmoDeviceEntity):
    device: Room
    _attr_device_info: Incomplete
    def __init__(self, room: NetatmoRoom) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def device_type(self) -> DeviceType: ...

class NetatmoModuleEntity(NetatmoDeviceEntity):
    device: Module
    _attr_configuration_url: str
    _attr_device_info: Incomplete
    def __init__(self, device: NetatmoDevice) -> None: ...
    @property
    def device_type(self) -> DeviceType: ...

class NetatmoWeatherModuleEntity(NetatmoModuleEntity):
    _attr_configuration_url = CONF_URL_WEATHER
    def __init__(self, device: NetatmoDevice) -> None: ...
    @property
    def device_type(self) -> DeviceType: ...
