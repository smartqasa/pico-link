import enum
from . import auth as auth
from .components.http import ApiConfig as ApiConfig
from .const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_HIDDEN as ATTR_HIDDEN, BASE_PLATFORMS as BASE_PLATFORMS, CONF_ALLOWLIST_EXTERNAL_DIRS as CONF_ALLOWLIST_EXTERNAL_DIRS, CONF_ALLOWLIST_EXTERNAL_URLS as CONF_ALLOWLIST_EXTERNAL_URLS, CONF_AUTH_MFA_MODULES as CONF_AUTH_MFA_MODULES, CONF_AUTH_PROVIDERS as CONF_AUTH_PROVIDERS, CONF_COUNTRY as CONF_COUNTRY, CONF_CURRENCY as CONF_CURRENCY, CONF_CUSTOMIZE as CONF_CUSTOMIZE, CONF_CUSTOMIZE_DOMAIN as CONF_CUSTOMIZE_DOMAIN, CONF_CUSTOMIZE_GLOB as CONF_CUSTOMIZE_GLOB, CONF_DEBUG as CONF_DEBUG, CONF_ELEVATION as CONF_ELEVATION, CONF_EXTERNAL_URL as CONF_EXTERNAL_URL, CONF_ID as CONF_ID, CONF_INTERNAL_URL as CONF_INTERNAL_URL, CONF_LANGUAGE as CONF_LANGUAGE, CONF_LATITUDE as CONF_LATITUDE, CONF_LEGACY_TEMPLATES as CONF_LEGACY_TEMPLATES, CONF_LONGITUDE as CONF_LONGITUDE, CONF_MEDIA_DIRS as CONF_MEDIA_DIRS, CONF_NAME as CONF_NAME, CONF_PACKAGES as CONF_PACKAGES, CONF_RADIUS as CONF_RADIUS, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_TIME_ZONE as CONF_TIME_ZONE, CONF_TYPE as CONF_TYPE, CONF_UNIT_SYSTEM as CONF_UNIT_SYSTEM, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, LEGACY_CONF_WHITELIST_EXTERNAL_DIRS as LEGACY_CONF_WHITELIST_EXTERNAL_DIRS, UnitOfLength as UnitOfLength, __version__ as __version__
from .core import HomeAssistant as HomeAssistant
from .generated.currencies import HISTORIC_CURRENCIES as HISTORIC_CURRENCIES
from .helpers.entity_values import EntityValues as EntityValues
from .helpers.frame import ReportBehavior as ReportBehavior, report_usage as report_usage
from .helpers.storage import Store as Store
from .helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from .util import location as location
from .util.hass_dict import HassKey as HassKey
from .util.package import is_docker_env as is_docker_env
from .util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM, UnitSystem as UnitSystem, _CONF_UNIT_SYSTEM_IMPERIAL as _CONF_UNIT_SYSTEM_IMPERIAL, _CONF_UNIT_SYSTEM_METRIC as _CONF_UNIT_SYSTEM_METRIC, _CONF_UNIT_SYSTEM_US_CUSTOMARY as _CONF_UNIT_SYSTEM_US_CUSTOMARY, get_unit_system as get_unit_system
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Final

_LOGGER: Incomplete
DATA_CUSTOMIZE: HassKey[EntityValues]
CONF_CREDENTIAL: Final[str]
CONF_ICE_SERVERS: Final[str]
CONF_WEBRTC: Final[str]
CORE_STORAGE_KEY: str
CORE_STORAGE_VERSION: int
CORE_STORAGE_MINOR_VERSION: int

class ConfigSource(enum.StrEnum):
    DEFAULT = 'default'
    DISCOVERED = 'discovered'
    STORAGE = 'storage'
    YAML = 'yaml'

def _no_duplicate_auth_provider(configs: Sequence[dict[str, Any]]) -> Sequence[dict[str, Any]]: ...
def _no_duplicate_auth_mfa_module(configs: Sequence[dict[str, Any]]) -> Sequence[dict[str, Any]]: ...
def _filter_bad_internal_external_urls(conf: dict) -> dict: ...

_PACKAGES_CONFIG_SCHEMA: Incomplete
_PACKAGE_DEFINITION_SCHEMA: Incomplete
_CUSTOMIZE_DICT_SCHEMA: Incomplete
_CUSTOMIZE_CONFIG_SCHEMA: Incomplete

def _raise_issue_if_imperial_unit_system(hass: HomeAssistant, config: dict[str, Any]) -> dict[str, Any]: ...
def _raise_issue_if_historic_currency(hass: HomeAssistant, currency: str) -> None: ...
def _raise_issue_if_no_country(hass: HomeAssistant, country: str | None) -> None: ...
def _validate_currency(data: Any) -> Any: ...
def _validate_stun_or_turn_url(value: Any) -> str: ...

CORE_CONFIG_SCHEMA: Incomplete

async def async_process_ha_core_config(hass: HomeAssistant, config: dict) -> None: ...

class _ComponentSet(set[str]):
    _top_level_components: Incomplete
    _all_components: Incomplete
    def __init__(self, top_level_components: set[str], all_components: set[str]) -> None: ...
    def add(self, component: str) -> None: ...
    def remove(self, component: str) -> None: ...
    def discard(self, component: str) -> None: ...

class Config:
    _store: Config._ConfigStore
    hass: Incomplete
    latitude: float
    longitude: float
    elevation: int
    radius: int
    debug: bool
    location_name: str
    time_zone: str
    units: UnitSystem
    internal_url: str | None
    external_url: str | None
    currency: str
    country: str | None
    language: str
    config_source: ConfigSource
    skip_pip: bool
    skip_pip_packages: list[str]
    top_level_components: set[str]
    all_components: set[str]
    components: _ComponentSet
    api: ApiConfig | None
    config_dir: str
    allowlist_external_dirs: set[str]
    allowlist_external_urls: set[str]
    media_dirs: dict[str, str]
    recovery_mode: bool
    legacy_templates: bool
    safe_mode: bool
    webrtc: Incomplete
    def __init__(self, hass: HomeAssistant, config_dir: str) -> None: ...
    def async_initialize(self) -> None: ...
    def distance(self, lat: float, lon: float) -> float | None: ...
    def path(self, *path: str) -> str: ...
    def is_allowed_external_url(self, url: str) -> bool: ...
    def is_allowed_path(self, path: str) -> bool: ...
    def as_dict(self) -> dict[str, Any]: ...
    async def async_set_time_zone(self, time_zone_str: str) -> None: ...
    def set_time_zone(self, time_zone_str: str) -> None: ...
    async def _async_update(self, *, country: str | UndefinedType | None = ..., currency: str | None = None, elevation: int | None = None, external_url: str | UndefinedType | None = ..., internal_url: str | UndefinedType | None = ..., language: str | None = None, latitude: float | None = None, location_name: str | None = None, longitude: float | None = None, radius: int | None = None, source: ConfigSource, time_zone: str | None = None, unit_system: str | None = None) -> None: ...
    async def async_update(self, **kwargs: Any) -> None: ...
    async def async_load(self) -> None: ...
    async def _async_store(self) -> None: ...
    class _ConfigStore(Store[dict[str, Any]]):
        _original_unit_system: str | None
        def __init__(self, hass: HomeAssistant) -> None: ...
        async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...
        async def async_save(self, data: dict[str, Any]) -> None: ...
