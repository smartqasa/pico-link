import axis
from _typeshed import Incomplete
from axis.stream_manager import Signal
from homeassistant.components import mqtt as mqtt
from homeassistant.components.mqtt import ReceiveMessage as ReceiveMessage
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.setup import async_when_setup as async_when_setup

class AxisEventSource:
    hass: Incomplete
    config_entry: Incomplete
    api: Incomplete
    signal_reachable: Incomplete
    available: bool
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, api: axis.AxisDevice) -> None: ...
    @callback
    def setup(self) -> None: ...
    @callback
    def teardown(self) -> None: ...
    @callback
    def _disconnect_from_stream(self) -> None: ...
    async def _async_use_mqtt(self, hass: HomeAssistant, component: str) -> None: ...
    @callback
    def _mqtt_message(self, message: ReceiveMessage) -> None: ...
    @callback
    def _connection_status_cb(self, status: Signal) -> None: ...
