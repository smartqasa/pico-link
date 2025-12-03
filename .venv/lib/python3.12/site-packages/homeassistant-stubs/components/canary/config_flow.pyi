from .const import CONF_FFMPEG_ARGUMENTS as CONF_FFMPEG_ARGUMENTS, DEFAULT_FFMPEG_ARGUMENTS as DEFAULT_FFMPEG_ARGUMENTS, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any, Final

_LOGGER: Final[Incomplete]

def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> bool: ...

class CanaryConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CanaryOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
