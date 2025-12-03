from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_LATEST_VIDEO as ATTR_LATEST_VIDEO, COORDINATOR as COORDINATOR, DOMAIN as DOMAIN
from .coordinator import YouTubeDataUpdateCoordinator as YouTubeDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
