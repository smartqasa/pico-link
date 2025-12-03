from .accessories import TYPES as TYPES
from .const import CHAR_LOCK_CURRENT_STATE as CHAR_LOCK_CURRENT_STATE, CHAR_LOCK_TARGET_STATE as CHAR_LOCK_TARGET_STATE, SERV_LOCK as SERV_LOCK
from .doorbell import HomeDoorbellAccessory as HomeDoorbellAccessory
from _typeshed import Incomplete
from homeassistant.components.lock import LockState as LockState
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import State as State, callback as callback
from typing import Any

_LOGGER: Incomplete
HASS_TO_HOMEKIT_CURRENT: Incomplete
HASS_TO_HOMEKIT_TARGET: Incomplete
VALID_TARGET_STATES: Incomplete
HOMEKIT_TO_HASS: Incomplete
STATE_TO_SERVICE: Incomplete

class Lock(HomeDoorbellAccessory):
    _code: Incomplete
    char_current_state: Incomplete
    char_target_state: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def set_state(self, value: int) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...
