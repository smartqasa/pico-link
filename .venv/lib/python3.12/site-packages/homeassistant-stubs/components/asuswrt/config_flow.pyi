import voluptuous as vol
from .bridge import AsusWrtBridge as AsusWrtBridge
from .const import CONF_DNSMASQ as CONF_DNSMASQ, CONF_INTERFACE as CONF_INTERFACE, CONF_REQUIRE_IP as CONF_REQUIRE_IP, CONF_SSH_KEY as CONF_SSH_KEY, CONF_TRACK_UNKNOWN as CONF_TRACK_UNKNOWN, DEFAULT_DNSMASQ as DEFAULT_DNSMASQ, DEFAULT_INTERFACE as DEFAULT_INTERFACE, DEFAULT_TRACK_UNKNOWN as DEFAULT_TRACK_UNKNOWN, DOMAIN as DOMAIN, MODE_AP as MODE_AP, MODE_ROUTER as MODE_ROUTER, PROTOCOL_HTTP as PROTOCOL_HTTP, PROTOCOL_HTTPS as PROTOCOL_HTTPS, PROTOCOL_SSH as PROTOCOL_SSH, PROTOCOL_TELNET as PROTOCOL_TELNET
from _typeshed import Incomplete
from homeassistant.components.device_tracker import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_BASE as CONF_BASE, CONF_HOST as CONF_HOST, CONF_MODE as CONF_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

ALLOWED_PROTOCOL: Incomplete
PASS_KEY: str
PASS_KEY_MSG: str
RESULT_CONN_ERROR: str
RESULT_SUCCESS: str
RESULT_UNKNOWN: str
_LOGGER: Incomplete
LEGACY_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete

async def get_options_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...

OPTIONS_FLOW: Incomplete

def _is_file(value: str) -> bool: ...
def _get_ip(host: str) -> str | None: ...

class AsusWrtFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _config_data: dict[str, Any]
    def __init__(self) -> None: ...
    @callback
    def _show_setup_form(self, error: str | None = None) -> ConfigFlowResult: ...
    async def _async_check_connection(self, user_input: dict[str, Any]) -> tuple[str, str | None]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_legacy(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_save_entry(self) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler: ...
