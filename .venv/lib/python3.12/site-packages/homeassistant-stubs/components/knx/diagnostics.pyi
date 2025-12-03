from . import CONFIG_SCHEMA as CONFIG_SCHEMA
from .const import CONF_KNX_KNXKEY_PASSWORD as CONF_KNX_KNXKEY_PASSWORD, CONF_KNX_ROUTING_BACKBONE_KEY as CONF_KNX_ROUTING_BACKBONE_KEY, CONF_KNX_SECURE_DEVICE_AUTHENTICATION as CONF_KNX_SECURE_DEVICE_AUTHENTICATION, CONF_KNX_SECURE_USER_PASSWORD as CONF_KNX_SECURE_USER_PASSWORD, DOMAIN as DOMAIN, KNX_MODULE_KEY as KNX_MODULE_KEY
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
