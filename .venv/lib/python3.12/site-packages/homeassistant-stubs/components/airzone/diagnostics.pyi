from . import AirzoneConfigEntry as AirzoneConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_API: Incomplete
TO_REDACT_CONFIG: Incomplete
TO_REDACT_COORD: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: AirzoneConfigEntry) -> dict[str, Any]: ...
