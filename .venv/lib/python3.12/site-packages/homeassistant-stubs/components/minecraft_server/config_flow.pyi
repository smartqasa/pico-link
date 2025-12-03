from .api import MinecraftServer as MinecraftServer, MinecraftServerAddressError as MinecraftServerAddressError, MinecraftServerType as MinecraftServerType
from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE
from typing import Any

DEFAULT_ADDRESS: str
_LOGGER: Incomplete

class MinecraftServerConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _show_config_form(self, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
