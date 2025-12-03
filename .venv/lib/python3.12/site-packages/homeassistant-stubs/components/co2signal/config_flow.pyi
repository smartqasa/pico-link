import voluptuous as vol
from .const import DOMAIN as DOMAIN
from .helpers import fetch_latest_carbon_intensity as fetch_latest_carbon_intensity
from .util import get_extra_name as get_extra_name
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_COUNTRY_CODE as CONF_COUNTRY_CODE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

TYPE_USE_HOME: str
TYPE_SPECIFY_COORDINATES: str
TYPE_SPECIFY_COUNTRY: str

class ElectricityMapsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _data: dict | None
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_coordinates(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_country(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _validate_and_create(self, step_id: str, data_schema: vol.Schema, data: Mapping[str, Any] | None) -> ConfigFlowResult: ...
