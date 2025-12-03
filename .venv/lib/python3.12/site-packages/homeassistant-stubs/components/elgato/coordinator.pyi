from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from elgato import BatteryInfo as BatteryInfo, Info as Info, Settings as Settings, State as State
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type ElgatoConfigEntry = ConfigEntry[ElgatoDataUpdateCoordinator]
@dataclass
class ElgatoData:
    battery: BatteryInfo | None
    info: Info
    settings: Settings
    state: State

class ElgatoDataUpdateCoordinator(DataUpdateCoordinator[ElgatoData]):
    config_entry: ElgatoConfigEntry
    has_battery: bool | None
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ElgatoConfigEntry) -> None: ...
    async def _async_update_data(self) -> ElgatoData: ...
