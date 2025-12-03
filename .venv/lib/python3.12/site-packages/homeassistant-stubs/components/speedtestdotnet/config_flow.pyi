from . import SpeedTestConfigEntry as SpeedTestConfigEntry
from .const import CONF_SERVER_ID as CONF_SERVER_ID, CONF_SERVER_NAME as CONF_SERVER_NAME, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SERVER as DEFAULT_SERVER, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from typing import Any

class SpeedTestFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: SpeedTestConfigEntry) -> SpeedTestOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class SpeedTestOptionsFlowHandler(OptionsFlow):
    _servers: dict
    def __init__(self) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
