from . import SamsungTVConfigEntry as SamsungTVConfigEntry
from .const import LOGGER as LOGGER
from .entity import SamsungTVEntity as SamsungTVEntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: SamsungTVConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SamsungTVRemote(SamsungTVEntity, RemoteEntity):
    _attr_name: Incomplete
    _attr_is_on: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
