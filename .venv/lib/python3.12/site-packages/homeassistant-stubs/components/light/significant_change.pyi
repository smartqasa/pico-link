from . import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change
from typing import Any

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
