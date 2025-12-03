from _typeshed import Incomplete
from aiosteamist import Steamist as Steamist, SteamistStatus
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class SteamistDataUpdateCoordinator(DataUpdateCoordinator[SteamistStatus]):
    client: Incomplete
    device_name: Incomplete
    def __init__(self, hass: HomeAssistant, client: Steamist, host: str, device_name: str | None) -> None: ...
    async def _async_update_data(self) -> SteamistStatus: ...
