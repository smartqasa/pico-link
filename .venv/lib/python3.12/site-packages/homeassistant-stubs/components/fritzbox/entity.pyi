import abc
from .const import DOMAIN as DOMAIN
from .coordinator import FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyfritzhome import FritzhomeDevice as FritzhomeDevice
from pyfritzhome.devicetypes.fritzhomeentitybase import FritzhomeEntityBase as FritzhomeEntityBase

class FritzBoxEntity(CoordinatorEntity[FritzboxDataUpdateCoordinator], ABC, metaclass=abc.ABCMeta):
    ain: Incomplete
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: FritzboxDataUpdateCoordinator, ain: str, entity_description: EntityDescription | None = None) -> None: ...
    @property
    @abstractmethod
    def data(self) -> FritzhomeEntityBase: ...

class FritzBoxDeviceEntity(FritzBoxEntity):
    @property
    def available(self) -> bool: ...
    @property
    def data(self) -> FritzhomeDevice: ...
    @property
    def device_info(self) -> DeviceInfo: ...
