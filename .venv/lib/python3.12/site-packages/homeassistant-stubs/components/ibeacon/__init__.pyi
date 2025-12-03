from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import IBeaconCoordinator as IBeaconCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

type IBeaconConfigEntry = ConfigEntry[IBeaconCoordinator]
async def async_setup_entry(hass: HomeAssistant, entry: IBeaconConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: IBeaconConfigEntry, device_entry: DeviceEntry) -> bool: ...
