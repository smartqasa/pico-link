from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from enum import IntEnum
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, StateVacuumEntityDescription as StateVacuumEntityDescription, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class OperationalState(IntEnum):
    NO_ERROR = 0
    UNABLE_TO_START_OR_RESUME = 1
    UNABLE_TO_COMPLETE_OPERATION = 2
    COMMAND_INVALID_IN_STATE = 3
    SEEKING_CHARGER = 64
    CHARGING = 65
    DOCKED = 66

class ModeTag(IntEnum):
    IDLE = 16384
    CLEANING = 16385
    MAPPING = 16386

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterVacuum(MatterEntity, StateVacuumEntity):
    _last_accepted_commands: list[int] | None
    _supported_run_modes: dict[int, clusters.RvcCleanMode.Structs.ModeOptionStruct] | None
    entity_description: StateVacuumEntityDescription
    _platform_translation_key: str
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    async def async_start(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def _send_device_command(self, command: clusters.ClusterCommand) -> None: ...
    _attr_battery_level: Incomplete
    _attr_activity: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    _attr_supported_features: Incomplete
    @callback
    def _calculate_features(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
