from . import SolarlogConfigEntry as SolarlogConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import slugify as slugify
from solarlog_cli.solarlog_models import SolarlogData

_LOGGER: Incomplete

class SolarLogCoordinator(DataUpdateCoordinator[SolarlogData]):
    new_device_callbacks: list[Callable[[int], None]]
    _devices_last_update: set[tuple[int, str]]
    unique_id: Incomplete
    host: Incomplete
    solarlog: Incomplete
    def __init__(self, hass: HomeAssistant, entry: SolarlogConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SolarlogData: ...
    def _async_add_remove_devices(self, data: SolarlogData) -> None: ...
    async def renew_authentication(self) -> bool: ...
