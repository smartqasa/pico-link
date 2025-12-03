from . import RainMachineConfigEntry as RainMachineConfigEntry
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_STATION_ID: str
CONF_STATION_NAME: str
CONF_STATION_SOURCE: str
CONF_TIMEZONE: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: RainMachineConfigEntry) -> dict[str, Any]: ...
