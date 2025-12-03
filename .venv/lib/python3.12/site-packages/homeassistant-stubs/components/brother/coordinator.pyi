from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from brother import Brother as Brother, BrotherSensors
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class BrotherDataUpdateCoordinator(DataUpdateCoordinator[BrotherSensors]):
    brother: Incomplete
    def __init__(self, hass: HomeAssistant, brother: Brother) -> None: ...
    async def _async_update_data(self) -> BrotherSensors: ...
