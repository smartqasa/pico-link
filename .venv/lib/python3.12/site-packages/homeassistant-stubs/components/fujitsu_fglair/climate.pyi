from . import FGLairConfigEntry as FGLairConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import FGLairCoordinator as FGLairCoordinator
from _typeshed import Incomplete
from ayla_iot_unofficial.fujitsu_hvac import FujitsuHVAC as FujitsuHVAC
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

HA_TO_FUJI_FAN: Incomplete
FUJI_TO_HA_FAN: Incomplete
HA_TO_FUJI_HVAC: Incomplete
FUJI_TO_HA_HVAC: Incomplete
HA_TO_FUJI_SWING: Incomplete
FUJI_TO_HA_SWING: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: FGLairConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FGLairDevice(CoordinatorEntity[FGLairCoordinator], ClimateEntity):
    _attr_temperature_unit: Incomplete
    _attr_precision = PRECISION_HALVES
    _attr_target_temperature_step: float
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, coordinator: FGLairCoordinator, device: FujitsuHVAC) -> None: ...
    @property
    def device(self) -> FujitsuHVAC: ...
    @property
    def available(self) -> bool: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    _attr_fan_mode: Incomplete
    _attr_fan_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_swing_mode: Incomplete
    _attr_swing_modes: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    def _set_attr(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
