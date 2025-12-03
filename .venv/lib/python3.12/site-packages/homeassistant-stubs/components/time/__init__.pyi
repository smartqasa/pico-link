from .const import DOMAIN as DOMAIN
from datetime import time
from homeassistant.helpers.entity import Entity, EntityDescription
from propcache import cached_property
from typing import final

__all__ = ['DOMAIN', 'TimeEntity', 'TimeEntityDescription']

class TimeEntityDescription(EntityDescription, frozen_or_thawed=True): ...

class TimeEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: TimeEntityDescription
    _attr_native_value: time | None
    _attr_device_class: None
    _attr_state: None
    @cached_property
    @final
    def device_class(self) -> None: ...
    @cached_property
    @final
    def state_attributes(self) -> None: ...
    @property
    @final
    def state(self) -> str | None: ...
    @cached_property
    def native_value(self) -> time | None: ...
    def set_value(self, value: time) -> None: ...
    async def async_set_value(self, value: time) -> None: ...
