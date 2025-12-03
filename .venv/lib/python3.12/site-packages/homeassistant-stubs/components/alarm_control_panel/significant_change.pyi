from . import ATTR_CHANGED_BY as ATTR_CHANGED_BY, ATTR_CODE_ARM_REQUIRED as ATTR_CODE_ARM_REQUIRED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

SIGNIFICANT_ATTRIBUTES: set[str]

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
