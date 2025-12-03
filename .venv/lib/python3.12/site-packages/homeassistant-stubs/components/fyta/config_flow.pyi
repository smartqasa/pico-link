from .const import CONF_EXPIRATION as CONF_EXPIRATION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from fyta_cli.fyta_models import Credentials as Credentials
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete
DATA_SCHEMA: Incomplete

class FytaConfigFlow(ConfigFlow, domain=DOMAIN):
    credentials: Credentials
    VERSION: int
    MINOR_VERSION: int
    async def async_auth(self, user_input: Mapping[str, Any]) -> dict[str, str]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
