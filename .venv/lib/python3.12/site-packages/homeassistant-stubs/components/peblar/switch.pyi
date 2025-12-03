from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarData as PeblarData, PeblarDataUpdateCoordinator as PeblarDataUpdateCoordinator, PeblarRuntimeData as PeblarRuntimeData
from .entity import PeblarEntity as PeblarEntity
from .helpers import peblar_exception_handler as peblar_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from peblar import PeblarApi as PeblarApi
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarSwitchEntityDescription(SwitchEntityDescription):
    has_fn: Callable[[PeblarRuntimeData], bool] = ...
    is_on_fn: Callable[[PeblarData], bool]
    set_fn: Callable[[PeblarApi, bool], Awaitable[Any]]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PeblarSwitchEntity(PeblarEntity[PeblarDataUpdateCoordinator], SwitchEntity):
    entity_description: PeblarSwitchEntityDescription
    @property
    def is_on(self) -> bool: ...
    @peblar_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @peblar_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
