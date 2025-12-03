from .const import CONF_LISTEN_CREDENTIALS as CONF_LISTEN_CREDENTIALS, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import RingDataCoordinator as RingDataCoordinator, RingListenCoordinator as RingListenCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import APPLICATION_NAME as APPLICATION_NAME, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from ring_doorbell import Ring, RingDevices as RingDevices

_LOGGER: Incomplete

@dataclass
class RingData:
    api: Ring
    devices: RingDevices
    devices_coordinator: RingDataCoordinator
    listen_coordinator: RingListenCoordinator
type RingConfigEntry = ConfigEntry[RingData]

def get_auth_user_agent() -> str: ...
async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
