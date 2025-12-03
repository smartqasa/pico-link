from .const import DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, NON_NUMERIC_DEVICE_CLASSES as NON_NUMERIC_DEVICE_CLASSES, SensorDeviceClass as SensorDeviceClass, UNIT_CONVERTERS as UNIT_CONVERTERS
from _typeshed import Incomplete
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

_NUMERIC_DEVICE_CLASSES: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
def ws_device_class_units(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def ws_numeric_device_classes(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
