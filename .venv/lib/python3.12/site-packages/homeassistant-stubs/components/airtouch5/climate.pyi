from . import Airtouch5ConfigEntry as Airtouch5ConfigEntry
from .const import DOMAIN as DOMAIN, FAN_INTELLIGENT_AUTO as FAN_INTELLIGENT_AUTO, FAN_TURBO as FAN_TURBO
from .entity import Airtouch5Entity as Airtouch5Entity
from _typeshed import Incomplete
from airtouch5py.airtouch5_simple_client import Airtouch5SimpleClient as Airtouch5SimpleClient
from airtouch5py.packets.ac_ability import AcAbility as AcAbility
from airtouch5py.packets.ac_control import SetAcFanSpeed, SetAcMode, SetPowerSetting, SetpointControl
from airtouch5py.packets.ac_status import AcStatus as AcStatus
from airtouch5py.packets.zone_control import ZoneSettingPower, ZoneSettingValue
from airtouch5py.packets.zone_name import ZoneName as ZoneName
from airtouch5py.packets.zone_status import ZoneStatusZone as ZoneStatusZone
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_DIFFUSE as FAN_DIFFUSE, FAN_FOCUS as FAN_FOCUS, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode, PRESET_BOOST as PRESET_BOOST, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete
AC_MODE_TO_HVAC_MODE: Incomplete
HVAC_MODE_TO_SET_AC_MODE: Incomplete
AC_FAN_SPEED_TO_FAN_SPEED: Incomplete
FAN_MODE_TO_SET_AC_FAN_SPEED: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: Airtouch5ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Airtouch5ClimateEntity(ClimateEntity, Airtouch5Entity):
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    _attr_target_temperature_step: int
    _attr_name: Incomplete

class Airtouch5AC(Airtouch5ClimateEntity):
    _ability: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_fan_modes: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def __init__(self, client: Airtouch5SimpleClient, ability: AcAbility) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_fan_mode: Incomplete
    @callback
    def _async_update_attrs(self, data: dict[int, AcStatus]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def _control(self, *, power: SetPowerSetting = ..., ac_mode: SetAcMode = ..., fan: SetAcFanSpeed = ..., setpoint: SetpointControl = ..., temp: int = 0) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...

class Airtouch5Zone(Airtouch5ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def __init__(self, client: Airtouch5SimpleClient, name: ZoneName, ac: AcAbility) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_preset_mode: Incomplete
    @callback
    def _async_update_attrs(self, data: dict[int, ZoneStatusZone]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def _control(self, *, zsv: ZoneSettingValue = ..., power: ZoneSettingPower = ..., value: float = 0) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
