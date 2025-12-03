from . import ATTR_DIRECTION as ATTR_DIRECTION, ATTR_OSCILLATING as ATTR_OSCILLATING, ATTR_PERCENTAGE as ATTR_PERCENTAGE, ATTR_PRESET_MODE as ATTR_PRESET_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_valid_float as check_valid_float
from typing import Any

SIGNIFICANT_ATTRIBUTES: set[str]

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
