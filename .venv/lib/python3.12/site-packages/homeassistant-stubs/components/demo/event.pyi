from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoEvent(EventEntity):
    _attr_device_class: Incomplete
    _attr_event_types: Incomplete
    _attr_has_entity_name: bool
    _attr_name: str
    _attr_should_poll: bool
    _attr_translation_key: str
    _attr_unique_id: str
    _attr_device_info: Incomplete
    def __init__(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, _: Event) -> None: ...
