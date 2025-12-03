from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from knocki import Event as Event, KnockiClient as KnockiClient, Trigger

class KnockiCoordinator(DataUpdateCoordinator[dict[int, Trigger]]):
    client: Incomplete
    _known_triggers: set[tuple[str, int]]
    def __init__(self, hass: HomeAssistant, client: KnockiClient) -> None: ...
    async def _async_update_data(self) -> dict[int, Trigger]: ...
    def add_trigger(self, event: Event) -> None: ...
    @callback
    def _async_delete_device(self, trigger: tuple[str, int]) -> None: ...
