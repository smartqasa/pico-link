from . import CambridgeAudioConfigEntry as CambridgeAudioConfigEntry
from .entity import CambridgeAudioEntity as CambridgeAudioEntity, command as command
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient as StreamMagicClient
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CambridgeAudioSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[StreamMagicClient], bool]
    set_value_fn: Callable[[StreamMagicClient, bool], Awaitable[None]]

CONTROL_ENTITIES: tuple[CambridgeAudioSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: CambridgeAudioConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CambridgeAudioSwitch(CambridgeAudioEntity, SwitchEntity):
    entity_description: CambridgeAudioSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, client: StreamMagicClient, description: CambridgeAudioSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @command
    async def async_turn_off(self, **kwargs: Any) -> None: ...
