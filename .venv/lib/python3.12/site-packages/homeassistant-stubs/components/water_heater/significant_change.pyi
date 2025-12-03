from . import ATTR_AWAY_MODE as ATTR_AWAY_MODE, ATTR_CURRENT_TEMPERATURE as ATTR_CURRENT_TEMPERATURE, ATTR_OPERATION_MODE as ATTR_OPERATION_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_valid_float as check_valid_float
from typing import Any

SIGNIFICANT_ATTRIBUTES: set[str]

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
