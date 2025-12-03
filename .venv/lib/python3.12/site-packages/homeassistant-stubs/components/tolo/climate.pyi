from .const import DOMAIN as DOMAIN
from .coordinator import ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tololib import TARGET_HUMIDITY_MAX, TARGET_HUMIDITY_MIN, TARGET_TEMPERATURE_MAX, TARGET_TEMPERATURE_MIN
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SaunaClimate(ToloSaunaCoordinatorEntity, ClimateEntity):
    _attr_fan_modes: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_max_humidity = TARGET_HUMIDITY_MAX
    _attr_max_temp = TARGET_TEMPERATURE_MAX
    _attr_min_humidity = TARGET_HUMIDITY_MIN
    _attr_min_temp = TARGET_TEMPERATURE_MIN
    _attr_name: Incomplete
    _attr_precision = PRECISION_WHOLE
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: int
    _attr_temperature_unit: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def current_temperature(self) -> int: ...
    @property
    def current_humidity(self) -> int: ...
    @property
    def target_temperature(self) -> int: ...
    @property
    def target_humidity(self) -> int: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def fan_mode(self) -> str: ...
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    def set_fan_mode(self, fan_mode: str) -> None: ...
    def set_humidity(self, humidity: int) -> None: ...
    def set_temperature(self, **kwargs: Any) -> None: ...
    def _set_power_and_fan(self, power_on: bool, fan_on: bool) -> None: ...
