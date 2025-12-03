from . import LeafDataStore as LeafDataStore
from .const import SIGNAL_UPDATE_LEAF as SIGNAL_UPDATE_LEAF
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from typing import Any

_LOGGER: Incomplete

class LeafEntity(Entity):
    car: Incomplete
    def __init__(self, car: LeafDataStore) -> None: ...
    def log_registration(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _update_callback(self) -> None: ...
