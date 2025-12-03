from .const import ATTR_LOCKED as ATTR_LOCKED, ATTR_OFFSET as ATTR_OFFSET, ATTR_VALVE as ATTR_VALVE
from .entity import DeconzDevice as DeconzDevice
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, DOMAIN as CLIMATE_DOMAIN, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor.thermostat import Thermostat
from typing import Any

DECONZ_FAN_SMART: str
FAN_MODE_TO_DECONZ: Incomplete
DECONZ_TO_FAN_MODE: Incomplete
HVAC_MODE_TO_DECONZ: Incomplete
DECONZ_PRESET_AUTO: str
DECONZ_PRESET_COMPLEX: str
DECONZ_PRESET_HOLIDAY: str
DECONZ_PRESET_MANUAL: str
PRESET_MODE_TO_DECONZ: Incomplete
DECONZ_TO_PRESET_MODE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzThermostat(DeconzDevice[Thermostat], ClimateEntity):
    TYPE = CLIMATE_DOMAIN
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _deconz_to_hvac_mode: Incomplete
    _attr_supported_features: Incomplete
    _attr_fan_modes: Incomplete
    _attr_preset_modes: Incomplete
    def __init__(self, device: Thermostat, hub: DeconzHub) -> None: ...
    @property
    def fan_mode(self) -> str: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool | int]: ...
