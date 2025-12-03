from .const import DEFAULT_UPDATE_INTERVAL as DEFAULT_UPDATE_INTERVAL, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from nettigo_air_monitor import NAMSensors, NettigoAirMonitor as NettigoAirMonitor

_LOGGER: Incomplete

class NAMDataUpdateCoordinator(DataUpdateCoordinator[NAMSensors]):
    unique_id: Incomplete
    device_info: Incomplete
    nam: Incomplete
    def __init__(self, hass: HomeAssistant, nam: NettigoAirMonitor, unique_id: str) -> None: ...
    async def _async_update_data(self) -> NAMSensors: ...
