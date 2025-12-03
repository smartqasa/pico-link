from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from gridnet import Device as Device, SmartBridge as SmartBridge
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import NamedTuple

class PureEnergieData(NamedTuple):
    device: Device
    smartbridge: SmartBridge

class PureEnergieDataUpdateCoordinator(DataUpdateCoordinator[PureEnergieData]):
    config_entry: ConfigEntry
    gridnet: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> PureEnergieData: ...
