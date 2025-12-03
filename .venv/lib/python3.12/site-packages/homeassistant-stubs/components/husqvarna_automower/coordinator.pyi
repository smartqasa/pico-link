from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes
from aioautomower.session import AutomowerSession as AutomowerSession
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
MAX_WS_RECONNECT_TIME: int
SCAN_INTERVAL: Incomplete
DEFAULT_RECONNECT_TIME: int

class AutomowerDataUpdateCoordinator(DataUpdateCoordinator[dict[str, MowerAttributes]]):
    config_entry: AutomowerConfigEntry
    api: Incomplete
    ws_connected: bool
    reconnect_time: Incomplete
    def __init__(self, hass: HomeAssistant, api: AutomowerSession) -> None: ...
    async def _async_update_data(self) -> dict[str, MowerAttributes]: ...
    @callback
    def callback(self, ws_data: dict[str, MowerAttributes]) -> None: ...
    async def client_listen(self, hass: HomeAssistant, entry: AutomowerConfigEntry, automower_client: AutomowerSession) -> None: ...
