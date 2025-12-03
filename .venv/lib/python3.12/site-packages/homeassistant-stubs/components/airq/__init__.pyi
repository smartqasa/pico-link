from .const import CONF_CLIP_NEGATIVE as CONF_CLIP_NEGATIVE, CONF_RETURN_AVERAGE as CONF_RETURN_AVERAGE
from .coordinator import AirQCoordinator as AirQCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
AirQConfigEntry = ConfigEntry[AirQCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AirQConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirQConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
