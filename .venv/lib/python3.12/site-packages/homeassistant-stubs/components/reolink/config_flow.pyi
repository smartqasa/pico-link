from .const import CONF_USE_HTTPS as CONF_USE_HTTPS, DOMAIN as DOMAIN
from .exceptions import PasswordIncompatible as PasswordIncompatible, ReolinkException as ReolinkException, ReolinkWebhookException as ReolinkWebhookException, UserNotAdmin as UserNotAdmin
from .host import ReolinkHost as ReolinkHost
from .util import ReolinkConfigEntry as ReolinkConfigEntry, is_connected as is_connected
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import dhcp as dhcp
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers import selector as selector
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

_LOGGER: Incomplete
DEFAULT_PROTOCOL: str
DEFAULT_OPTIONS: Incomplete

class ReolinkOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class ReolinkFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _host: str | None
    _username: str
    _password: str | None
    def __init__(self) -> None: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ReolinkConfigEntry) -> ReolinkOptionsFlowHandler: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_dhcp(self, discovery_info: dhcp.DhcpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
