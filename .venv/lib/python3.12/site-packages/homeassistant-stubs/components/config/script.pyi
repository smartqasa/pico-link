from .const import ACTION_DELETE as ACTION_DELETE
from .view import EditKeyBasedConfigView as EditKeyBasedConfigView
from homeassistant.components.script.config import async_validate_config_item as async_validate_config_item
from homeassistant.config import SCRIPT_CONFIG_PATH as SCRIPT_CONFIG_PATH
from homeassistant.const import SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> bool: ...

class EditScriptConfigView(EditKeyBasedConfigView):
    def _write_value(self, hass: HomeAssistant, data: dict[str, dict[str, Any]], config_key: str, new_value: dict[str, Any]) -> None: ...
