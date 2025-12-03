import voluptuous as vol
from .const import CONF_BALANCING_AUTHORITY as CONF_BALANCING_AUTHORITY, CONF_BALANCING_AUTHORITY_ABBREV as CONF_BALANCING_AUTHORITY_ABBREV, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiowatttime import Client
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

CONF_LOCATION_TYPE: str
LOCATION_TYPE_COORDINATES: str
LOCATION_TYPE_HOME: str
STEP_COORDINATES_DATA_SCHEMA: Incomplete
STEP_LOCATION_DATA_SCHEMA: Incomplete
STEP_REAUTH_CONFIRM_DATA_SCHEMA: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

@callback
def get_unique_id(data: dict[str, Any]) -> str: ...

class WattTimeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _client: Client | None
    _data: dict[str, Any]
    def __init__(self) -> None: ...
    async def _async_validate_credentials(self, username: str, password: str, error_step_id: str, error_schema: vol.Schema) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> WattTimeOptionsFlowHandler: ...
    async def async_step_coordinates(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_location(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class WattTimeOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
