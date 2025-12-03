from . import ATTR_ACTION as ATTR_ACTION, ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_valid_float as check_valid_float
from typing import Any

SIGNIFICANT_ATTRIBUTES: set[str]

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
