from . import EcovacsConfigEntry as EcovacsConfigEntry
from .const import CONF_OVERRIDE_MQTT_URL as CONF_OVERRIDE_MQTT_URL, CONF_OVERRIDE_REST_URL as CONF_OVERRIDE_REST_URL
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

REDACT_CONFIG: Incomplete
REDACT_DEVICE: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: EcovacsConfigEntry) -> dict[str, Any]: ...
