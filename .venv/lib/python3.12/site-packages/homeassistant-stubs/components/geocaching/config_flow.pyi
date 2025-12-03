import logging
from .const import DOMAIN as DOMAIN, ENVIRONMENT as ENVIRONMENT
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler as AbstractOAuth2FlowHandler
from typing import Any

class GeocachingFlowHandler(AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION: int
    @property
    def logger(self) -> logging.Logger: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
