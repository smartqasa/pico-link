from .coordinator import TwenteMilieuConfigEntry as TwenteMilieuConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: TwenteMilieuConfigEntry) -> dict[str, Any]: ...
