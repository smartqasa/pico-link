from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

_LOGGER: Incomplete
DATA_SCHEMA: Incomplete

class FAADelaysConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
