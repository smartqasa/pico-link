from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .onewirehub import CannotConnect as CannotConnect, OneWireHub as OneWireHub
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr

_LOGGER: Incomplete
type OneWireConfigEntry = ConfigEntry[OneWireHub]

async def async_setup_entry(hass: HomeAssistant, entry: OneWireConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: OneWireConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: OneWireConfigEntry) -> bool: ...
async def options_update_listener(hass: HomeAssistant, entry: OneWireConfigEntry) -> None: ...
