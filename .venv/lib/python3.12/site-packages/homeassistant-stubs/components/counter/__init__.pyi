from _typeshed import Incomplete
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_MAXIMUM as CONF_MAXIMUM, CONF_MINIMUM as CONF_MINIMUM, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import collection as collection
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from typing import Any, Self

_LOGGER: Incomplete
ATTR_INITIAL: str
ATTR_STEP: str
ATTR_MINIMUM: str
ATTR_MAXIMUM: str
VALUE: str
CONF_INITIAL: str
CONF_RESTORE: str
CONF_STEP: str
DEFAULT_INITIAL: int
DEFAULT_STEP: int
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
SERVICE_DECREMENT: str
SERVICE_INCREMENT: str
SERVICE_RESET: str
SERVICE_SET_VALUE: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_FIELDS: VolDictType

def _none_to_empty_dict[_T](value: _T | None) -> _T | dict[str, Any]: ...

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class CounterStorageCollection(collection.DictStorageCollection):
    CREATE_UPDATE_SCHEMA: Incomplete
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    def _get_suggested_id(self, info: dict) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...

class Counter(collection.CollectionEntity, RestoreEntity):
    _attr_should_poll: bool
    editable: bool
    _config: ConfigType
    _state: int | None
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
    def state(self) -> int | None: ...
    @property
    def extra_state_attributes(self) -> dict: ...
    @property
    def unique_id(self) -> str | None: ...
    def compute_next_state(self, state: int | None) -> int | None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def async_decrement(self) -> None: ...
    @callback
    def async_increment(self) -> None: ...
    @callback
    def async_reset(self) -> None: ...
    @callback
    def async_set_value(self, value: int) -> None: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
