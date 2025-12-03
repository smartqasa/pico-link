from . import RussoundConfigEntry as RussoundConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: RussoundConfigEntry) -> dict[str, Any]: ...
