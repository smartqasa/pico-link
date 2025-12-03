from .const import CONF_PROFILE_ID as CONF_PROFILE_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PROFILE_NAME as CONF_PROFILE_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from nextdns import NextDns
from typing import Any

AUTH_SCHEMA: Incomplete

async def async_init_nextdns(hass: HomeAssistant, api_key: str) -> NextDns: ...

class NextDnsFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    nextdns: NextDns
    api_key: str
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_profiles(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
