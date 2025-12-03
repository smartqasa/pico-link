from _typeshed import Incomplete
from homeassistant.components.water_heater import WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SUPPORT_FLAGS_HEATER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoWaterHeater(WaterHeaterEntity):
    _attr_should_poll: bool
    _attr_supported_features = SUPPORT_FLAGS_HEATER
    _attr_name: Incomplete
    _attr_target_temperature: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_is_away_mode_on: Incomplete
    _attr_current_operation: Incomplete
    _attr_operation_list: Incomplete
    def __init__(self, name: str, target_temperature: int, unit_of_measurement: str, away: bool, current_operation: str) -> None: ...
    def set_temperature(self, **kwargs: Any) -> None: ...
    def set_operation_mode(self, operation_mode: str) -> None: ...
    def turn_away_mode_on(self) -> None: ...
    def turn_away_mode_off(self) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
