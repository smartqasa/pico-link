from .const import NumberDeviceClass as NumberDeviceClass
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_percentage_change as check_percentage_change, check_valid_float as check_valid_float
from typing import Any

def _absolute_and_relative_change(old_state: float | None, new_state: float | None, absolute_change: float, percentage_change: float) -> bool: ...
@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
