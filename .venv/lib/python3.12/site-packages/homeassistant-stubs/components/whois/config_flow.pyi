from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN
from typing import Any

class WhoisFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    imported_name: str | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
