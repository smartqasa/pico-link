from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .coordinator import FritzboxConfigEntry as FritzboxConfigEntry, FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries

async def async_setup_entry(hass: HomeAssistant, entry: FritzboxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FritzboxConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: FritzboxConfigEntry, device: DeviceEntry) -> bool: ...
