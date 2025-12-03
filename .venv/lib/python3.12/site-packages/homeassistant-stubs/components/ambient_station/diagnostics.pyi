from . import AmbientStationConfigEntry as AmbientStationConfigEntry
from .const import CONF_APP_KEY as CONF_APP_KEY
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LOCATION as CONF_LOCATION, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_API_KEY_CAMEL: str
CONF_APP_KEY_CAMEL: str
CONF_DEVICE_ID_CAMEL: str
CONF_MAC_ADDRESS: str
CONF_MAC_ADDRESS_CAMEL: str
CONF_TITLE: str
CONF_TZ: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AmbientStationConfigEntry) -> dict[str, Any]: ...
