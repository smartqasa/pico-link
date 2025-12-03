import re
from .const import DOMAIN as DOMAIN, LockState as LockState
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_CODE_FORMAT as ATTR_CODE_FORMAT, SERVICE_LOCK as SERVICE_LOCK, SERVICE_OPEN as SERVICE_OPEN, SERVICE_UNLOCK as SERVICE_UNLOCK, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING, _DEPRECATED_STATE_JAMMED as _DEPRECATED_STATE_JAMMED, _DEPRECATED_STATE_LOCKED as _DEPRECATED_STATE_LOCKED, _DEPRECATED_STATE_LOCKING as _DEPRECATED_STATE_LOCKING, _DEPRECATED_STATE_UNLOCKED as _DEPRECATED_STATE_UNLOCKED, _DEPRECATED_STATE_UNLOCKING as _DEPRECATED_STATE_UNLOCKING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.deprecation import all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any, final

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[LockEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
ATTR_CHANGED_BY: str
CONF_DEFAULT_CODE: str
MIN_TIME_BETWEEN_SCANS: Incomplete
LOCK_SERVICE_SCHEMA: Incomplete

class LockEntityFeature(IntFlag):
    OPEN = 1

PROP_TO_ATTR: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class LockEntityDescription(EntityDescription, frozen_or_thawed=True): ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class LockEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: LockEntityDescription
    _attr_changed_by: str | None
    _attr_code_format: str | None
    _attr_is_locked: bool | None
    _attr_is_locking: bool | None
    _attr_is_open: bool | None
    _attr_is_opening: bool | None
    _attr_is_unlocking: bool | None
    _attr_is_jammed: bool | None
    _attr_state: None
    _attr_supported_features: LockEntityFeature
    _lock_option_default_code: str
    __code_format_cmp: re.Pattern[str] | None
    @final
    @callback
    def add_default_code(self, data: dict[Any, Any]) -> dict[Any, Any]: ...
    @cached_property
    def changed_by(self) -> str | None: ...
    @cached_property
    def code_format(self) -> str | None: ...
    @property
    @final
    def code_format_cmp(self) -> re.Pattern[str] | None: ...
    @cached_property
    def is_locked(self) -> bool | None: ...
    @cached_property
    def is_locking(self) -> bool | None: ...
    @cached_property
    def is_unlocking(self) -> bool | None: ...
    @cached_property
    def is_open(self) -> bool | None: ...
    @cached_property
    def is_opening(self) -> bool | None: ...
    @cached_property
    def is_jammed(self) -> bool | None: ...
    @final
    async def async_handle_lock_service(self, **kwargs: Any) -> None: ...
    def lock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    @final
    async def async_handle_unlock_service(self, **kwargs: Any) -> None: ...
    def unlock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    @final
    async def async_handle_open_service(self, **kwargs: Any) -> None: ...
    def open(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, StateType]: ...
    @final
    @property
    def state(self) -> str | None: ...
    @cached_property
    def supported_features(self) -> LockEntityFeature: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @callback
    def async_registry_entry_updated(self) -> None: ...
    @callback
    def _async_read_entity_options(self) -> None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
