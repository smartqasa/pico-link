from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from romy import RomyRobot as RomyRobot

class RomyVacuumCoordinator(DataUpdateCoordinator[None]):
    hass: Incomplete
    romy: Incomplete
    def __init__(self, hass: HomeAssistant, romy: RomyRobot) -> None: ...
    async def _async_update_data(self) -> None: ...
