from . import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from datetime import datetime, time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

@dataclass(frozen=True)
class RequiredKeysMixin(Generic[_RobotT]):
    value_fn: Callable[[_RobotT], time | None]
    set_fn: Callable[[_RobotT, time], Coroutine[Any, Any, bool]]

@dataclass(frozen=True)
class RobotTimeEntityDescription(TimeEntityDescription, RequiredKeysMixin[_RobotT]): ...

def _as_local_time(start: datetime | None) -> time | None: ...

LITTER_ROBOT_3_SLEEP_START: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotTimeEntity(LitterRobotEntity[_RobotT], TimeEntity):
    entity_description: RobotTimeEntityDescription[_RobotT]
    @property
    def native_value(self) -> time | None: ...
    async def async_set_value(self, value: time) -> None: ...
