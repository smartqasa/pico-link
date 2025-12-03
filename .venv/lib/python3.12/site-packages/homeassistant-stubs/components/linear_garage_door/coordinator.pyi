from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from linear_garage_door import Linear
from typing import Any

_LOGGER: Incomplete

@dataclass
class LinearDevice:
    name: str
    subdevices: dict[str, dict[str, str]]

class LinearUpdateCoordinator(DataUpdateCoordinator[dict[str, LinearDevice]]):
    _devices: list[dict[str, Any]] | None
    config_entry: ConfigEntry
    site_id: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> dict[str, LinearDevice]: ...
    async def execute[_T](self, func: Callable[[Linear], Awaitable[_T]]) -> _T: ...
