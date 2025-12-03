from .const import CONNECTION_TIMEOUT as CONNECTION_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, REQUEST_REFRESH_DEFAULT_IMMEDIATE as REQUEST_REFRESH_DEFAULT_IMMEDIATE, UpdateFailed as UpdateFailed
from typing import Final

_LOGGER: Incomplete
UPDATE_INTERVAL: Final[Incomplete]
REQUEST_REFRESH_COOLDOWN: Final[int]

class APCUPSdData(dict[str, str]):
    @property
    def name(self) -> str | None: ...
    @property
    def model(self) -> str | None: ...
    @property
    def serial_no(self) -> str | None: ...

class APCUPSdCoordinator(DataUpdateCoordinator[APCUPSdData]):
    config_entry: ConfigEntry
    _host: Incomplete
    _port: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, port: int) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def _async_update_data(self) -> APCUPSdData: ...
