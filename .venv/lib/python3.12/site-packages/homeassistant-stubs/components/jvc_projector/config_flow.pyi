from .const import DOMAIN as DOMAIN, NAME as NAME
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.util.network import is_host_valid as is_host_valid
from typing import Any

class JvcProjectorConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...

class InvalidHost(Exception): ...

async def get_mac_address(host: str, port: int, password: str | None) -> str: ...
