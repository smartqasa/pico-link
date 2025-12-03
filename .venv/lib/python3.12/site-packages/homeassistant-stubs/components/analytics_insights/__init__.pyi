from .const import CONF_TRACKED_INTEGRATIONS as CONF_TRACKED_INTEGRATIONS
from .coordinator import HomeassistantAnalyticsDataUpdateCoordinator as HomeassistantAnalyticsDataUpdateCoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]
type AnalyticsInsightsConfigEntry = ConfigEntry[AnalyticsInsightsData]

@dataclass(frozen=True)
class AnalyticsInsightsData:
    coordinator: HomeassistantAnalyticsDataUpdateCoordinator
    names: dict[str, str]

async def async_setup_entry(hass: HomeAssistant, entry: AnalyticsInsightsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AnalyticsInsightsConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: AnalyticsInsightsConfigEntry) -> None: ...
