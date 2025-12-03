from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyschlage import Lock as Lock, Schlage as Schlage
from pyschlage.log import LockLog as LockLog

@dataclass
class LockData:
    lock: Lock
    logs: list[LockLog]

@dataclass
class SchlageData:
    locks: dict[str, LockData]

class SchlageDataUpdateCoordinator(DataUpdateCoordinator[SchlageData]):
    config_entry: ConfigEntry
    data: Incomplete
    api: Incomplete
    new_locks_callbacks: list[Callable[[dict[str, LockData]], None]]
    def __init__(self, hass: HomeAssistant, username: str, api: Schlage) -> None: ...
    async def _async_update_data(self) -> SchlageData: ...
    def _get_lock_data(self, lock: Lock) -> LockData: ...
    @callback
    def _add_remove_locks(self) -> None: ...
