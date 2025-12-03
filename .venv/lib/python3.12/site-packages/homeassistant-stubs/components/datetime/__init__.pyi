from .const import ATTR_DATETIME as ATTR_DATETIME, DOMAIN as DOMAIN
from datetime import datetime
from homeassistant.helpers.entity import Entity, EntityDescription
from propcache import cached_property
from typing import final

__all__ = ['ATTR_DATETIME', 'DOMAIN', 'DateTimeEntity', 'DateTimeEntityDescription']

class DateTimeEntityDescription(EntityDescription, frozen_or_thawed=True): ...

class DateTimeEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: DateTimeEntityDescription
    _attr_device_class: None
    _attr_state: None
    _attr_native_value: datetime | None
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
    def native_value(self) -> datetime | None: ...
    def set_value(self, value: datetime) -> None: ...
    async def async_set_value(self, value: datetime) -> None: ...
