import abc
from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import RingDataCoordinator as RingDataCoordinator, RingListenCoordinator as RingListenCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.update_coordinator import BaseCoordinatorEntity as BaseCoordinatorEntity, CoordinatorEntity as CoordinatorEntity
from ring_doorbell import RingDevices as RingDevices, RingGeneric
from typing import Any, Concatenate, Generic
from typing_extensions import TypeVar

RingDeviceT = TypeVar('RingDeviceT', bound=RingGeneric, default=RingGeneric)
_RingCoordinatorT = TypeVar('_RingCoordinatorT', bound=RingDataCoordinator | RingListenCoordinator)

@dataclass(slots=True)
class DeprecatedInfo:
    new_platform: Platform
    breaks_in_ha_version: str

@dataclass(frozen=True, kw_only=True)
class RingEntityDescription(EntityDescription):
    deprecated_info: DeprecatedInfo | None = ...

def exception_wrap[_RingBaseEntityT: RingBaseEntity[Any, Any], **_P, _R](async_func: Callable[Concatenate[_RingBaseEntityT, _P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[_RingBaseEntityT, _P], Coroutine[Any, Any, _R]]: ...
def refresh_after[_RingEntityT: RingEntity[Any], **_P](func: Callable[Concatenate[_RingEntityT, _P], Awaitable[None]]) -> Callable[Concatenate[_RingEntityT, _P], Coroutine[Any, Any, None]]: ...
def async_check_create_deprecated(hass: HomeAssistant, platform: Platform, unique_id: str, entity_description: RingEntityDescription) -> bool: ...

class RingBaseEntity(BaseCoordinatorEntity[_RingCoordinatorT], Generic[_RingCoordinatorT, RingDeviceT], metaclass=abc.ABCMeta):
    _attr_attribution = ATTRIBUTION
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: _RingCoordinatorT) -> None: ...

class RingEntity(RingBaseEntity[RingDataCoordinator, RingDeviceT], CoordinatorEntity):
    def _get_coordinator_data(self) -> RingDevices: ...
    _device: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
