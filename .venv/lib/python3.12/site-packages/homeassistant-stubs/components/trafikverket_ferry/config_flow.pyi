from .const import CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from .util import create_unique_id as create_unique_id
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.helpers import selector as selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

DATA_SCHEMA: Incomplete
DATA_SCHEMA_REAUTH: Incomplete

class TVFerryConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def validate_input(self, api_key: str, ferry_from: str, ferry_to: str) -> None: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
