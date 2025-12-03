from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
