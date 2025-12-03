from . import YaleConfigEntry as YaleConfigEntry
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER, YALE_BASE_ERRORS as YALE_BASE_ERRORS
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any
from yalesmartalarmclient import YaleLock
from yalesmartalarmclient.client import YaleSmartAlarmClient

class YaleDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    yale: YaleSmartAlarmClient
    config_entry: YaleConfigEntry
    locks: list[YaleLock]
    def __init__(self, hass: HomeAssistant, config_entry: YaleConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    def get_updates(self) -> dict[str, Any]: ...
