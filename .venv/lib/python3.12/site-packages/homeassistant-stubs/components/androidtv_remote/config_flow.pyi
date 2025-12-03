from .const import CONF_APPS as CONF_APPS, CONF_APP_ICON as CONF_APP_ICON, CONF_APP_NAME as CONF_APP_NAME, CONF_ENABLE_IME as CONF_ENABLE_IME, DOMAIN as DOMAIN
from .helpers import create_api as create_api, get_enable_ime as get_enable_ime
from _typeshed import Incomplete
from androidtvremote2 import AndroidTVRemote as AndroidTVRemote
from collections.abc import Mapping
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

_LOGGER: Incomplete
APPS_NEW_ID: str
CONF_APP_DELETE: str
CONF_APP_ID: str
STEP_USER_DATA_SCHEMA: Incomplete
STEP_PAIR_DATA_SCHEMA: Incomplete

class AndroidTVRemoteConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    api: AndroidTVRemote
    host: str
    name: str
    mac: str
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_start_pair(self) -> ConfigFlowResult: ...
    async def async_step_pair(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> AndroidTVRemoteOptionsFlowHandler: ...

class AndroidTVRemoteOptionsFlowHandler(OptionsFlow):
    _apps: dict[str, Any]
    _conf_app_id: str | None
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    @callback
    def _save_config(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_apps(self, user_input: dict[str, Any] | None = None, app_id: str | None = None) -> ConfigFlowResult: ...
    @callback
    def _async_apps_form(self, app_id: str) -> ConfigFlowResult: ...
