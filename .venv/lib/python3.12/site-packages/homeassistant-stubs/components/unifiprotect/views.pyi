from .data import ProtectData as ProtectData, async_get_data_for_entry_id as async_get_data_for_entry_id, async_get_data_for_nvr_id as async_get_data_for_nvr_id
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from http import HTTPStatus
from typing import Any
from uiprotect.data import Camera, Event as Event

_LOGGER: Incomplete

@callback
def async_generate_thumbnail_url(event_id: str, nvr_id: str, width: int | None = None, height: int | None = None) -> str: ...
@callback
def async_generate_event_video_url(event: Event) -> str: ...
@callback
def async_generate_proxy_event_video_url(nvr_id: str, event_id: str) -> str: ...
@callback
def _client_error(message: Any, code: HTTPStatus) -> web.Response: ...
@callback
def _400(message: Any) -> web.Response: ...
@callback
def _403(message: Any) -> web.Response: ...
@callback
def _404(message: Any) -> web.Response: ...
@callback
def _validate_event(event: Event) -> None: ...

class ProtectProxyView(HomeAssistantView):
    requires_auth: bool
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def _get_data_or_404(self, nvr_id_or_entry_id: str) -> ProtectData | web.Response: ...
    @callback
    def _async_get_camera(self, data: ProtectData, camera_id: str) -> Camera | None: ...

class ThumbnailProxyView(ProtectProxyView):
    url: str
    name: str
    async def get(self, request: web.Request, nvr_id: str, event_id: str) -> web.Response: ...

class VideoProxyView(ProtectProxyView):
    url: str
    name: str
    async def get(self, request: web.Request, nvr_id: str, camera_id: str, start: str, end: str) -> web.StreamResponse: ...

class VideoEventProxyView(ProtectProxyView):
    url: str
    name: str
    async def get(self, request: web.Request, nvr_id: str, event_id: str) -> web.StreamResponse: ...
