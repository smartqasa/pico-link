from .const import CONF_CLIP_NEGATIVE as CONF_CLIP_NEGATIVE, CONF_RETURN_AVERAGE as CONF_RETURN_AVERAGE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.schema_config_entry_flow import SchemaFlowFormStep as SchemaFlowFormStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
OPTIONS_FLOW: Incomplete

class AirQConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler: ...
