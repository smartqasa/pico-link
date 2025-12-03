import datetime
import voluptuous as vol
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat
from homeassistant.const import CONF_ARMING_TIME as CONF_ARMING_TIME, CONF_CODE as CONF_CODE, CONF_DELAY_TIME as CONF_DELAY_TIME, CONF_DISARM_AFTER_TRIGGER as CONF_DISARM_AFTER_TRIGGER, CONF_NAME as CONF_NAME, CONF_TRIGGER_TIME as CONF_TRIGGER_TIME, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_time as async_track_point_in_time
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DOMAIN: str
CONF_ARMING_STATES: str
CONF_CODE_TEMPLATE: str
CONF_CODE_ARM_REQUIRED: str
CONF_ALARM_ARMED_AWAY: str
CONF_ALARM_ARMED_CUSTOM_BYPASS: str
CONF_ALARM_ARMED_HOME: str
CONF_ALARM_ARMED_NIGHT: str
CONF_ALARM_ARMED_VACATION: str
CONF_ALARM_ARMING: str
CONF_ALARM_DISARMED: str
CONF_ALARM_PENDING: str
CONF_ALARM_TRIGGERED: str
DEFAULT_ALARM_NAME: str
DEFAULT_DELAY_TIME: Incomplete
DEFAULT_ARMING_TIME: Incomplete
DEFAULT_TRIGGER_TIME: Incomplete
DEFAULT_DISARM_AFTER_TRIGGER: bool
SUPPORTED_STATES: Incomplete
SUPPORTED_PRETRIGGER_STATES: Incomplete
SUPPORTED_ARMING_STATES: Incomplete
SUPPORTED_ARMING_STATE_TO_FEATURE: Incomplete
ATTR_PREVIOUS_STATE: str
ATTR_NEXT_STATE: str

def _state_validator(config: dict[AlarmControlPanelState | str, Any]) -> dict[str, Any]: ...
def _state_schema(state: str) -> vol.Schema: ...

PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ManualAlarm(AlarmControlPanelEntity, RestoreEntity):
    _attr_should_poll: bool
    _state: AlarmControlPanelState
    _hass: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _code: Incomplete
    _attr_code_arm_required: Incomplete
    _disarm_after_trigger: Incomplete
    _previous_state: AlarmControlPanelState
    _state_ts: datetime.datetime
    _delay_time_by_state: dict[AlarmControlPanelState, Any]
    _trigger_time_by_state: dict[AlarmControlPanelState, Any]
    _arming_time_by_state: dict[AlarmControlPanelState, Any]
    _attr_supported_features: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, unique_id: str | None, code: str | None, code_template: Template | None, code_arm_required: bool, disarm_after_trigger: bool, config: dict[str, Any]) -> None: ...
    @property
    def alarm_state(self) -> AlarmControlPanelState: ...
    @property
    def _active_state(self) -> AlarmControlPanelState: ...
    def _arming_time(self, state: AlarmControlPanelState) -> datetime.timedelta: ...
    def _pending_time(self, state: AlarmControlPanelState) -> datetime.timedelta: ...
    def _within_arming_time(self, state: AlarmControlPanelState) -> bool: ...
    def _within_pending_time(self, state: AlarmControlPanelState) -> bool: ...
    @property
    def code_format(self) -> CodeFormat | None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    async def async_alarm_trigger(self, code: str | None = None) -> None: ...
    def _async_update_state(self, state: AlarmControlPanelState) -> None: ...
    def _async_set_state_update_events(self) -> None: ...
    def _async_validate_code(self, code: str | None, state: str) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @callback
    def async_scheduled_update(self, now: datetime.datetime) -> None: ...
    async def async_added_to_hass(self) -> None: ...
