from .api import MinecraftServer as MinecraftServer, MinecraftServerConnectionError as MinecraftServerConnectionError, MinecraftServerData as MinecraftServerData, MinecraftServerNotInitializedError as MinecraftServerNotInitializedError
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class MinecraftServerCoordinator(DataUpdateCoordinator[MinecraftServerData]):
    _api: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, api: MinecraftServer) -> None: ...
    async def _async_update_data(self) -> MinecraftServerData: ...
