from .types import NestConfigEntry as NestConfigEntry
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

REDACT_DEVICE_TRAITS: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: NestConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: NestConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
