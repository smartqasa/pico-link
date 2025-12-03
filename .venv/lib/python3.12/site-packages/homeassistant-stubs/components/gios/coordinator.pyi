from .const import API_TIMEOUT as API_TIMEOUT, DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from gios.model import GiosSensors
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class GiosDataUpdateCoordinator(DataUpdateCoordinator[GiosSensors]):
    gios: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, station_id: int) -> None: ...
    async def _async_update_data(self) -> GiosSensors: ...
