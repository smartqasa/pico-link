import voluptuous as vol
from .const import DOMAIN as DOMAIN, INVALID_AUTH_ERRORS as INVALID_AUTH_ERRORS, OPTION_DIAGNOSTICS_INCLUDE_FIXTURES as OPTION_DIAGNOSTICS_INCLUDE_FIXTURES, OPTION_DIAGNOSTICS_INCLUDE_FIXTURES_DEFAULT_VALUE as OPTION_DIAGNOSTICS_INCLUDE_FIXTURES_DEFAULT_VALUE, OPTION_DISABLE_KEEP_ALIVE as OPTION_DISABLE_KEEP_ALIVE, OPTION_DISABLE_KEEP_ALIVE_DEFAULT_VALUE as OPTION_DISABLE_KEEP_ALIVE_DEFAULT_VALUE
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.typing import VolDictType as VolDictType
from pyenphase import Envoy
from typing import Any

_LOGGER: Incomplete
ENVOY: str
CONF_SERIAL: str
INSTALLER_AUTH_USERNAME: str

async def validate_input(hass: HomeAssistant, host: str, username: str, password: str) -> Envoy: ...

class EnphaseConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _reauth_entry: ConfigEntry
    ip_address: str | None
    username: Incomplete
    protovers: str | None
    def __init__(self) -> None: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: EnphaseConfigEntry) -> EnvoyOptionsFlowHandler: ...
    @callback
    def _async_generate_schema(self) -> vol.Schema: ...
    @callback
    def _async_current_hosts(self) -> set[str]: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    def _async_envoy_name(self) -> str: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class EnvoyOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
