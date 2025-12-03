from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultEntity as RenaultEntity
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultButtonEntityDescription(ButtonEntityDescription):
    async_press: Callable[[RenaultButtonEntity], Coroutine[Any, Any, Any]]
    requires_electricity: bool = ...

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultButtonEntity(RenaultEntity, ButtonEntity):
    entity_description: RenaultButtonEntityDescription
    async def async_press(self) -> None: ...

BUTTON_TYPES: tuple[RenaultButtonEntityDescription, ...]
