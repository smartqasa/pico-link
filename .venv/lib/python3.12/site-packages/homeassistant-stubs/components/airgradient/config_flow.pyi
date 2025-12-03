from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from airgradient import AirGradientClient
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

MIN_VERSION: Incomplete

class AirGradientConfigFlow(ConfigFlow, domain=DOMAIN):
    data: dict[str, Any]
    client: AirGradientClient | None
    def __init__(self) -> None: ...
    async def set_configuration_source(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
