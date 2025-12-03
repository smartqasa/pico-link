from .const import CONF_STATION_NUMBER as CONF_STATION_NUMBER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiowaqi import WAQIAirQuality as WAQIAirQuality, WAQIClient
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_METHOD as CONF_METHOD
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import LocationSelector as LocationSelector, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any

_LOGGER: Incomplete
CONF_MAP: str

async def get_by_station_number(client: WAQIClient, station_number: int) -> tuple[WAQIAirQuality | None, dict[str, str]]: ...

class WAQIConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_map(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_station_number(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_create_entry(self, measuring_station: WAQIAirQuality) -> ConfigFlowResult: ...
