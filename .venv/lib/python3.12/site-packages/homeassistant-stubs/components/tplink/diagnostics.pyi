from . import TPLinkConfigEntry as TPLinkConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: TPLinkConfigEntry) -> dict[str, Any]: ...
