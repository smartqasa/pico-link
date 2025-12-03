from . import ImapConfigEntry as ImapConfigEntry
from .const import CONF_CHARSET as CONF_CHARSET, CONF_CUSTOM_EVENT_DATA_TEMPLATE as CONF_CUSTOM_EVENT_DATA_TEMPLATE, CONF_ENABLE_PUSH as CONF_ENABLE_PUSH, CONF_EVENT_MESSAGE_DATA as CONF_EVENT_MESSAGE_DATA, CONF_FOLDER as CONF_FOLDER, CONF_MAX_MESSAGE_SIZE as CONF_MAX_MESSAGE_SIZE, CONF_SEARCH as CONF_SEARCH, CONF_SERVER as CONF_SERVER, CONF_SSL_CIPHER_LIST as CONF_SSL_CIPHER_LIST, DEFAULT_MAX_MESSAGE_SIZE as DEFAULT_MAX_MESSAGE_SIZE, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, MAX_MESSAGE_SIZE_LIMIT as MAX_MESSAGE_SIZE_LIMIT, MESSAGE_DATA_OPTIONS as MESSAGE_DATA_OPTIONS
from .coordinator import connect_to_server as connect_to_server
from .errors import InvalidAuth as InvalidAuth, InvalidFolder as InvalidFolder
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector, TemplateSelectorConfig as TemplateSelectorConfig
from homeassistant.util.ssl import SSLCipherList as SSLCipherList
from typing import Any

BOOLEAN_SELECTOR: Incomplete
CIPHER_SELECTOR: Incomplete
TEMPLATE_SELECTOR: Incomplete
EVENT_MESSAGE_DATA_SELECTOR: Incomplete
CONFIG_SCHEMA: Incomplete
CONFIG_SCHEMA_ADVANCED: Incomplete
OPTIONS_SCHEMA: Incomplete
OPTIONS_SCHEMA_ADVANCED: Incomplete

async def validate_input(hass: HomeAssistant, user_input: dict[str, Any]) -> dict[str, str]: ...

class IMAPConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ImapConfigEntry) -> ImapOptionsFlow: ...

class ImapOptionsFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
