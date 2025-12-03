from . import JVCConfigEntry as JVCConfigEntry, JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from .entity import JvcProjectorEntity as JvcProjectorEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jvcprojector import JvcProjector as JvcProjector
from typing import Final

@dataclass(frozen=True, kw_only=True)
class JvcProjectorSelectDescription(SelectEntityDescription):
    command: Callable[[JvcProjector, str], Awaitable[None]]

OPTIONS: Final[dict[str, dict[str, str]]]
SELECTS: Final[list[JvcProjectorSelectDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JvcProjectorSelectEntity(JvcProjectorEntity, SelectEntity):
    entity_description: JvcProjectorSelectDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator, description: JvcProjectorSelectDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
