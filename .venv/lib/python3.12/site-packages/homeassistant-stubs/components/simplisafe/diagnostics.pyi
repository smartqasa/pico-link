from . import SimpliSafe as SimpliSafe
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_CODE as CONF_CODE, CONF_LOCATION as CONF_LOCATION, CONF_TOKEN as CONF_TOKEN, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_CREDIT_CARD: str
CONF_EXPIRES: str
CONF_LOCATION_NAME: str
CONF_PAYMENT_PROFILE_ID: str
CONF_SERIAL: str
CONF_SID: str
CONF_SYSTEM_ID: str
CONF_TITLE: str
CONF_UID: str
CONF_WIFI_SSID: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
