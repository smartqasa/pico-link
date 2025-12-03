from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_FRIENDLY_NAME as CONF_FRIENDLY_NAME
from homeassistant.core import callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

DATA_SCHEMA: Incomplete

class RecollectWasteConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> RecollectWasteOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class RecollectWasteOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
