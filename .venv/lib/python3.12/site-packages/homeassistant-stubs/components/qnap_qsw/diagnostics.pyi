from .const import DOMAIN as DOMAIN, QSW_COORD_DATA as QSW_COORD_DATA, QSW_COORD_FW as QSW_COORD_FW
from .coordinator import QswDataCoordinator as QswDataCoordinator, QswFirmwareCoordinator as QswFirmwareCoordinator
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_CONFIG: Incomplete
TO_REDACT_DATA: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
