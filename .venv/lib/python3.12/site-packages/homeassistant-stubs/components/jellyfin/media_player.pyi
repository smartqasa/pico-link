from . import JellyfinConfigEntry as JellyfinConfigEntry
from .browse_media import build_item_response as build_item_response, build_root_response as build_root_response
from .client_wrapper import get_artwork_url as get_artwork_url
from .const import CONTENT_TYPE_MAP as CONTENT_TYPE_MAP, LOGGER as LOGGER
from .coordinator import JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from .entity import JellyfinClientEntity as JellyfinClientEntity
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import parse_datetime as parse_datetime
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: JellyfinConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JellyfinMediaPlayer(JellyfinClientEntity, MediaPlayerEntity):
    _attr_unique_id: Incomplete
    now_playing: dict[str, Any] | None
    play_state: dict[str, Any] | None
    def __init__(self, coordinator: JellyfinDataUpdateCoordinator, session_id: str) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_state: Incomplete
    _attr_is_volume_muted: Incomplete
    _attr_volume_level: Incomplete
    _attr_media_content_type: Incomplete
    _attr_media_content_id: Incomplete
    _attr_media_title: Incomplete
    _attr_media_series_title: Incomplete
    _attr_media_season: Incomplete
    _attr_media_episode: Incomplete
    _attr_media_album_name: Incomplete
    _attr_media_album_artist: Incomplete
    _attr_media_artist: Incomplete
    _attr_media_track: Incomplete
    _attr_media_duration: Incomplete
    _attr_media_position: Incomplete
    _attr_media_position_updated_at: Incomplete
    _attr_media_image_remotely_accessible: bool
    @callback
    def _update_from_session_data(self) -> None: ...
    @property
    def media_image_url(self) -> str | None: ...
    @property
    def supported_features(self) -> MediaPlayerEntityFeature: ...
    def media_seek(self, position: float) -> None: ...
    def media_pause(self) -> None: ...
    def media_play(self) -> None: ...
    def media_play_pause(self) -> None: ...
    def media_stop(self) -> None: ...
    def play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    def set_volume_level(self, volume: float) -> None: ...
    def mute_volume(self, mute: bool) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
