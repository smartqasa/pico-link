from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, VALID_UNITS as VALID_UNITS, WeatherEntityFeature as WeatherEntityFeature
from _typeshed import Incomplete
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.json import JsonValueType as JsonValueType
from typing import Any

FORECAST_TYPE_TO_FLAG: Incomplete

@callback
def async_setup(hass: HomeAssistant) -> None: ...
@callback
def ws_convertible_units(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def ws_subscribe_forecast(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
