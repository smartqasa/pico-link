from . import TVFerryConfigEntry as TVFerryConfigEntry
from .const import CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import date, time
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytrafikverket.models import FerryStopModel as FerryStopModel
from typing import Any

_LOGGER: Incomplete
TIME_BETWEEN_UPDATES: Incomplete

def next_weekday(fromdate: date, weekday: int) -> date: ...
def next_departuredate(departure: list[str]) -> date: ...

class TVDataUpdateCoordinator(DataUpdateCoordinator):
    config_entry: TVFerryConfigEntry
    _ferry_api: Incomplete
    _from: str
    _to: str
    _time: time | None
    _weekdays: list[str]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
