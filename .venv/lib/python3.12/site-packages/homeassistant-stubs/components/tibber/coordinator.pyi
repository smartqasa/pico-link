import tibber
from _typeshed import Incomplete
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData
from homeassistant.components.recorder.statistics import async_add_external_statistics as async_add_external_statistics, get_last_statistics as get_last_statistics, statistics_during_period as statistics_during_period
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfEnergy as UnitOfEnergy
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

FIVE_YEARS: Incomplete
_LOGGER: Incomplete

class TibberDataCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    _tibber_connection: Incomplete
    def __init__(self, hass: HomeAssistant, tibber_connection: tibber.Tibber) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _insert_statistics(self) -> None: ...
