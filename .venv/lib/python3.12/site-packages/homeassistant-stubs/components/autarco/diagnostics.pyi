from . import AutarcoConfigEntry as AutarcoConfigEntry, AutarcoDataUpdateCoordinator as AutarcoDataUpdateCoordinator
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: AutarcoConfigEntry) -> dict[str, Any]: ...
