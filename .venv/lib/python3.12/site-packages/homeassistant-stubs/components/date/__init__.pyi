from .const import DOMAIN as DOMAIN
from datetime import date
from homeassistant.helpers.entity import Entity, EntityDescription
from propcache import cached_property
from typing import final

__all__ = ['DOMAIN', 'DateEntity', 'DateEntityDescription']

class DateEntityDescription(EntityDescription, frozen_or_thawed=True): ...

class DateEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: DateEntityDescription
    _attr_device_class: None
    _attr_native_value: date | None
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
    def native_value(self) -> date | None: ...
    def set_value(self, value: date) -> None: ...
    async def async_set_value(self, value: date) -> None: ...
