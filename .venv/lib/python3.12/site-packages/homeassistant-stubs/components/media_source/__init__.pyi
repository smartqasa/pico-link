from .const import DOMAIN as DOMAIN, MEDIA_CLASS_MAP as MEDIA_CLASS_MAP, MEDIA_MIME_TYPES as MEDIA_MIME_TYPES
from .error import MediaSourceError as MediaSourceError, Unresolvable as Unresolvable
from .models import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia
from collections.abc import Callable
from homeassistant.components import websocket_api
from homeassistant.components.media_player import BrowseMedia
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.typing import UndefinedType
from homeassistant.loader import bind_hass
from typing import Protocol

__all__ = ['DOMAIN', 'is_media_source_id', 'generate_media_source_id', 'async_browse_media', 'async_resolve_media', 'BrowseMediaSource', 'PlayMedia', 'MediaSourceItem', 'Unresolvable', 'MediaSource', 'MediaSourceError', 'MEDIA_CLASS_MAP', 'MEDIA_MIME_TYPES']

class MediaSourceProtocol(Protocol):
    async def async_get_media_source(self, hass: HomeAssistant) -> MediaSource: ...

def is_media_source_id(media_content_id: str) -> bool: ...
def generate_media_source_id(domain: str, identifier: str) -> str: ...
@bind_hass
async def async_browse_media(hass: HomeAssistant, media_content_id: str | None, *, content_filter: Callable[[BrowseMedia], bool] | None = None) -> BrowseMediaSource: ...
@bind_hass
async def async_resolve_media(hass: HomeAssistant, media_content_id: str, target_media_player: str | None | UndefinedType = ...) -> PlayMedia: ...
