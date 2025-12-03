from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_TOKEN as CONF_TOKEN, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any, NamedTuple

CONF_AUTH_CODE: str
STEP_USER_SCHEMA: Incomplete

class SimpliSafeOAuthValues(NamedTuple):
    auth_url: str
    code_verifier: str

@callback
def async_get_simplisafe_oauth_values() -> SimpliSafeOAuthValues: ...

class SimpliSafeFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _oauth_values: SimpliSafeOAuthValues
    _reauth: bool
    def __init__(self) -> None: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SimpliSafeOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class SimpliSafeOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
