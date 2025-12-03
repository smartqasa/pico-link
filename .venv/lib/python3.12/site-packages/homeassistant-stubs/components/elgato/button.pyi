from .coordinator import ElgatoConfigEntry as ElgatoConfigEntry, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from elgato import Elgato as Elgato
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ElgatoButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Elgato], Awaitable[Any]]

BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElgatoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoButtonEntity(ElgatoEntity, ButtonEntity):
    entity_description: ElgatoButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
