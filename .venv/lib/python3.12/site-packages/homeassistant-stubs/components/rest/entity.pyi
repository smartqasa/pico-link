import abc
from .data import RestData as RestData
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class RestEntity(Entity, metaclass=abc.ABCMeta):
    _coordinator: Incomplete
    rest: Incomplete
    _resource_template: Incomplete
    _attr_should_poll: Incomplete
    _attr_force_update: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[Any] | None, rest: RestData, resource_template: Template | None, force_update: bool) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_update(self) -> None: ...
    @abstractmethod
    def _update_from_rest_data(self) -> None: ...
