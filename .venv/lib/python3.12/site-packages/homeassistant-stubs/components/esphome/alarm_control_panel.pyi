from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import APIIntEnum, AlarmControlPanelEntityState as ESPHomeAlarmControlPanelEntityState, AlarmControlPanelInfo, AlarmControlPanelState as ESPHomeAlarmControlPanelState, EntityInfo as EntityInfo
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat
from homeassistant.core import callback as callback

_ESPHOME_ACP_STATE_TO_HASS_STATE: EsphomeEnumMapper[ESPHomeAlarmControlPanelState, AlarmControlPanelState]

class EspHomeACPFeatures(APIIntEnum):
    ARM_HOME: int
    ARM_AWAY: int
    ARM_NIGHT: int
    TRIGGER: int
    ARM_CUSTOM_BYPASS: int
    ARM_VACATION: int

class EsphomeAlarmControlPanel(EsphomeEntity[AlarmControlPanelInfo, ESPHomeAlarmControlPanelEntityState], AlarmControlPanelEntity):
    _attr_supported_features: Incomplete
    _attr_code_format: Incomplete
    _attr_code_arm_required: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    @convert_api_error_ha_error
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    @convert_api_error_ha_error
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    @convert_api_error_ha_error
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    @convert_api_error_ha_error
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    @convert_api_error_ha_error
    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    @convert_api_error_ha_error
    async def async_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    @convert_api_error_ha_error
    async def async_alarm_trigger(self, code: str | None = None) -> None: ...

async_setup_entry: Incomplete
