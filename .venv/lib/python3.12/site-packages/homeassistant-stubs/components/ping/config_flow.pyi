from .const import CONF_PING_COUNT as CONF_PING_COUNT, DEFAULT_PING_COUNT as DEFAULT_PING_COUNT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.device_tracker import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from homeassistant.util.network import is_ip_address as is_ip_address
from typing import Any

_LOGGER: Incomplete

def _clean_user_input(user_input: dict[str, Any]) -> dict[str, Any]: ...

class PingConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
