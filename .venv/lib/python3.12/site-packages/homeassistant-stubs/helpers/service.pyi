import dataclasses
from . import area_registry as area_registry, device_registry as device_registry, entity_registry as entity_registry, floor_registry as floor_registry, label_registry as label_registry, template as template, translation as translation
from .entity import Entity as Entity
from .group import expand_entity_ids as expand_entity_ids
from .selector import TargetSelector as TargetSelector
from .typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType, VolDictType as VolDictType, VolSchemaType as VolSchemaType
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine, Iterable
from functools import cache
from homeassistant.auth.permissions.const import CAT_ENTITIES as CAT_ENTITIES, POLICY_CONTROL as POLICY_CONTROL
from homeassistant.const import ATTR_AREA_ID as ATTR_AREA_ID, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FLOOR_ID as ATTR_FLOOR_ID, ATTR_LABEL_ID as ATTR_LABEL_ID, CONF_ACTION as CONF_ACTION, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_SERVICE_DATA as CONF_SERVICE_DATA, CONF_SERVICE_DATA_TEMPLATE as CONF_SERVICE_DATA_TEMPLATE, CONF_SERVICE_TEMPLATE as CONF_SERVICE_TEMPLATE, CONF_TARGET as CONF_TARGET, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE
from homeassistant.core import Context as Context, EntityServiceResponse as EntityServiceResponse, HassJob as HassJob, HassJobType as HassJobType, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceNotSupported as ServiceNotSupported, TemplateError as TemplateError, Unauthorized as Unauthorized, UnknownUser as UnknownUser
from homeassistant.loader import Integration as Integration, async_get_integrations as async_get_integrations, bind_hass as bind_hass
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.yaml import load_yaml_dict as load_yaml_dict
from homeassistant.util.yaml.loader import JSON_TYPE as JSON_TYPE
from types import ModuleType
from typing import Any, TypeGuard, TypedDict

CONF_SERVICE_ENTITY_ID: str
_LOGGER: Incomplete
SERVICE_DESCRIPTION_CACHE: HassKey[dict[tuple[str, str], dict[str, Any] | None]]
ALL_SERVICE_DESCRIPTIONS_CACHE: HassKey[tuple[set[tuple[str, str]], dict[str, dict[str, Any]]]]

@cache
def _base_components() -> dict[str, ModuleType]: ...
def _validate_option_or_feature(option_or_feature: str, label: str) -> Any: ...
def validate_attribute_option(attribute_option: str) -> Any: ...
def validate_supported_feature(supported_feature: str) -> Any: ...

_FIELD_SCHEMA: Incomplete
_SECTION_SCHEMA: Incomplete
_SERVICE_SCHEMA: Incomplete

def starts_with_dot(key: str) -> str: ...

_SERVICES_SCHEMA: Incomplete

class ServiceParams(TypedDict):
    domain: str
    service: str
    service_data: dict[str, Any]
    target: dict | None

class ServiceTargetSelector:
    __slots__: Incomplete
    entity_ids: Incomplete
    device_ids: Incomplete
    area_ids: Incomplete
    floor_ids: Incomplete
    label_ids: Incomplete
    def __init__(self, service_call: ServiceCall) -> None: ...
    @property
    def has_any_selector(self) -> bool: ...

@dataclasses.dataclass(slots=True)
class SelectedEntities:
    referenced: set[str] = dataclasses.field(default_factory=set)
    indirectly_referenced: set[str] = dataclasses.field(default_factory=set)
    missing_devices: set[str] = dataclasses.field(default_factory=set)
    missing_areas: set[str] = dataclasses.field(default_factory=set)
    missing_floors: set[str] = dataclasses.field(default_factory=set)
    missing_labels: set[str] = dataclasses.field(default_factory=set)
    referenced_devices: set[str] = dataclasses.field(default_factory=set)
    referenced_areas: set[str] = dataclasses.field(default_factory=set)
    def log_missing(self, missing_entities: set[str]) -> None: ...

@bind_hass
def call_from_config(hass: HomeAssistant, config: ConfigType, blocking: bool = False, variables: TemplateVarsType = None, validate_config: bool = True) -> None: ...
@bind_hass
async def async_call_from_config(hass: HomeAssistant, config: ConfigType, blocking: bool = False, variables: TemplateVarsType = None, validate_config: bool = True, context: Context | None = None) -> None: ...
@callback
@bind_hass
def async_prepare_call_from_config(hass: HomeAssistant, config: ConfigType, variables: TemplateVarsType = None, validate_config: bool = False) -> ServiceParams: ...
@bind_hass
def extract_entity_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> set[str]: ...
@bind_hass
async def async_extract_entities[_EntityT: Entity](hass: HomeAssistant, entities: Iterable[_EntityT], service_call: ServiceCall, expand_group: bool = True) -> list[_EntityT]: ...
@bind_hass
async def async_extract_entity_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> set[str]: ...
def _has_match(ids: str | list[str] | None) -> TypeGuard[str | list[str]]: ...
@bind_hass
def async_extract_referenced_entity_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> SelectedEntities: ...
@bind_hass
async def async_extract_config_entry_ids(hass: HomeAssistant, service_call: ServiceCall, expand_group: bool = True) -> set[str]: ...
def _load_services_file(hass: HomeAssistant, integration: Integration) -> JSON_TYPE: ...
def _load_services_files(hass: HomeAssistant, integrations: Iterable[Integration]) -> list[JSON_TYPE]: ...
@callback
def async_get_cached_service_description(hass: HomeAssistant, domain: str, service: str) -> dict[str, Any] | None: ...
@bind_hass
async def async_get_all_descriptions(hass: HomeAssistant) -> dict[str, dict[str, Any]]: ...
@callback
def remove_entity_service_fields(call: ServiceCall) -> dict[Any, Any]: ...
@callback
@bind_hass
def async_set_service_schema(hass: HomeAssistant, domain: str, service: str, schema: dict[str, Any]) -> None: ...
def _get_permissible_entity_candidates(call: ServiceCall, entities: dict[str, Entity], entity_perms: Callable[[str, str], bool] | None, target_all_entities: bool, all_referenced: set[str] | None) -> list[Entity]: ...
@bind_hass
async def entity_service_call(hass: HomeAssistant, registered_entities: dict[str, Entity], func: str | HassJob, call: ServiceCall, required_features: Iterable[int] | None = None) -> EntityServiceResponse | None: ...
async def _handle_entity_call(hass: HomeAssistant, entity: Entity, func: str | HassJob, data: dict | ServiceCall, context: Context) -> ServiceResponse: ...
async def _async_admin_handler(hass: HomeAssistant, service_job: HassJob[[ServiceCall], Awaitable[None] | None], call: ServiceCall) -> None: ...
@bind_hass
@callback
def async_register_admin_service(hass: HomeAssistant, domain: str, service: str, service_func: Callable[[ServiceCall], Awaitable[None] | None], schema: VolSchemaType = ...) -> None: ...
@bind_hass
@callback
def verify_domain_control(hass: HomeAssistant, domain: str) -> Callable[[Callable[[ServiceCall], Any]], Callable[[ServiceCall], Any]]: ...

class ReloadServiceHelper[_T]:
    _service_func: Incomplete
    _service_running: bool
    _service_condition: Incomplete
    _pending_reload_targets: set[_T]
    _reload_targets_func: Incomplete
    def __init__(self, service_func: Callable[[ServiceCall], Coroutine[Any, Any, Any]], reload_targets_func: Callable[[ServiceCall], set[_T]]) -> None: ...
    async def execute_service(self, service_call: ServiceCall) -> None: ...

@callback
def async_register_entity_service(hass: HomeAssistant, domain: str, name: str, *, entities: dict[str, Entity], func: str | Callable[..., Any], job_type: HassJobType | None, required_features: Iterable[int] | None = None, schema: VolDictType | VolSchemaType | None, supports_response: SupportsResponse = ...) -> None: ...
