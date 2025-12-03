from . import BraviaTVConfigEntry as BraviaTVConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_PIN as CONF_PIN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: BraviaTVConfigEntry) -> dict[str, Any]: ...
