from . import JellyfinConfigEntry as JellyfinConfigEntry
from .const import LOGGER as LOGGER
from .coordinator import JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from .entity import JellyfinClientEntity as JellyfinClientEntity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_DELAY_SECS as ATTR_DELAY_SECS, ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, DEFAULT_DELAY_SECS as DEFAULT_DELAY_SECS, DEFAULT_NUM_REPEATS as DEFAULT_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: JellyfinConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JellyfinRemote(JellyfinClientEntity, RemoteEntity):
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JellyfinDataUpdateCoordinator, session_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
