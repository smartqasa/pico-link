from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

@dataclass
class NamConfig:
    mac_address: str
    auth_enabled: bool

_LOGGER: Incomplete
AUTH_SCHEMA: Incomplete

async def async_get_config(hass: HomeAssistant, host: str) -> NamConfig: ...
async def async_check_credentials(hass: HomeAssistant, host: str, data: dict[str, Any]) -> None: ...

class NAMFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _config: NamConfig
    host: str
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_credentials(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
