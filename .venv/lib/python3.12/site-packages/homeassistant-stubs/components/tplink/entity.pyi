import abc
from . import get_device_name as get_device_name, legacy_device_id as legacy_device_id
from .const import ATTR_CURRENT_A as ATTR_CURRENT_A, ATTR_CURRENT_POWER_W as ATTR_CURRENT_POWER_W, ATTR_TODAY_ENERGY_KWH as ATTR_TODAY_ENERGY_KWH, ATTR_TOTAL_ENERGY_KWH as ATTR_TOTAL_ENERGY_KWH, DOMAIN as DOMAIN, PRIMARY_STATE_ID as PRIMARY_STATE_ID
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .deprecate import DeprecatedInfo as DeprecatedInfo, async_check_create_deprecated as async_check_create_deprecated
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable as Callable, Coroutine, Mapping
from dataclasses import dataclass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from kasa import Device, Feature
from typing import Any, Concatenate

_LOGGER: Incomplete
FEATURE_CATEGORY_TO_ENTITY_CATEGORY: Incomplete
DEVICETYPES_WITH_SPECIALIZED_PLATFORMS: Incomplete
FEATURES_ALLOW_LIST: Incomplete
EXCLUDED_FEATURES: Incomplete
LEGACY_KEY_MAPPING: Incomplete

@dataclass(frozen=True, kw_only=True)
class TPLinkFeatureEntityDescription(EntityDescription):
    deprecated_info: DeprecatedInfo | None = ...
    available_fn: Callable[[Device], bool] = ...

@dataclass(frozen=True, kw_only=True)
class TPLinkModuleEntityDescription(EntityDescription):
    deprecated_info: DeprecatedInfo | None = ...
    available_fn: Callable[[Device], bool] = ...

def async_refresh_after[_T: CoordinatedTPLinkEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

class CoordinatedTPLinkEntity(CoordinatorEntity[TPLinkDataUpdateCoordinator], ABC, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _device: Device
    _feature: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature: Feature | None = None, parent: Device | None = None) -> None: ...
    def _get_unique_id(self) -> str: ...
    @abstractmethod
    @callback
    def _async_update_attrs(self) -> bool: ...
    _attr_available: bool
    @callback
    def _async_call_update_attrs(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...

class CoordinatedTPLinkFeatureEntity(CoordinatedTPLinkEntity, ABC, metaclass=abc.ABCMeta):
    entity_description: TPLinkFeatureEntityDescription
    _feature: Feature
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature: Feature, description: TPLinkFeatureEntityDescription, parent: Device | None = None) -> None: ...
    def _get_unique_id(self) -> str: ...
    @staticmethod
    def _get_feature_unique_id(device: Device, entity_description: TPLinkFeatureEntityDescription) -> str: ...
    @classmethod
    def _category_for_feature(cls, feature: Feature | None) -> EntityCategory | None: ...
    @classmethod
    def _description_for_feature[_D: EntityDescription](cls, feature: Feature, descriptions: Mapping[str, _D], *, device: Device, parent: Device | None = None) -> _D | None: ...
    @classmethod
    def _entities_for_device[_E: CoordinatedTPLinkFeatureEntity, _D: TPLinkFeatureEntityDescription](cls, hass: HomeAssistant, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature_type: Feature.Type, entity_class: type[_E], descriptions: Mapping[str, _D], parent: Device | None = None) -> list[_E]: ...
    @classmethod
    def entities_for_device_and_its_children[_E: CoordinatedTPLinkFeatureEntity, _D: TPLinkFeatureEntityDescription](cls, hass: HomeAssistant, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature_type: Feature.Type, entity_class: type[_E], descriptions: Mapping[str, _D], child_coordinators: list[TPLinkDataUpdateCoordinator] | None = None) -> list[_E]: ...
