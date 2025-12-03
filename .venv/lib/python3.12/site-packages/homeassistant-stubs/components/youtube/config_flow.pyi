import logging
from .const import CHANNEL_CREATION_HELP_URL as CHANNEL_CREATION_HELP_URL, CONF_CHANNELS as CONF_CHANNELS, DEFAULT_ACCESS as DEFAULT_ACCESS, DOMAIN as DOMAIN, LOGGER as LOGGER
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import callback as callback
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any
from youtubeaio.youtube import YouTube

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    _data: dict[str, Any]
    _title: str
    DOMAIN = DOMAIN
    _youtube: YouTube | None
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> YouTubeOptionsFlowHandler: ...
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def get_resource(self, token: str) -> YouTube: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_channels(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class YouTubeOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
