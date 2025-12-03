from .const import ATTR_INSTALLED_VERSION as ATTR_INSTALLED_VERSION, ATTR_LATEST_VERSION as ATTR_LATEST_VERSION
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
