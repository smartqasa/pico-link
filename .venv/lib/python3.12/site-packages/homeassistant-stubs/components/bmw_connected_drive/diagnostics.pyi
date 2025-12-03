from . import BMWConfigEntry as BMWConfigEntry
from .const import CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from typing import Any

PARALLEL_UPDATES: int
TO_REDACT_INFO: Incomplete
TO_REDACT_DATA: Incomplete

def vehicle_to_dict(vehicle: MyBMWVehicle | None) -> dict: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: BMWConfigEntry) -> dict[str, Any]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: BMWConfigEntry, device: DeviceEntry) -> dict[str, Any]: ...
