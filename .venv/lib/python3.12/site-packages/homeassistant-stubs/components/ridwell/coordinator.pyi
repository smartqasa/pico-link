from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from aioridwell.model import RidwellAccount as RidwellAccount, RidwellPickupEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

UPDATE_INTERVAL: Incomplete

class RidwellDataUpdateCoordinator(DataUpdateCoordinator[dict[str, list[RidwellPickupEvent]]]):
    config_entry: ConfigEntry
    accounts: dict[str, RidwellAccount]
    dashboard_url: str
    user_id: str
    def __init__(self, hass: HomeAssistant, *, name: str) -> None: ...
    async def _async_update_data(self) -> dict[str, list[RidwellPickupEvent]]: ...
    async def async_initialize(self) -> None: ...
