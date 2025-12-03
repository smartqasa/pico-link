from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import collection as collection
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from typing import Any, Self

_LOGGER: Incomplete
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
DEFAULT_DURATION: int
DEFAULT_RESTORE: bool
ATTR_DURATION: str
ATTR_REMAINING: str
ATTR_FINISHES_AT: str
ATTR_RESTORE: str
ATTR_FINISHED_AT: str
CONF_DURATION: str
CONF_RESTORE: str
STATUS_IDLE: str
STATUS_ACTIVE: str
STATUS_PAUSED: str
EVENT_TIMER_FINISHED: str
EVENT_TIMER_CANCELLED: str
EVENT_TIMER_CHANGED: str
EVENT_TIMER_STARTED: str
EVENT_TIMER_RESTARTED: str
EVENT_TIMER_PAUSED: str
SERVICE_START: str
SERVICE_PAUSE: str
SERVICE_CANCEL: str
SERVICE_CHANGE: str
SERVICE_FINISH: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_FIELDS: VolDictType

def _format_timedelta(delta: timedelta) -> str: ...
def _none_to_empty_dict[_T](value: _T | None) -> _T | dict[Any, Any]: ...

CONFIG_SCHEMA: Incomplete
RELOAD_SERVICE_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class TimerStorageCollection(collection.DictStorageCollection):
    CREATE_UPDATE_SCHEMA: Incomplete
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    def _get_suggested_id(self, info: dict) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...

class Timer(collection.CollectionEntity, RestoreEntity):
    editable: bool
    _config: dict
    _state: str
    _configured_duration: Incomplete
    _running_duration: timedelta
    _remaining: timedelta | None
    _end: datetime | None
    _listener: Callable[[], None] | None
    _restore: bool
    _attr_should_poll: bool
    _attr_force_update: bool
    def __init__(self, config: ConfigType) -> None: ...
    @classmethod
    def from_storage(cls, config: ConfigType) -> Self: ...
    @classmethod
    def from_yaml(cls, config: ConfigType) -> Self: ...
    @property
    def name(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def state(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def unique_id(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_start(self, duration: timedelta | None = None) -> None: ...
    @callback
    def async_change(self, duration: timedelta) -> None: ...
    @callback
    def async_pause(self) -> None: ...
    @callback
    def async_cancel(self) -> None: ...
    @callback
    def async_finish(self) -> None: ...
    @callback
    def _async_finished(self, time: datetime) -> None: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
