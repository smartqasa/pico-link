from .const import DOMAIN as DOMAIN
from .models import DomainData as DomainData
from _typeshed import DataclassInstance, Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

def _async_redact_data(obj: DataclassInstance | None) -> dict[str, Any] | None: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
