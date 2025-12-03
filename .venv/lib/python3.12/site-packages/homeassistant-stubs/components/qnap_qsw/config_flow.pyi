from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import dhcp as dhcp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete

class QNapQSWConfigFlow(ConfigFlow, domain=DOMAIN):
    _discovered_mac: str | None
    _discovered_url: str | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovered_connection(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
