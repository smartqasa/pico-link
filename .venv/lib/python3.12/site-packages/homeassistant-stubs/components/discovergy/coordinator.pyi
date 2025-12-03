from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pydiscovergy import Discovergy as Discovergy
from pydiscovergy.models import Meter as Meter, Reading

_LOGGER: Incomplete

class DiscovergyUpdateCoordinator(DataUpdateCoordinator[Reading]):
    meter: Incomplete
    discovergy_client: Incomplete
    def __init__(self, hass: HomeAssistant, meter: Meter, discovergy_client: Discovergy) -> None: ...
    async def _async_update_data(self) -> Reading: ...
