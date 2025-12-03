from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import Iterable
from enum import StrEnum
from homeassistant.components import automation as automation, group as group, person as person, script as script, websocket_api as websocket_api
from homeassistant.components.homeassistant import scene as scene
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers import area_registry as ar, device_registry as dr, entity_registry as er
from homeassistant.helpers.entity import EntityInfo as EntityInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DOMAIN: str
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

class ItemType(StrEnum):
    AREA = 'area'
    AUTOMATION = 'automation'
    AUTOMATION_BLUEPRINT = 'automation_blueprint'
    CONFIG_ENTRY = 'config_entry'
    DEVICE = 'device'
    ENTITY = 'entity'
    FLOOR = 'floor'
    GROUP = 'group'
    INTEGRATION = 'integration'
    LABEL = 'label'
    PERSON = 'person'
    SCENE = 'scene'
    SCRIPT = 'script'
    SCRIPT_BLUEPRINT = 'script_blueprint'

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def websocket_search_related(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

class Searcher:
    EXIST_AS_ENTITY: Incomplete
    hass: Incomplete
    _area_registry: Incomplete
    _device_registry: Incomplete
    _entity_registry: Incomplete
    _entity_sources: Incomplete
    results: defaultdict[ItemType, set[str]]
    def __init__(self, hass: HomeAssistant, entity_sources: dict[str, EntityInfo]) -> None: ...
    @callback
    def async_search(self, item_type: ItemType, item_id: str) -> dict[str, set[str]]: ...
    @callback
    def _add(self, item_type: ItemType, item_id: str | Iterable[str] | None) -> None: ...
    @callback
    def _async_search_area(self, area_id: str, *, entry_point: bool = True) -> None: ...
    @callback
    def _async_search_automation(self, automation_entity_id: str) -> None: ...
    @callback
    def _async_search_automation_blueprint(self, blueprint_path: str) -> None: ...
    @callback
    def _async_search_config_entry(self, config_entry_id: str) -> None: ...
    @callback
    def _async_search_device(self, device_id: str, *, entry_point: bool = True) -> None: ...
    @callback
    def _async_search_entity(self, entity_id: str, *, entry_point: bool = True) -> None: ...
    @callback
    def _async_search_floor(self, floor_id: str) -> None: ...
    @callback
    def _async_search_group(self, group_entity_id: str) -> None: ...
    @callback
    def _async_search_label(self, label_id: str) -> None: ...
    @callback
    def _async_search_person(self, person_entity_id: str) -> None: ...
    @callback
    def _async_search_scene(self, scene_entity_id: str) -> None: ...
    @callback
    def _async_search_script(self, script_entity_id: str, *, entry_point: bool = True) -> None: ...
    @callback
    def _async_search_script_blueprint(self, blueprint_path: str) -> None: ...
    @callback
    def _async_resolve_up_device(self, device_id: str) -> dr.DeviceEntry | None: ...
    @callback
    def _async_resolve_up_entity(self, entity_id: str) -> er.RegistryEntry | None: ...
    @callback
    def _async_resolve_up_area(self, area_id: str) -> ar.AreaEntry | None: ...
