from .const import FLUX_LED_EXCEPTIONS as FLUX_LED_EXCEPTIONS
from _typeshed import Incomplete
from flux_led.aio import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Final

_LOGGER: Incomplete
REQUEST_REFRESH_DELAY: Final[float]

class FluxLedUpdateCoordinator(DataUpdateCoordinator[None]):
    device: Incomplete
    title: Incomplete
    entry: Incomplete
    force_next_update: bool
    def __init__(self, hass: HomeAssistant, device: AIOWifiLedBulb, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
