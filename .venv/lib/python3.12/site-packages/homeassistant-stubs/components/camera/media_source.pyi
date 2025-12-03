from . import Camera as Camera, _async_stream_endpoint_url as _async_stream_endpoint_url
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, StreamType as StreamType
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.components.stream import FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, HLS_PROVIDER as HLS_PROVIDER
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

async def async_get_media_source(hass: HomeAssistant) -> CameraMediaSource: ...
def _media_source_for_camera(hass: HomeAssistant, camera: Camera, content_type: str) -> BrowseMediaSource: ...

class CameraMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
