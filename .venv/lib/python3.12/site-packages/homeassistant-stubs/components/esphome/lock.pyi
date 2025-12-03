from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, LockEntityState, LockInfo
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature
from homeassistant.const import ATTR_CODE as ATTR_CODE
from homeassistant.core import callback as callback
from typing import Any

class EsphomeLock(EsphomeEntity[LockInfo, LockEntityState], LockEntity):
    _attr_assumed_state: Incomplete
    _attr_supported_features: Incomplete
    _attr_code_format: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    @esphome_state_property
    def is_locked(self) -> bool | None: ...
    @property
    @esphome_state_property
    def is_locking(self) -> bool | None: ...
    @property
    @esphome_state_property
    def is_unlocking(self) -> bool | None: ...
    @property
    @esphome_state_property
    def is_jammed(self) -> bool | None: ...
    @convert_api_error_ha_error
    async def async_lock(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_unlock(self, **kwargs: Any) -> None: ...
    @convert_api_error_ha_error
    async def async_open(self, **kwargs: Any) -> None: ...

async_setup_entry: Incomplete
