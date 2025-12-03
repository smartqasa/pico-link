import abc
from .const import DOMAIN as DOMAIN
from .coordinator import AmbientNetworkDataUpdateCoordinator as AmbientNetworkDataUpdateCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AmbientNetworkEntity(CoordinatorEntity[AmbientNetworkDataUpdateCoordinator], metaclass=abc.ABCMeta):
    _attr_attribution: str
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AmbientNetworkDataUpdateCoordinator, description: EntityDescription, mac_address: str) -> None: ...
    @abstractmethod
    def _update_attrs(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
