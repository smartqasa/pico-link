from . import CONF_STUN_SERVER as CONF_STUN_SERVER, DATA_SERVER_URL as DATA_SERVER_URL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.service_info.hassio import HassioServiceInfo as HassioServiceInfo
from typing import Any

_LOGGER: Incomplete
DATA_SCHEMA: Incomplete

class RTSPToWebRTCConfigFlow(ConfigFlow, domain=DOMAIN):
    _hassio_discovery: dict[str, Any]
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _test_connection(self, url: str) -> str | None: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> ConfigFlowResult: ...
    async def async_step_hassio_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
