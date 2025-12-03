from .const import STATE_SCAN_INTERVAL as STATE_SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from vallox_websocket_api import MetricData, Vallox as Vallox

_LOGGER: Incomplete

class ValloxDataUpdateCoordinator(DataUpdateCoordinator[MetricData]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, client: Vallox) -> None: ...
    async def _async_update_data(self) -> MetricData: ...
