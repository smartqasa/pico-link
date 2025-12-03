from . import DeviceTuple as DeviceTuple, async_setup_platform_entry as async_setup_platform_entry
from .const import DEVICE_PACKET_TYPE_LIGHTING4 as DEVICE_PACKET_TYPE_LIGHTING4
from .entity import RfxtrxEntity as RfxtrxEntity
from RFXtrx import RFXtrxDevice as RFXtrxDevice, RFXtrxEvent as RFXtrxEvent
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RfxtrxEventEntity(RfxtrxEntity, EventEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_event_types: Incomplete
    _attr_translation_key: Incomplete
    _value_attribute: Incomplete
    def __init__(self, device: RFXtrxDevice, device_id: DeviceTuple, device_attribute: str, value_attribute: str, translation_key: str) -> None: ...
    @callback
    def _handle_event(self, event: RFXtrxEvent, device_id: DeviceTuple) -> None: ...
