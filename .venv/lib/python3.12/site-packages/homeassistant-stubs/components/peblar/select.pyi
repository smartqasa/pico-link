from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarUserConfigurationDataUpdateCoordinator as PeblarUserConfigurationDataUpdateCoordinator
from .entity import PeblarEntity as PeblarEntity
from .helpers import peblar_exception_handler as peblar_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from peblar import Peblar as Peblar, PeblarUserConfiguration as PeblarUserConfiguration
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarSelectEntityDescription(SelectEntityDescription):
    current_fn: Callable[[PeblarUserConfiguration], str | None]
    select_fn: Callable[[Peblar, str], Awaitable[Any]]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PeblarSelectEntity(PeblarEntity[PeblarUserConfigurationDataUpdateCoordinator], SelectEntity):
    entity_description: PeblarSelectEntityDescription
    @property
    def current_option(self) -> str | None: ...
    @peblar_exception_handler
    async def async_select_option(self, option: str) -> None: ...
