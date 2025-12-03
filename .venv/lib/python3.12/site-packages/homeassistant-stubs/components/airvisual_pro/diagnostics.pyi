from . import AirVisualProConfigEntry as AirVisualProConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_MAC_ADDRESS: str
CONF_SERIAL_NUMBER: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AirVisualProConfigEntry) -> dict[str, Any]: ...
