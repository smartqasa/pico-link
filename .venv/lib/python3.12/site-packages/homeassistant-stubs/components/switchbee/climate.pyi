from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBeeCoordinator as SwitchBeeCoordinator
from .entity import SwitchBeeDeviceEntity as SwitchBeeDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from switchbee.device import SwitchBeeThermostat
from typing import Any

FAN_SB_TO_HASS: Incomplete
FAN_HASS_TO_SB: dict[str | None, str]
HVAC_MODE_SB_TO_HASS: Incomplete
HVAC_MODE_HASS_TO_SB: dict[HVACMode | str | None, str]
HVAC_ACTION_SB_TO_HASS: Incomplete
HVAC_UNIT_SB_TO_HASS: Incomplete
SUPPORTED_FAN_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitchBeeClimateEntity(SwitchBeeDeviceEntity[SwitchBeeThermostat], ClimateEntity):
    _attr_fan_modes = SUPPORTED_FAN_MODES
    _attr_target_temperature_step: int
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, device: SwitchBeeThermostat, coordinator: SwitchBeeCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_hvac_mode: HVACMode
    _attr_fan_mode: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    def _update_attrs_from_coordinator(self) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def _operate(self, power: str | None = None, mode: str | None = None, fan: str | None = None, target_temperature: int | None = None) -> None: ...
