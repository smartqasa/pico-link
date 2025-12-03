from . import BangOlufsenConfigEntry as BangOlufsenConfigEntry
from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: BangOlufsenConfigEntry) -> dict[str, Any]: ...
