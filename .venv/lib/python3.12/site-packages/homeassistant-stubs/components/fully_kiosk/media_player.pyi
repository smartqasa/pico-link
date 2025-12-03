from . import FullyKioskConfigEntry as FullyKioskConfigEntry
from .const import AUDIOMANAGER_STREAM_MUSIC as AUDIOMANAGER_STREAM_MUSIC, MEDIA_SUPPORT_FULLYKIOSK as MEDIA_SUPPORT_FULLYKIOSK
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from .entity import FullyKioskEntity as FullyKioskEntity
from _typeshed import Incomplete
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: FullyKioskConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FullyMediaPlayer(FullyKioskEntity, MediaPlayerEntity):
    _attr_name: Incomplete
    _attr_supported_features = MEDIA_SUPPORT_FULLYKIOSK
    _attr_assumed_state: bool
    _attr_unique_id: Incomplete
    _attr_state: Incomplete
    def __init__(self, coordinator: FullyKioskDataUpdateCoordinator) -> None: ...
    _attr_media_content_type: Incomplete
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    async def async_media_stop(self) -> None: ...
    _attr_volume_level: Incomplete
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
