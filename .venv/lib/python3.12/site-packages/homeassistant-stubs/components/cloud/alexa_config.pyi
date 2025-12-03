from .client import CloudClient as CloudClient
from .const import CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_FILTER as CONF_FILTER, PREF_ALEXA_REPORT_STATE as PREF_ALEXA_REPORT_STATE, PREF_ENABLE_ALEXA as PREF_ENABLE_ALEXA, PREF_SHOULD_EXPOSE as PREF_SHOULD_EXPOSE
from .prefs import ALEXA_SETTINGS_VERSION as ALEXA_SETTINGS_VERSION, CloudPreferences as CloudPreferences
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from hass_nabucasa import Cloud as Cloud
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.components.alexa import config as alexa_config
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.homeassistant.exposed_entities import async_expose_entity as async_expose_entity, async_get_assistant_settings as async_get_assistant_settings, async_listen_entity_updates as async_listen_entity_updates, async_should_expose as async_should_expose
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CLOUD_NEVER_EXPOSED_ENTITIES as CLOUD_NEVER_EXPOSED_ENTITIES
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as er, start as start
from homeassistant.helpers.entity import get_device_class as get_device_class
from homeassistant.helpers.entityfilter import EntityFilter as EntityFilter
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.setup import async_setup_component as async_setup_component
from homeassistant.util.dt import utcnow as utcnow
from typing import Any
from yarl import URL as URL

_LOGGER: Incomplete
CLOUD_ALEXA: Incomplete
SYNC_DELAY: int
SUPPORTED_DOMAINS: Incomplete
SUPPORTED_BINARY_SENSOR_DEVICE_CLASSES: Incomplete
SUPPORTED_SENSOR_DEVICE_CLASSES: Incomplete

def entity_supported(hass: HomeAssistant, entity_id: str) -> bool: ...

class CloudAlexaConfig(alexa_config.AbstractConfig):
    _config: Incomplete
    _cloud_user: Incomplete
    _prefs: Incomplete
    _cloud: Incomplete
    _token: Incomplete
    _token_valid: datetime | None
    _cur_entity_prefs: Incomplete
    _alexa_sync_unsub: Callable[[], None] | None
    _endpoint: str | URL | None
    def __init__(self, hass: HomeAssistant, config: dict, cloud_user: str, prefs: CloudPreferences, cloud: Cloud[CloudClient]) -> None: ...
    @property
    def enabled(self) -> bool: ...
    @property
    def supports_auth(self) -> bool: ...
    @property
    def should_report_state(self) -> bool: ...
    @property
    def endpoint(self) -> str | URL | None: ...
    @property
    def locale(self) -> str: ...
    @property
    def entity_config(self) -> dict[str, Any]: ...
    @callback
    def user_identifier(self) -> str: ...
    def _migrate_alexa_entity_settings_v1(self) -> None: ...
    async def async_initialize(self) -> None: ...
    def _should_expose_legacy(self, entity_id: str) -> bool: ...
    @callback
    def should_expose(self, entity_id: str) -> bool: ...
    @callback
    def async_invalidate_access_token(self) -> None: ...
    async def async_get_access_token(self) -> str | None: ...
    async def _async_prefs_updated(self, prefs: CloudPreferences) -> None: ...
    @callback
    def _async_exposed_entities_updated(self) -> None: ...
    async def _sync_prefs(self, _now: datetime) -> None: ...
    async def async_sync_entities(self) -> bool: ...
    async def _sync_helper(self, to_update: list[str], to_remove: list[str]) -> bool: ...
    async def _handle_entity_registry_updated(self, event: Event[er.EventEntityRegistryUpdatedData]) -> None: ...
