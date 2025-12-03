from . import AirzoneConfigEntry as AirzoneConfigEntry
from .const import API_TEMPERATURE_STEP as API_TEMPERATURE_STEP, TEMP_UNIT_LIB_TO_HASS as TEMP_UNIT_LIB_TO_HASS
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from aioairzone.common import OperationAction, OperationMode
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

BASE_FAN_SPEEDS: Final[dict[int, str]]
FAN_SPEED_MAPS: Final[dict[int, dict[int, str]]]
HVAC_ACTION_LIB_TO_HASS: Final[dict[OperationAction, HVACAction]]
HVAC_MODE_LIB_TO_HASS: Final[dict[OperationMode, HVACMode]]
HVAC_MODE_HASS_TO_LIB: Final[dict[HVACMode, OperationMode]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneClimate(AirzoneZoneEntity, ClimateEntity):
    _attr_name: Incomplete
    _speeds: dict[int, str]
    _speeds_reverse: dict[str, int]
    _attr_unique_id: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry, system_zone_id: str, zone_data: dict) -> None: ...
    _attr_fan_modes: Incomplete
    def _set_fan_speeds(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_current_humidity: Incomplete
    _attr_hvac_action: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_fan_mode: Incomplete
    _attr_target_temperature_high: Incomplete
    _attr_target_temperature_low: Incomplete
    _attr_target_temperature: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
