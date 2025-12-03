from .const import API_STATION_INDOOR as API_STATION_INDOOR, API_STATION_INFO as API_STATION_INFO, API_STATION_MAC_ADDRESS as API_STATION_MAC_ADDRESS, DOMAIN as DOMAIN
from .helper import get_station_name as get_station_name
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_MAC as CONF_MAC, CONF_RADIUS as CONF_RADIUS, UnitOfLength as UnitOfLength
from homeassistant.helpers.selector import LocationSelector as LocationSelector, LocationSelectorConfig as LocationSelectorConfig, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter
from typing import Any

CONF_USER: str
CONF_STATION: str
CONF_RADIUS_DEFAULT: float

class AmbientNetworkConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _longitude: float
    _latitude: float
    _radius: float
    _stations: dict[str, dict[str, Any]]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_station(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
