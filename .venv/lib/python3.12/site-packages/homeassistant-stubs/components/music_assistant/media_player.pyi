from . import MusicAssistantConfigEntry as MusicAssistantConfigEntry
from .const import ATTR_ACTIVE as ATTR_ACTIVE, ATTR_ACTIVE_QUEUE as ATTR_ACTIVE_QUEUE, ATTR_ALBUM as ATTR_ALBUM, ATTR_ANNOUNCE_VOLUME as ATTR_ANNOUNCE_VOLUME, ATTR_ARTIST as ATTR_ARTIST, ATTR_AUTO_PLAY as ATTR_AUTO_PLAY, ATTR_CURRENT_INDEX as ATTR_CURRENT_INDEX, ATTR_CURRENT_ITEM as ATTR_CURRENT_ITEM, ATTR_ELAPSED_TIME as ATTR_ELAPSED_TIME, ATTR_ITEMS as ATTR_ITEMS, ATTR_MASS_PLAYER_TYPE as ATTR_MASS_PLAYER_TYPE, ATTR_MEDIA_ID as ATTR_MEDIA_ID, ATTR_MEDIA_TYPE as ATTR_MEDIA_TYPE, ATTR_NEXT_ITEM as ATTR_NEXT_ITEM, ATTR_QUEUE_ID as ATTR_QUEUE_ID, ATTR_RADIO_MODE as ATTR_RADIO_MODE, ATTR_REPEAT_MODE as ATTR_REPEAT_MODE, ATTR_SHUFFLE_ENABLED as ATTR_SHUFFLE_ENABLED, ATTR_SOURCE_PLAYER as ATTR_SOURCE_PLAYER, ATTR_URL as ATTR_URL, ATTR_USE_PRE_ANNOUNCE as ATTR_USE_PRE_ANNOUNCE, DOMAIN as DOMAIN
from .entity import MusicAssistantEntity as MusicAssistantEntity
from .media_browser import async_browse_media as async_browse_media
from .schemas import QUEUE_DETAILS_SCHEMA as QUEUE_DETAILS_SCHEMA, queue_item_dict_from_mass_item as queue_item_dict_from_mass_item
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Mapping
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import ATTR_MEDIA_ENQUEUE as ATTR_MEDIA_ENQUEUE, ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, BrowseMedia as BrowseMedia, MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEnqueue as MediaPlayerEnqueue, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, RepeatMode as RepeatMode, async_process_play_media_url as async_process_play_media_url
from homeassistant.const import ATTR_NAME as ATTR_NAME, STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp
from music_assistant_client import MusicAssistantClient as MusicAssistantClient
from music_assistant_models.enums import MediaType, QueueOption
from music_assistant_models.event import MassEvent as MassEvent
from music_assistant_models.player import Player as Player
from music_assistant_models.player_queue import PlayerQueue as PlayerQueue
from typing import Any, Concatenate

SUPPORTED_FEATURES: Incomplete
QUEUE_OPTION_MAP: Incomplete
SERVICE_PLAY_MEDIA_ADVANCED: str
SERVICE_PLAY_ANNOUNCEMENT: str
SERVICE_TRANSFER_QUEUE: str
SERVICE_GET_QUEUE: str

def catch_musicassistant_error[_R, **P](func: Callable[Concatenate[MusicAssistantPlayer, P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[MusicAssistantPlayer, P], Coroutine[Any, Any, _R]]: ...
async def async_setup_entry(hass: HomeAssistant, entry: MusicAssistantConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MusicAssistantPlayer(MusicAssistantEntity, MediaPlayerEntity):
    _attr_name: Incomplete
    _attr_media_image_remotely_accessible: bool
    _attr_media_content_type: Incomplete
    _attr_icon: Incomplete
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _prev_time: float
    def __init__(self, mass: MusicAssistantClient, player_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def active_queue(self) -> PlayerQueue | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    _attr_state: Incomplete
    _attr_group_members: Incomplete
    _attr_volume_level: Incomplete
    _attr_is_volume_muted: Incomplete
    async def async_on_update(self) -> None: ...
    @catch_musicassistant_error
    async def async_media_play(self) -> None: ...
    @catch_musicassistant_error
    async def async_media_pause(self) -> None: ...
    @catch_musicassistant_error
    async def async_media_stop(self) -> None: ...
    @catch_musicassistant_error
    async def async_media_next_track(self) -> None: ...
    @catch_musicassistant_error
    async def async_media_previous_track(self) -> None: ...
    @catch_musicassistant_error
    async def async_media_seek(self, position: float) -> None: ...
    @catch_musicassistant_error
    async def async_mute_volume(self, mute: bool) -> None: ...
    @catch_musicassistant_error
    async def async_set_volume_level(self, volume: float) -> None: ...
    @catch_musicassistant_error
    async def async_volume_up(self) -> None: ...
    @catch_musicassistant_error
    async def async_volume_down(self) -> None: ...
    @catch_musicassistant_error
    async def async_turn_on(self) -> None: ...
    @catch_musicassistant_error
    async def async_turn_off(self) -> None: ...
    @catch_musicassistant_error
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    @catch_musicassistant_error
    async def async_set_repeat(self, repeat: RepeatMode) -> None: ...
    @catch_musicassistant_error
    async def async_clear_playlist(self) -> None: ...
    @catch_musicassistant_error
    async def async_play_media(self, media_type: MediaType | str, media_id: str, enqueue: MediaPlayerEnqueue | None = None, announce: bool | None = None, **kwargs: Any) -> None: ...
    @catch_musicassistant_error
    async def async_join_players(self, group_members: list[str]) -> None: ...
    @catch_musicassistant_error
    async def async_unjoin_player(self) -> None: ...
    @catch_musicassistant_error
    async def _async_handle_play_media(self, media_id: list[str], artist: str | None = None, album: str | None = None, enqueue: MediaPlayerEnqueue | QueueOption | None = None, radio_mode: bool | None = None, media_type: str | None = None) -> None: ...
    @catch_musicassistant_error
    async def _async_handle_play_announcement(self, url: str, use_pre_announce: bool | None = None, announce_volume: int | None = None) -> None: ...
    @catch_musicassistant_error
    async def _async_handle_transfer_queue(self, source_player: str | None = None, auto_play: bool | None = None) -> None: ...
    @catch_musicassistant_error
    async def _async_handle_get_queue(self) -> ServiceResponse: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    _attr_media_image_url: Incomplete
    def _update_media_image_url(self, player: Player, queue: PlayerQueue | None) -> None: ...
    _attr_media_artist: Incomplete
    _attr_media_album_artist: Incomplete
    _attr_media_album_name: Incomplete
    _attr_media_title: Incomplete
    _attr_media_content_id: Incomplete
    _attr_media_duration: Incomplete
    _attr_media_position: Incomplete
    _attr_media_position_updated_at: Incomplete
    _attr_app_id: Incomplete
    _attr_shuffle: Incomplete
    _attr_repeat: Incomplete
    _attr_source: Incomplete
    def _update_media_attributes(self, player: Player, queue: PlayerQueue | None) -> None: ...
    def _convert_queueoption_to_media_player_enqueue(self, queue_option: MediaPlayerEnqueue | QueueOption | None) -> QueueOption | None: ...
