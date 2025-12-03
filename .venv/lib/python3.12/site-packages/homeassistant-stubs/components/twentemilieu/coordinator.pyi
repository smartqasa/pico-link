from .const import CONF_HOUSE_LETTER as CONF_HOUSE_LETTER, CONF_HOUSE_NUMBER as CONF_HOUSE_NUMBER, CONF_POST_CODE as CONF_POST_CODE, DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from datetime import date
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from twentemilieu import WasteType

type TwenteMilieuConfigEntry = ConfigEntry[TwenteMilieuDataUpdateCoordinator]
class TwenteMilieuDataUpdateCoordinator(DataUpdateCoordinator[dict[WasteType, list[date]]]):
    twentemilieu: Incomplete
    def __init__(self, hass: HomeAssistant, entry: TwenteMilieuConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[WasteType, list[date]]: ...
