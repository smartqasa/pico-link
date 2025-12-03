from .const import DOMAIN as DOMAIN
from .model import CanaryData as CanaryData
from _typeshed import Incomplete
from canary.api import Api as Api
from canary.model import Location as Location, Reading as Reading
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class CanaryDataUpdateCoordinator(DataUpdateCoordinator[CanaryData]):
    canary: Incomplete
    def __init__(self, hass: HomeAssistant, *, api: Api) -> None: ...
    def _update_data(self) -> CanaryData: ...
    async def _async_update_data(self) -> CanaryData: ...
