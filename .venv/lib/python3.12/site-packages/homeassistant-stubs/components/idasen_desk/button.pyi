from . import IdasenDeskConfigEntry as IdasenDeskConfigEntry, IdasenDeskCoordinator as IdasenDeskCoordinator
from .entity import IdasenDeskEntity as IdasenDeskEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class IdasenDeskButtonDescription(ButtonEntityDescription):
    press_action: Callable[[IdasenDeskCoordinator], Callable[[], Coroutine[Any, Any, Any]]]

BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: IdasenDeskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IdasenDeskButton(IdasenDeskEntity, ButtonEntity):
    entity_description: IdasenDeskButtonDescription
    def __init__(self, coordinator: IdasenDeskCoordinator, description: IdasenDeskButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
    @property
    def available(self) -> bool: ...
