from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity, api_call as api_call
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from velbusaio.channels import SelectedProgram as SelectedProgram

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusSelect(VelbusEntity, SelectEntity):
    _channel: SelectedProgram
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, channel: SelectedProgram) -> None: ...
    @api_call
    async def async_select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str: ...
