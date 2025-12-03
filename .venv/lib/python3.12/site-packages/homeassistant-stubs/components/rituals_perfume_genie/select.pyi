from .const import DOMAIN as DOMAIN
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfArea as UnitOfArea
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser

@dataclass(frozen=True, kw_only=True)
class RitualsSelectEntityDescription(SelectEntityDescription):
    current_fn: Callable[[Diffuser], str]
    select_fn: Callable[[Diffuser, str], Awaitable[None]]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RitualsSelectEntity(DiffuserEntity, SelectEntity):
    entity_description: RitualsSelectEntityDescription
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, coordinator: RitualsDataUpdateCoordinator, description: RitualsSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
