from . import TractiveConfigEntry as TractiveConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: TractiveConfigEntry) -> dict[str, Any]: ...
