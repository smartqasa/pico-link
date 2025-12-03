from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from music_assistant_client import MusicAssistantClient as MusicAssistantClient
from music_assistant_models.event import MassEvent as MassEvent
from music_assistant_models.player import Player as Player

class MusicAssistantEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    mass: Incomplete
    player_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, mass: MusicAssistantClient, player_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def player(self) -> Player: ...
    @property
    def unique_id(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    async def __on_mass_update(self, event: MassEvent) -> None: ...
    async def async_on_update(self) -> None: ...
