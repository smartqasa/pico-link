import psutil_home_assistant as ha_psutil
from .const import DOMAIN as DOMAIN
from .hardware import async_process_hardware_platforms as async_process_hardware_platforms
from .models import HardwareProtocol as HardwareProtocol
from dataclasses import dataclass
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from typing import Any

@dataclass(slots=True)
class SystemStatus:
    ha_psutil: ha_psutil
    remove_periodic_timer: CALLBACK_TYPE | None
    subscribers: set[tuple[websocket_api.ActiveConnection, int]]

async def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.async_response
async def ws_info(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def ws_subscribe_system_status(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
