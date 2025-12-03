import logging
from .const import CONF_LANGUAGE_CODE as CONF_LANGUAGE_CODE, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, SUPPORTED_LANGUAGE_CODES as SUPPORTED_LANGUAGE_CODES
from .helpers import default_language_code as default_language_code
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.core import callback as callback
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

_LOGGER: Incomplete

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
