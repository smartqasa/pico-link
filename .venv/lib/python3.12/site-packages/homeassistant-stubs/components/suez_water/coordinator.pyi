from .const import CONF_COUNTER_ID as CONF_COUNTER_ID, DATA_REFRESH_INTERVAL as DATA_REFRESH_INTERVAL, DOMAIN as DOMAIN
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, _LOGGER as _LOGGER
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysuez import SuezClient

@dataclass
class SuezWaterAggregatedAttributes:
    this_month_consumption: dict[str, float]
    previous_month_consumption: dict[str, float]
    last_year_overall: dict[str, float]
    this_year_overall: dict[str, float]
    history: dict[str, float]
    highest_monthly_consumption: float

@dataclass
class SuezWaterData:
    aggregated_value: float
    aggregated_attr: SuezWaterAggregatedAttributes
    price: float
type SuezWaterConfigEntry = ConfigEntry[SuezWaterCoordinator]

class SuezWaterCoordinator(DataUpdateCoordinator[SuezWaterData]):
    _suez_client: SuezClient
    config_entry: SuezWaterConfigEntry
    def __init__(self, hass: HomeAssistant, config_entry: SuezWaterConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SuezWaterData: ...
