from . import get_auth_user_agent as get_auth_user_agent
from .const import CONF_2FA as CONF_2FA, CONF_CONFIG_ENTRY_MINOR_VERSION as CONF_CONFIG_ENTRY_MINOR_VERSION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import dhcp as dhcp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete
STEP_RECONFIGURE_DATA_SCHEMA: Incomplete
UNKNOWN_RING_ACCOUNT: str

async def validate_input(hass: HomeAssistant, hardware_id: str, data: dict[str, str]) -> dict[str, Any]: ...

class RingConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION = CONF_CONFIG_ENTRY_MINOR_VERSION
    user_pass: dict[str, Any]
    hardware_id: str | None
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_2fa(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class Require2FA(HomeAssistantError): ...
class InvalidAuth(HomeAssistantError): ...
