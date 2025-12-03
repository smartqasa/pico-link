from .const import CHILD_CALLBACK as CHILD_CALLBACK, DevId as DevId, GatewayId as GatewayId, NODE_CALLBACK as NODE_CALLBACK
from .entity import get_mysensors_devices as get_mysensors_devices
from .helpers import discover_mysensors_node as discover_mysensors_node, discover_mysensors_platform as discover_mysensors_platform, validate_set_msg as validate_set_msg
from collections.abc import Callable as Callable
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.util import decorator as decorator
from mysensors import Message as Message

HANDLERS: decorator.Registry[str, Callable[[HomeAssistant, GatewayId, Message], None]]

@callback
def handle_set(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
@callback
def handle_internal(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
@callback
def handle_battery_level(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
@callback
def handle_heartbeat(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
@callback
def handle_sketch_name(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
@callback
def handle_sketch_version(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
@callback
def handle_presentation(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
@callback
def _handle_child_update(hass: HomeAssistant, gateway_id: GatewayId, validated: dict[Platform, list[DevId]]) -> None: ...
@callback
def _handle_node_update(hass: HomeAssistant, gateway_id: GatewayId, msg: Message) -> None: ...
