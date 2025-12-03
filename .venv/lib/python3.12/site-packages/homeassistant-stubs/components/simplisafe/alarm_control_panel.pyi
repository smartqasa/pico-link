from . import SimpliSafe as SimpliSafe
from .const import ATTR_ALARM_DURATION as ATTR_ALARM_DURATION, ATTR_ALARM_VOLUME as ATTR_ALARM_VOLUME, ATTR_CHIME_VOLUME as ATTR_CHIME_VOLUME, ATTR_ENTRY_DELAY_AWAY as ATTR_ENTRY_DELAY_AWAY, ATTR_ENTRY_DELAY_HOME as ATTR_ENTRY_DELAY_HOME, ATTR_EXIT_DELAY_AWAY as ATTR_EXIT_DELAY_AWAY, ATTR_EXIT_DELAY_HOME as ATTR_EXIT_DELAY_HOME, ATTR_LIGHT as ATTR_LIGHT, ATTR_VOICE_PROMPT_VOLUME as ATTR_VOICE_PROMPT_VOLUME, DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import SimpliSafeEntity as SimpliSafeEntity
from .typing import SystemType as SystemType
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.websocket import WebsocketEvent as WebsocketEvent

ATTR_BATTERY_BACKUP_POWER_LEVEL: str
ATTR_GSM_STRENGTH: str
ATTR_PIN_NAME: str
ATTR_RF_JAMMING: str
ATTR_WALL_POWER_LEVEL: str
ATTR_WIFI_STRENGTH: str
STATE_MAP_FROM_REST_API: Incomplete
STATE_MAP_FROM_WEBSOCKET_EVENT: Incomplete
WEBSOCKET_EVENTS_TO_LISTEN_FOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimpliSafeAlarm(SimpliSafeEntity, AlarmControlPanelEntity):
    _attr_code_arm_required: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _last_event: Incomplete
    def __init__(self, simplisafe: SimpliSafe, system: SystemType) -> None: ...
    _attr_alarm_state: Incomplete
    @callback
    def _set_state_from_system_data(self) -> None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    @callback
    def async_update_from_rest_api(self) -> None: ...
    _attr_changed_by: Incomplete
    @callback
    def async_update_from_websocket_event(self, event: WebsocketEvent) -> None: ...
