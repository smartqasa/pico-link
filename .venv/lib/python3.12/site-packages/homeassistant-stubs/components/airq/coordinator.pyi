from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class AirQCoordinator(DataUpdateCoordinator):
    airq: Incomplete
    device_id: Incomplete
    device_info: Incomplete
    clip_negative: Incomplete
    return_average: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, clip_negative: bool = True, return_average: bool = True) -> None: ...
    async def _async_update_data(self) -> dict: ...
