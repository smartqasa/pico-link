import voluptuous as vol
from .deprecation import DeferredDeprecatedAlias as DeferredDeprecatedAlias, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import Enum
from typing import Any, Never

type GPSType = tuple[float, float]
type ConfigType = dict[str, Any]
type DiscoveryInfoType = dict[str, Any]
type ServiceDataType = dict[str, Any]
type StateType = str | int | float | None
type TemplateVarsType = Mapping[str, Any] | None
type NoEventData = Mapping[str, Never]
type VolSchemaType = vol.Schema | vol.All | vol.Any
type VolDictType = dict[str | vol.Marker, Any]
type QueryType = Any
class UndefinedType(Enum):
    _singleton = 0

UNDEFINED: Incomplete

def _deprecated_typing_helper(attr: str) -> DeferredDeprecatedAlias: ...

_DEPRECATED_ContextType: Incomplete
_DEPRECATED_EventType: Incomplete
_DEPRECATED_HomeAssistantType: Incomplete
_DEPRECATED_ServiceCallType: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
