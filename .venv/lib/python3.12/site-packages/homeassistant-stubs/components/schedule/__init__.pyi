from .const import ATTR_NEXT_EVENT as ATTR_NEXT_EVENT, CONF_ALL_DAYS as CONF_ALL_DAYS, CONF_DATA as CONF_DATA, CONF_FROM as CONF_FROM, CONF_TO as CONF_TO, DOMAIN as DOMAIN, LOGGER as LOGGER, WEEKDAY_TO_CONF as WEEKDAY_TO_CONF
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, SERVICE_RELOAD as SERVICE_RELOAD, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.collection import CollectionEntity as CollectionEntity, DictStorageCollection as DictStorageCollection, DictStorageCollectionWebsocket as DictStorageCollectionWebsocket, IDManager as IDManager, SerializedStorageCollection as SerializedStorageCollection, YamlCollection as YamlCollection, sync_entity_lifecycle as sync_entity_lifecycle
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from typing import Any, Literal

STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int

def valid_schedule(schedule: list[dict[str, str]]) -> list[dict[str, str]]: ...
def deserialize_to_time(value: Any) -> Any: ...
def serialize_to_time(value: Any) -> Any: ...

BASE_SCHEMA: VolDictType
CUSTOM_DATA_SCHEMA: Incomplete
TIME_RANGE_SCHEMA: VolDictType
STORAGE_TIME_RANGE_SCHEMA: Incomplete
SCHEDULE_SCHEMA: VolDictType
STORAGE_SCHEDULE_SCHEMA: VolDictType
CONFIG_SCHEMA: Incomplete
STORAGE_SCHEMA: Incomplete
ENTITY_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class ScheduleStorageCollection(DictStorageCollection):
    SCHEMA: Incomplete
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    def _get_suggested_id(self, info: dict) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...
    async def _async_load_data(self) -> SerializedStorageCollection | None: ...

class Schedule(CollectionEntity):
    _entity_component_unrecorded_attributes: Incomplete
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_state: Literal['on', 'off']
    _config: ConfigType
    _next: datetime
    _unsub_update: Callable[[], None] | None
    _attr_capability_attributes: Incomplete
    _attr_icon: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _unrecorded_attributes: Incomplete
    _Entity__combined_unrecorded_attributes: Incomplete
    def __init__(self, config: ConfigType, editable: bool) -> None: ...
    @classmethod
    def from_storage(cls, config: ConfigType) -> Schedule: ...
    @classmethod
    def from_yaml(cls, config: ConfigType) -> Schedule: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
    @callback
    def _clean_up_listener(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update(self, _: datetime | None = None) -> None: ...
    def all_custom_data_keys(self) -> frozenset[str]: ...
