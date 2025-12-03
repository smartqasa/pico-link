from .const import DOMAIN as DOMAIN, ENVIRONMENT as ENVIRONMENT, LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from geocachingapi.models import GeocachingStatus
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class GeocachingDataUpdateCoordinator(DataUpdateCoordinator[GeocachingStatus]):
    session: Incomplete
    entry: Incomplete
    geocaching: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry, session: OAuth2Session) -> None: ...
    async def _async_update_data(self) -> GeocachingStatus: ...
