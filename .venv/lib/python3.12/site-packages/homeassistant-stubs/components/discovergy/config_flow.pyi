from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

class DiscovergyConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...
