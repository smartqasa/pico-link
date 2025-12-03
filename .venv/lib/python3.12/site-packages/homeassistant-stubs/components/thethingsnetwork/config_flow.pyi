from .const import CONF_APP_ID as CONF_APP_ID, DOMAIN as DOMAIN, TTN_API_HOST as TTN_API_HOST
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete

class TTNFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
