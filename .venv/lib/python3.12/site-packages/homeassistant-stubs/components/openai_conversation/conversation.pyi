from . import OpenAIConfigEntry as OpenAIConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_PROMPT as CONF_PROMPT, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, DOMAIN as DOMAIN, LOGGER as LOGGER, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import assist_pipeline as assist_pipeline, conversation as conversation
from homeassistant.components.conversation import trace as trace
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LLM_HASS_API as CONF_LLM_HASS_API, MATCH_ALL as MATCH_ALL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, TemplateError as TemplateError
from homeassistant.helpers import intent as intent, llm as llm, template as template
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import ulid as ulid
from openai.types.chat import ChatCompletionMessage as ChatCompletionMessage, ChatCompletionMessageParam as ChatCompletionMessageParam, ChatCompletionToolParam
from typing import Any, Literal

MAX_TOOL_ITERATIONS: int

async def async_setup_entry(hass: HomeAssistant, config_entry: OpenAIConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _format_tool(tool: llm.Tool, custom_serializer: Callable[[Any], Any] | None) -> ChatCompletionToolParam: ...

class OpenAIConversationEntity(conversation.ConversationEntity, conversation.AbstractConversationAgent):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    entry: Incomplete
    history: dict[str, list[ChatCompletionMessageParam]]
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, entry: OpenAIConfigEntry) -> None: ...
    @property
    def supported_languages(self) -> list[str] | Literal['*']: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_process(self, user_input: conversation.ConversationInput) -> conversation.ConversationResult: ...
    async def _async_entry_update_listener(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
