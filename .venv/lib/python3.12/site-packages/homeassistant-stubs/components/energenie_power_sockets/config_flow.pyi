from .const import CONF_DEVICE_API_ID as CONF_DEVICE_API_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from typing import Any

class EGPSConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
