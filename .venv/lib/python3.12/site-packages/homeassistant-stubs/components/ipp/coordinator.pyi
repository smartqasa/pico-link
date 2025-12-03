from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyipp import Printer as IPPPrinter

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class IPPDataUpdateCoordinator(DataUpdateCoordinator[IPPPrinter]):
    device_id: Incomplete
    ipp: Incomplete
    def __init__(self, hass: HomeAssistant, *, host: str, port: int, base_path: str, tls: bool, verify_ssl: bool, device_id: str) -> None: ...
    async def _async_update_data(self) -> IPPPrinter: ...
