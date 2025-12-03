from .const import DOMAIN as DOMAIN, RUN_TIMEOUT as RUN_TIMEOUT
from .models import BAFDiscovery as BAFDiscovery
from _typeshed import Incomplete
from aiobafi6 import Device
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS
from typing import Any

_LOGGER: Incomplete

async def async_try_connect(ip_address: str) -> Device: ...

class BAFFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery: BAFDiscovery | None
    def __init__(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class CannotConnect(Exception): ...
