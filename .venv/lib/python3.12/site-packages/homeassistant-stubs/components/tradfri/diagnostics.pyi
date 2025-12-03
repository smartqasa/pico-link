from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
