from .const import DOMAIN as DOMAIN, MEDIA_PLAYER_PREFIX as MEDIA_PLAYER_PREFIX, MEDIA_TYPE_SHOW as MEDIA_TYPE_SHOW, PLAYABLE_MEDIA_TYPES as PLAYABLE_MEDIA_TYPES
from .util import fetch_image_url as fetch_image_url
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.media_player import BrowseError as BrowseError, BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaType as MediaType
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant
from spotifyaio import Artist as Artist, BasePlaylist as BasePlaylist, SimplifiedAlbum as SimplifiedAlbum, SimplifiedTrack as SimplifiedTrack, SpotifyClient as SpotifyClient
from spotifyaio.models import SimplifiedEpisode
from typing import Any, TypedDict

BROWSE_LIMIT: int
_LOGGER: Incomplete

class ItemPayload(TypedDict):
    name: str
    type: str
    uri: str
    id: str | None
    thumbnail: str | None

def _get_artist_item_payload(artist: Artist) -> ItemPayload: ...
def _get_album_item_payload(album: SimplifiedAlbum) -> ItemPayload: ...
def _get_playlist_item_payload(playlist: BasePlaylist) -> ItemPayload: ...
def _get_track_item_payload(track: SimplifiedTrack, show_thumbnails: bool = True) -> ItemPayload: ...
def _get_episode_item_payload(episode: SimplifiedEpisode) -> ItemPayload: ...

class BrowsableMedia(StrEnum):
    CURRENT_USER_PLAYLISTS = 'current_user_playlists'
    CURRENT_USER_FOLLOWED_ARTISTS = 'current_user_followed_artists'
    CURRENT_USER_SAVED_ALBUMS = 'current_user_saved_albums'
    CURRENT_USER_SAVED_TRACKS = 'current_user_saved_tracks'
    CURRENT_USER_SAVED_SHOWS = 'current_user_saved_shows'
    CURRENT_USER_RECENTLY_PLAYED = 'current_user_recently_played'
    CURRENT_USER_TOP_ARTISTS = 'current_user_top_artists'
    CURRENT_USER_TOP_TRACKS = 'current_user_top_tracks'
    NEW_RELEASES = 'new_releases'

LIBRARY_MAP: Incomplete
CONTENT_TYPE_MEDIA_CLASS: dict[str, Any]

class MissingMediaInformation(BrowseError): ...
class UnknownMediaType(BrowseError): ...

async def async_browse_media(hass: HomeAssistant, media_content_type: str | None, media_content_id: str | None, *, can_play_artist: bool = True) -> BrowseMedia: ...
async def async_browse_media_internal(hass: HomeAssistant, spotify: SpotifyClient, media_content_type: str | None, media_content_id: str | None, *, can_play_artist: bool = True) -> BrowseMedia: ...
async def build_item_response(spotify: SpotifyClient, payload: dict[str, str | None], *, can_play_artist: bool) -> BrowseMedia | None: ...
def item_payload(item: ItemPayload, *, can_play_artist: bool) -> BrowseMedia: ...
async def library_payload(*, can_play_artist: bool) -> BrowseMedia: ...
