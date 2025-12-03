from .bridge import SamsungTVBridge as SamsungTVBridge
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SCAN_INTERVAL: int

class SamsungTVDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    bridge: Incomplete
    is_on: bool | None
    async_extra_update: Callable[[], Coroutine[Any, Any, None]] | None
    def __init__(self, hass: HomeAssistant, bridge: SamsungTVBridge) -> None: ...
    async def _async_update_data(self) -> None: ...
