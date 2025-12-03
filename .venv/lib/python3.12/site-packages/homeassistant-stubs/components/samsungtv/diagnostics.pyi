from . import SamsungTVConfigEntry as SamsungTVConfigEntry
from .const import CONF_SESSION_ID as CONF_SESSION_ID
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: SamsungTVConfigEntry) -> dict[str, Any]: ...
