from .const import DOMAIN as DOMAIN
from .models import SpotifyData as SpotifyData
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from spotifyaio import PlaybackState as PlaybackState, Playlist as Playlist, SpotifyClient as SpotifyClient, UserProfile as UserProfile

_LOGGER: Incomplete
type SpotifyConfigEntry = ConfigEntry[SpotifyData]

@dataclass
class SpotifyCoordinatorData:
    current_playback: PlaybackState | None
    position_updated_at: datetime | None
    playlist: Playlist | None
    dj_playlist: bool = ...

SPOTIFY_DJ_PLAYLIST_URI: str

class SpotifyCoordinator(DataUpdateCoordinator[SpotifyCoordinatorData]):
    current_user: UserProfile
    config_entry: SpotifyConfigEntry
    client: Incomplete
    _playlist: Playlist | None
    _checked_playlist_id: str | None
    def __init__(self, hass: HomeAssistant, client: SpotifyClient) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> SpotifyCoordinatorData: ...
