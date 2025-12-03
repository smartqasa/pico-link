import abc
from .const import ATTR_MAJOR as ATTR_MAJOR, ATTR_MINOR as ATTR_MINOR, ATTR_SOURCE as ATTR_SOURCE, ATTR_UUID as ATTR_UUID, DOMAIN as DOMAIN
from .coordinator import IBeaconCoordinator as IBeaconCoordinator, signal_seen as signal_seen, signal_unavailable as signal_unavailable
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from ibeacon_ble import iBeaconAdvertisement as iBeaconAdvertisement

class IBeaconEntity(Entity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _device_unique_id: Incomplete
    _coordinator: Incomplete
    _ibeacon_advertisement: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: IBeaconCoordinator, identifier: str, device_unique_id: str, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str | int]: ...
    @abstractmethod
    @callback
    def _async_seen(self, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    @abstractmethod
    @callback
    def _async_unavailable(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
