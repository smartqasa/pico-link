from . import AndroidTVConfigEntry as AndroidTVConfigEntry
from .const import DOMAIN as DOMAIN, PROP_ETHMAC as PROP_ETHMAC, PROP_SERIALNO as PROP_SERIALNO, PROP_WIFIMAC as PROP_WIFIMAC
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete
TO_REDACT_DEV: Incomplete
TO_REDACT_DEV_PROP: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AndroidTVConfigEntry) -> dict[str, dict[str, Any]]: ...
