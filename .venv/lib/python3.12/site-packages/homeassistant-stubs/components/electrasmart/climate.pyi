from .const import API_DELAY as API_DELAY, CONSECUTIVE_FAILURE_THRESHOLD as CONSECUTIVE_FAILURE_THRESHOLD, DOMAIN as DOMAIN, PRESET_NONE as PRESET_NONE, PRESET_SHABAT as PRESET_SHABAT, SCAN_INTERVAL_SEC as SCAN_INTERVAL_SEC, UNAVAILABLE_THRESH_SEC as UNAVAILABLE_THRESH_SEC
from _typeshed import Incomplete
from electrasmart.api import ElectraAPI as ElectraAPI
from electrasmart.device import ElectraAirConditioner as ElectraAirConditioner
from electrasmart.device.const import MAX_TEMP, MIN_TEMP
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

FAN_ELECTRA_TO_HASS: Incomplete
FAN_HASS_TO_ELECTRA: Incomplete
HVAC_MODE_ELECTRA_TO_HASS: Incomplete
HVAC_MODE_HASS_TO_ELECTRA: Incomplete
ELECTRA_FAN_MODES: Incomplete
ELECTRA_MODES: Incomplete
_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElectraClimateEntity(ClimateEntity):
    _attr_fan_modes = ELECTRA_FAN_MODES
    _attr_target_temperature_step: int
    _attr_max_temp = MAX_TEMP
    _attr_min_temp = MIN_TEMP
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes = ELECTRA_MODES
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _api: Incomplete
    _electra_ac_device: Incomplete
    _attr_unique_id: Incomplete
    _attr_supported_features: Incomplete
    _attr_swing_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_device_info: Incomplete
    _last_state_update: int
    _consecutive_failures: int
    _skip_update: bool
    _was_available: bool
    def __init__(self, device: ElectraAirConditioner, api: ElectraAPI) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _attr_fan_mode: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_swing_mode: Incomplete
    _attr_preset_mode: Incomplete
    def _update_device_attrs(self) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def _async_operate_electra_ac(self) -> None: ...
