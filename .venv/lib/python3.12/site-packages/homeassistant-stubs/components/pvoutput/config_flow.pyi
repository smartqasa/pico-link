from .const import CONF_SYSTEM_ID as CONF_SYSTEM_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

async def validate_input(hass: HomeAssistant, *, api_key: str, system_id: int) -> None: ...

class PVOutputFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    imported_name: str | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
