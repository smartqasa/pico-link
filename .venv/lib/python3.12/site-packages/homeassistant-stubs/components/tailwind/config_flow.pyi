from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from collections.abc import Mapping
from homeassistant.components import zeroconf as zeroconf
from homeassistant.components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

LOCAL_CONTROL_KEY_URL: str

class TailwindFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> ConfigFlowResult: ...
    async def _async_step_create_entry(self, *, host: str, token: str) -> ConfigFlowResult: ...
