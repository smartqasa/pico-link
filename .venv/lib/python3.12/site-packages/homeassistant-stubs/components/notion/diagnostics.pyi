from .const import CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, CONF_USER_UUID as CONF_USER_UUID, DOMAIN as DOMAIN
from .coordinator import NotionDataUpdateCoordinator as NotionDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_DEVICE_KEY: str
CONF_HARDWARE_ID: str
CONF_LAST_BRIDGE_HARDWARE_ID: str
CONF_TITLE: str
CONF_USER_ID: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
