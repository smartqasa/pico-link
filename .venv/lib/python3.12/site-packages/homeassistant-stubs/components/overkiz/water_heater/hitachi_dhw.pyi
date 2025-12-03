from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.water_heater import STATE_HIGH_DEMAND as STATE_HIGH_DEMAND, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, UnitOfTemperature as UnitOfTemperature
from typing import Any

OVERKIZ_TO_OPERATION_MODE: dict[str, str]
OPERATION_MODE_TO_OVERKIZ: Incomplete

class HitachiDHW(OverkizEntity, WaterHeaterEntity):
    _attr_min_temp: float
    _attr_max_temp: float
    _attr_precision = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_operation_list: Incomplete
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def current_operation(self) -> str | None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
