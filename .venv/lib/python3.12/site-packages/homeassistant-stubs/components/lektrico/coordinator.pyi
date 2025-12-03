from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

SCAN_INTERVAL: Incomplete

class LektricoDeviceDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: ConfigEntry
    device: Incomplete
    serial_number: str
    board_revision: str
    device_type: str
    def __init__(self, hass: HomeAssistant, device_name: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
