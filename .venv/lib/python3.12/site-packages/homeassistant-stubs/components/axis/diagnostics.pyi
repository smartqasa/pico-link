from . import AxisConfigEntry as AxisConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

REDACT_CONFIG: Incomplete
REDACT_BASIC_DEVICE_INFO: Incomplete
REDACT_VAPIX_PARAMS: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: AxisConfigEntry) -> dict[str, Any]: ...
