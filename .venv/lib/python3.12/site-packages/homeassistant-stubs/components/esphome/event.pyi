from .entity import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, Event, EventInfo
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity
from homeassistant.core import callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

class EsphomeEvent(EsphomeEntity[EventInfo, Event], EventEntity):
    _attr_event_types: Incomplete
    _attr_device_class: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @callback
    def _on_state_update(self) -> None: ...

async_setup_entry: Incomplete
