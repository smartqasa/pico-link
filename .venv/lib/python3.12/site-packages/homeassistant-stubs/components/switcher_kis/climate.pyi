from . import SwitcherConfigEntry as SwitcherConfigEntry
from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .entity import SwitcherEntity as SwitcherEntity
from .utils import get_breeze_remote_manager as get_breeze_remote_manager
from _typeshed import Incomplete
from aioswitcher.api.remotes import SwitcherBreezeRemote as SwitcherBreezeRemote
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode, SWING_OFF as SWING_OFF, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

API_CONTROL_BREEZE_DEVICE: str
DEVICE_MODE_TO_HA: Incomplete
HA_TO_DEVICE_MODE: Incomplete
DEVICE_FAN_TO_HA: Incomplete
HA_TO_DEVICE_FAN: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: SwitcherConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherClimateEntity(SwitcherEntity, ClimateEntity):
    _attr_name: Incomplete
    _remote: Incomplete
    _attr_unique_id: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_target_temperature_step: int
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, remote: SwitcherBreezeRemote) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_fan_mode: Incomplete
    _attr_fan_modes: Incomplete
    _attr_swing_mode: Incomplete
    _attr_swing_modes: Incomplete
    def _update_data(self, force_update: bool = False) -> None: ...
    async def _async_control_breeze_device(self, **kwargs: Any) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
