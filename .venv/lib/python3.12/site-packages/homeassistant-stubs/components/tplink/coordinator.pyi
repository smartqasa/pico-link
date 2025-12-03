from _typeshed import Incomplete
from datetime import timedelta
from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from kasa import Device as Device

_LOGGER: Incomplete
REQUEST_REFRESH_DELAY: float

class TPLinkDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: config_entries.ConfigEntry
    device: Incomplete
    def __init__(self, hass: HomeAssistant, device: Device, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> None: ...
