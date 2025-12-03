from .const import DEFAULT_INTERVAL as DEFAULT_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class FastdotcomDataUpdateCoordinator(DataUpdateCoordinator[float]):
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> float: ...
