from .coordinator import RAVEnConfigEntry as RAVEnConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

TO_REDACT_CONFIG: Incomplete
TO_REDACT_DATA: Incomplete

@callback
def async_redact_meter_macs(data: dict) -> dict: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: RAVEnConfigEntry) -> Mapping[str, Any]: ...
