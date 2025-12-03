from .const import DOMAIN as DOMAIN, RUSSOUND_RIO_EXCEPTIONS as RUSSOUND_RIO_EXCEPTIONS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from typing import Any

DATA_SCHEMA: Incomplete
_LOGGER: Incomplete

class FlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
