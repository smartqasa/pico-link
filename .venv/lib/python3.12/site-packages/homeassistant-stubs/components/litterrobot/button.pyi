from . import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True)
class RequiredKeysMixin(Generic[_RobotT]):
    press_fn: Callable[[_RobotT], Coroutine[Any, Any, bool]]

@dataclass(frozen=True)
class RobotButtonEntityDescription(ButtonEntityDescription, RequiredKeysMixin[_RobotT]): ...

LITTER_ROBOT_BUTTON: Incomplete
FEEDER_ROBOT_BUTTON: Incomplete

class LitterRobotButtonEntity(LitterRobotEntity[_RobotT], ButtonEntity):
    entity_description: RobotButtonEntityDescription[_RobotT]
    async def async_press(self) -> None: ...
