from . import SchlageConfigEntry as SchlageConfigEntry
from .coordinator import LockData as LockData, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from .entity import SchlageEntity as SchlageEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: SchlageConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SchlageSelect(SchlageEntity, SelectEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SchlageDataUpdateCoordinator, description: SelectEntityDescription, device_id: str) -> None: ...
    @property
    def current_option(self) -> str: ...
    def select_option(self, option: str) -> None: ...
