from . import VlcConfigEntry as VlcConfigEntry
from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiovlc.client import Client as Client
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Concatenate

MAX_VOLUME: int

def _get_str(data: dict, key: str) -> str | None: ...
async def async_setup_entry(hass: HomeAssistant, entry: VlcConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def catch_vlc_errors[_VlcDeviceT: VlcDevice, **_P](func: Callable[Concatenate[_VlcDeviceT, _P], Awaitable[None]]) -> Callable[Concatenate[_VlcDeviceT, _P], Coroutine[Any, Any, None]]: ...

class VlcDevice(MediaPlayerEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_media_content_type: Incomplete
    _attr_supported_features: Incomplete
    _volume_bkp: float
    volume_level: int
    _config_entry: Incomplete
    _vlc: Incomplete
    _attr_available: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _using_addon: Incomplete
    def __init__(self, config_entry: ConfigEntry, vlc: Client, name: str, available: bool) -> None: ...
    _attr_state: Incomplete
    _attr_volume_level: Incomplete
    _attr_media_duration: Incomplete
    _attr_media_position_updated_at: Incomplete
    _attr_media_position: Incomplete
    _attr_media_album_name: Incomplete
    _attr_media_artist: Incomplete
    _attr_media_title: Incomplete
    @catch_vlc_errors
    async def async_update(self) -> None: ...
    @catch_vlc_errors
    async def async_media_seek(self, position: float) -> None: ...
    _attr_is_volume_muted: Incomplete
    @catch_vlc_errors
    async def async_mute_volume(self, mute: bool) -> None: ...
    @catch_vlc_errors
    async def async_set_volume_level(self, volume: float) -> None: ...
    @catch_vlc_errors
    async def async_media_play(self) -> None: ...
    @catch_vlc_errors
    async def async_media_pause(self) -> None: ...
    @catch_vlc_errors
    async def async_media_stop(self) -> None: ...
    @catch_vlc_errors
    async def async_play_media(self, media_type: MediaType | str, media_id: str, **kwargs: Any) -> None: ...
    @catch_vlc_errors
    async def async_media_previous_track(self) -> None: ...
    @catch_vlc_errors
    async def async_media_next_track(self) -> None: ...
    @catch_vlc_errors
    async def async_clear_playlist(self) -> None: ...
    @catch_vlc_errors
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    async def async_browse_media(self, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
