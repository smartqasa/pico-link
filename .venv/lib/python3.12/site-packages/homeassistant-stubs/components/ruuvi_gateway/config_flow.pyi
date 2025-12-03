from . import DOMAIN as DOMAIN
from .schemata import CONFIG_SCHEMA as CONFIG_SCHEMA, get_config_schema_with_default_host as get_config_schema_with_default_host
from _typeshed import Incomplete
from homeassistant.components import dhcp as dhcp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from typing import Any

_LOGGER: Incomplete

class RuuviConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    config_schema: Incomplete
    def __init__(self) -> None: ...
    async def _async_validate(self, user_input: dict[str, Any]) -> tuple[ConfigFlowResult | None, dict[str, str]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
