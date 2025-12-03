from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarUserConfigurationDataUpdateCoordinator as PeblarUserConfigurationDataUpdateCoordinator
from .entity import PeblarEntity as PeblarEntity
from .helpers import peblar_exception_handler as peblar_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from peblar import Peblar as Peblar
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Peblar], Awaitable[Any]]

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PeblarButtonEntity(PeblarEntity[PeblarUserConfigurationDataUpdateCoordinator], ButtonEntity):
    entity_description: PeblarButtonEntityDescription
    @peblar_exception_handler
    async def async_press(self) -> None: ...
