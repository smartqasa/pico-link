from . import JVCConfigEntry as JVCConfigEntry
from .entity import JvcProjectorEntity as JvcProjectorEntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

COMMANDS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JvcProjectorRemote(JvcProjectorEntity, RemoteEntity):
    _attr_name: Incomplete
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
