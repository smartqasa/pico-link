from .const import ATTR_STATE_BATTERY_LOW as ATTR_STATE_BATTERY_LOW, ATTR_STATE_HOLIDAY_MODE as ATTR_STATE_HOLIDAY_MODE, ATTR_STATE_SUMMER_MODE as ATTR_STATE_SUMMER_MODE, ATTR_STATE_WINDOW_OPEN as ATTR_STATE_WINDOW_OPEN, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import FritzboxConfigEntry as FritzboxConfigEntry, FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from .entity import FritzBoxDeviceEntity as FritzBoxDeviceEntity
from .model import ClimateExtraAttributes as ClimateExtraAttributes
from .sensor import value_scheduled_preset as value_scheduled_preset
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

HVAC_MODES: Incomplete
PRESET_HOLIDAY: str
PRESET_SUMMER: str
PRESET_MODES: Incomplete
SUPPORTED_FEATURES: Incomplete
MIN_TEMPERATURE: int
MAX_TEMPERATURE: int
ON_API_TEMPERATURE: float
OFF_API_TEMPERATURE: float
ON_REPORT_SET_TEMPERATURE: float
OFF_REPORT_SET_TEMPERATURE: float

async def async_setup_entry(hass: HomeAssistant, entry: FritzboxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxThermostat(FritzBoxDeviceEntity, ClimateEntity):
    _attr_precision = PRECISION_HALVES
    _attr_temperature_unit: Incomplete
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    def __init__(self, coordinator: FritzboxDataUpdateCoordinator, ain: str) -> None: ...
    @callback
    def async_write_ha_state(self) -> None: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    def min_temp(self) -> int: ...
    @property
    def max_temp(self) -> int: ...
    @property
    def extra_state_attributes(self) -> ClimateExtraAttributes: ...
