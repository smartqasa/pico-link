from .const import ATTR_API_ADVICE as ATTR_API_ADVICE, ATTR_API_CAQI as ATTR_API_CAQI, ATTR_API_CAQI_DESCRIPTION as ATTR_API_CAQI_DESCRIPTION, ATTR_API_CAQI_LEVEL as ATTR_API_CAQI_LEVEL, DOMAIN as DOMAIN, MAX_UPDATE_INTERVAL as MAX_UPDATE_INTERVAL, MIN_UPDATE_INTERVAL as MIN_UPDATE_INTERVAL, NO_AIRLY_SENSORS as NO_AIRLY_SENSORS
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

def set_update_interval(instances_count: int, requests_remaining: int) -> timedelta: ...

class AirlyDataUpdateCoordinator(DataUpdateCoordinator[dict[str, str | float | int]]):
    latitude: Incomplete
    longitude: Incomplete
    airly: Incomplete
    use_nearest: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, api_key: str, latitude: float, longitude: float, update_interval: timedelta, use_nearest: bool) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> dict[str, str | float | int]: ...
