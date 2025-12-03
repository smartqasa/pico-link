from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Incomplete

class UpCloudConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    username: str
    password: str
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_show_form(self, step_id: str, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> UpCloudOptionsFlow: ...

class UpCloudOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
