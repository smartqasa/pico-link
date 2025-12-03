from .const import DEFAULT_NAME as DEFAULT_NAME, DEVICE_ID as DEVICE_ID, DOMAIN as DOMAIN, EVENT_TAG_SCANNED as EVENT_TAG_SCANNED, LOGGER as LOGGER, TAG_ID as TAG_ID
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ID as CONF_ID, CONF_NAME as CONF_NAME
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import collection as collection, entity_registry as er
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from homeassistant.util import slugify as slugify
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, final

_LOGGER: Incomplete
LAST_SCANNED: str
LAST_SCANNED_BY_DEVICE_ID: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int
TAG_DATA: HassKey[TagStorageCollection]
CREATE_FIELDS: VolDictType
UPDATE_FIELDS: VolDictType
CONFIG_SCHEMA: Incomplete

class TagIDExistsError(HomeAssistantError):
    item_id: Incomplete
    def __init__(self, item_id: str) -> None: ...

class TagIDManager(collection.IDManager):
    def generate_id(self, suggestion: str) -> str: ...

def _create_entry(entity_registry: er.EntityRegistry, tag_id: str, name: str | None) -> er.RegistryEntry: ...

class TagStore(Store[collection.SerializedStorageCollection]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> dict: ...

class TagStorageCollection(collection.DictStorageCollection):
    CREATE_SCHEMA: Incomplete
    UPDATE_SCHEMA: Incomplete
    entity_registry: Incomplete
    def __init__(self, store: TagStore, id_manager: collection.IDManager | None = None) -> None: ...
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    def _get_suggested_id(self, info: dict[str, str]) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...
    def _serialize_item(self, item_id: str, item: dict) -> dict: ...

class TagDictStorageCollectionWebsocket(collection.StorageCollectionWebsocket[TagStorageCollection]):
    entity_registry: Incomplete
    def __init__(self, storage_collection: TagStorageCollection, api_prefix: str, model_name: str, create_schema: VolDictType, update_schema: VolDictType) -> None: ...
    @callback
    def ws_list_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_scan_tag(hass: HomeAssistant, tag_id: str, device_id: str | None, context: Context | None = None) -> None: ...

class TagEntity(Entity):
    _unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    _entity_update_handlers: Incomplete
    _attr_name: Incomplete
    _tag_id: Incomplete
    _attr_unique_id: Incomplete
    _last_device_id: str | None
    _last_scanned: Incomplete
    def __init__(self, entity_update_handlers: dict[str, Callable[[str | None, str | None], None]], name: str, tag_id: str, last_scanned: str | None, device_id: str | None) -> None: ...
    @callback
    def async_handle_event(self, device_id: str | None, last_scanned: str | None) -> None: ...
    @property
    @final
    def state(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
