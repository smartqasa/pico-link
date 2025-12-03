from . import RenaultConfigEntry as RenaultConfigEntry
from .const import CONF_KAMEREON_ACCOUNT_ID as CONF_KAMEREON_ACCOUNT_ID
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: RenaultConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, entry: RenaultConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
def _get_vehicle_diagnostics(vehicle: RenaultVehicleProxy) -> dict[str, Any]: ...
