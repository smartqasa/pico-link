import logging
from .const import DOMAIN as DOMAIN, SPOTIFY_SCOPES as SPOTIFY_SCOPES
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_NAME as CONF_NAME, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

class SpotifyFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION: int
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
