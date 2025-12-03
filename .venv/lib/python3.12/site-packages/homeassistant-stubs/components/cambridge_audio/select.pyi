from . import CambridgeAudioConfigEntry as CambridgeAudioConfigEntry
from .entity import CambridgeAudioEntity as CambridgeAudioEntity, command as command
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient as StreamMagicClient
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass, field
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CambridgeAudioSelectEntityDescription(SelectEntityDescription):
    options_fn: Callable[[StreamMagicClient], list[str]] = field(default=Incomplete)
    load_fn: Callable[[StreamMagicClient], bool] = field(default=Incomplete)
    value_fn: Callable[[StreamMagicClient], str | None]
    set_value_fn: Callable[[StreamMagicClient, str], Awaitable[None]]

async def _audio_output_set_value_fn(client: StreamMagicClient, value: str) -> None: ...
def _audio_output_value_fn(client: StreamMagicClient) -> str | None: ...

CONTROL_ENTITIES: tuple[CambridgeAudioSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: CambridgeAudioConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CambridgeAudioSelect(CambridgeAudioEntity, SelectEntity):
    entity_description: CambridgeAudioSelectEntityDescription
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, client: StreamMagicClient, description: CambridgeAudioSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @command
    async def async_select_option(self, option: str) -> None: ...
