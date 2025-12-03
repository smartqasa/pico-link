from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, TOKEN_EXPIRATION_DAYS as TOKEN_EXPIRATION_DAYS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

STEP_USER_DATA_SCHEMA: Incomplete

class SensoterraConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
