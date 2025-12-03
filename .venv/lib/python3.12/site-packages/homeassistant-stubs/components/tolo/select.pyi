from .const import AromaTherapySlot as AromaTherapySlot, DOMAIN as DOMAIN, LampMode as LampMode
from .coordinator import ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tololib import ToloClient as ToloClient, ToloSettings as ToloSettings

@dataclass(frozen=True, kw_only=True)
class ToloSelectEntityDescription(SelectEntityDescription):
    options: list[str]
    getter: Callable[[ToloSettings], str]
    setter: Callable[[ToloClient, str], bool]

SELECTS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloSelectEntity(ToloSaunaCoordinatorEntity, SelectEntity):
    _attr_entity_category: Incomplete
    entity_description: ToloSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry, entity_description: ToloSelectEntityDescription) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str: ...
    def select_option(self, option: str) -> None: ...
