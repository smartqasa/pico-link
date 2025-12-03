import voluptuous as vol
from .const import CONF_ALLOW_INACTIVE_ZONES_TO_RUN as CONF_ALLOW_INACTIVE_ZONES_TO_RUN, CONF_DEFAULT_ZONE_RUN_TIME as CONF_DEFAULT_ZONE_RUN_TIME, CONF_USE_APP_RUN_TIMES as CONF_USE_APP_RUN_TIMES, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_ZONE_RUN as DEFAULT_ZONE_RUN, DOMAIN as DOMAIN
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from regenmaschine import Client
from regenmaschine.controller import Controller as Controller
from typing import Any

@callback
def get_client_controller(client: Client) -> Controller: ...
async def async_get_controller(hass: HomeAssistant, ip_address: str, password: str, port: int, ssl: bool) -> Controller | None: ...

class RainMachineFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_ip_address: str | None
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> RainMachineOptionsFlowHandler: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_homekit_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    @callback
    def _async_generate_schema(self) -> vol.Schema: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class RainMachineOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
