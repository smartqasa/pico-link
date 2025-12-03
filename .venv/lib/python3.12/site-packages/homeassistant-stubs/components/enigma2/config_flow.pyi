import voluptuous as vol
from .const import CONF_DEEP_STANDBY as CONF_DEEP_STANDBY, CONF_SOURCE_BOUQUET as CONF_SOURCE_BOUQUET, CONF_USE_CHANNEL_ICON as CONF_USE_CHANNEL_ICON, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from typing import Any

CONFIG_SCHEMA: Incomplete

async def get_options_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...

OPTIONS_FLOW: Incomplete

class Enigma2ConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    DATA_KEYS: Incomplete
    OPTIONS_KEYS: Incomplete
    async def validate_user_input(self, user_input: dict[str, Any]) -> dict[str, str] | None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler: ...
