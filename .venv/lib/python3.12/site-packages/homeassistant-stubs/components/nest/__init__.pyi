import abc
from . import api as api
from .const import CONF_PROJECT_ID as CONF_PROJECT_ID, CONF_SUBSCRIBER_ID as CONF_SUBSCRIBER_ID, CONF_SUBSCRIBER_ID_IMPORTED as CONF_SUBSCRIBER_ID_IMPORTED, CONF_SUBSCRIPTION_NAME as CONF_SUBSCRIPTION_NAME, DATA_SDM as DATA_SDM, DOMAIN as DOMAIN
from .events import EVENT_NAME_MAP as EVENT_NAME_MAP, NEST_EVENT as NEST_EVENT
from .media_source import EVENT_MEDIA_API_URL_FORMAT as EVENT_MEDIA_API_URL_FORMAT, EVENT_THUMBNAIL_URL_FORMAT as EVENT_THUMBNAIL_URL_FORMAT, async_get_media_event_store as async_get_media_event_store, async_get_media_source_devices as async_get_media_source_devices, async_get_transcoder as async_get_transcoder
from .types import NestConfigEntry as NestConfigEntry, NestData as NestData
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from aiohttp import web
from collections.abc import Awaitable, Callable as Callable
from google_nest_sdm.device import Device as Device
from google_nest_sdm.event import EventMessage as EventMessage
from google_nest_sdm.event_media import Media as Media
from homeassistant.auth.permissions.const import POLICY_READ as POLICY_READ
from homeassistant.components.camera import Image as Image, img_util as img_util
from homeassistant.components.http import KEY_HASS_USER as KEY_HASS_USER
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_SENSORS as CONF_SENSORS, CONF_STRUCTURE as CONF_STRUCTURE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized
from homeassistant.helpers.entity_registry import async_entries_for_device as async_entries_for_device
from homeassistant.helpers.typing import ConfigType as ConfigType
from http import HTTPStatus

_LOGGER: Incomplete
SENSOR_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
EVENT_MEDIA_CACHE_SIZE: int
THUMBNAIL_SIZE_PX: int

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class SignalUpdateCallback:
    _hass: Incomplete
    _config_reload_cb: Incomplete
    _config_entry: Incomplete
    def __init__(self, hass: HomeAssistant, config_reload_cb: Callable[[], Awaitable[None]], config_entry: NestConfigEntry) -> None: ...
    async def async_handle_event(self, event_message: EventMessage) -> None: ...
    def _supported_traits(self, device_id: str) -> list[str]: ...

async def async_setup_entry(hass: HomeAssistant, entry: NestConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class NestEventViewBase(HomeAssistantView, ABC, metaclass=abc.ABCMeta):
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def get(self, request: web.Request, device_id: str, event_token: str) -> web.StreamResponse: ...
    @abstractmethod
    async def load_media(self, nest_device: Device, event_token: str) -> Media | None: ...
    @abstractmethod
    async def handle_media(self, media: Media) -> web.StreamResponse: ...
    def _json_error(self, message: str, status: HTTPStatus) -> web.StreamResponse: ...

class NestEventMediaView(NestEventViewBase):
    url: str
    name: str
    async def load_media(self, nest_device: Device, event_token: str) -> Media | None: ...
    async def handle_media(self, media: Media) -> web.StreamResponse: ...

class NestEventMediaThumbnailView(NestEventViewBase):
    url: str
    name: str
    _lock: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def load_media(self, nest_device: Device, event_token: str) -> Media | None: ...
    async def handle_media(self, media: Media) -> web.StreamResponse: ...
