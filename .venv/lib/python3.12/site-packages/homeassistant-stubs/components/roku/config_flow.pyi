from . import RokuConfigEntry as RokuConfigEntry
from .const import CONF_PLAY_MEDIA_APP_ID as CONF_PLAY_MEDIA_APP_ID, DEFAULT_PLAY_MEDIA_APP_ID as DEFAULT_PLAY_MEDIA_APP_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import ssdp as ssdp, zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

DATA_SCHEMA: Incomplete
ERROR_CANNOT_CONNECT: str
ERROR_UNKNOWN: str
_LOGGER: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]: ...

class RokuConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery_info: dict[str, Any]
    def __init__(self) -> None: ...
    @callback
    def _show_form(self, user_input: dict[str, Any] | None, errors: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: RokuConfigEntry) -> RokuOptionsFlowHandler: ...

class RokuOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
