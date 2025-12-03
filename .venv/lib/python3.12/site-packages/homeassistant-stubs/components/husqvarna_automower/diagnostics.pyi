from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

CONF_REFRESH_TOKEN: str
POSITIONS: str
TO_REDACT: Incomplete
_LOGGER: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AutomowerConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, entry: AutomowerConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
