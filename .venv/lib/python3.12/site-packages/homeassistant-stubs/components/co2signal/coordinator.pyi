from .const import DOMAIN as DOMAIN
from .helpers import fetch_latest_carbon_intensity as fetch_latest_carbon_intensity
from _typeshed import Incomplete
from aioelectricitymaps import CarbonIntensityResponse, ElectricityMaps as ElectricityMaps
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class CO2SignalCoordinator(DataUpdateCoordinator[CarbonIntensityResponse]):
    config_entry: ConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: ElectricityMaps) -> None: ...
    @property
    def entry_id(self) -> str: ...
    async def _async_update_data(self) -> CarbonIntensityResponse: ...
