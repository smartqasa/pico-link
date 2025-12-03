from .const import API_TIMEOUT as API_TIMEOUT, CONF_REGION as CONF_REGION, DOMAIN as DOMAIN, REGION_DEFAULT as REGION_DEFAULT, REGION_EU as REGION_EU
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

class FGLairConfigFlow(ConfigFlow, domain=DOMAIN):
    MINOR_VERSION: int
    async def _async_validate_credentials(self, user_input: dict[str, Any]) -> dict[str, str]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
