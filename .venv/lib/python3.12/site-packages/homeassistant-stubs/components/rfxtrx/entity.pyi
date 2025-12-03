import RFXtrx as rfxtrxmod
from . import DeviceTuple as DeviceTuple
from .const import ATTR_EVENT as ATTR_EVENT, COMMAND_GROUP_LIST as COMMAND_GROUP_LIST, DATA_RFXOBJECT as DATA_RFXOBJECT, DOMAIN as DOMAIN, SIGNAL_EVENT as SIGNAL_EVENT
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity

def _get_identifiers_from_device_tuple(device_tuple: DeviceTuple) -> set[tuple[str, str]]: ...

class RfxtrxEntity(RestoreEntity):
    _attr_assumed_state: bool
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _device: rfxtrxmod.RFXtrxDevice
    _event: rfxtrxmod.RFXtrxEvent | None
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _device_id: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, event: rfxtrxmod.RFXtrxEvent | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    def _event_applies(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> bool: ...
    def _apply_event(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    @callback
    def _handle_event(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> None: ...

class RfxtrxCommandEntity(RfxtrxEntity):
    _attr_name: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, event: rfxtrxmod.RFXtrxEvent | None = None) -> None: ...
    async def _async_send[*_Ts](self, fun: Callable[[rfxtrxmod.PySerialTransport, *_Ts], None], *args: *_Ts) -> None: ...
