from .const import CONF_APP_KEY as CONF_APP_KEY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

class AmbientStationFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    def __init__(self) -> None: ...
    async def _show_form(self, errors: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
