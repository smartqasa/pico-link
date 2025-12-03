from . import JellyfinConfigEntry as JellyfinConfigEntry
from .client_wrapper import CannotConnect as CannotConnect, InvalidAuth as InvalidAuth, create_client as create_client, validate_input as validate_input
from .const import CONF_CLIENT_DEVICE_ID as CONF_CLIENT_DEVICE_ID, DOMAIN as DOMAIN, SUPPORTED_AUDIO_CODECS as SUPPORTED_AUDIO_CODECS
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.util.uuid import random_uuid_hex as random_uuid_hex
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
REAUTH_DATA_SCHEMA: Incomplete
OPTIONAL_DATA_SCHEMA: Incomplete

def _generate_client_device_id() -> str: ...

class JellyfinConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    client_device_id: str | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: JellyfinConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
