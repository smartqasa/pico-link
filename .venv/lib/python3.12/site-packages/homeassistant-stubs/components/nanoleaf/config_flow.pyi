from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aionanoleaf import Nanoleaf
from collections.abc import Mapping
from homeassistant.components import ssdp as ssdp, zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.json import save_json as save_json
from homeassistant.util.json import JsonObjectType as JsonObjectType, JsonValueType as JsonValueType, load_json_object as load_json_object
from typing import Any, Final

_LOGGER: Incomplete
CONFIG_FILE: Final[str]
USER_SCHEMA: Final[Incomplete]

class NanoleafConfigFlow(ConfigFlow, domain=DOMAIN):
    nanoleaf: Nanoleaf
    discovery_conf: JsonObjectType
    device_id: str
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_homekit(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def _async_homekit_zeroconf_discovery_handler(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def _async_discovery_handler(self, host: str, name: str, device_id: str) -> ConfigFlowResult: ...
    async def async_step_link(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_setup_finish(self, discovery_integration_import: bool = False) -> ConfigFlowResult: ...
