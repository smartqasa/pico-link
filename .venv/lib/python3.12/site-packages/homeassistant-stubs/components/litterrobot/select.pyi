from . import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import Robot as Robot
from pylitterbot.robot.litterrobot4 import BrightnessLevel
from typing import Any, Generic, TypeVar

_CastTypeT = TypeVar('_CastTypeT', int, float, str)
BRIGHTNESS_LEVEL_ICON_MAP: dict[BrightnessLevel | None, str]

@dataclass(frozen=True)
class RequiredKeysMixin(Generic[_RobotT, _CastTypeT]):
    current_fn: Callable[[_RobotT], _CastTypeT | None]
    options_fn: Callable[[_RobotT], list[_CastTypeT]]
    select_fn: Callable[[_RobotT, str], Coroutine[Any, Any, bool]]

@dataclass(frozen=True)
class RobotSelectEntityDescription(SelectEntityDescription, RequiredKeysMixin[_RobotT, _CastTypeT]):
    entity_category: EntityCategory = ...
    icon_fn: Callable[[_RobotT], str] | None = ...

ROBOT_SELECT_MAP: dict[type[Robot], RobotSelectEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotSelectEntity(LitterRobotEntity[_RobotT], SelectEntity, Generic[_RobotT, _CastTypeT]):
    entity_description: RobotSelectEntityDescription[_RobotT, _CastTypeT]
    _attr_options: Incomplete
    def __init__(self, robot: _RobotT, hub: LitterRobotHub, description: RobotSelectEntityDescription[_RobotT, _CastTypeT]) -> None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
