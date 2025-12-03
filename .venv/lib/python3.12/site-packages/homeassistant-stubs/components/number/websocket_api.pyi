from .const import DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, UNIT_CONVERTERS as UNIT_CONVERTERS
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
def ws_device_class_units(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
