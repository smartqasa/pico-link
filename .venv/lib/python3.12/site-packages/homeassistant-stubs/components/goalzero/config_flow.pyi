from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from homeassistant.components import dhcp as dhcp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete

class GoalZeroFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _discovered_ip: str
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_try_connect(self, host: str) -> tuple[str | None, str | None]: ...
