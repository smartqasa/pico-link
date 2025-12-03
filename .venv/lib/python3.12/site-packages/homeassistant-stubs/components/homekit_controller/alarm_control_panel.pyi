from . import KNOWN_DEVICES as KNOWN_DEVICES
from .connection import HKDevice as HKDevice
from .entity import HomeKitEntity as HomeKitEntity
from _typeshed import Incomplete
from aiohomekit.model.services import Service as Service
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

CURRENT_STATE_MAP: Incomplete
TARGET_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeKitAlarmControlPanelEntity(HomeKitEntity, AlarmControlPanelEntity):
    _attr_supported_features: Incomplete
    _attr_code_arm_required: bool
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def alarm_state(self) -> AlarmControlPanelState: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def set_alarm_state(self, state: AlarmControlPanelState, code: str | None = None) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
