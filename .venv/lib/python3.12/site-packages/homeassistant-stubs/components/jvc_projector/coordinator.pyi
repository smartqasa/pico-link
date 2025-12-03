from .const import NAME as NAME
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from jvcprojector import JvcProjector as JvcProjector
from typing import Any

_LOGGER: Incomplete
INTERVAL_SLOW: Incomplete
INTERVAL_FAST: Incomplete

class JvcProjectorDataUpdateCoordinator(DataUpdateCoordinator[dict[str, str]]):
    device: Incomplete
    unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, device: JvcProjector) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> dict[str, Any]: ...
