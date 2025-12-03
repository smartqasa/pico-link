from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

type HomeWizardConfigEntry = ConfigEntry[HWEnergyDeviceUpdateCoordinator]
async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry) -> bool: ...
