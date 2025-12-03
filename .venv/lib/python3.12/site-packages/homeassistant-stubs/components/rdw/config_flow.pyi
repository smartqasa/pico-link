from .const import CONF_LICENSE_PLATE as CONF_LICENSE_PLATE, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class RDWFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
