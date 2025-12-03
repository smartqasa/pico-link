import abc
from .const import DOMAIN as DOMAIN
from .coordinator import EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from eheimdigital.device import EheimDigitalDevice
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class EheimDigitalEntity[_DeviceT: EheimDigitalDevice](CoordinatorEntity[EheimDigitalUpdateCoordinator], ABC, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _device: Incomplete
    _device_address: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT) -> None: ...
    @abstractmethod
    def _async_update_attrs(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
