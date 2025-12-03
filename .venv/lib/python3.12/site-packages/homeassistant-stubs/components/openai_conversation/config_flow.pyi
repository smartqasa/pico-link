from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_PROMPT as CONF_PROMPT, CONF_RECOMMENDED as CONF_RECOMMENDED, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, DOMAIN as DOMAIN, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LLM_HASS_API as CONF_LLM_HASS_API
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import llm as llm
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, TemplateSelector as TemplateSelector
from homeassistant.helpers.typing import VolDictType as VolDictType
from types import MappingProxyType
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
RECOMMENDED_OPTIONS: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> None: ...

class OpenAIConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class OpenAIOptionsFlow(OptionsFlow):
    last_rendered_recommended: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

def openai_config_option_schema(hass: HomeAssistant, options: dict[str, Any] | MappingProxyType[str, Any]) -> VolDictType: ...
