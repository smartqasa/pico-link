from .const import DOMAIN as DOMAIN
from collections.abc import Iterable
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Iterable[Any]

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
