import httpx
from .const import CONF_MJPEG_URL as CONF_MJPEG_URL, CONF_STILL_IMAGE_URL as CONF_STILL_IMAGE_URL, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import AsyncIterator
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_web as async_aiohttp_proxy_web, async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

TIMEOUT: int
BUFFER_SIZE: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_extract_image_from_mjpeg(stream: AsyncIterator[bytes]) -> bytes | None: ...

class MjpegCamera(Camera):
    _attr_name: Incomplete
    _authentication: Incomplete
    _username: Incomplete
    _password: Incomplete
    _mjpeg_url: Incomplete
    _still_image_url: Incomplete
    _auth: Incomplete
    _verify_ssl: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, name: str | None = None, mjpeg_url: str, still_image_url: str | None, authentication: str | None = None, username: str | None = None, password: str = '', verify_ssl: bool = True, unique_id: str | None = None, device_info: DeviceInfo | None = None) -> None: ...
    async def stream_source(self) -> str: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    def _get_httpx_auth(self) -> httpx.Auth: ...
    async def _async_digest_or_fallback_camera_image(self) -> bytes | None: ...
    async def _handle_async_mjpeg_digest_stream(self, request: web.Request) -> web.StreamResponse | None: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse | None: ...
