from .const import ATTR_EVENT_ID as ATTR_EVENT_ID, ATTR_EVENT_SCORE as ATTR_EVENT_SCORE, DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Sequence
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from typing import Any, Generic, TypeVar
from uiprotect.data import Event as Event, ModelType, NVR, ProtectAdoptableDeviceModel, SmartDetectObjectType as SmartDetectObjectType

_LOGGER: Incomplete
T = TypeVar('T', bound=ProtectAdoptableDeviceModel | NVR)

class PermRequired(int, Enum):
    NO_WRITE = 1
    WRITE = 2
    DELETE = 3

@callback
def _async_device_entities(data: ProtectData, klass: type[BaseProtectEntity], model_type: ModelType, descs: Sequence[ProtectEntityDescription], unadopted_descs: Sequence[ProtectEntityDescription] | None = None, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[BaseProtectEntity]: ...

_ALL_MODEL_TYPES: Incomplete

@callback
def _combine_model_descs(model_type: ModelType, model_descriptions: dict[ModelType, Sequence[ProtectEntityDescription]] | None, all_descs: Sequence[ProtectEntityDescription] | None) -> list[ProtectEntityDescription]: ...
@callback
def async_all_device_entities(data: ProtectData, klass: type[BaseProtectEntity], model_descriptions: dict[ModelType, Sequence[ProtectEntityDescription]] | None = None, all_descs: Sequence[ProtectEntityDescription] | None = None, unadopted_descs: list[ProtectEntityDescription] | None = None, ufp_device: ProtectAdoptableDeviceModel | None = None) -> list[BaseProtectEntity]: ...

class BaseProtectEntity(Entity):
    device: ProtectDeviceType
    _attr_should_poll: bool
    _attr_attribution = DEFAULT_ATTRIBUTION
    _state_attrs: tuple[str, ...]
    _attr_has_entity_name: bool
    _async_get_ufp_enabled: Callable[[ProtectAdoptableDeviceModel], bool] | None
    data: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    entity_description: Incomplete
    _state_getters: Incomplete
    def __init__(self, data: ProtectData, device: ProtectDeviceType, description: EntityDescription | None = None) -> None: ...
    async def async_update(self) -> None: ...
    @callback
    def _async_set_device_info(self) -> None: ...
    _attr_available: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    @callback
    def _async_updated_event(self, device: ProtectDeviceType) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class ProtectIsOnEntity(BaseProtectEntity):
    _state_attrs: tuple[str, ...]
    _attr_is_on: bool | None
    entity_description: ProtectEntityDescription
    def _async_update_device_from_protect(self, device: ProtectAdoptableDeviceModel | NVR) -> None: ...

class ProtectDeviceEntity(BaseProtectEntity):
    _attr_device_info: Incomplete
    @callback
    def _async_set_device_info(self) -> None: ...

class ProtectNVREntity(BaseProtectEntity):
    device: NVR
    _attr_device_info: Incomplete
    @callback
    def _async_set_device_info(self) -> None: ...

class EventEntityMixin(ProtectDeviceEntity):
    entity_description: ProtectEventMixin
    _unrecorded_attributes: Incomplete
    _event: Event | None
    _event_end: datetime | None
    @callback
    def _set_event_done(self) -> None: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def _set_event_attrs(self, event: Event) -> None: ...
    @callback
    def _async_event_with_immediate_end(self) -> None: ...
    @callback
    def _event_already_ended(self, prev_event: Event | None, prev_event_end: datetime | None) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class ProtectEntityDescription(EntityDescription, Generic[T]):
    ufp_required_field: str | None = ...
    ufp_value: str | None = ...
    ufp_value_fn: Callable[[T], Any] | None = ...
    ufp_enabled: str | None = ...
    ufp_perm: PermRequired | None = ...
    has_required: Callable[[T], bool] = ...
    get_ufp_enabled: Callable[[T], bool] | None = ...
    def get_ufp_value(self, obj: T) -> Any: ...
    def __post_init__(self) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ProtectEventMixin(ProtectEntityDescription[T]):
    ufp_event_obj: str | None = ...
    ufp_obj_type: SmartDetectObjectType | None = ...
    def get_event_obj(self, obj: T) -> Event | None: ...
    def has_matching_smart(self, event: Event) -> bool: ...
    def __post_init__(self) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ProtectSetableKeysMixin(ProtectEntityDescription[T]):
    ufp_set_method: str | None = ...
    ufp_set_method_fn: Callable[[T, Any], Coroutine[Any, Any, None]] | None = ...
    async def ufp_set(self, obj: T, value: Any) -> None: ...
