import abc
from .models import WizData as WizData
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.const import ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MODEL as ATTR_MODEL
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, ToggleEntity as ToggleEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from pywizlight.bulblibrary import BulbType as BulbType
from typing import Any

class WizEntity(CoordinatorEntity[DataUpdateCoordinator[float | None]], Entity, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @callback
    @abstractmethod
    def _async_update_attrs(self) -> None: ...

class WizToggleEntity(WizEntity, ToggleEntity):
    _attr_is_on: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
