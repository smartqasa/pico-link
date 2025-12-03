from . import DsmrConfigEntry as DsmrConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.json import json_loads as json_loads
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: DsmrConfigEntry) -> dict[str, Any]: ...
