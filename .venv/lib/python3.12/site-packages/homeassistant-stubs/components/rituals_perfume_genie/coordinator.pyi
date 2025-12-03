from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pyrituals import Diffuser as Diffuser

_LOGGER: Incomplete

class RitualsDataUpdateCoordinator(DataUpdateCoordinator[None]):
    diffuser: Incomplete
    def __init__(self, hass: HomeAssistant, diffuser: Diffuser, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> None: ...
