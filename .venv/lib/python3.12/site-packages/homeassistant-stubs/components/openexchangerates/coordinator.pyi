from .const import CLIENT_TIMEOUT as CLIENT_TIMEOUT, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from aioopenexchangerates import Latest
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class OpenexchangeratesCoordinator(DataUpdateCoordinator[Latest]):
    base: Incomplete
    client: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, api_key: str, base: str, update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> Latest: ...
