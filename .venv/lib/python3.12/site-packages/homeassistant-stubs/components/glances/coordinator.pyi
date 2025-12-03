from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from glances_api import Glances as Glances
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.dt import parse_duration as parse_duration, utcnow as utcnow
from typing import Any

_LOGGER: Incomplete

class GlancesDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: ConfigEntry
    hass: Incomplete
    host: str
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: Glances) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
