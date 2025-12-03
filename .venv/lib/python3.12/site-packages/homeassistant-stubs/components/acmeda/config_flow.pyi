import aiopulse
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID
from typing import Any

class AcmedaFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_hubs: dict[str, aiopulse.Hub] | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_create(self, hub: aiopulse.Hub) -> ConfigFlowResult: ...
