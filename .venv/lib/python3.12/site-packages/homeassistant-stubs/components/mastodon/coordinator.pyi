from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from mastodon import Mastodon as Mastodon
from typing import Any

class MastodonCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: Mastodon) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
