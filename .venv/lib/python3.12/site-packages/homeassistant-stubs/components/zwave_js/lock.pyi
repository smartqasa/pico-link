from .const import ATTR_AUTO_RELOCK_TIME as ATTR_AUTO_RELOCK_TIME, ATTR_BLOCK_TO_BLOCK as ATTR_BLOCK_TO_BLOCK, ATTR_HOLD_AND_RELEASE_TIME as ATTR_HOLD_AND_RELEASE_TIME, ATTR_LOCK_TIMEOUT as ATTR_LOCK_TIMEOUT, ATTR_OPERATION_TYPE as ATTR_OPERATION_TYPE, ATTR_TWIST_ASSIST as ATTR_TWIST_ASSIST, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER, SERVICE_CLEAR_LOCK_USERCODE as SERVICE_CLEAR_LOCK_USERCODE, SERVICE_SET_LOCK_CONFIGURATION as SERVICE_SET_LOCK_CONFIGURATION, SERVICE_SET_LOCK_USERCODE as SERVICE_SET_LOCK_USERCODE
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockState as LockState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.const.command_class.lock import OperationType

PARALLEL_UPDATES: int
STATE_TO_ZWAVE_MAP: dict[int, dict[str, int | bool]]
UNIT16_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveLock(ZWaveBaseEntity, LockEntity):
    @property
    def is_locked(self) -> bool | None: ...
    async def _set_lock_state(self, target_state: LockState, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_set_lock_usercode(self, code_slot: int, usercode: str) -> None: ...
    async def async_clear_lock_usercode(self, code_slot: int) -> None: ...
    async def async_set_lock_configuration(self, operation_type: OperationType, lock_timeout: int | None = None, auto_relock_time: int | None = None, hold_and_release_time: int | None = None, twist_assist: bool | None = None, block_to_block: bool | None = None) -> None: ...
