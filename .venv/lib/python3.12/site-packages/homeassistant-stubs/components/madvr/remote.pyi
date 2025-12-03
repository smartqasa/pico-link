from . import MadVRConfigEntry as MadVRConfigEntry
from .coordinator import MadVRCoordinator as MadVRCoordinator
from .entity import MadVREntity as MadVREntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MadVRConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MadvrRemote(MadVREntity, RemoteEntity):
    _attr_name: Incomplete
    madvr_client: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MadVRCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
