from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_DEBOUNCER_COOLDOWN_SECONDS: Incomplete

class OpenUvCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: ConfigEntry
    update_method: Callable[[], Awaitable[dict[str, Any]]]
    _entry: Incomplete
    latitude: Incomplete
    longitude: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry, name: str, latitude: str, longitude: str, update_method: Callable[[], Awaitable[dict[str, Any]]]) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
