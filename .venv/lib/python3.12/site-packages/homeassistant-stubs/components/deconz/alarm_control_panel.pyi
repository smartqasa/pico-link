from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat, DOMAIN as ALARM_CONTROl_PANEL_DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor.ancillary_control import AncillaryControl

DECONZ_TO_ALARM_STATE: Incomplete

def get_alarm_system_id_for_unique_id(hub: DeconzHub, unique_id: str) -> str | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzAlarmControlPanel(DeconzDevice[AncillaryControl], AlarmControlPanelEntity):
    _update_key: str
    TYPE = ALARM_CONTROl_PANEL_DOMAIN
    _attr_code_format: Incomplete
    _attr_supported_features: Incomplete
    alarm_system_id: Incomplete
    def __init__(self, device: AncillaryControl, hub: DeconzHub, alarm_system_id: str) -> None: ...
    @callback
    def async_update_callback(self) -> None: ...
    @property
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
