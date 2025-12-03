from .const import CONF_AREA_ID as CONF_AREA_ID, CONF_LOCK_CODE_DIGITS as CONF_LOCK_CODE_DIGITS, DEFAULT_AREA_ID as DEFAULT_AREA_ID, DOMAIN as DOMAIN, YALE_BASE_ERRORS as YALE_BASE_ERRORS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from typing import Any

DATA_SCHEMA: Incomplete
DATA_SCHEMA_AUTH: Incomplete
OPTIONS_SCHEMA: Incomplete

def validate_credentials(username: str, password: str) -> dict[str, Any]: ...

class YaleConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> YaleOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class YaleOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
