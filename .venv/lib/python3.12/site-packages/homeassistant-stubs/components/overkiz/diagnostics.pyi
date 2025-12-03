from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .const import CONF_API_TYPE as CONF_API_TYPE, CONF_HUB as CONF_HUB
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: OverkizDataConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, entry: OverkizDataConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
