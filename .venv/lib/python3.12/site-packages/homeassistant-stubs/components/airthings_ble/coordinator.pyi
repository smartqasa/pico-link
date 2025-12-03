from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from airthings_ble import AirthingsDevice
from bleak.backends.device import BLEDevice as BLEDevice
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM

_LOGGER: Incomplete
type AirthingsBLEConfigEntry = ConfigEntry[AirthingsBLEDataUpdateCoordinator]

class AirthingsBLEDataUpdateCoordinator(DataUpdateCoordinator[AirthingsDevice]):
    ble_device: BLEDevice
    config_entry: AirthingsBLEConfigEntry
    airthings: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AirthingsBLEConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> AirthingsDevice: ...
