from . import SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN, VACUUM_FAN_SPEED_MAX as VACUUM_FAN_SPEED_MAX, VACUUM_FAN_SPEED_QUIET as VACUUM_FAN_SPEED_QUIET, VACUUM_FAN_SPEED_STANDARD as VACUUM_FAN_SPEED_STANDARD, VACUUM_FAN_SPEED_STRONG as VACUUM_FAN_SPEED_STRONG
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from switchbot_api import Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

VACUUM_SWITCHBOT_STATE_TO_HA_STATE: dict[str, VacuumActivity]
VACUUM_FAN_SPEED_TO_SWITCHBOT_FAN_SPEED: dict[str, str]

class SwitchBotCloudVacuum(SwitchBotCloudEntity, StateVacuumEntity):
    _attr_supported_features: VacuumEntityFeature
    _attr_name: Incomplete
    _attr_fan_speed_list: list[str]
    _attr_fan_speed: Incomplete
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_start(self) -> None: ...
    _attr_battery_level: Incomplete
    _attr_available: Incomplete
    _attr_activity: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> SwitchBotCloudVacuum: ...
