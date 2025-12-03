from _typeshed import Incomplete
from asyncio import Semaphore
from collections.abc import Awaitable, Callable as Callable
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from logging import Logger

class DevoloDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT]):
    _semaphore: Incomplete
    def __init__(self, hass: HomeAssistant, logger: Logger, *, config_entry: ConfigEntry, name: str, semaphore: Semaphore, update_interval: timedelta, update_method: Callable[[], Awaitable[_DataT]]) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
