from .const import DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiowebostv import WebOsClient as WebOsClient
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
