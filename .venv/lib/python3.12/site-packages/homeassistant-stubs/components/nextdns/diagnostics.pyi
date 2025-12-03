from . import NextDnsConfigEntry as NextDnsConfigEntry
from .const import CONF_PROFILE_ID as CONF_PROFILE_ID
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: NextDnsConfigEntry) -> dict[str, Any]: ...
