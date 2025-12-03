from . import AutomowerConfigEntry as AutomowerConfigEntry
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerControlEntity as AutomowerControlEntity, handle_sending_exception as handle_sending_exception
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int
HEADLIGHT_MODES: list

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerSelectEntity(AutomowerControlEntity, SelectEntity):
    _attr_options = HEADLIGHT_MODES
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
