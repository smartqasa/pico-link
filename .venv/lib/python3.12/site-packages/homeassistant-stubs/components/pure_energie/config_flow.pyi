from .const import DOMAIN as DOMAIN
from gridnet import Device as Device
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import TextSelector as TextSelector
from typing import Any

class PureEnergieFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_host: str
    discovered_device: Device
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_get_device(self, host: str) -> Device: ...
