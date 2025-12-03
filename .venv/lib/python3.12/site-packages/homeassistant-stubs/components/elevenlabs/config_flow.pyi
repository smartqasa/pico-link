import voluptuous as vol
from . import ElevenLabsConfigEntry as ElevenLabsConfigEntry
from .const import CONF_CONFIGURE_VOICE as CONF_CONFIGURE_VOICE, CONF_MODEL as CONF_MODEL, CONF_OPTIMIZE_LATENCY as CONF_OPTIMIZE_LATENCY, CONF_SIMILARITY as CONF_SIMILARITY, CONF_STABILITY as CONF_STABILITY, CONF_STYLE as CONF_STYLE, CONF_USE_SPEAKER_BOOST as CONF_USE_SPEAKER_BOOST, CONF_VOICE as CONF_VOICE, DEFAULT_MODEL as DEFAULT_MODEL, DEFAULT_OPTIMIZE_LATENCY as DEFAULT_OPTIMIZE_LATENCY, DEFAULT_SIMILARITY as DEFAULT_SIMILARITY, DEFAULT_STABILITY as DEFAULT_STABILITY, DEFAULT_STYLE as DEFAULT_STYLE, DEFAULT_USE_SPEAKER_BOOST as DEFAULT_USE_SPEAKER_BOOST, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any

USER_STEP_SCHEMA: Incomplete
_LOGGER: Incomplete

async def get_voices_models(hass: HomeAssistant, api_key: str) -> tuple[dict[str, str], dict[str, str]]: ...

class ElevenLabsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ElevenLabsConfigEntry) -> OptionsFlow: ...

class ElevenLabsOptionsFlow(OptionsFlow):
    api_key: str
    voices: dict[str, str]
    models: dict[str, str]
    model: str | None
    voice: str | None
    def __init__(self, config_entry: ElevenLabsConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def elevenlabs_config_option_schema(self) -> vol.Schema: ...
    async def async_step_voice_settings(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def elevenlabs_config_options_voice_schema(self) -> vol.Schema: ...
