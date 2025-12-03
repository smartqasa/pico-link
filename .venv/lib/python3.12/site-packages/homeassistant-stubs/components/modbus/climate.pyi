from . import get_hub as get_hub
from .const import CALL_TYPE_REGISTER_HOLDING as CALL_TYPE_REGISTER_HOLDING, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CALL_TYPE_WRITE_REGISTERS as CALL_TYPE_WRITE_REGISTERS, CONF_CLIMATES as CONF_CLIMATES, CONF_FAN_MODE_AUTO as CONF_FAN_MODE_AUTO, CONF_FAN_MODE_DIFFUSE as CONF_FAN_MODE_DIFFUSE, CONF_FAN_MODE_FOCUS as CONF_FAN_MODE_FOCUS, CONF_FAN_MODE_HIGH as CONF_FAN_MODE_HIGH, CONF_FAN_MODE_LOW as CONF_FAN_MODE_LOW, CONF_FAN_MODE_MEDIUM as CONF_FAN_MODE_MEDIUM, CONF_FAN_MODE_MIDDLE as CONF_FAN_MODE_MIDDLE, CONF_FAN_MODE_OFF as CONF_FAN_MODE_OFF, CONF_FAN_MODE_ON as CONF_FAN_MODE_ON, CONF_FAN_MODE_REGISTER as CONF_FAN_MODE_REGISTER, CONF_FAN_MODE_TOP as CONF_FAN_MODE_TOP, CONF_FAN_MODE_VALUES as CONF_FAN_MODE_VALUES, CONF_HVAC_MODE_AUTO as CONF_HVAC_MODE_AUTO, CONF_HVAC_MODE_COOL as CONF_HVAC_MODE_COOL, CONF_HVAC_MODE_DRY as CONF_HVAC_MODE_DRY, CONF_HVAC_MODE_FAN_ONLY as CONF_HVAC_MODE_FAN_ONLY, CONF_HVAC_MODE_HEAT as CONF_HVAC_MODE_HEAT, CONF_HVAC_MODE_HEAT_COOL as CONF_HVAC_MODE_HEAT_COOL, CONF_HVAC_MODE_OFF as CONF_HVAC_MODE_OFF, CONF_HVAC_MODE_REGISTER as CONF_HVAC_MODE_REGISTER, CONF_HVAC_MODE_VALUES as CONF_HVAC_MODE_VALUES, CONF_HVAC_ONOFF_REGISTER as CONF_HVAC_ONOFF_REGISTER, CONF_MAX_TEMP as CONF_MAX_TEMP, CONF_MIN_TEMP as CONF_MIN_TEMP, CONF_STEP as CONF_STEP, CONF_SWING_MODE_REGISTER as CONF_SWING_MODE_REGISTER, CONF_SWING_MODE_SWING_BOTH as CONF_SWING_MODE_SWING_BOTH, CONF_SWING_MODE_SWING_HORIZ as CONF_SWING_MODE_SWING_HORIZ, CONF_SWING_MODE_SWING_OFF as CONF_SWING_MODE_SWING_OFF, CONF_SWING_MODE_SWING_ON as CONF_SWING_MODE_SWING_ON, CONF_SWING_MODE_SWING_VERT as CONF_SWING_MODE_SWING_VERT, CONF_SWING_MODE_VALUES as CONF_SWING_MODE_VALUES, CONF_TARGET_TEMP as CONF_TARGET_TEMP, CONF_TARGET_TEMP_WRITE_REGISTERS as CONF_TARGET_TEMP_WRITE_REGISTERS, CONF_WRITE_REGISTERS as CONF_WRITE_REGISTERS, DataType as DataType
from .entity import BaseStructPlatform as BaseStructPlatform
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_DIFFUSE as FAN_DIFFUSE, FAN_FOCUS as FAN_FOCUS, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_MIDDLE as FAN_MIDDLE, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, FAN_TOP as FAN_TOP, HVACMode as HVACMode, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_ON as SWING_ON, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
HVACMODE_TO_TARG_TEMP_REG_INDEX_ARRAY: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ModbusThermostat(BaseStructPlatform, RestoreEntity, ClimateEntity):
    _attr_supported_features: Incomplete
    _target_temperature_register: Incomplete
    _target_temperature_write_registers: Incomplete
    _unit: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_precision: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_target_temperature_step: Incomplete
    _hvac_mode_register: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _hvac_mode_mapping: list[tuple[int, HVACMode]]
    _hvac_mode_write_registers: Incomplete
    _fan_mode_register: Incomplete
    _attr_fan_modes: Incomplete
    _attr_fan_mode: Incomplete
    _fan_mode_mapping_to_modbus: dict[str, int]
    _fan_mode_mapping_from_modbus: dict[int, str]
    _swing_mode_register: Incomplete
    _attr_swing_modes: Incomplete
    _attr_swing_mode: Incomplete
    _swing_mode_modbus_mapping: list[tuple[int, str]]
    _hvac_onoff_register: Incomplete
    _hvac_onoff_write_registers: Incomplete
    def __init__(self, hass: HomeAssistant, hub: ModbusHub, config: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    _attr_available: Incomplete
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_update(self, now: datetime | None = None) -> None: ...
    _value: Incomplete
    async def _async_read_register(self, register_type: str, register: int, raw: bool | None = False) -> float | None: ...
