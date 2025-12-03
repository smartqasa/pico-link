from .const import ACTION_DELETE as ACTION_DELETE
from .view import EditIdBasedConfigView as EditIdBasedConfigView
from homeassistant.components.scene import PLATFORM_SCHEMA as SCENE_PLATFORM_SCHEMA
from homeassistant.config import SCENE_CONFIG_PATH as SCENE_CONFIG_PATH
from homeassistant.const import CONF_ID as CONF_ID, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

PLATFORM_SCHEMA = SCENE_PLATFORM_SCHEMA

@callback
def async_setup(hass: HomeAssistant) -> bool: ...

class EditSceneConfigView(EditIdBasedConfigView):
    def _write_value(self, hass: HomeAssistant, data: list[dict[str, Any]], config_key: str, new_value: dict[str, Any]) -> None: ...
