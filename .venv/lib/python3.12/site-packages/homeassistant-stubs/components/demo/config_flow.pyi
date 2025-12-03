from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from typing import Any

CONF_STRING: str
CONF_BOOLEAN: str
CONF_INT: str
CONF_SELECT: str
CONF_MULTISELECT: str

class DemoConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...

class OptionsFlowHandler(OptionsFlow):
    options: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_options_1(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_options_2(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _update_options(self) -> ConfigFlowResult: ...
