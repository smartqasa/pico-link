from .const import DOMAIN as DOMAIN, TYPE_TO_PLATFORM as TYPE_TO_PLATFORM
from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator
from .entity import LookinCoordinatorEntity as LookinCoordinatorEntity
from .models import LookinData as LookinData
from _typeshed import Incomplete
from aiolookin import Climate, MeteoSensor as MeteoSensor, Remote as Remote
from aiolookin.models import UDPEvent as UDPEvent
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MIDDLE as FAN_MIDDLE, HVACMode as HVACMode, SWING_BOTH as SWING_BOTH, SWING_OFF as SWING_OFF
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

LOOKIN_FAN_MODE_IDX_TO_HASS: Final[Incomplete]
LOOKIN_SWING_MODE_IDX_TO_HASS: Final[Incomplete]
LOOKIN_HVAC_MODE_IDX_TO_HASS: Final[Incomplete]
HASS_TO_LOOKIN_HVAC_MODE: dict[str, int]
HASS_TO_LOOKIN_FAN_MODE: dict[str, int]
HASS_TO_LOOKIN_SWING_MODE: dict[str, int]
MIN_TEMP: Final[int]
MAX_TEMP: Final[int]
LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ConditionerEntity(LookinCoordinatorEntity, ClimateEntity):
    _attr_current_humidity: float | None
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_fan_modes: list[str]
    _attr_swing_modes: list[str]
    _attr_hvac_modes: list[HVACMode]
    _attr_min_temp = MIN_TEMP
    _attr_max_temp = MAX_TEMP
    _attr_target_temperature_step = PRECISION_WHOLE
    def __init__(self, uuid: str, device: Climate, lookin_data: LookinData, coordinator: LookinDataUpdateCoordinator[Remote]) -> None: ...
    @property
    def _climate(self) -> Climate: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def _async_update_conditioner(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_fan_mode: Incomplete
    _attr_swing_mode: Incomplete
    _attr_hvac_mode: Incomplete
    def _async_update_from_data(self) -> None: ...
    @callback
    def _async_update_meteo_from_value(self, event: UDPEvent) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @callback
    def _async_push_update(self, event: UDPEvent) -> None: ...
    async def async_added_to_hass(self) -> None: ...
