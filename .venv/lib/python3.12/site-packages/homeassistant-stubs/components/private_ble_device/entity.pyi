import abc
from .const import DOMAIN as DOMAIN
from .coordinator import async_get_coordinator as async_get_coordinator, async_last_service_info as async_last_service_info
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class BasePrivateDeviceEntity(Entity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _entry: Incomplete
    _irk: Incomplete
    _last_info: bluetooth.BluetoothServiceInfoBleak | None
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @abstractmethod
    @callback
    def _async_track_unavailable(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    @abstractmethod
    @callback
    def _async_track_service_info(self, service_info: bluetooth.BluetoothServiceInfoBleak, change: bluetooth.BluetoothChange) -> None: ...
