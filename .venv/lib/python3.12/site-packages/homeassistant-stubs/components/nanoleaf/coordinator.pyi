from _typeshed import Incomplete
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class NanoleafCoordinator(DataUpdateCoordinator[None]):
    nanoleaf: Incomplete
    def __init__(self, hass: HomeAssistant, nanoleaf: Nanoleaf) -> None: ...
    async def _async_update_data(self) -> None: ...
