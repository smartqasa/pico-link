import voluptuous as vol
from .const import CLIENT_TIMEOUT as CLIENT_TIMEOUT, DEFAULT_BASE as DEFAULT_BASE, DOMAIN as DOMAIN, LOGGER as LOGGER
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_BASE as CONF_BASE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

def get_data_schema(currencies: dict[str, str], existing_data: Mapping[str, str]) -> vol.Schema: ...
async def validate_input(hass: HomeAssistant, data: dict[str, str]) -> dict[str, str]: ...

class OpenExchangeRatesConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    currencies: dict[str, str]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_get_currencies(self) -> dict[str, str]: ...
