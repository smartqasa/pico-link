from _typeshed import Incomplete
from homeassistant.components.homeassistant import exposed_entities as exposed_entities
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, ToggleEntity as ToggleEntity
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from typing import Any

class BaseEntity(Entity):
    _attr_should_poll: bool
    _is_new_entity: bool
    _device_id: Incomplete
    _attr_device_info: Incomplete
    _attr_entity_category: Incomplete
    _attr_has_entity_name: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _switch_entity_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry_title: str, domain: str, switch_entity_id: str, unique_id: str) -> None: ...
    _attr_available: bool
    @callback
    def async_state_changed_listener(self, event: Event[EventStateChangedData] | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_generate_entity_options(self) -> dict[str, Any]: ...

class BaseToggleEntity(BaseEntity, ToggleEntity):
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def async_state_changed_listener(self, event: Event[EventStateChangedData] | None = None) -> None: ...

class BaseInvertableEntity(BaseEntity):
    _invert_state: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry_title: str, domain: str, invert: bool, switch_entity_id: str, unique_id: str) -> None: ...
    @callback
    def async_generate_entity_options(self) -> dict[str, Any]: ...
