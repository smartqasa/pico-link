import voluptuous as vol
from .const import CONF_HTTPS as CONF_HTTPS, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import dhcp as dhcp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete
TIMEOUT: int

def _base_schema(discovery_info: dict[str, Any] | None = None) -> vol.Schema: ...

class SqueezeboxConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data_schema: Incomplete
    discovery_info: dict[str, Any] | None
    def __init__(self) -> None: ...
    async def _discover(self, uuid: str | None = None) -> None: ...
    async def _validate_input(self, data: dict[str, Any]) -> str | None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_edit(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
