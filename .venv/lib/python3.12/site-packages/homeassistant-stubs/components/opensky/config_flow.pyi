from .const import CONF_ALTITUDE as CONF_ALTITUDE, CONF_CONTRIBUTING_USER as CONF_CONTRIBUTING_USER, DEFAULT_ALTITUDE as DEFAULT_ALTITUDE, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_RADIUS as CONF_RADIUS, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class OpenSkyConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OpenSkyOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class OpenSkyOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
