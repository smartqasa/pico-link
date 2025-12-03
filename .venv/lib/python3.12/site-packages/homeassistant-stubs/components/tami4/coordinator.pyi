from Tami4EdgeAPI import Tami4EdgeAPI as Tami4EdgeAPI
from Tami4EdgeAPI.water_quality import WaterQuality as WaterQuality
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import date
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

@dataclass
class FlattenedWaterQuality:
    uv_upcoming_replacement: date
    uv_installed: bool
    filter_upcoming_replacement: date
    filter_installed: bool
    filter_litters_passed: float
    def __init__(self, water_quality: WaterQuality) -> None: ...

class Tami4EdgeCoordinator(DataUpdateCoordinator[FlattenedWaterQuality]):
    _api: Incomplete
    def __init__(self, hass: HomeAssistant, api: Tami4EdgeAPI) -> None: ...
    async def _async_update_data(self) -> FlattenedWaterQuality: ...
