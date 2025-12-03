from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiolookin import Device as Device
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

LOGGER: Incomplete

class LookinFlowHandler(ConfigFlow, domain=DOMAIN):
    _host: str | None
    _name: str | None
    def __init__(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _validate_device(self, host: str) -> Device: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
