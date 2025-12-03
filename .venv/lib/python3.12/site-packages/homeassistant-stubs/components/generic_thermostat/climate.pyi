from .const import CONF_AC_MODE as CONF_AC_MODE, CONF_COLD_TOLERANCE as CONF_COLD_TOLERANCE, CONF_HEATER as CONF_HEATER, CONF_HOT_TOLERANCE as CONF_HOT_TOLERANCE, CONF_MAX_TEMP as CONF_MAX_TEMP, CONF_MIN_DUR as CONF_MIN_DUR, CONF_MIN_TEMP as CONF_MIN_TEMP, CONF_PRESETS as CONF_PRESETS, CONF_SENSOR as CONF_SENSOR, DEFAULT_TOLERANCE as DEFAULT_TOLERANCE, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from collections.abc import Mapping
from datetime import datetime, timedelta
from homeassistant.components.climate import ATTR_PRESET_MODE as ATTR_PRESET_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import CoreState as CoreState, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import ConditionError as ConditionError
from homeassistant.helpers import condition as condition
from homeassistant.helpers.device import async_device_info_to_link_from_entity as async_device_info_to_link_from_entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, VolDictType as VolDictType
from typing import Any

_LOGGER: Incomplete
DEFAULT_NAME: str
CONF_INITIAL_HVAC_MODE: str
CONF_KEEP_ALIVE: str
CONF_PRECISION: str
CONF_TARGET_TEMP: str
CONF_TEMP_STEP: str
PRESETS_SCHEMA: VolDictType
PLATFORM_SCHEMA_COMMON: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def _async_setup_config(hass: HomeAssistant, config: Mapping[str, Any], unique_id: str | None, async_add_entities: AddEntitiesCallback) -> None: ...

class GenericThermostat(ClimateEntity, RestoreEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    heater_entity_id: Incomplete
    sensor_entity_id: Incomplete
    _attr_device_info: Incomplete
    ac_mode: Incomplete
    min_cycle_duration: Incomplete
    _cold_tolerance: Incomplete
    _hot_tolerance: Incomplete
    _keep_alive: Incomplete
    _hvac_mode: Incomplete
    _saved_target_temp: Incomplete
    _temp_precision: Incomplete
    _temp_target_temperature_step: Incomplete
    _attr_hvac_modes: Incomplete
    _active: bool
    _cur_temp: float | None
    _temp_lock: Incomplete
    _min_temp: Incomplete
    _max_temp: Incomplete
    _attr_preset_mode: Incomplete
    _target_temp: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_unique_id: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _presets: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, heater_entity_id: str, sensor_entity_id: str, min_temp: float | None, max_temp: float | None, target_temp: float | None, ac_mode: bool | None, min_cycle_duration: timedelta | None, cold_tolerance: float, hot_tolerance: float, keep_alive: timedelta | None, initial_hvac_mode: HVACMode | None, presets: dict[str, float], precision: float | None, target_temperature_step: float | None, unit: UnitOfTemperature, unique_id: str | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def precision(self) -> float: ...
    @property
    def target_temperature_step(self) -> float: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode | None: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def target_temperature(self) -> float | None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    async def _async_sensor_changed(self, event: Event[EventStateChangedData]) -> None: ...
    async def _check_switch_initial_state(self) -> None: ...
    @callback
    def _async_switch_changed(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_update_temp(self, state: State) -> None: ...
    async def _async_control_heating(self, time: datetime | None = None, force: bool = False) -> None: ...
    @property
    def _is_device_active(self) -> bool | None: ...
    async def _async_heater_turn_on(self) -> None: ...
    async def _async_heater_turn_off(self) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
