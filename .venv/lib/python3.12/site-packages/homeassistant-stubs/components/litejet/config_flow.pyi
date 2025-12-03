from .const import CONF_DEFAULT_TRANSITION as CONF_DEFAULT_TRANSITION, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from typing import Any

class LiteJetOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class LiteJetConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> LiteJetOptionsFlow: ...
