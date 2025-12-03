from . import AirNowConfigEntry as AirNowConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

ATTR_LATITUDE_CAP: str
ATTR_LONGITUDE_CAP: str
ATTR_REPORTING_AREA: str
ATTR_STATE_CODE: str
CONF_TITLE: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AirNowConfigEntry) -> dict[str, Any]: ...
