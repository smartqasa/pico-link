from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants

DOMAIN: str

class VacuumActivity(StrEnum):
    CLEANING = 'cleaning'
    DOCKED = 'docked'
    IDLE = 'idle'
    PAUSED = 'paused'
    RETURNING = 'returning'
    ERROR = 'error'

_DEPRECATED_STATE_CLEANING: Incomplete
_DEPRECATED_STATE_DOCKED: Incomplete
_DEPRECATED_STATE_RETURNING: Incomplete
_DEPRECATED_STATE_ERROR: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
