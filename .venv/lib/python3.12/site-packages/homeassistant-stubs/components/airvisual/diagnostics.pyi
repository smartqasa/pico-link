from . import AirVisualConfigEntry as AirVisualConfigEntry
from .const import CONF_CITY as CONF_CITY
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_COUNTRY as CONF_COUNTRY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_STATE as CONF_STATE, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_COORDINATES: str
CONF_TITLE: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AirVisualConfigEntry) -> dict[str, Any]: ...
