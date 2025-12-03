from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from aioskybell import SkybellDevice as SkybellDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class SkybellDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    device: Incomplete
    def __init__(self, hass: HomeAssistant, device: SkybellDevice) -> None: ...
    async def _async_update_data(self) -> None: ...
