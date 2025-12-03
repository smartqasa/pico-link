from _typeshed import Incomplete
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, ATTR_MODE as ATTR_MODE, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import collection as collection
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from typing import Any, Self

_LOGGER: Incomplete
DOMAIN: str
CONF_INITIAL: str
CONF_MIN: str
CONF_MIN_VALUE: int
CONF_MAX: str
CONF_MAX_VALUE: int
CONF_PATTERN: str
CONF_VALUE: str
MODE_TEXT: str
MODE_PASSWORD: str
ATTR_VALUE = CONF_VALUE
ATTR_MIN: str
ATTR_MAX: str
ATTR_PATTERN = CONF_PATTERN
SERVICE_SET_VALUE: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_FIELDS: VolDictType

def _cv_input_text(config: dict[str, Any]) -> dict[str, Any]: ...

CONFIG_SCHEMA: Incomplete
RELOAD_SERVICE_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class InputTextStorageCollection(collection.DictStorageCollection):
    CREATE_UPDATE_SCHEMA: Incomplete
    async def _process_create_data(self, data: dict[str, Any]) -> dict[str, Any]: ...
    @callback
    def _get_suggested_id(self, info: dict[str, Any]) -> str: ...
    async def _update_data(self, item: dict[str, Any], update_data: dict[str, Any]) -> dict[str, Any]: ...

class InputText(collection.CollectionEntity, RestoreEntity):
    _unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    _current_value: str | None
    editable: bool
    _config: Incomplete
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
    def _maximum(self) -> int: ...
    @property
    def _minimum(self) -> int: ...
    @property
    def state(self) -> str | None: ...
    @property
    def unit_of_measurement(self) -> str | None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_value(self, value: str) -> None: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
