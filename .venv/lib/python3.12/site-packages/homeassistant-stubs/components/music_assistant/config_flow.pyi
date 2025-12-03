import voluptuous as vol
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from music_assistant_models.api import ServerInfoMessage
from typing import Any

DEFAULT_URL: str
DEFAULT_TITLE: str

def get_manual_schema(user_input: dict[str, Any]) -> vol.Schema: ...
async def get_server_info(hass: HomeAssistant, url: str) -> ServerInfoMessage: ...

class MusicAssistantConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    server_info: ServerInfoMessage | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
