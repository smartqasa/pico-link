from . import SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_SWITCHBOT_HVAC_MODES: dict[HVACMode, int]
_DEFAULT_SWITCHBOT_HVAC_MODE: Incomplete
_SWITCHBOT_FAN_MODES: dict[str, int]
_DEFAULT_SWITCHBOT_FAN_MODE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitchBotCloudAirConditioner(SwitchBotCloudEntity, ClimateEntity):
    _attr_assumed_state: bool
    _attr_supported_features: Incomplete
    _attr_fan_modes: Incomplete
    _attr_fan_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_target_temperature: int
    _attr_target_temperature_step: int
    _attr_precision: int
    _attr_name: Incomplete
    async def _do_send_command(self, hvac_mode: HVACMode | None = None, fan_mode: str | None = None, temperature: float | None = None) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
