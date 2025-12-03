from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from london_tube_status import TubeData as TubeData

_LOGGER: Incomplete

class LondonTubeCoordinator(DataUpdateCoordinator[dict[str, dict[str, str]]]):
    _data: Incomplete
    def __init__(self, hass: HomeAssistant, data: TubeData) -> None: ...
    async def _async_update_data(self) -> dict[str, dict[str, str]]: ...
