from . import get_api as get_api
from .const import CONF_LIMIT as CONF_LIMIT, CONF_ORDER as CONF_ORDER, DEFAULT_LIMIT as DEFAULT_LIMIT, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_ORDER as DEFAULT_ORDER, DEFAULT_PATH as DEFAULT_PATH, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_SSL as DEFAULT_SSL, DOMAIN as DOMAIN, SUPPORTED_ORDER_MODES as SUPPORTED_ORDER_MODES
from .errors import AuthenticationError as AuthenticationError, CannotConnect as CannotConnect, UnknownError as UnknownError
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PATH as CONF_PATH, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from typing import Any

DATA_SCHEMA: Incomplete

class TransmissionFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> TransmissionOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...

class TransmissionOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
