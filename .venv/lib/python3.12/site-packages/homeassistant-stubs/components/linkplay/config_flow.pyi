from .const import DOMAIN as DOMAIN
from .utils import async_get_client_session as async_get_client_session
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL
from linkplay.bridge import LinkPlayBridge as LinkPlayBridge
from typing import Any

_LOGGER: Incomplete

class LinkPlayConfigFlow(ConfigFlow, domain=DOMAIN):
    data: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
