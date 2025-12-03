import voluptuous as vol
from .const import DEFAULT_PORT as DEFAULT_PORT, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, FLOW_SMILE as FLOW_SMILE, FLOW_STRETCH as FLOW_STRETCH, SMILE as SMILE, STRETCH as STRETCH, STRETCH_USERNAME as STRETCH_USERNAME, ZEROCONF_MAP as ZEROCONF_MAP
from _typeshed import Incomplete
from homeassistant.components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_USER as SOURCE_USER
from homeassistant.const import ATTR_CONFIGURATION_URL as ATTR_CONFIGURATION_URL, CONF_BASE as CONF_BASE, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from plugwise import Smile
from typing import Any, Self

_LOGGER: Incomplete
SMILE_RECONF_SCHEMA: Incomplete

def smile_user_schema(discovery_info: ZeroconfServiceInfo | None) -> vol.Schema: ...
async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> Smile: ...
async def verify_connection(hass: HomeAssistant, user_input: dict[str, Any]) -> tuple[Smile | None, dict[str, str]]: ...

class PlugwiseConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovery_info: ZeroconfServiceInfo | None
    product: str
    _username: str
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    def is_matching(self, other_flow: Self) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
