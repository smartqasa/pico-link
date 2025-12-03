from _typeshed import Incomplete
from homeassistant.components.select import ATTR_CYCLE as ATTR_CYCLE, ATTR_OPTION as ATTR_OPTION, ATTR_OPTIONS as ATTR_OPTIONS, SERVICE_SELECT_FIRST as SERVICE_SELECT_FIRST, SERVICE_SELECT_LAST as SERVICE_SELECT_LAST, SERVICE_SELECT_NEXT as SERVICE_SELECT_NEXT, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION, SERVICE_SELECT_PREVIOUS as SERVICE_SELECT_PREVIOUS, SelectEntity as SelectEntity
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import collection as collection
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from typing import Any, Self

_LOGGER: Incomplete
DOMAIN: str
CONF_INITIAL: str
CONF_OPTIONS: str
SERVICE_SET_OPTIONS: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int

def _unique(options: Any) -> Any: ...

STORAGE_FIELDS: VolDictType

def _remove_duplicates(options: list[str], name: str | None) -> list[str]: ...
def _cv_input_select(cfg: dict[str, Any]) -> dict[str, Any]: ...

CONFIG_SCHEMA: Incomplete
RELOAD_SERVICE_SCHEMA: Incomplete

class InputSelectStore(Store):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class InputSelectStorageCollection(collection.DictStorageCollection):
    CREATE_UPDATE_SCHEMA: Incomplete
    async def _process_create_data(self, data: dict[str, Any]) -> dict[str, Any]: ...
    @callback
    def _get_suggested_id(self, info: dict[str, Any]) -> str: ...
    async def _update_data(self, item: dict[str, Any], update_data: dict[str, Any]) -> dict[str, Any]: ...

class InputSelect(collection.CollectionEntity, SelectEntity, RestoreEntity):
    _entity_component_unrecorded_attributes: Incomplete
    _unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    editable: bool
    _attr_current_option: Incomplete
    _attr_icon: Incomplete
    _attr_name: Incomplete
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    @classmethod
    def from_storage(cls, config: ConfigType) -> Self: ...
    @classmethod
    def from_yaml(cls, config: ConfigType) -> Self: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
    async def async_select_option(self, option: str) -> None: ...
    async def async_set_options(self, options: list[str]) -> None: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
