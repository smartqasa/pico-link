from . import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity
from _typeshed import Incomplete
from datetime import time
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, StateVacuumEntityDescription as StateVacuumEntityDescription, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import LitterRobot
from typing import Any

SERVICE_SET_SLEEP_MODE: str
LITTER_BOX_STATUS_STATE_MAP: Incomplete
LITTER_BOX_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotCleaner(LitterRobotEntity[LitterRobot], StateVacuumEntity):
    _attr_supported_features: Incomplete
    @property
    def activity(self) -> VacuumActivity: ...
    @property
    def status(self) -> str: ...
    async def async_start(self) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_set_sleep_mode(self, enabled: bool, start_time: str | None = None) -> None: ...
    @staticmethod
    def parse_time_at_default_timezone(time_str: str | None) -> time | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
