from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source import BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, State as State

async def async_get_media_source(hass: HomeAssistant) -> ImageMediaSource: ...

class ImageMediaSource(MediaSource):
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
