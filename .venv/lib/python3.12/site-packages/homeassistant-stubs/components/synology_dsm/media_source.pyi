from .const import DOMAIN as DOMAIN, SHARED_SUFFIX as SHARED_SUFFIX
from .models import SynologyDSMData as SynologyDSMData
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components import http as http
from homeassistant.components.media_player import MediaClass as MediaClass
from homeassistant.components.media_source import BrowseError as BrowseError, BrowseMediaSource as BrowseMediaSource, MediaSource as MediaSource, MediaSourceItem as MediaSourceItem, PlayMedia as PlayMedia, Unresolvable as Unresolvable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from synology_dsm.api.photos import SynoPhotosItem

async def async_get_media_source(hass: HomeAssistant) -> MediaSource: ...

class SynologyPhotosMediaSourceIdentifier:
    unique_id: Incomplete
    album_id: Incomplete
    cache_key: Incomplete
    file_name: Incomplete
    is_shared: bool
    passphrase: str
    def __init__(self, identifier: str) -> None: ...

class SynologyPhotosMediaSource(MediaSource):
    name: str
    hass: Incomplete
    entries: Incomplete
    def __init__(self, hass: HomeAssistant, entries: list[ConfigEntry]) -> None: ...
    async def async_browse_media(self, item: MediaSourceItem) -> BrowseMediaSource: ...
    async def _async_build_diskstations(self, item: MediaSourceItem) -> list[BrowseMediaSource]: ...
    async def async_resolve_media(self, item: MediaSourceItem) -> PlayMedia: ...
    async def async_get_thumbnail(self, item: SynoPhotosItem, diskstation: SynologyDSMData) -> str | None: ...

class SynologyDsmMediaView(http.HomeAssistantView):
    url: str
    name: str
    hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def get(self, request: web.Request, source_dir_id: str, location: str) -> web.Response: ...
