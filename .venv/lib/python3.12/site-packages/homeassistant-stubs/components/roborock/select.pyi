from . import RoborockConfigEntry as RoborockConfigEntry
from .const import MAP_SLEEP as MAP_SLEEP
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from roborock.containers import Status as Status
from roborock.roborock_message import RoborockDataProtocol
from roborock.roborock_typing import RoborockCommand

@dataclass(frozen=True, kw_only=True)
class RoborockSelectDescription(SelectEntityDescription):
    api_command: RoborockCommand
    value_fn: Callable[[Status], str | None]
    options_lambda: Callable[[Status], list[str] | None]
    parameter_lambda: Callable[[str, Status], list[int]]
    protocol_listener: RoborockDataProtocol | None = ...

SELECT_DESCRIPTIONS: list[RoborockSelectDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockSelectEntity(RoborockCoordinatedEntityV1, SelectEntity):
    entity_description: RoborockSelectDescription
    _attr_options: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockSelectDescription, options: list[str]) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...

class RoborockCurrentMapSelectEntity(RoborockCoordinatedEntityV1, SelectEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    async def async_select_option(self, option: str) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
