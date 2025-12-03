from . import WLEDConfigEntry as WLEDConfigEntry
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: WLEDConfigEntry) -> dict[str, Any]: ...
