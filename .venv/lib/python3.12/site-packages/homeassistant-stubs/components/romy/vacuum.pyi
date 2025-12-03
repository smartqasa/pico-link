from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import RomyVacuumCoordinator as RomyVacuumCoordinator
from .entity import RomyEntity as RomyEntity
from _typeshed import Incomplete
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

FAN_SPEED_NONE: str
FAN_SPEED_NORMAL: str
FAN_SPEED_SILENT: str
FAN_SPEED_INTENSIVE: str
FAN_SPEED_SUPER_SILENT: str
FAN_SPEED_HIGH: str
FAN_SPEED_AUTO: str
FAN_SPEEDS: list[str]
SUPPORT_ROMY_ROBOT: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RomyVacuumEntity(RomyEntity, StateVacuumEntity):
    _attr_supported_features = SUPPORT_ROMY_ROBOT
    _attr_fan_speed_list = FAN_SPEEDS
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RomyVacuumCoordinator) -> None: ...
    _attr_fan_speed: Incomplete
    _attr_battery_level: Incomplete
    _attr_activity: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_start(self, **kwargs: Any) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
