from .const import CONF_ZIP_CODE as CONF_ZIP_CODE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

class IqviaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
