from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from imgw_pib import HydrologicalData, ImgwPib as ImgwPib

_LOGGER: Incomplete

class ImgwPibDataUpdateCoordinator(DataUpdateCoordinator[HydrologicalData]):
    imgwpib: Incomplete
    station_id: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, imgwpib: ImgwPib, station_id: str) -> None: ...
    async def _async_update_data(self) -> HydrologicalData: ...
