import voluptuous as vol
from .base import FritzBoxPhonebook as FritzBoxPhonebook
from .const import CONF_PHONEBOOK as CONF_PHONEBOOK, CONF_PREFIXES as CONF_PREFIXES, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PHONEBOOK as DEFAULT_PHONEBOOK, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, FRITZ_ATTR_NAME as FRITZ_ATTR_NAME, FRITZ_ATTR_SERIAL_NUMBER as FRITZ_ATTR_SERIAL_NUMBER, SERIAL_NUMBER as SERIAL_NUMBER
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from typing import Any

DATA_SCHEMA_USER: Incomplete

class ConnectResult(StrEnum):
    INVALID_AUTH = 'invalid_auth'
    INSUFFICIENT_PERMISSIONS = 'insufficient_permissions'
    MALFORMED_PREFIXES = 'malformed_prefixes'
    NO_DEVIES_FOUND = 'no_devices_found'
    SUCCESS = 'success'

class FritzBoxCallMonitorConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _entry: ConfigEntry
    _host: str
    _port: int
    _username: str
    _password: str
    _phonebook_name: str
    _phonebook_id: int
    _phonebook_ids: list[int]
    _fritzbox_phonebook: FritzBoxPhonebook
    _serial_number: str
    _phonebook_names: list[str] | None
    def __init__(self) -> None: ...
    def _get_config_entry(self) -> ConfigFlowResult: ...
    def _try_connect(self) -> ConnectResult: ...
    async def _get_name_of_phonebook(self, phonebook_id: int) -> str: ...
    async def _get_list_of_phonebook_names(self) -> list[str]: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> FritzBoxCallMonitorOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_phonebook(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    def _show_setup_form_reauth_confirm(self, user_input: dict[str, Any], errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class FritzBoxCallMonitorOptionsFlowHandler(OptionsFlow):
    @classmethod
    def _are_prefixes_valid(cls, prefixes: str | None) -> bool: ...
    @classmethod
    def _get_list_of_prefixes(cls, prefixes: str | None) -> list[str] | None: ...
    def _get_option_schema_prefixes(self) -> vol.Schema: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
