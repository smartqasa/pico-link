from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL, THRESHOLD_HOUR as THRESHOLD_HOUR
from _typeshed import Incomplete
from easyenergy import Electricity as Electricity, Gas as Gas
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import NamedTuple

type EasyEnergyConfigEntry = ConfigEntry[EasyEnergyDataUpdateCoordinator]
class EasyEnergyData(NamedTuple):
    energy_today: Electricity
    energy_tomorrow: Electricity | None
    gas_today: Gas | None

class EasyEnergyDataUpdateCoordinator(DataUpdateCoordinator[EasyEnergyData]):
    config_entry: EasyEnergyConfigEntry
    easyenergy: Incomplete
    def __init__(self, hass: HomeAssistant, entry: EasyEnergyConfigEntry) -> None: ...
    async def _async_update_data(self) -> EasyEnergyData: ...
