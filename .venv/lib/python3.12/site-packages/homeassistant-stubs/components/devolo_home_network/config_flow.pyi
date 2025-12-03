from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import DOMAIN as DOMAIN, PRODUCT as PRODUCT, SERIAL_NUMBER as SERIAL_NUMBER, TITLE as TITLE
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class DevoloHomeNetworkConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    host: str
    _reauth_entry: DevoloHomeNetworkConfigEntry
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
