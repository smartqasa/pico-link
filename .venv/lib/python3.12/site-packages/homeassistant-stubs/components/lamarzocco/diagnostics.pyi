from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.core import HomeAssistant as HomeAssistant
from pylamarzocco.const import FirmwareType as FirmwareType
from typing import Any, TypedDict

TO_REDACT: Incomplete

class DiagnosticsData(TypedDict):
    model: str
    config: dict[str, Any]
    firmware: list[dict[FirmwareType, dict[str, Any]]]
    statistics: dict[str, Any]

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: LaMarzoccoConfigEntry) -> dict[str, Any]: ...
