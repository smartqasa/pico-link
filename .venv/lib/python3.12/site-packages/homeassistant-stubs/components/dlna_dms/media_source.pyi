from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, PATH_OBJECT_ID_FLAG as PATH_OBJECT_ID_FLAG, ROOT_OBJECT_ID as ROOT_OBJECT_ID, SOURCE_SEP as SOURCE_SEP
from .dms import DidlPlayMedia as DidlPlayMedia, get_domain_data as get_domain_data
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass, MediaType as MediaType
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, Unresolvable as Unresolvable
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_get_media_source(hass: HomeAssistant) -> DmsMediaSource: ...

class DmsMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> DidlPlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...

def _parse_identifier(item: MediaSourceItem) -> tuple[str | None, str | None]: ...
