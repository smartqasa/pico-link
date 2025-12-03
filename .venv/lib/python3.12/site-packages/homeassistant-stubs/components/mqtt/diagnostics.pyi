from . import debug_info as debug_info, is_connected as is_connected
from .models import DATA_MQTT as DATA_MQTT
from _typeshed import Incomplete
from homeassistant.components import device_tracker as device_tracker
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

REDACT_CONFIG: Incomplete
REDACT_STATE_DEVICE_TRACKER: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, entry: ConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
@callback
def _async_get_diagnostics(hass: HomeAssistant, entry: ConfigEntry, device: DeviceEntry | None = None) -> dict[str, Any]: ...
@callback
def _async_device_as_dict(hass: HomeAssistant, device: DeviceEntry) -> dict[str, Any]: ...
