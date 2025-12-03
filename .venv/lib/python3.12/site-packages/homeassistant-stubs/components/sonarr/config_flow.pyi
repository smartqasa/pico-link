import voluptuous as vol
from .const import CONF_UPCOMING_DAYS as CONF_UPCOMING_DAYS, CONF_WANTED_MAX_ITEMS as CONF_WANTED_MAX_ITEMS, DEFAULT_UPCOMING_DAYS as DEFAULT_UPCOMING_DAYS, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DEFAULT_WANTED_MAX_ITEMS as DEFAULT_WANTED_MAX_ITEMS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

async def _validate_input(hass: HomeAssistant, data: dict[str, Any]) -> None: ...

class SonarrConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SonarrOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _get_user_data_schema(self) -> dict[vol.Marker, type]: ...

class SonarrOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, int] | None = None) -> ConfigFlowResult: ...
