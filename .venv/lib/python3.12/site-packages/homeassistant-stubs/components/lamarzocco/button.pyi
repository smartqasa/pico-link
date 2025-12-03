from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry, LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
BACKFLUSH_ENABLED_DURATION: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoButtonEntityDescription(LaMarzoccoEntityDescription, ButtonEntityDescription):
    press_fn: Callable[[LaMarzoccoUpdateCoordinator], Coroutine[Any, Any, None]]

async def async_backflush_and_update(coordinator: LaMarzoccoUpdateCoordinator) -> None: ...

ENTITIES: tuple[LaMarzoccoButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoButtonEntity(LaMarzoccoEntity, ButtonEntity):
    entity_description: LaMarzoccoButtonEntityDescription
    async def async_press(self) -> None: ...
