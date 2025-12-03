from .const import ATTR_EVENT_TYPE as ATTR_EVENT_TYPE, ATTR_EVENT_TYPES as ATTR_EVENT_TYPES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.restore_state import ExtraStoredData, RestoreEntity
from propcache import cached_property
from typing import Any, Self, final

__all__ = ['ATTR_EVENT_TYPE', 'ATTR_EVENT_TYPES', 'DOMAIN', 'PLATFORM_SCHEMA_BASE', 'PLATFORM_SCHEMA', 'EventDeviceClass', 'EventEntity', 'EventEntityDescription']

PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete

class EventDeviceClass(StrEnum):
    DOORBELL = 'doorbell'
    BUTTON = 'button'
    MOTION = 'motion'

class EventEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: EventDeviceClass | None = ...
    event_types: list[str] | None = ...

@dataclass
class EventExtraStoredData(ExtraStoredData):
    last_event_type: str | None
    last_event_attributes: dict[str, Any] | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Self | None: ...

class EventEntity(RestoreEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: EventEntityDescription
    _attr_device_class: EventDeviceClass | None
    _attr_event_types: list[str]
    _attr_state: None
    __last_event_triggered: datetime | None
    __last_event_type: str | None
    __last_event_attributes: dict[str, Any] | None
    @cached_property
    def device_class(self) -> EventDeviceClass | None: ...
    @cached_property
    def event_types(self) -> list[str]: ...
    @final
    def _trigger_event(self, event_type: str, event_attributes: dict[str, Any] | None = None) -> None: ...
    def _default_to_device_class_name(self) -> bool: ...
    @property
    @final
    def capability_attributes(self) -> dict[str, list[str]]: ...
    @property
    @final
    def state(self) -> str | None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @final
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def extra_restore_state_data(self) -> EventExtraStoredData: ...
    async def async_get_last_event_data(self) -> EventExtraStoredData | None: ...
