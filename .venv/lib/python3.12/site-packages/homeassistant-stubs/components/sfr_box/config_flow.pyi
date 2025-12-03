from .const import DEFAULT_HOST as DEFAULT_HOST, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers import selector as selector
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from sfrbox_api.bridge import SFRBox
from typing import Any

DATA_SCHEMA: Incomplete
AUTH_SCHEMA: Incomplete

class SFRBoxFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _box: SFRBox
    _config: dict[str, Any]
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_choose_auth(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_auth(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_skip_auth(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
