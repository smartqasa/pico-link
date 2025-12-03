from .const import ATTR_API_AQI as ATTR_API_AQI, ATTR_API_AQI_DESCRIPTION as ATTR_API_AQI_DESCRIPTION, ATTR_API_AQI_LEVEL as ATTR_API_AQI_LEVEL, ATTR_API_AQI_PARAM as ATTR_API_AQI_PARAM, ATTR_API_CATEGORY as ATTR_API_CATEGORY, ATTR_API_CAT_DESCRIPTION as ATTR_API_CAT_DESCRIPTION, ATTR_API_CAT_LEVEL as ATTR_API_CAT_LEVEL, ATTR_API_PM25 as ATTR_API_PM25, ATTR_API_POLLUTANT as ATTR_API_POLLUTANT, ATTR_API_REPORT_DATE as ATTR_API_REPORT_DATE, ATTR_API_REPORT_HOUR as ATTR_API_REPORT_HOUR, ATTR_API_REPORT_TZ as ATTR_API_REPORT_TZ, ATTR_API_STATE as ATTR_API_STATE, ATTR_API_STATION as ATTR_API_STATION, ATTR_API_STATION_LATITUDE as ATTR_API_STATION_LATITUDE, ATTR_API_STATION_LONGITUDE as ATTR_API_STATION_LONGITUDE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

class AirNowDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    latitude: Incomplete
    longitude: Incomplete
    distance: Incomplete
    airnow: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, api_key: str, latitude: float, longitude: float, distance: int, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
