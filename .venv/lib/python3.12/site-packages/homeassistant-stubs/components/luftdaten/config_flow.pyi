from .const import CONF_SENSOR_ID as CONF_SENSOR_ID, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP
from homeassistant.core import callback as callback
from typing import Any

class SensorCommunityFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @callback
    def _show_form(self, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
