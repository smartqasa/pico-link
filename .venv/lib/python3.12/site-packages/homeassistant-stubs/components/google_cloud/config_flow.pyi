from .const import CONF_KEY_FILE as CONF_KEY_FILE, CONF_SERVICE_ACCOUNT_INFO as CONF_SERVICE_ACCOUNT_INFO, CONF_STT_MODEL as CONF_STT_MODEL, DEFAULT_LANG as DEFAULT_LANG, DEFAULT_STT_MODEL as DEFAULT_STT_MODEL, DOMAIN as DOMAIN, SUPPORTED_STT_MODELS as SUPPORTED_STT_MODELS, TITLE as TITLE
from .helpers import async_tts_voices as async_tts_voices, tts_options_schema as tts_options_schema, tts_platform_schema as tts_platform_schema, validate_service_account_info as validate_service_account_info
from _typeshed import Incomplete
from homeassistant.components.file_upload import process_uploaded_file as process_uploaded_file
from homeassistant.components.tts import CONF_LANG as CONF_LANG
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import FileSelector as FileSelector, FileSelectorConfig as FileSelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

_LOGGER: Incomplete
UPLOADED_KEY_FILE: str
STEP_USER_DATA_SCHEMA: Incomplete

class GoogleCloudConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _name: str | None
    entry: ConfigEntry | None
    abort_reason: str | None
    def _parse_uploaded_file(self, uploaded_file_id: str) -> dict[str, Any]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> GoogleCloudOptionsFlowHandler: ...

class GoogleCloudOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
