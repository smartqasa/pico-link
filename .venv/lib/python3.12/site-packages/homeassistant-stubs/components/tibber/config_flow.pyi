from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

DATA_SCHEMA: Incomplete
ERR_TIMEOUT: str
ERR_CLIENT: str
ERR_TOKEN: str
TOKEN_URL: str

class TibberConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
