import collections
import httpx
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, IMAGE_TIMEOUT as IMAGE_TIMEOUT
from _typeshed import Incomplete
from aiohttp import web
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONTENT_TYPE_MULTIPART as CONTENT_TYPE_MULTIPART, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.typing import ConfigType as ConfigType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType, VolDictType as VolDictType
from propcache import cached_property
from typing import Final, final

_LOGGER: Incomplete
SERVICE_SNAPSHOT: Final[str]
ENTITY_ID_FORMAT: Final[Incomplete]
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Final[Incomplete]
ATTR_FILENAME: Final[str]
DEFAULT_CONTENT_TYPE: Final[str]
ENTITY_IMAGE_URL: Final[str]
TOKEN_CHANGE_INTERVAL: Final[Incomplete]
_RND: Final[Incomplete]
GET_IMAGE_TIMEOUT: Final[int]
FRAME_BOUNDARY: str
FRAME_SEPARATOR: Incomplete
LAST_FRAME_MARKER: Incomplete
IMAGE_SERVICE_SNAPSHOT: VolDictType

class ImageEntityDescription(EntityDescription, frozen_or_thawed=True): ...

@dataclass
class Image:
    content_type: str
    content: bytes

class ImageContentTypeError(HomeAssistantError): ...

def valid_image_content_type(content_type: str | None) -> str: ...
async def _async_get_image(image_entity: ImageEntity, timeout: int) -> Image: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class ImageEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    _attr_content_type: str
    _attr_image_last_updated: datetime | None
    _attr_image_url: str | None | UndefinedType
    _attr_should_poll: bool
    _attr_state: None
    _cached_image: Image | None
    _client: Incomplete
    access_tokens: collections.deque
    def __init__(self, hass: HomeAssistant, verify_ssl: bool = False) -> None: ...
    @cached_property
    def content_type(self) -> str: ...
    @property
    def entity_picture(self) -> str | None: ...
    @cached_property
    def image_last_updated(self) -> datetime | None: ...
    @cached_property
    def image_url(self) -> str | None | UndefinedType: ...
    def image(self) -> bytes | None: ...
    async def _fetch_url(self, url: str) -> httpx.Response | None: ...
    async def _async_load_image_from_url(self, url: str) -> Image | None: ...
    async def async_image(self) -> bytes | None: ...
    @property
    @final
    def state(self) -> str | None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, str | None]: ...
    @callback
    def async_update_token(self) -> None: ...

class ImageView(HomeAssistantView):
    name: str
    requires_auth: bool
    url: str
    component: Incomplete
    def __init__(self, component: EntityComponent[ImageEntity]) -> None: ...
    async def get(self, request: web.Request, entity_id: str) -> web.StreamResponse: ...
    async def handle(self, request: web.Request, image_entity: ImageEntity) -> web.StreamResponse: ...

async def async_get_still_stream(request: web.Request, image_entity: ImageEntity) -> web.StreamResponse: ...

class ImageStreamView(ImageView):
    url: str
    name: str
    async def handle(self, request: web.Request, image_entity: ImageEntity) -> web.StreamResponse: ...

async def async_handle_snapshot_service(image: ImageEntity, service_call: ServiceCall) -> None: ...
