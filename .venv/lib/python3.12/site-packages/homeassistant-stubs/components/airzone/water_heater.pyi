from . import AirzoneConfigEntry as AirzoneConfigEntry
from .const import TEMP_UNIT_LIB_TO_HASS as TEMP_UNIT_LIB_TO_HASS
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneHotWaterEntity as AirzoneHotWaterEntity
from _typeshed import Incomplete
from aioairzone.common import HotWaterOperation
from homeassistant.components.water_heater import STATE_ECO as STATE_ECO, STATE_PERFORMANCE as STATE_PERFORMANCE, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

OPERATION_LIB_TO_HASS: Final[dict[HotWaterOperation, str]]
OPERATION_MODE_TO_DHW_PARAMS: Final[dict[str, dict[str, Any]]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneWaterHeater(AirzoneHotWaterEntity, WaterHeaterEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _attr_operation_list: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_current_operation: Incomplete
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_target_temperature: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
