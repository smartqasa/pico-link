from . import PlugwiseConfigEntry as PlugwiseConfigEntry
from .const import SelectOptionsType as SelectOptionsType, SelectType as SelectType
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PlugwiseSelectEntityDescription(SelectEntityDescription):
    key: SelectType
    options_key: SelectOptionsType

SELECT_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseSelectEntity(PlugwiseEntity, SelectEntity):
    entity_description: PlugwiseSelectEntityDescription
    _attr_unique_id: Incomplete
    _location: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, entity_description: PlugwiseSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str: ...
    @property
    def options(self) -> list[str]: ...
    @plugwise_command
    async def async_select_option(self, option: str) -> None: ...
