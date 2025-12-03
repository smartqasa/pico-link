from . import RokuConfigEntry as RokuConfigEntry
from .entity import RokuEntity as RokuEntity
from .helpers import roku_exception_handler as roku_exception_handler
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: RokuConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuRemote(RokuEntity, RemoteEntity):
    _attr_name: Incomplete
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
