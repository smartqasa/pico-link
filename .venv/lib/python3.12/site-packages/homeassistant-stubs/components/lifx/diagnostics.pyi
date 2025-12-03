from .const import CONF_LABEL as CONF_LABEL, DOMAIN as DOMAIN
from .coordinator import LIFXUpdateCoordinator as LIFXUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
