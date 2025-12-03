from .const import ATTR_PASSIVE as ATTR_PASSIVE, ATTR_RADIUS as ATTR_RADIUS, CONF_PASSIVE as CONF_PASSIVE, DOMAIN as DOMAIN, HOME_ZONE as HOME_ZONE
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_PERSONS as ATTR_PERSONS, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, CONF_RADIUS as CONF_RADIUS, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, SERVICE_RELOAD as SERVICE_RELOAD, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback
from homeassistant.helpers import collection as collection, entity_component as entity_component, event as event, service as service, storage as storage
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.location import distance as distance
from typing import Any, Self

_LOGGER: Incomplete
DEFAULT_PASSIVE: bool
DEFAULT_RADIUS: int
ENTITY_ID_FORMAT: str
ENTITY_ID_HOME: Incomplete
ICON_HOME: str
ICON_IMPORT: str
CREATE_FIELDS: VolDictType
UPDATE_FIELDS: VolDictType

def empty_value(value: Any) -> Any: ...

CONFIG_SCHEMA: Incomplete
RELOAD_SERVICE_SCHEMA: Incomplete
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
ENTITY_ID_SORTER: Incomplete
ZONE_ENTITY_IDS: str

@bind_hass
def async_active_zone(hass: HomeAssistant, latitude: float, longitude: float, radius: int = 0) -> State | None: ...
@callback
def async_setup_track_zone_entity_ids(hass: HomeAssistant) -> None: ...
def in_zone(zone: State, latitude: float, longitude: float, radius: float = 0) -> bool: ...

class ZoneStorageCollection(collection.DictStorageCollection):
    CREATE_SCHEMA: Incomplete
    UPDATE_SCHEMA: Incomplete
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    def _get_suggested_id(self, info: dict) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _home_conf(hass: HomeAssistant) -> dict: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...

class Zone(collection.CollectionEntity):
    editable: bool
    _attr_should_poll: bool
    _config: Incomplete
    _attrs: dict | None
    _remove_listener: Callable[[], None] | None
    _persons_in_zone: set[str]
    def __init__(self, config: ConfigType) -> None: ...
    _attr_name: Incomplete
    _case_folded_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_icon: Incomplete
    def _set_attrs_from_config(self) -> None: ...
    @classmethod
    def from_storage(cls, config: ConfigType) -> Self: ...
    @classmethod
    def from_yaml(cls, config: ConfigType) -> Self: ...
    @property
    def state(self) -> int: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
    @callback
    def _person_state_change_listener(self, evt: Event[EventStateChangedData]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def _generate_attrs(self) -> None: ...
    @callback
    def _state_is_in_zone(self, state: State | None) -> bool: ...
