from . import PowerfoxConfigEntry as PowerfoxConfigEntry, PowerfoxDataUpdateCoordinator as PowerfoxDataUpdateCoordinator
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: PowerfoxConfigEntry) -> dict[str, Any]: ...
