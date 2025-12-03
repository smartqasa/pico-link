from .const import ATTR_ENCRYPTED as ATTR_ENCRYPTED, CONF_DEVICE_KEY as CONF_DEVICE_KEY, CONF_SALT as CONF_SALT, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD
from typing import Any

def validate_input(entry: dict[str, str]) -> dict[str, str] | None: ...

class SimplePushFlowHandler(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
