import re
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.restore_state import ExtraStoredData, RestoreEntity
from propcache import cached_property
from typing import Any, final

__all__ = ['DOMAIN', 'TextEntity', 'TextEntityDescription', 'TextMode']

class TextMode(StrEnum):
    PASSWORD = 'password'
    TEXT = 'text'

class TextEntityDescription(EntityDescription, frozen_or_thawed=True):
    native_min: int = ...
    native_max: int = ...
    mode: TextMode = ...
    pattern: str | None = ...

class TextEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: TextEntityDescription
    _attr_mode: TextMode
    _attr_native_value: str | None
    _attr_native_min: int
    _attr_native_max: int
    _attr_pattern: str | None
    _attr_state: None
    __pattern_cmp: re.Pattern | None
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    @final
    def state(self) -> str | None: ...
    @cached_property
    def mode(self) -> TextMode: ...
    @cached_property
    def native_min(self) -> int: ...
    @property
    @final
    def min(self) -> int: ...
    @cached_property
    def native_max(self) -> int: ...
    @property
    @final
    def max(self) -> int: ...
    @property
    @final
    def pattern_cmp(self) -> re.Pattern | None: ...
    @cached_property
    def pattern(self) -> str | None: ...
    @cached_property
    def native_value(self) -> str | None: ...
    def set_value(self, value: str) -> None: ...
    async def async_set_value(self, value: str) -> None: ...

@dataclass
class TextExtraStoredData(ExtraStoredData):
    native_value: str | None
    native_min: int
    native_max: int
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> TextExtraStoredData | None: ...

class RestoreText(TextEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> TextExtraStoredData: ...
    async def async_get_last_text_data(self) -> TextExtraStoredData | None: ...
