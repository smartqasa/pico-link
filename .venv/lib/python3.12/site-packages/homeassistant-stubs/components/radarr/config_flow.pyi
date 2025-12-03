from .const import DEFAULT_NAME as DEFAULT_NAME, DEFAULT_URL as DEFAULT_URL, DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class RadarrConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> tuple[str, str, str] | None: ...
